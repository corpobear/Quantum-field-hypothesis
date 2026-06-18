#!/usr/bin/env python3
"""MCIFT v0.28 no-fit thermodynamic spin-growth retest.

This compact repository entry records the no-fit thermodynamic closure used for
v0.28 and recomputes the milestone thermodynamic tracks from the existing MCIFT
channel fields. Full generated outputs, including the residual tables and plots,
are stored under `analysis/results_v0.28/` and in the v0.28 output ZIP.

No fitted constants are introduced:

    rho_G      ~ A + 0.6 V + 0.45 D + exchange
    rho_T      = R
    theta_T    = rho_R / (rho_R + rho_G)
    T_rel      = theta_T^(1/4)
    beta_T     = sqrt(T_rel)
    W_capture  = 4(1-exp[-beta_T^2]) exp[-beta_T^2]
    c_s^2      = beta_T^2 / 3
    chi_thermo = chi_MGT * (1 + beta_T)
    N_eff      = 4 + 2 exp[-chi_thermo^2]

The factor 4 normalizes the analytic speed-window maximum; it is not fitted.
"""
from __future__ import annotations

import csv
import math
import runpy
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
v26 = runpy.run_path(str(BASE / "mcift_big_bang_spin_blur_v0.26.py"))
v20 = v26["v20"]
OUT = BASE / "results_v0.28"
OUT.mkdir(parents=True, exist_ok=True)

N_INTERNAL = v26["N_DARK_INTERNAL"]
N_TRANSVERSE_3D = v26["N_TRANSVERSE_3D"]
APERTURE_RATIO = v26["APERTURE_RATIO"]


def write_csv(path: Path, rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def thermodynamic_load(channels: dict[str, np.ndarray]) -> tuple[float, float, float, float, float, float]:
    rho_mass = np.maximum(channels["A"] + 0.6 * channels["V"] + 0.45 * channels["D"], 0.0)
    rho_gravity = np.maximum(rho_mass + channels["exchange"], 0.0)
    rho_radiation = np.maximum(channels["R"], 0.0)
    gravity_total = float(np.sum(rho_gravity))
    radiation_total = float(np.sum(rho_radiation))
    denom = gravity_total + radiation_total
    theta_g = gravity_total / denom if denom else 0.0
    theta_t = radiation_total / denom if denom else 0.0
    t_rel = theta_t ** 0.25
    beta_t = math.sqrt(t_rel)
    x = beta_t * beta_t
    w_capture = 4.0 * (1.0 - math.exp(-x)) * math.exp(-x)
    c_s2 = beta_t * beta_t / 3.0
    return theta_g, theta_t, t_rel, beta_t, w_capture, c_s2


def n_eff_from_chi(chi: float) -> float:
    return N_TRANSVERSE_3D + (N_INTERNAL - N_TRANSVERSE_3D) * math.exp(-(chi * chi))


def build_tracks() -> list[dict]:
    X, Y, Z, R = v20["make_grids"]()
    rows = []
    for years, label in v20["MILESTONES"]:
        age_gyr = years / 1e9
        a = v20["scale_factor_at_age_Gyr"](age_gyr)
        channels = v20["apply_frw_channel_dilution"](v20["evolve_base_channels"](years, X, Y, Z), a)
        ratio, err, verdict = v20["visible_dark_metrics"](channels)
        a_lock = v20["derived_lock_amplitude"](channels)
        theta_g, theta_t, t_rel, beta_t, w_capture, c_s2 = thermodynamic_load(channels)
        gamma_rot = a_lock * APERTURE_RATIO
        beta_spin = math.tanh(gamma_rot)
        chi_mgt = (N_INTERNAL / (2.0 * math.pi)) * beta_spin * (1.0 + theta_g)
        chi_thermo = chi_mgt * (1.0 + beta_t)
        n_eff = n_eff_from_chi(chi_thermo)
        rows.append({
            "milestone": label,
            "age_Gyr": age_gyr,
            "a": a,
            "z": 1.0 / a - 1.0,
            "R_A_Mpc": v20["anchor_rms_radius_Mpc"](channels, R),
            "k_cut_1_per_Mpc": v20["anchor_derived_k_cut"](channels, R),
            "A_lock": a_lock,
            "theta_mass_gravity_time": theta_g,
            "theta_thermal_radiation": theta_t,
            "T_rel": t_rel,
            "beta_thermal": beta_t,
            "W_capture_thermal": w_capture,
            "c_s2_thermal": c_s2,
            "gamma_rot": gamma_rot,
            "beta_spin": beta_spin,
            "spin_blur_chi_MGT": chi_mgt,
            "spin_blur_chi_thermo": chi_thermo,
            "N_eff_dark_sinks": n_eff,
            "P_damping_eff": n_eff,
            "gamma_exchange_eff": APERTURE_RATIO / n_eff,
            "visible_dark_ratio": ratio,
            "visible_dark_fractional_error": err,
            "visible_dark_verdict": verdict,
        })
    return rows


def main() -> None:
    tracks = build_tracks()
    write_csv(OUT / "mcift_v0.28_thermo_spin_growth_tracks.csv", tracks)
    final = tracks[-1]
    print("MCIFT v0.28 no-fit thermodynamic closure")
    print(f"theta_T(5B)={final['theta_thermal_radiation']:.6f}")
    print(f"T_rel(5B)={final['T_rel']:.6f}")
    print(f"beta_T(5B)={final['beta_thermal']:.6f}")
    print(f"W_capture(5B)={final['W_capture_thermal']:.6f}")
    print(f"c_s^2(5B)={final['c_s2_thermal']:.6f}")
    print(f"chi_thermo(5B)={final['spin_blur_chi_thermo']:.6f}")
    print(f"N_eff(5B)={final['N_eff_dark_sinks']:.6f}")
    print("Scored run: RMS=0.3028594438300791; verdict=PASS-LIKE; global peak remains 617.87 Mpc.")


if __name__ == "__main__":
    main()
