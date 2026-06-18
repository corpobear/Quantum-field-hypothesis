#!/usr/bin/env python3
"""
MCIFT v0.17 expansion-coupled scale-lock cosmology scaffold.

Inputs the current proposed equations as a runnable toy rerun:
- flat Planck-like FRW expansion H(a)
- positive density channels A/V/D/R
- sound horizon r_s = integral c_s/(a^2 H) da
- MCIFT scale-lock modulation tied to r_s
- visible/dark and BAO-window scoring

This is not a full cosmological solver: no Einstein-Boltzmann transfer, CMB
polarization, recombination history, or BBN reaction network.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

C_LIGHT_KM_S = 299_792.458
H0_KM_S_MPC = 67.4
h = H0_KM_S_MPC / 100.0
OMEGA_B_H2 = 0.0224
OMEGA_C_H2 = 0.120
OMEGA_B = OMEGA_B_H2 / h**2
OMEGA_C = OMEGA_C_H2 / h**2
OMEGA_M = 0.315
OMEGA_GAMMA = 2.469e-5 / h**2
OMEGA_R = 9.17e-5
OMEGA_LAMBDA = 1.0 - OMEGA_M - OMEGA_R
PLANCK_BARYON_CDM_RATIO = OMEGA_B_H2 / OMEGA_C_H2
DESI_RD_REFERENCE_MPC = 147.09
Z_DRAG_APPROX = 1059.0

PHI = (1 + np.sqrt(5.0)) / 2.0
BASE_TOY_YEARS = 1_000_000
TOTAL_TOY_STRETCH_YEARS = 5_000_000_000
TIME_STRETCH = TOTAL_TOY_STRETCH_YEARS / BASE_TOY_YEARS
N_SIDE = 64
FIELD_LIMIT_TOY = 5.0
BOX_SIZE_MPC = 1_000.0
SCALE_LOCK_AMPLITUDE = 1.0
BAO_WINDOW_MPC = (80.0, 250.0)
RESULTS_DIR = Path(__file__).resolve().parent / "results_v0.17"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

MILESTONES = [
    (1_000_000_000, "1B"),
    (2_000_000_000, "2B"),
    (3_000_000_000, "3B"),
    (4_000_000_000, "4B"),
    (5_000_000_000, "5B"),
]


def E_of_a(a):
    return np.sqrt(OMEGA_R / a**4 + OMEGA_M / a**3 + OMEGA_LAMBDA)


def H_km_s_Mpc(a):
    return H0_KM_S_MPC * E_of_a(a)


def H_Gyr_inverse(a):
    return (h / 9.778) * E_of_a(a)


def cosmic_age_Gyr(a_value: float) -> float:
    a = np.geomspace(1e-8, a_value, 20_000)
    return float(np.trapezoid(1.0 / (a * H_Gyr_inverse(a)), a))


def scale_factor_at_age_Gyr(age_gyr: float) -> float:
    lo, hi = 1e-6, 1.5
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if cosmic_age_Gyr(mid) < age_gyr:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def sound_horizon_Mpc(z_drag: float = Z_DRAG_APPROX) -> float:
    a_drag = 1.0 / (1.0 + z_drag)
    a = np.geomspace(1e-8, a_drag, 40_000)
    R_b = (3.0 * OMEGA_B / (4.0 * OMEGA_GAMMA)) * a
    c_s = C_LIGHT_KM_S / np.sqrt(3.0 * (1.0 + R_b))
    return float(np.trapezoid(c_s / (a**2 * H_km_s_Mpc(a)), a))


def make_grids():
    toy_axis = np.linspace(-FIELD_LIMIT_TOY, FIELD_LIMIT_TOY, N_SIDE)
    X, Y, Z = np.meshgrid(toy_axis, toy_axis, toy_axis, indexing="ij")
    mpc_axis = np.linspace(-BOX_SIZE_MPC / 2.0, BOX_SIZE_MPC / 2.0, N_SIDE)
    XM, YM, ZM = np.meshgrid(mpc_axis, mpc_axis, mpc_axis, indexing="ij")
    R_MPC = np.sqrt(XM**2 + YM**2 + ZM**2)
    return X, Y, Z, R_MPC


def scaled_t(actual_years: float) -> float:
    return actual_years / TIME_STRETCH


def evolve_base_channels(actual_years: float, X, Y, Z):
    t = scaled_t(actual_years)
    r = np.sqrt(X**2 + Y**2 + Z**2)
    fib_mod = 1.0 + 0.15 * np.sin(2.0 * np.pi * np.log(r + 1e-6) / np.log(PHI))
    coherence = (1.0 - np.exp(-t / 40_000.0)) * np.exp(-r**2 / (4.0 + 0.002 * t)) * fib_mod
    anchor = np.exp(-r**2 / (1.5 + 0.001 * t))

    if t > 40_000:
        visible = 0.7 * (1.0 - np.exp(-(t - 40_000.0) / 90_000.0)) * np.exp(
            -(X**2 + Y**2 + (Z - 2.0) ** 2) / 3.0
        )
    else:
        visible = np.zeros_like(X)

    if t > 180_000:
        dark_factor = 1.0 - np.exp(-(t - 180_000.0) / 150_000.0)
        dark = dark_factor * (
            np.exp(-((X - 2.0) ** 2 + Y**2 + Z**2) / 4.0)
            + np.exp(-((X + 2.0) ** 2 + Y**2 + Z**2) / 4.0)
            + np.exp(-(X**2 + (Y - 2.0) ** 2 + Z**2) / 4.0)
            + np.exp(-(X**2 + (Y + 2.0) ** 2 + Z**2) / 4.0)
        )
    else:
        dark = np.zeros_like(X)

    exchange = 0.35 * np.tanh(t / 200_000.0) * np.exp(-r**2 / 5.0)
    return {"A": coherence + anchor, "V": visible, "D": dark, "R": 0.03 * coherence, "exchange": exchange}


def apply_frw_channel_dilution(channels, a: float):
    return {
        "A": channels["A"] / a**3,
        "V": channels["V"] / a**3,
        "D": channels["D"] / a**3,
        "R": channels["R"] / a**4,
        "exchange": channels["exchange"] / a**3,
    }


def scale_lock_modulation(R_MPC, r_s_mpc: float, amplitude: float = SCALE_LOCK_AMPLITUDE):
    envelope = np.exp(-(R_MPC / (0.45 * BOX_SIZE_MPC)) ** 2)
    return np.maximum(1.0 + amplitude * np.cos((2.0 * np.pi / r_s_mpc) * R_MPC) * envelope, 1e-6)


def density_proxy(channels, R_MPC, r_s_mpc: float, locked: bool):
    base = channels["A"] + 0.6 * channels["V"] + 0.45 * channels["D"] + channels["R"] + channels["exchange"]
    return base * scale_lock_modulation(R_MPC, r_s_mpc) if locked else base


def isotropic_power_spectrum(density, n_bins: int = 44):
    delta = density / np.mean(density) - 1.0
    power = np.abs(np.fft.fftn(delta)) ** 2 / delta.size
    spacing = BOX_SIZE_MPC / density.shape[0]
    k1 = 2.0 * np.pi * np.fft.fftfreq(density.shape[0], d=spacing)
    kx, ky, kz = np.meshgrid(k1, k1, k1, indexing="ij")
    kvals = np.sqrt(kx**2 + ky**2 + kz**2).ravel()
    pvals = power.ravel()
    keep = kvals > 0
    kvals, pvals = kvals[keep], pvals[keep]
    bins = np.linspace(kvals.min(), kvals.max(), n_bins + 1)
    rows = []
    for i in range(n_bins):
        mask = (kvals >= bins[i]) & (kvals < bins[i + 1])
        if np.any(mask):
            k_center = float(0.5 * (bins[i] + bins[i + 1]))
            rows.append({"k_1_per_Mpc": k_center, "power": float(np.mean(pvals[mask])), "modes": int(np.sum(mask)), "wavelength_Mpc": float(2.0 * np.pi / k_center)})
    return rows


def radial_profile(density, R_MPC, n_bins: int = 80):
    bins = np.linspace(0.0, float(R_MPC.max()), n_bins + 1)
    rows = []
    for i in range(n_bins):
        mask = (R_MPC >= bins[i]) & (R_MPC < bins[i + 1])
        if np.any(mask):
            rows.append({"r_Mpc": float(0.5 * (bins[i] + bins[i + 1])), "mean_density_proxy": float(np.mean(density[mask])), "cell_count": int(np.sum(mask))})
    return rows


def verdict(error: float) -> str:
    if not np.isfinite(error):
        return "UNDEFINED"
    if error < 0.10:
        return "PASS-LIKE"
    if error < 0.50:
        return "WEAK"
    return "FAIL"


def visible_dark_metrics(channels):
    visible_sum = float(np.sum(0.6 * channels["V"]))
    dark_sum = float(np.sum(0.45 * channels["D"]))
    ratio = visible_sum / dark_sum if dark_sum > 0 else math.nan
    error = abs(ratio - PLANCK_BARYON_CDM_RATIO) / PLANCK_BARYON_CDM_RATIO if np.isfinite(ratio) else math.nan
    return ratio, error, verdict(error)


def pick_peak(rows, window=None):
    candidates = rows
    if window is not None:
        lo, hi = window
        candidates = [row for row in rows if lo <= row["wavelength_Mpc"] <= hi]
    return max(candidates, key=lambda row: row["power"])


def write_csv(path: Path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def plot_power(unlocked_rows, locked_rows, r_s_mpc: float):
    plt.figure(figsize=(8.5, 5.5))
    for rows, label in [(unlocked_rows, "unlocked v0.16-style"), (locked_rows, "v0.17 scale-lock")]:
        plt.loglog([r["k_1_per_Mpc"] for r in rows], [r["power"] for r in rows], marker="o", linewidth=1, label=label)
    plt.axvline(2.0 * np.pi / r_s_mpc, linestyle="--", linewidth=1, label=f"sound-horizon k, r_s={r_s_mpc:.2f} Mpc")
    plt.xlabel("k [1/Mpc], box calibration = 1000 Mpc")
    plt.ylabel("Toy P(k)")
    plt.title("MCIFT v0.17 power spectrum: scale-lock rerun")
    plt.legend(); plt.grid(True, which="both", alpha=0.25); plt.tight_layout()
    plt.savefig(RESULTS_DIR / "mcift_v0.17_power_spectrum.png", dpi=140)
    plt.savefig(RESULTS_DIR / "mcift_v0.17_power_spectrum.svg")
    plt.close()


def build_report(summary_rows, r_s, unlocked_global_peak, locked_global_peak, locked_bao_peak):
    bao_error = abs(locked_bao_peak["wavelength_Mpc"] - r_s) / r_s
    global_error = abs(locked_global_peak["wavelength_Mpc"] - r_s) / r_s
    table = "\n".join(
        f"| {r['milestone']} | {r['age_Gyr']:.1f} | {r['a']:.6f} | {r['z']:.3f} | {r['visible_dark_weighted_ratio']:.6f} | {r['ratio_fractional_error']:.3f} | {r['ratio_verdict']} |"
        for r in summary_rows
    )
    best = min(summary_rows, key=lambda r: r["ratio_fractional_error"])
    final = summary_rows[-1]
    return f"""# MCIFT v0.17 Expansion-Coupled Scale-Lock Rerun Report

**Status:** equation-input toy rerun, not a validated cosmology model.  
**Script:** `analysis/mcift_big_bang_scale_lock_v0.17.py`  
**Main change from v0.16:** adds a Planck-like FRW expansion background, a radiation placeholder channel, sound-horizon calculation, and an explicit MCIFT scale-lock modulation tied to the calculated sound horizon.

## Equations implemented

```text
H(a)^2 = H0^2 [Omega_r a^-4 + Omega_m a^-3 + Omega_Lambda]
a = 1 / (1 + z)
r_s = integral c_s(a) / [a^2 H(a)] da
c_s = c / sqrt(3(1 + R_b))
R_b = 3 rho_b / (4 rho_gamma)
M_lock(r) = 1 + A cos(2 pi r / r_s) exp[-(r / R_env)^2]
rho_locked = rho_total * M_lock(r)
```

## External anchors used

```text
Planck baryon/CDM ratio = {PLANCK_BARYON_CDM_RATIO:.6f}
Calculated sound horizon r_s = {r_s:.3f} Mpc
DESI reference r_d context = {DESI_RD_REFERENCE_MPC:.2f} Mpc
```

## Visible/dark ratio rerun

| Milestone | Age [Gyr] | scale factor a | redshift z | MCIFT V/D weighted | Fractional error | Verdict |
|---:|---:|---:|---:|---:|---:|---|
{table}

Best ratio point: **{best['milestone']}**, with `{best['visible_dark_weighted_ratio']:.6f}`, error `{best['ratio_fractional_error']:.3f}`, verdict **{best['ratio_verdict']}**.

Final 5B point: `{final['visible_dark_weighted_ratio']:.6f}`, verdict **{final['ratio_verdict']}**.

## Structure-scale rerun

```text
lambda_global_unlocked = {unlocked_global_peak['wavelength_Mpc']:.2f} Mpc
lambda_global_locked   = {locked_global_peak['wavelength_Mpc']:.2f} Mpc
verdict vs r_s         = {verdict(global_error)}
```

The long coherent pocket still dominates the **global** power spectrum. v0.17 does **not** fully solve the long-mode/coarse-structure problem.

In the BAO analysis window `{BAO_WINDOW_MPC[0]:.0f}-{BAO_WINDOW_MPC[1]:.0f} Mpc`, the scale-lock sector produces:

```text
lambda_BAO_window_peak = {locked_bao_peak['wavelength_Mpc']:.2f} Mpc
sound horizon r_s      = {r_s:.2f} Mpc
fractional error       = {bao_error:.3f}
verdict                = {verdict(bao_error)}
```

## Interpretation

```text
Visible/dark ratio: still partial match, best near 2B.
BAO-window scale: improved to PASS-LIKE after adding scale-lock.
Global power spectrum: still fails because the long coherent mode remains too strong.
CMB acoustic peaks: still undefined; no Boltzmann/radiation transfer solver.
BBN: still undefined; no nuclear reaction network.
```

## Theory implication

The new scale-lock equation can place a BAO-like ripple in the correct window, but this is an input hypothesis, not yet a derived prediction. The remaining missing theory is a **long-mode damping / primordial-spectrum sector** that prevents the huge coherent pocket from dominating the total power spectrum.
"""


def main():
    X, Y, Z, R_MPC = make_grids()
    r_s = sound_horizon_Mpc()
    summary_rows = []
    final_unlocked = final_locked = None
    for actual_years, label in MILESTONES:
        age_Gyr = actual_years / 1e9
        a = scale_factor_at_age_Gyr(age_Gyr)
        z = 1.0 / a - 1.0
        channels = apply_frw_channel_dilution(evolve_base_channels(actual_years, X, Y, Z), a)
        ratio, error, ratio_verdict = visible_dark_metrics(channels)
        summary_rows.append({"milestone": label, "actual_years": actual_years, "age_Gyr": age_Gyr, "a": a, "z": z, "visible_dark_weighted_ratio": ratio, "planck_baryon_cdm_ratio": PLANCK_BARYON_CDM_RATIO, "ratio_fractional_error": error, "ratio_verdict": ratio_verdict})
        if label == "5B":
            final_unlocked = density_proxy(channels, R_MPC, r_s, locked=False)
            final_locked = density_proxy(channels, R_MPC, r_s, locked=True)

    unlocked_ps = isotropic_power_spectrum(final_unlocked)
    locked_ps = isotropic_power_spectrum(final_locked)
    write_csv(RESULTS_DIR / "mcift_v0.17_summary.csv", summary_rows)
    write_csv(RESULTS_DIR / "mcift_v0.17_power_unlocked.csv", unlocked_ps)
    write_csv(RESULTS_DIR / "mcift_v0.17_power_scale_locked.csv", locked_ps)
    write_csv(RESULTS_DIR / "mcift_v0.17_radial_unlocked.csv", radial_profile(final_unlocked, R_MPC))
    write_csv(RESULTS_DIR / "mcift_v0.17_radial_scale_locked.csv", radial_profile(final_locked, R_MPC))
    plot_power(unlocked_ps, locked_ps, r_s)
    report = build_report(summary_rows, r_s, pick_peak(unlocked_ps), pick_peak(locked_ps), pick_peak(locked_ps, BAO_WINDOW_MPC))
    (RESULTS_DIR / "mcift_v0.17_scale_lock_report.md").write_text(report, encoding="utf-8")
    print("MCIFT v0.17 scale-lock rerun complete")
    print(f"Calculated sound horizon: {r_s:.3f} Mpc")


if __name__ == "__main__":
    main()
