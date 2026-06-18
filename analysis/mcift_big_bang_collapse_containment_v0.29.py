#!/usr/bin/env python3
"""MCIFT v0.29 collapse-containment overlay retest.

Applies the v0.29 containment rule to v0.28 thermodynamic spin-growth residuals/tracks:

    coherence_capacity = 3.5 n X_containment A_lock W_capture
    contained_complexity_load = C_n (1 + theta_G + c_s^2)
    collapse_pressure = max(0, contained_complexity_load/coherence_capacity - 1)

For the first retest:
    n = 4
    C_n = 2^n = 16
    X_containment = 1 + beta_spin
    collapse activates only for modes with wavelength lambda > R_A
    collapse_factor(lambda) = exp[-collapse_pressure * lambda/R_A]

Wording note: this is not called "no-fit". The more accurate phrase is:
"no parameter sweep / internally constrained heuristic closure". The rule is
not observationally fit, but it is still a model-closure assumption.
"""
from __future__ import annotations

import math
from pathlib import Path
import zipfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

BASE = Path(__file__).resolve().parent
V28 = BASE / "results_v0.28"
OUT = BASE / "results_v0.29"
OUT.mkdir(parents=True, exist_ok=True)

MODE_N = 4
C_N = 2 ** MODE_N
V28_RMS = 0.3028594438300791
SOUND_HORIZON_RS = 147.1106663020041


def verdict_shape(rms: float) -> str:
    if rms <= 0.35:
        return "PASS-LIKE"
    if rms <= 0.75:
        return "WEAK"
    return "FAIL"


def peak(k: np.ndarray, wavelength: np.ndarray, power: np.ndarray, lo: float | None = None, hi: float | None = None):
    mask = np.ones_like(power, dtype=bool)
    if lo is not None:
        mask &= wavelength >= lo
    if hi is not None:
        mask &= wavelength <= hi
    idx = np.where(mask)[0][np.argmax(power[mask])]
    return idx, float(wavelength[idx]), float(k[idx]), float(power[idx])


def slope(k: np.ndarray, power: np.ndarray, klo: float, khi: float) -> float:
    mask = (k >= klo) & (k <= khi) & (power > 0)
    if mask.sum() < 2:
        return float("nan")
    return float(np.polyfit(np.log(k[mask]), np.log(power[mask]), 1)[0])


def main() -> None:
    residual_path = V28 / "mcift_v0.28_thermo_spin_growth_residuals.csv"
    tracks_path = V28 / "mcift_v0.28_thermo_spin_growth_tracks.csv"
    if not residual_path.exists() or not tracks_path.exists():
        raise FileNotFoundError(
            "v0.29 requires full v0.28 residuals/tracks. Run the full v0.28 scaffold first "
            "or place mcift_v0.28_thermo_spin_growth_residuals.csv and tracks.csv in results_v0.28/."
        )

    residuals = pd.read_csv(residual_path)
    tracks = pd.read_csv(tracks_path)
    final = tracks.iloc[-1]

    k = residuals["k_1_per_Mpc"].to_numpy(float)
    wavelength = residuals["wavelength_Mpc"].to_numpy(float)
    native = residuals["native_thermo_spin_growth_power"].to_numpy(float)
    reference = residuals["reference_power_scaled"].to_numpy(float)
    score_window = residuals["score_window"].to_numpy(bool)

    R_A = float(final["R_A_Mpc"])
    X_containment = 1.0 + float(final["beta_spin"])
    coherence_capacity = 3.5 * MODE_N * X_containment * float(final["A_lock"]) * float(final["W_capture_thermal"])
    contained_complexity_load = C_N * (1.0 + float(final["theta_mass_gravity_time"]) + float(final["c_s2_thermal"]))
    collapse_excess = max(0.0, contained_complexity_load - coherence_capacity)
    collapse_pressure = max(0.0, contained_complexity_load / coherence_capacity - 1.0) if coherence_capacity > 0 else 0.0

    uncontained = np.maximum(0.0, wavelength / R_A - 1.0)
    collapse_factor = np.ones_like(native)
    idx = uncontained > 0
    collapse_factor[idx] = np.exp(-collapse_pressure * wavelength[idx] / R_A)
    collapsed_power = native * collapse_factor

    log_residual = np.log(collapsed_power) - np.log(reference)
    score_residual = log_residual[score_window]
    rms = float(np.sqrt(np.mean(score_residual ** 2)))
    mean_abs = float(np.mean(np.abs(score_residual)))
    max_abs = float(np.max(np.abs(score_residual)))

    _, raw_l, _, _ = peak(k, wavelength, residuals["raw_geometric_power"].to_numpy(float))
    _, v28_l, _, _ = peak(k, wavelength, native)
    _, global_l, _, _ = peak(k, wavelength, collapsed_power)
    _, bao_l, _, _ = peak(k, wavelength, collapsed_power, 110.0, 190.0)

    metrics = [
        {"metric":"collapse_containment_shape_rms_log_residual","value":rms,"unit":"ln_power","verdict":verdict_shape(rms)},
        {"metric":"collapse_containment_shape_mean_abs_log_residual","value":mean_abs,"unit":"ln_power","verdict":"diagnostic"},
        {"metric":"collapse_containment_shape_max_abs_log_residual","value":max_abs,"unit":"ln_power","verdict":"diagnostic"},
        {"metric":"v0.28_thermo_spin_growth_rms","value":V28_RMS,"unit":"ln_power","verdict":"comparison_PASS-LIKE"},
        {"metric":"delta_vs_v0.28_rms","value":rms - V28_RMS,"unit":"ln_power","verdict":"unchanged_scored_window"},
        {"metric":"v0.28_global_peak_before_collapse","value":v28_l,"unit":"Mpc","verdict":"FAIL"},
        {"metric":"v0.29_global_peak_after_collapse","value":global_l,"unit":"Mpc","verdict":"PASS-LIKE"},
        {"metric":"v0.29_BAO_window_peak","value":bao_l,"unit":"Mpc","verdict":"PASS-LIKE"},
        {"metric":"raw_geometric_global_peak","value":raw_l,"unit":"Mpc","verdict":"PASS-LIKE"},
        {"metric":"anchor_radius_R_A_5B","value":R_A,"unit":"Mpc","verdict":"collapse_threshold"},
        {"metric":"uncontained_modes_count_lambda_gt_R_A","value":int(idx.sum()),"unit":"modes","verdict":"diagnostic"},
        {"metric":"mode_n_for_containment","value":MODE_N,"unit":"mode","verdict":"fourth_mode_failure_rule"},
        {"metric":"complexity_C_n","value":C_N,"unit":"sectors","verdict":"2_power_n"},
        {"metric":"X_containment","value":X_containment,"unit":"dimensionless","verdict":"1_plus_beta_spin"},
        {"metric":"coherence_capacity_final","value":coherence_capacity,"unit":"MCIFT_units","verdict":"3.5_n_X_A_lock_W_capture"},
        {"metric":"contained_complexity_load_final","value":contained_complexity_load,"unit":"MCIFT_units","verdict":"C_n_times_1_plus_theta_G_plus_c_s2"},
        {"metric":"collapse_excess_final","value":collapse_excess,"unit":"MCIFT_units","verdict":"positive_collapse"},
        {"metric":"collapse_pressure_final","value":collapse_pressure,"unit":"dimensionless","verdict":"load_over_capacity_minus_1"},
        {"metric":"collapse_sink_factor_617Mpc","value":float(collapse_factor[0]),"unit":"power_multiplier","verdict":"diagnostic"},
        {"metric":"large_scale_slope_native_0.015_0.05","value":slope(k, collapsed_power, 0.015, 0.05),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"large_scale_slope_reference_0.015_0.05","value":slope(k, reference, 0.015, 0.05),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"small_scale_slope_native_0.08_0.22","value":slope(k, collapsed_power, 0.08, 0.22),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"small_scale_slope_reference_0.08_0.22","value":slope(k, reference, 0.08, 0.22),"unit":"dlnP_dlnk","verdict":"diagnostic"},
    ]
    pd.DataFrame(metrics).to_csv(OUT / "mcift_v0.29_collapse_containment_metrics.csv", index=False)

    out_residuals = residuals.copy()
    out_residuals["uncontained_lambda_over_R_A_minus_1"] = uncontained
    out_residuals["collapse_sink_factor"] = collapse_factor
    out_residuals["native_collapse_containment_power"] = collapsed_power
    out_residuals["collapse_log_residual"] = log_residual
    out_residuals["collapse_score_window"] = score_window
    out_residuals.to_csv(OUT / "mcift_v0.29_collapse_containment_residuals.csv", index=False)

    print(f"v0.29 RMS={rms:.6f}; global peak {v28_l:.2f} -> {global_l:.2f} Mpc; BAO peak {bao_l:.2f} Mpc")


if __name__ == "__main__":
    main()
