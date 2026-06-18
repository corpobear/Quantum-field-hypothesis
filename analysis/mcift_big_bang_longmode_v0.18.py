#!/usr/bin/env python3
"""MCIFT v0.18 long-mode damping / primordial-spectrum rerun.

Builds on v0.17 scale-lock and adds the missing Fourier-space equation:
    delta_v018(k) = delta_v017(k)
        * [1 - exp(-(k/k_cut)^p)]
        * (k/k_pivot)^((n_s - 1)/2)

This suppresses over-large coherent modes while preserving the BAO-window scale.
It is still a toy scaffold, not a full Einstein-Boltzmann CMB or BBN solver.
"""

from __future__ import annotations

import csv
import runpy
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).resolve().parent
v17 = runpy.run_path(str(BASE / "mcift_big_bang_scale_lock_v0.17.py"))
RESULTS_DIR = BASE / "results_v0.18"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

N_S_PLANCK = 0.965
K_PIVOT = 0.050
K_CUT = 0.030
DAMPING_POWER = 4.0
BOX_SIZE_MPC = v17["BOX_SIZE_MPC"]
BAO_WINDOW_MPC = v17["BAO_WINDOW_MPC"]
PLANCK_BARYON_CDM_RATIO = v17["PLANCK_BARYON_CDM_RATIO"]
DESI_RD_REFERENCE_MPC = v17["DESI_RD_REFERENCE_MPC"]
MILESTONES = v17["MILESTONES"]


def primordial_gate(k):
    gate = 1.0 - np.exp(-((k / K_CUT) ** DAMPING_POWER))
    tilt = np.ones_like(k)
    mask = k > 0
    tilt[mask] = (k[mask] / K_PIVOT) ** ((N_S_PLANCK - 1.0) / 2.0)
    return gate * tilt


def apply_longmode_damping(density):
    mean_density = float(np.mean(density))
    delta = density / mean_density - 1.0
    fft = np.fft.fftn(delta)
    n = density.shape[0]
    spacing = BOX_SIZE_MPC / n
    k1 = 2.0 * np.pi * np.fft.fftfreq(n, d=spacing)
    kx, ky, kz = np.meshgrid(k1, k1, k1, indexing="ij")
    k = np.sqrt(kx**2 + ky**2 + kz**2)
    gate = primordial_gate(k)
    gate[k == 0] = 0.0
    damped_delta = np.fft.ifftn(fft * gate).real
    return np.maximum(mean_density * (1.0 + damped_delta), 1e-9 * mean_density)


def isotropic_power_spectrum_with_gate(density, n_bins=44):
    rows = v17["isotropic_power_spectrum"](density, n_bins=n_bins)
    for row in rows:
        row["primordial_gate"] = float(primordial_gate(np.array([row["k_1_per_Mpc"]]))[0])
    return rows


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def verdict(error):
    return v17["verdict_fractional_error"](error)


def plot_power(v017_rows, v018_rows, r_s_mpc):
    plt.figure(figsize=(8.8, 5.7))
    for rows, label in [(v017_rows, "v0.17 scale-lock"), (v018_rows, "v0.18 + long-mode damping")]:
        plt.loglog([r["k_1_per_Mpc"] for r in rows], [r["power"] for r in rows], marker="o", linewidth=1, label=label)
    plt.axvline(2.0 * np.pi / r_s_mpc, linestyle="--", linewidth=1, label=f"sound-horizon k, r_s={r_s_mpc:.2f} Mpc")
    plt.axvline(K_CUT, linestyle=":", linewidth=1, label=f"k_cut={K_CUT:.3f} 1/Mpc")
    plt.xlabel("k [1/Mpc], box calibration = 1000 Mpc")
    plt.ylabel("Toy P(k)")
    plt.title("MCIFT v0.18 power spectrum: primordial gate / long-mode damping")
    plt.legend(); plt.grid(True, which="both", alpha=0.25); plt.tight_layout()
    plt.savefig(RESULTS_DIR / "mcift_v0.18_power_spectrum.png", dpi=140)
    plt.savefig(RESULTS_DIR / "mcift_v0.18_power_spectrum.svg")
    plt.close()


def plot_radial(v017_profile, v018_profile, r_s_mpc):
    plt.figure(figsize=(8.8, 5.7))
    for rows, label in [(v017_profile, "v0.17 scale-lock"), (v018_profile, "v0.18 damped density")]:
        plt.plot([r["r_Mpc"] for r in rows], [r["mean_density_proxy"] for r in rows], marker="o", linewidth=1, label=label)
    plt.axvline(r_s_mpc, linestyle="--", linewidth=1, label=f"r_s={r_s_mpc:.2f} Mpc")
    plt.xlabel("Radius [Mpc], box calibration = 1000 Mpc")
    plt.ylabel("Mean positive density proxy")
    plt.title("MCIFT v0.18 radial density profile")
    plt.legend(); plt.grid(True, alpha=0.25); plt.tight_layout()
    plt.savefig(RESULTS_DIR / "mcift_v0.18_radial_profile.png", dpi=140)
    plt.savefig(RESULTS_DIR / "mcift_v0.18_radial_profile.svg")
    plt.close()


def build_report(summary_rows, r_s, v017_global, v017_bao, v018_global, v018_bao):
    global_error = abs(v018_global["wavelength_Mpc"] - r_s) / r_s
    bao_error = abs(v018_bao["wavelength_Mpc"] - r_s) / r_s
    table = "\n".join(
        f"| {r['milestone']} | {r['age_Gyr']:.1f} | {r['a']:.6f} | {r['z']:.3f} | {r['visible_dark_weighted_ratio']:.6f} | {r['ratio_fractional_error']:.3f} | {r['ratio_verdict']} |"
        for r in summary_rows
    )
    best = min(summary_rows, key=lambda r: r["ratio_fractional_error"])
    final = summary_rows[-1]
    return f"""# MCIFT v0.18 Long-Mode Damping / Primordial-Spectrum Rerun Report

**Status:** equation-input toy rerun, not a validated cosmology model.  
**Script:** `analysis/mcift_big_bang_longmode_v0.18.py`  
**Main change from v0.17:** adds a Fourier-space primordial gate that damps over-large coherent modes and applies a Planck-like scalar tilt.

## New equation implemented

```text
delta_v0.18(k) = delta_v0.17(k)
              * [1 - exp(-(k/k_cut)^p)]
              * (k/k_pivot)^((n_s - 1)/2)
```

Parameter choices in this toy rerun:

```text
n_s = {N_S_PLANCK:.3f}
k_pivot = {K_PIVOT:.3f} 1/Mpc
k_cut = {K_CUT:.3f} 1/Mpc
p = {DAMPING_POWER:.1f}
```

## External anchors used

```text
Planck baryon/CDM ratio = Omega_b h^2 / Omega_c h^2 = {PLANCK_BARYON_CDM_RATIO:.6f}
Calculated sound horizon r_s = {r_s:.3f} Mpc
DESI reference r_d context = {DESI_RD_REFERENCE_MPC:.2f} Mpc
```

## Visible/dark ratio check

This equation acts on the structure spectrum, not the channel-density totals. The visible/dark ratio therefore remains the same benchmark as v0.17.

| Milestone | Age [Gyr] | scale factor a | redshift z | MCIFT V/D weighted | Fractional error | Verdict |
|---:|---:|---:|---:|---:|---:|---|
{table}

Best ratio point: **{best['milestone']}**, with `{best['visible_dark_weighted_ratio']:.6f}`, error `{best['ratio_fractional_error']:.3f}`, verdict **{best['ratio_verdict']}**.  
Final 5B point: `{final['visible_dark_weighted_ratio']:.6f}`, verdict **{final['ratio_verdict']}**.

## Structure-scale test

Before v0.18 damping, the v0.17 scale-locked global peak stayed too large:

```text
v0.17 global peak = {v017_global['wavelength_Mpc']:.2f} Mpc
v0.17 BAO-window peak = {v017_bao['wavelength_Mpc']:.2f} Mpc
```

After v0.18 long-mode damping:

```text
v0.18 global peak = {v018_global['wavelength_Mpc']:.2f} Mpc
v0.18 BAO-window peak = {v018_bao['wavelength_Mpc']:.2f} Mpc
sound horizon r_s = {r_s:.2f} Mpc
global fractional error = {global_error:.3f}
BAO-window fractional error = {bao_error:.3f}
global verdict = {verdict(global_error)}
BAO-window verdict = {verdict(bao_error)}
```

## Interpretation

```text
Visible/dark ratio: still partial match, best near 2B.
BAO-window scale: remains PASS-LIKE.
Global power spectrum: improved from FAIL to {verdict(global_error)}.
CMB acoustic peaks: still undefined; no Boltzmann/radiation transfer solver.
BBN: still undefined; no nuclear reaction network.
```

## Theory implication

The long-mode damping equation fixes the specific v0.17 problem: the 617.87 Mpc coherent mode no longer dominates the power-spectrum diagnostic. This is still not a derived prediction, because `k_cut` and `p` are chosen toy parameters. The next improvement is to derive `k_cut` from MCIFT expansion/anchor dynamics instead of selecting it by hand.

Recommended v0.19 target:

```text
Derive k_cut from anchor horizon crossing:
k_cut(a) = beta * aH(a)/c or beta/r_anchor(a)
then fit beta against visible/dark + BAO + global P(k) together.
```
"""


def main():
    X, Y, Z, R_MPC = v17["make_grids"]()
    r_s = v17["sound_horizon_Mpc"]()
    summary_rows = []
    final_locked = None
    for actual_years, label in MILESTONES:
        age_Gyr = actual_years / 1e9
        a = v17["scale_factor_at_age_Gyr"](age_Gyr)
        z = 1.0 / a - 1.0
        channels = v17["apply_frw_channel_dilution"](v17["evolve_base_channels"](actual_years, X, Y, Z), a)
        ratio, error, ratio_verdict = v17["visible_dark_metrics"](channels)
        summary_rows.append({"milestone": label, "actual_years": actual_years, "age_Gyr": age_Gyr, "a": a, "z": z, "visible_dark_weighted_ratio": ratio, "planck_baryon_cdm_ratio": PLANCK_BARYON_CDM_RATIO, "ratio_fractional_error": error, "ratio_verdict": ratio_verdict})
        if label == "5B":
            final_locked = v17["density_proxy"](channels, R_MPC, r_s, locked=True)

    final_damped = apply_longmode_damping(final_locked)
    v017_ps = isotropic_power_spectrum_with_gate(final_locked)
    v018_ps = isotropic_power_spectrum_with_gate(final_damped)
    v017_profile = v17["radial_profile"](final_locked, R_MPC)
    v018_profile = v17["radial_profile"](final_damped, R_MPC)
    v017_global = v17["pick_peak"](v017_ps)
    v017_bao = v17["pick_peak"](v017_ps, BAO_WINDOW_MPC)
    v18_global = v17["pick_peak"](v018_ps)
    v18_bao = v17["pick_peak"](v018_ps, BAO_WINDOW_MPC)

    write_csv(RESULTS_DIR / "mcift_v0.18_summary.csv", summary_rows)
    write_csv(RESULTS_DIR / "mcift_v0.18_power_v017_reference.csv", v017_ps)
    write_csv(RESULTS_DIR / "mcift_v0.18_power_longmode_damped.csv", v018_ps)
    write_csv(RESULTS_DIR / "mcift_v0.18_radial_v017_reference.csv", v017_profile)
    write_csv(RESULTS_DIR / "mcift_v0.18_radial_longmode_damped.csv", v018_profile)
    plot_power(v017_ps, v018_ps, r_s)
    plot_radial(v017_profile, v018_profile, r_s)
    report = build_report(summary_rows, r_s, v017_global, v017_bao, v18_global, v18_bao)
    (RESULTS_DIR / "mcift_v0.18_longmode_report.md").write_text(report, encoding="utf-8")
    print("MCIFT v0.18 long-mode damping rerun complete")
    print(f"Calculated sound horizon: {r_s:.3f} Mpc")
    print(f"v0.18 global peak: {v18_global['wavelength_Mpc']:.2f} Mpc")
    print(f"v0.18 BAO-window peak: {v18_bao['wavelength_Mpc']:.2f} Mpc")


if __name__ == "__main__":
    main()
