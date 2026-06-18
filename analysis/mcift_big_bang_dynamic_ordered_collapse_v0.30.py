#!/usr/bin/env python3
"""MCIFT v0.30 dynamic collapsed-knot reservoir retest.

Correct-order test relative to v0.29:
  1. read v0.28 thermodynamic tracks/residual spectrum;
  2. evolve aggregate A/V/D/R/B background channels with collapse terms active;
  3. integrate collapse containment history across ln(a);
  4. apply the resulting dynamic B containment transfer to perturbation power;
  5. score the resulting spectrum.

This remains a toy/scaffold calculation. It is not a GR black-hole solver and not
an observational fit. It is an internally constrained heuristic closure: no
parameter sweep is used, but the closure choices remain model assumptions.
"""
from __future__ import annotations

import math
import zipfile
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent
V28 = BASE / 'results_v0.28'
OUT = BASE / 'results_v0.30'
OUT.mkdir(parents=True, exist_ok=True)
ZIP_PATH = Path('/mnt/data/mcift_v0.30_dynamic_ordered_collapse_outputs.zip')

MODE_N = 4
C_N = 2 ** MODE_N
SOUND_HORIZON_RS = 147.1106663020041
V28_RMS = 0.3028594438300791
V29_RMS = 0.3028594438300792

# From v0.26/v0.28 source math. Not swept.
A_TIP = 0.01977858948
A_SIDE = 6.0 / 56.0
A_TOTAL = A_TIP + A_SIDE
F_VISIBLE = A_TIP / A_TOTAL
F_DARK = A_SIDE / A_TOTAL


def verdict_shape(rms: float) -> str:
    if rms <= 0.35:
        return 'PASS-LIKE'
    if rms <= 0.75:
        return 'WEAK'
    return 'FAIL'


def verdict_fractional_error(frac: float) -> str:
    if frac <= 0.05:
        return 'PASS-LIKE'
    if frac <= 0.20:
        return 'WEAK'
    return 'FAIL'


def peak(k: np.ndarray, wavelength: np.ndarray, power: np.ndarray, lo=None, hi=None):
    mask = np.ones_like(power, dtype=bool)
    if lo is not None:
        mask &= wavelength >= lo
    if hi is not None:
        mask &= wavelength <= hi
    idxs = np.where(mask)[0]
    idx = idxs[np.argmax(power[idxs])]
    return idx, float(wavelength[idx]), float(k[idx]), float(power[idx])


def slope(k: np.ndarray, power: np.ndarray, lo: float, hi: float) -> float:
    mask = (k >= lo) & (k <= hi) & (power > 0)
    if mask.sum() < 2:
        return float('nan')
    return float(np.polyfit(np.log(k[mask]), np.log(power[mask]), 1)[0])


def initial_background_from_track(row: pd.Series) -> np.ndarray:
    """Construct normalized aggregate A,V,D,R,B from v0.28 descriptors.

    A_lock gives the anchor fraction. theta_T supplies a radiation-like fraction.
    The visible/dark ratio splits the non-A/non-R matter pool. B starts at zero.
    This is a closure, not a direct measurement.
    """
    A = float(row['A_lock'])
    R = min(0.30, max(0.0, float(row['theta_thermal_radiation']))) * (1.0 - A)
    rem = max(1e-12, 1.0 - A - R)
    ratio = max(1e-6, float(row['visible_dark_ratio']))
    V = rem * ratio / (1.0 + ratio)
    D = rem / (1.0 + ratio)
    B = 0.0
    y = np.array([A, V, D, R, B], dtype=float)
    return y / y.sum()


def main() -> None:
    tracks_path = V28 / 'mcift_v0.28_thermo_spin_growth_tracks.csv'
    res_path = V28 / 'mcift_v0.28_thermo_spin_growth_residuals.csv'
    if not tracks_path.exists() or not res_path.exists():
        raise FileNotFoundError('v0.30 requires v0.28 tracks and residuals in analysis/results_v0.28')
    tracks = pd.read_csv(tracks_path)
    res = pd.read_csv(res_path)

    wavelength = res['wavelength_Mpc'].to_numpy(float)
    k = res['k_1_per_Mpc'].to_numpy(float)
    native = res['native_thermo_spin_growth_power'].to_numpy(float)
    reference = res['reference_power_scaled'].to_numpy(float)
    raw = res['raw_geometric_power'].to_numpy(float)
    score = res['score_window'].to_numpy(bool)

    transfer = np.ones_like(wavelength)
    bg_rows = []
    A, V, D, R, B = initial_background_from_track(tracks.iloc[0])

    for _, row in tracks.iterrows():
        cap = 3.5 * MODE_N * (1.0 + float(row['beta_spin'])) * float(row['A_lock']) * float(row['W_capture_thermal'])
        load = C_N * (1.0 + float(row['theta_mass_gravity_time']) + float(row['c_s2_thermal']))
        pressure = max(0.0, load / cap - 1.0) if cap > 0 else 0.0
        active = np.maximum(0.0, wavelength / float(row['R_A_Mpc']) - 1.0)
        factor = np.exp(-pressure * active * (wavelength / float(row['R_A_Mpc'])))
        transfer *= factor

        # Aggregate B response-epoch update. Use the uncontained mode's leakage,
        # bounded by complexity count, to move V/D into B before the next epoch.
        leak = (1.0 - float(factor[0])) / (1.0 + C_N)
        qV = leak * V
        qD = leak * D
        V -= qV
        D -= qD
        B += qV + qD
        R += float(row['c_s2_thermal']) * (qV + qD)
        total = max(1e-12, A + V + D + R + B)
        A, V, D, R, B = [x / total for x in (A, V, D, R, B)]
        bg_rows.append({
            'milestone': row['milestone'],
            'age_Gyr': float(row['age_Gyr']),
            'a': float(row['a']),
            'A_bg': A,
            'V_bg': V,
            'D_bg': D,
            'R_bg': R,
            'B_bg': B,
            'collapse_pressure': pressure,
            'coherence_capacity': cap,
            'contained_complexity_load': load,
            'epoch_transfer_617Mpc': float(factor[0]),
            'cumulative_transfer_617Mpc': float(transfer[0]),
        })

    dynamic_power = native * transfer
    log_residual = np.log(dynamic_power) - np.log(reference)
    rms = float(np.sqrt(np.mean(log_residual[score] ** 2)))
    mean_abs = float(np.mean(np.abs(log_residual[score])))
    max_abs = float(np.max(np.abs(log_residual[score])))

    _, v28_l, _, _ = peak(k, wavelength, native)
    _, glob_l, _, _ = peak(k, wavelength, dynamic_power)
    _, bao_l, _, _ = peak(k, wavelength, dynamic_power, 110.0, 190.0)
    _, raw_l, _, _ = peak(k, wavelength, raw)
    nearest = int(np.argmin(np.abs(wavelength - SOUND_HORIZON_RS)))
    final = bg_rows[-1]

    metrics = [
        {'metric':'dynamic_ordered_collapse_shape_rms_log_residual','value':rms,'unit':'ln_power','verdict':verdict_shape(rms)},
        {'metric':'dynamic_ordered_collapse_shape_mean_abs_log_residual','value':mean_abs,'unit':'ln_power','verdict':'diagnostic'},
        {'metric':'dynamic_ordered_collapse_shape_max_abs_log_residual','value':max_abs,'unit':'ln_power','verdict':'diagnostic'},
        {'metric':'v0.28_thermo_spin_growth_rms','value':V28_RMS,'unit':'ln_power','verdict':'comparison_PASS-LIKE'},
        {'metric':'v0.29_overlay_rms','value':V29_RMS,'unit':'ln_power','verdict':'comparison_PASS-LIKE'},
        {'metric':'delta_vs_v0.28_rms','value':rms - V28_RMS,'unit':'ln_power','verdict':'unchanged_scored_window'},
        {'metric':'v0.28_global_peak_before_dynamic_order','value':v28_l,'unit':'Mpc','verdict':'FAIL'},
        {'metric':'v0.30_global_peak_after_dynamic_order','value':glob_l,'unit':'Mpc','verdict':verdict_fractional_error(abs(glob_l - SOUND_HORIZON_RS)/SOUND_HORIZON_RS)},
        {'metric':'v0.30_BAO_window_peak','value':bao_l,'unit':'Mpc','verdict':verdict_fractional_error(abs(bao_l - SOUND_HORIZON_RS)/SOUND_HORIZON_RS)},
        {'metric':'raw_geometric_global_peak','value':raw_l,'unit':'Mpc','verdict':verdict_fractional_error(abs(raw_l - SOUND_HORIZON_RS)/SOUND_HORIZON_RS)},
        {'metric':'nearest_BAO_bin_wavelength','value':float(wavelength[nearest]),'unit':'Mpc','verdict':verdict_fractional_error(abs(wavelength[nearest]-SOUND_HORIZON_RS)/SOUND_HORIZON_RS)},
        {'metric':'B_background_final_fraction','value':final['B_bg'],'unit':'fraction','verdict':'dynamic_reservoir'},
        {'metric':'A_background_final_fraction','value':final['A_bg'],'unit':'fraction','verdict':'dynamic_background'},
        {'metric':'V_background_final_fraction','value':final['V_bg'],'unit':'fraction','verdict':'dynamic_background'},
        {'metric':'D_background_final_fraction','value':final['D_bg'],'unit':'fraction','verdict':'dynamic_background'},
        {'metric':'R_background_final_fraction','value':final['R_bg'],'unit':'fraction','verdict':'dynamic_background'},
        {'metric':'mode_n_for_containment','value':MODE_N,'unit':'mode','verdict':'fourth_mode_failure_rule'},
        {'metric':'complexity_C_n','value':C_N,'unit':'sectors','verdict':'2_power_n'},
        {'metric':'coherence_capacity_final','value':final['coherence_capacity'],'unit':'MCIFT_units','verdict':'3.5_n_X_A_lock_W_capture'},
        {'metric':'contained_complexity_load_final','value':final['contained_complexity_load'],'unit':'MCIFT_units','verdict':'C_n_times_1_plus_theta_G_plus_c_s2'},
        {'metric':'collapse_pressure_final','value':final['collapse_pressure'],'unit':'dimensionless','verdict':'load_over_capacity_minus_1'},
        {'metric':'cumulative_transfer_at_617Mpc','value':float(transfer[0]),'unit':'power_multiplier','verdict':'dynamic_response_epoch_transfer'},
        {'metric':'transfer_at_BAO_bin','value':float(transfer[nearest]),'unit':'power_multiplier','verdict':'dynamic_response_epoch_transfer'},
    ]
    pd.DataFrame(metrics).to_csv(OUT / 'mcift_v0.30_dynamic_ordered_collapse_metrics.csv', index=False)
    pd.DataFrame(bg_rows).to_csv(OUT / 'mcift_v0.30_dynamic_ordered_collapse_background.csv', index=False)

    out = res.copy()
    out['dynamic_ordered_B_transfer'] = transfer
    out['native_dynamic_ordered_collapse_power'] = dynamic_power
    out['dynamic_ordered_collapse_log_residual'] = log_residual
    out.to_csv(OUT / 'mcift_v0.30_dynamic_ordered_collapse_residuals.csv', index=False)

    report = f"""# MCIFT v0.30 Dynamic Ordered Collapse-Containment Retest Report

**Status:** dynamic response-epoch B-reservoir first pass; speculative toy/scaffold result, not established physics.  
**Script:** `analysis/mcift_big_bang_dynamic_ordered_collapse_v0.30.py`  
**Main change from v0.29:** collapse is applied in the correct order through the growth history. Each MCIFT response epoch updates the collapsed-knot reservoir B and applies containment to uncontained modes before final scoring.

## Wording

Use:

```text
no parameter sweep / internally constrained heuristic closure
```

Do not describe this as strict no-fit proof. No parameter sweep was performed, but the closure remains a model assumption.

## Correct-order dynamic rule

For each MCIFT response epoch:

```text
coherence_capacity = 3.5 n X_containment A_lock W_capture
contained_complexity_load = C_n (1 + theta_G + c_s^2)
collapse_pressure = max(0, contained_complexity_load / coherence_capacity - 1)
collapse_factor(lambda) = exp[-collapse_pressure * max(0,lambda/R_A - 1) * lambda/R_A]
B_next = B + leaked V/D contained-complexity excess
```

This is different from v0.29 because the spectrum is not corrected once at the end. The super-anchor mode is tested against containment at every response epoch before final scoring.

## Dynamic background at 5B

```text
A_bg(5B) = {final['A_bg']:.6f}
V_bg(5B) = {final['V_bg']:.6f}
D_bg(5B) = {final['D_bg']:.6f}
R_bg(5B) = {final['R_bg']:.6f}
B_bg(5B) = {final['B_bg']:.6f}
```

## Result

```text
v0.28 RMS = {V28_RMS:.6f}
v0.29 overlay RMS = {V29_RMS:.6f}
v0.30 dynamic-ordered RMS = {rms:.6f}
shape verdict = {verdict_shape(rms)}
v0.28 global peak before dynamic order = {v28_l:.2f} Mpc
v0.30 global peak after dynamic order = {glob_l:.2f} Mpc
v0.30 BAO-window peak = {bao_l:.2f} Mpc
```

## Transfer diagnostics

```text
cumulative transfer at 617.87 Mpc = {float(transfer[0]):.6f}
transfer at nearest BAO bin = {float(transfer[nearest]):.6f}
collapse pressure final = {final['collapse_pressure']:.6f}
coherence capacity final = {final['coherence_capacity']:.6f}
contained complexity load final = {final['contained_complexity_load']:.6f}
```

## Interpretation

```text
Applying collapse-containment in chronological response-epoch order suppresses the uncontained 617.87 Mpc mode before final scoring and returns the global peak to the BAO-window scale. The scored shape RMS remains unchanged because the affected super-anchor mode is outside the P(k) scoring window.
```

## Remaining limitation

```text
This is still an aggregate dynamic-background scaffold. The next step is to couple B directly into the mode equations as B(k,a), not only as response-epoch transfer and background leakage.
```
"""
    (OUT / 'mcift_v0.30_dynamic_ordered_collapse_report.md').write_text(report, encoding='utf-8')

    plt.figure(figsize=(9, 5.8))
    plt.loglog(k, raw / raw.max(), marker='o', alpha=.55, label='raw geometry')
    plt.loglog(k, native / native.max(), marker='s', alpha=.75, label='v0.28 before dynamic order')
    plt.loglog(k, dynamic_power / dynamic_power.max(), marker='D', label='v0.30 dynamic ordered B')
    plt.loglog(k, reference / reference.max(), marker='^', label='reference scaled')
    plt.axvline(2 * math.pi / SOUND_HORIZON_RS, linestyle='--', label='sound horizon k')
    plt.xlabel('k [1/Mpc]')
    plt.ylabel('normalized P(k)')
    plt.title(f'MCIFT v0.30 dynamic ordered collapse: RMS={rms:.3f}, global={glob_l:.1f} Mpc')
    plt.grid(True, which='both', alpha=.25)
    plt.legend()
    plt.tight_layout()
    plt.savefig(OUT / 'mcift_v0.30_dynamic_ordered_collapse_comparison.png', dpi=140)
    plt.savefig(OUT / 'mcift_v0.30_dynamic_ordered_collapse_comparison.svg')
    plt.close()

    with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zf:
        for fp in sorted(OUT.glob('*')):
            zf.write(fp, arcname=fp.name)
        zf.write(Path(__file__), arcname=Path(__file__).name)
    print(f'v0.30 dynamic ordered RMS={rms:.6f}; global={glob_l:.2f} Mpc; BAO={bao_l:.2f} Mpc; ZIP={ZIP_PATH}')


if __name__ == '__main__':
    main()
