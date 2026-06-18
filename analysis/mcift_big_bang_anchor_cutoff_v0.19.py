#!/usr/bin/env python3
"""MCIFT v0.19 anchor-derived cutoff rerun.

Derives k_cut from the MCIFT anchor/coherence channel instead of fitting it:
    R_A(a) = sqrt(sum(r^2 rho_A) / sum(rho_A))
    k_cut(a) = 2*pi / R_A(a)
    p = N_dark_sinks = 4
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
OUT = BASE / "results_v0.19"
OUT.mkdir(parents=True, exist_ok=True)
N_S = 0.965
K_PIVOT = 0.05
P_DARK_SINKS = 4.0


def anchor_radius(channels, r_mpc):
    rho_a = np.maximum(channels["A"], 0.0)
    return float(np.sqrt(np.sum(r_mpc**2 * rho_a) / np.sum(rho_a)))


def k_cut_from_anchor(channels, r_mpc):
    return float(2.0 * np.pi / anchor_radius(channels, r_mpc))


def gate(k, k_cut):
    g = 1.0 - np.exp(-((k / k_cut) ** P_DARK_SINKS))
    t = np.ones_like(k)
    mask = k > 0
    t[mask] = (k[mask] / K_PIVOT) ** ((N_S - 1.0) / 2.0)
    return g * t


def damp_density(density, k_cut):
    mean = float(np.mean(density))
    delta = density / mean - 1.0
    fft = np.fft.fftn(delta)
    n = density.shape[0]
    spacing = v17["BOX_SIZE_MPC"] / n
    k1 = 2.0 * np.pi * np.fft.fftfreq(n, d=spacing)
    kx, ky, kz = np.meshgrid(k1, k1, k1, indexing="ij")
    kval = np.sqrt(kx**2 + ky**2 + kz**2)
    g = gate(kval, k_cut)
    g[kval == 0] = 0.0
    out = np.fft.ifftn(fft * g).real
    return np.maximum(mean * (1.0 + out), 1e-9 * mean)


def rows_to_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)


def verdict(error):
    return v17["verdict_fractional_error"](error)


def main():
    X, Y, Z, R = v17["make_grids"]()
    r_s = v17["sound_horizon_Mpc"]()
    summary = []
    final_channels = final_locked = None
    for years, label in v17["MILESTONES"]:
        age = years / 1e9
        a = v17["scale_factor_at_age_Gyr"](age)
        z = 1.0 / a - 1.0
        ch = v17["apply_frw_channel_dilution"](v17["evolve_base_channels"](years, X, Y, Z), a)
        ratio, err, vdict = v17["visible_dark_metrics"](ch)
        r_a = anchor_radius(ch, R)
        k_cut = k_cut_from_anchor(ch, R)
        summary.append({"milestone": label, "actual_years": years, "age_Gyr": age, "a": a, "z": z, "visible_dark_weighted_ratio": ratio, "planck_baryon_cdm_ratio": v17["PLANCK_BARYON_CDM_RATIO"], "ratio_fractional_error": err, "ratio_verdict": vdict, "anchor_radius_Mpc": r_a, "derived_k_cut_1_per_Mpc": k_cut, "damping_power": P_DARK_SINKS})
        if label == "5B":
            final_channels = ch
            final_locked = v17["density_proxy"](ch, R, r_s, locked=True)
    r_a = anchor_radius(final_channels, R)
    k_cut = k_cut_from_anchor(final_channels, R)
    damped = damp_density(final_locked, k_cut)
    ref_ps = v17["isotropic_power_spectrum"](final_locked)
    damp_ps = v17["isotropic_power_spectrum"](damped)
    ref_global = v17["pick_peak"](ref_ps)
    ref_bao = v17["pick_peak"](ref_ps, v17["BAO_WINDOW_MPC"])
    global_peak = v17["pick_peak"](damp_ps)
    bao_peak = v17["pick_peak"](damp_ps, v17["BAO_WINDOW_MPC"])
    gerr = abs(global_peak["wavelength_Mpc"] - r_s) / r_s
    berr = abs(bao_peak["wavelength_Mpc"] - r_s) / r_s
    metrics = [
        {"metric": "reference_global_peak", "value": ref_global["wavelength_Mpc"], "unit": "Mpc", "verdict": "FAIL"},
        {"metric": "reference_BAO_window_peak", "value": ref_bao["wavelength_Mpc"], "unit": "Mpc", "verdict": "PASS-LIKE"},
        {"metric": "v0.19_global_peak", "value": global_peak["wavelength_Mpc"], "unit": "Mpc", "verdict": verdict(gerr)},
        {"metric": "v0.19_BAO_window_peak", "value": bao_peak["wavelength_Mpc"], "unit": "Mpc", "verdict": verdict(berr)},
        {"metric": "sound_horizon_rs", "value": r_s, "unit": "Mpc", "verdict": "reference"},
        {"metric": "anchor_radius_R_A_5B", "value": r_a, "unit": "Mpc", "verdict": "derived"},
        {"metric": "derived_k_cut_5B", "value": k_cut, "unit": "1/Mpc", "verdict": "derived_not_fit"},
        {"metric": "damping_power", "value": P_DARK_SINKS, "unit": "dimensionless", "verdict": "derived_from_4_dark_sinks"},
        {"metric": "global_fractional_error", "value": gerr, "unit": "ratio", "verdict": verdict(gerr)},
        {"metric": "BAO_window_fractional_error", "value": berr, "unit": "ratio", "verdict": verdict(berr)},
    ]
    rows_to_csv(OUT / "mcift_v0.19_summary.csv", summary)
    rows_to_csv(OUT / "mcift_v0.19_structure_metrics.csv", metrics)
    rows_to_csv(OUT / "mcift_v0.19_power_anchor_damped.csv", damp_ps)
    plt.figure(figsize=(8, 5)); plt.loglog([r["k_1_per_Mpc"] for r in ref_ps], [r["power"] for r in ref_ps], marker="o", label="reference"); plt.loglog([r["k_1_per_Mpc"] for r in damp_ps], [r["power"] for r in damp_ps], marker="o", label="anchor cutoff"); plt.axvline(2*np.pi/r_s, linestyle="--", label="sound-horizon k"); plt.axvline(k_cut, linestyle=":", label="derived k_cut"); plt.legend(); plt.tight_layout(); plt.savefig(OUT / "mcift_v0.19_power_spectrum.png", dpi=140); plt.close()
    print(f"R_A(5B)={r_a:.3f} Mpc")
    print(f"k_cut(5B)={k_cut:.6f} 1/Mpc")
    print(f"global_peak={global_peak['wavelength_Mpc']:.2f} Mpc, verdict={verdict(gerr)}")


if __name__ == "__main__":
    main()
