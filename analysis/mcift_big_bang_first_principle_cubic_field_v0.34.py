#!/usr/bin/env python3
"""MCIFT v0.34 first-principle cubic field toy solver.

Runs the v0.33 node-link-face-cell formula on the existing v0.28 toy P(k)
scaffold. This is a speculative scaffold, not established physics.
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
OUT = BASE / "results_v0.34"
OUT.mkdir(parents=True, exist_ok=True)

MODE_N = 4
C_N = 2 ** MODE_N
V30_RMS = 0.3028594438300792
V30_TRANSFER_617 = 0.5587022886073253
SOUND_HORIZON_RS = 147.1106663020041
DIRECTIONS = ["+x", "-x", "+y", "-y", "+z", "-z"]
PAIRS = [("+x", "-x"), ("+y", "-y"), ("+z", "-z")]


def sigmoid(x: float, kappa: float = 6.0) -> float:
    return 0.5 * (1.0 + math.tanh(kappa * x))


def verdict_shape(rms: float) -> str:
    return "PASS-LIKE" if rms <= 0.35 else "WEAK" if rms <= 0.75 else "FAIL"


def verdict_peak(wavelength: float) -> str:
    frac = abs(wavelength - SOUND_HORIZON_RS) / SOUND_HORIZON_RS
    return "PASS-LIKE" if frac <= 0.05 else "WEAK" if frac <= 0.20 else "FAIL"


def peak(k: np.ndarray, wavelength: np.ndarray, power: np.ndarray, lo=None, hi=None):
    mask = np.ones_like(power, dtype=bool)
    if lo is not None:
        mask &= wavelength >= lo
    if hi is not None:
        mask &= wavelength <= hi
    idxs = np.where(mask)[0]
    idx = idxs[np.argmax(power[idxs])]
    return int(idx), float(wavelength[idx]), float(k[idx]), float(power[idx])


def slope(k: np.ndarray, power: np.ndarray, lo: float, hi: float) -> float:
    mask = (k >= lo) & (k <= hi) & (power > 0)
    return float(np.polyfit(np.log(k[mask]), np.log(power[mask]), 1)[0]) if mask.sum() >= 2 else float("nan")


def build_connectors(base: float, uncontained: float, beta_spin: float) -> dict[str, float]:
    strain = base * beta_spin * (uncontained / (1.0 + uncontained)) / 2.0
    vals = {mu: base for mu in DIRECTIONS}
    vals["+x"] = min(1.0, base + strain)
    vals["-x"] = max(0.0, base - strain)
    return vals


def connector_stats(vals: dict[str, float]) -> tuple[float, float, float]:
    a_mean = sum(vals.values()) / 6.0
    delta = math.sqrt(sum((vals[p] - vals[m]) ** 2 for p, m in PAIRS))
    coh = max(0.0, 6.0 * a_mean - delta)
    return a_mean, delta, coh


def main() -> None:
    residuals = pd.read_csv(V28 / "mcift_v0.28_thermo_spin_growth_residuals.csv")
    tracks = pd.read_csv(V28 / "mcift_v0.28_thermo_spin_growth_tracks.csv")

    k = residuals["k_1_per_Mpc"].to_numpy(float)
    wavelength = residuals["wavelength_Mpc"].to_numpy(float)
    native = residuals["native_thermo_spin_growth_power"].to_numpy(float)
    reference = residuals["reference_power_scaled"].to_numpy(float)
    raw = residuals["raw_geometric_power"].to_numpy(float)
    score = residuals["score_window"].to_numpy(bool)

    transfer = np.ones_like(wavelength, dtype=float)
    history_rows = []
    background_rows = []
    reservoir = 0.0

    for _, tr in tracks.iterrows():
        R_A = float(tr["R_A_Mpc"])
        A_lock = float(tr["A_lock"])
        W_capture = float(tr["W_capture_thermal"])
        beta_spin = float(tr["beta_spin"])
        theta_G = float(tr["theta_mass_gravity_time"])
        c_s2 = float(tr["c_s2_thermal"])
        beta_T = float(tr["beta_thermal"])
        X_containment = 1.0 + beta_spin
        epoch_load = 0.0
        for idx, lam in enumerate(wavelength):
            r = lam / R_A
            uncontained = max(0.0, r - 1.0)
            base_a = max(0.0, min(1.0, A_lock * W_capture))
            a = build_connectors(base_a, uncontained, beta_spin)
            a_mean, Delta_i, Coh_i = connector_stats(a)
            A_ij = math.sqrt(max(0.0, a_mean * a_mean))
            P_phase = math.cos(0.5 * math.pi * min(1.0, uncontained)) ** 2
            P_timing = math.exp(-((beta_T * uncontained) ** 2))
            P_match = math.exp(-(uncontained ** 2))
            chi = A_ij * P_phase * P_timing * P_match
            H = max(0.0, min(1.0, theta_G * A_lock))
            chi_c = 1.0 / math.sqrt(2.0)
            omega = H * sigmoid(chi - chi_c)
            m_i = 6.0 * omega * a_mean
            vortex_grad = 6.0 * omega * uncontained
            q_base = C_N * (1.0 + theta_G + c_s2)
            q_mass = (m_i / 6.0) * C_N * uncontained
            q_vortex = (vortex_grad / 6.0) * C_N
            q_i = q_base + q_mass + q_vortex
            capacity = 3.5 * MODE_N * X_containment * (Coh_i / 6.0)
            S_i = capacity - q_i
            pressure = max(0.0, q_i / capacity - 1.0) if capacity > 0 else 0.0
            epoch_transfer = math.exp(-pressure * uncontained * r)
            transfer[idx] *= epoch_transfer
            q_to_reservoir = max(0.0, -S_i) * uncontained / C_N
            epoch_load += q_to_reservoir
            history_rows.append({
                "milestone": tr["milestone"], "age_Gyr": float(tr["age_Gyr"]),
                "k_1_per_Mpc": float(k[idx]), "wavelength_Mpc": float(lam),
                "lambda_over_R_A": r, "uncontained_excess": uncontained,
                "a_mean": a_mean, "Delta_i": Delta_i, "Coh_i_local": Coh_i,
                "chi_i_mu": chi, "H_i_mu": H, "Omega_i_mu": omega,
                "m_i": m_i, "q_i": q_i, "coherence_capacity": capacity,
                "S_i": S_i, "collapse_pressure": pressure,
                "epoch_transfer": epoch_transfer, "cumulative_transfer": float(transfer[idx]),
                "Q_to_reservoir_mode": q_to_reservoir,
            })
        reservoir = 1.0 - (1.0 - reservoir) * math.exp(-epoch_load / max(1e-9, len(wavelength)))
        background_rows.append({
            "milestone": tr["milestone"], "age_Gyr": float(tr["age_Gyr"]), "a": float(tr["a"]),
            "reservoir_proxy": reservoir, "epoch_load_proxy": epoch_load,
            "mean_transfer": float(np.mean(transfer)), "transfer_617Mpc": float(transfer[0]),
        })

    power = native * transfer
    log_resid = np.log(power) - np.log(reference)
    rms = float(np.sqrt(np.mean(log_resid[score] ** 2)))
    mean_abs = float(np.mean(np.abs(log_resid[score])))
    max_abs = float(np.max(np.abs(log_resid[score])))
    _, v28_l, _, _ = peak(k, wavelength, native)
    _, v34_l, _, _ = peak(k, wavelength, power)
    _, bao_l, _, _ = peak(k, wavelength, power, 110.0, 190.0)
    _, raw_l, _, _ = peak(k, wavelength, raw)
    nearest = int(np.argmin(np.abs(wavelength - SOUND_HORIZON_RS)))
    hist = pd.DataFrame(history_rows)
    final_617 = hist[hist["k_1_per_Mpc"] == k[0]].iloc[-1]

    metrics = [
        ["v0.34_cubic_field_shape_rms_log_residual", rms, "ln_power", verdict_shape(rms)],
        ["v0.34_cubic_field_shape_mean_abs_log_residual", mean_abs, "ln_power", "diagnostic"],
        ["v0.34_cubic_field_shape_max_abs_log_residual", max_abs, "ln_power", "diagnostic"],
        ["v0.30_dynamic_ordered_rms", V30_RMS, "ln_power", "comparison_PASS-LIKE"],
        ["delta_vs_v0.30_rms", rms - V30_RMS, "ln_power", "scored_window_delta"],
        ["v0.28_global_peak_before_cubic_field", v28_l, "Mpc", "FAIL"],
        ["v0.34_global_peak_after_cubic_field", v34_l, "Mpc", verdict_peak(v34_l)],
        ["v0.34_BAO_window_peak", bao_l, "Mpc", verdict_peak(bao_l)],
        ["raw_geometric_global_peak", raw_l, "Mpc", verdict_peak(raw_l)],
        ["v0.34_transfer_at_617Mpc", float(transfer[0]), "power_multiplier", "mode_coupled_transfer"],
        ["v0.34_transfer_at_BAO_bin", float(transfer[nearest]), "power_multiplier", "mode_coupled_transfer"],
        ["v0.34_final_reservoir_proxy", background_rows[-1]["reservoir_proxy"], "fraction_proxy", "diagnostic"],
        ["v0.34_final_chi_617Mpc", float(final_617["chi_i_mu"]), "compatibility", "diagnostic"],
        ["v0.34_final_Omega_617Mpc", float(final_617["Omega_i_mu"]), "vortex_strength", "diagnostic"],
        ["v0.34_final_m_i_617Mpc", float(final_617["m_i"]), "mass_proxy", "diagnostic"],
        ["v0.34_final_q_i_617Mpc", float(final_617["q_i"]), "complexity_proxy", "diagnostic"],
        ["v0.34_final_Coh_capacity_617Mpc", float(final_617["coherence_capacity"]), "capacity_proxy", "diagnostic"],
        ["v0.34_final_S_i_617Mpc", float(final_617["S_i"]), "stability_proxy", "collapse_if_negative"],
        ["large_scale_slope_native_0.015_0.05", slope(k, power, 0.015, 0.05), "dlnP_dlnk", "diagnostic"],
        ["small_scale_slope_native_0.08_0.22", slope(k, power, 0.08, 0.22), "dlnP_dlnk", "diagnostic"],
    ]
    pd.DataFrame(metrics, columns=["metric", "value", "unit", "verdict"]).to_csv(OUT / "mcift_v0.34_first_principle_cubic_field_metrics.csv", index=False)
    hist.to_csv(OUT / "mcift_v0.34_first_principle_cubic_field_history.csv", index=False)
    pd.DataFrame(background_rows).to_csv(OUT / "mcift_v0.34_first_principle_cubic_field_background.csv", index=False)
    out = residuals.copy()
    out["v0.34_cubic_field_transfer"] = transfer
    out["native_v0.34_cubic_field_power"] = power
    out["v0.34_cubic_field_log_residual"] = log_resid
    out.to_csv(OUT / "mcift_v0.34_first_principle_cubic_field_residuals.csv", index=False)
    print(f"v0.34 RMS={rms:.6f}; global={v34_l:.2f} Mpc; BAO={bao_l:.2f} Mpc; transfer617={transfer[0]:.6f}")


if __name__ == "__main__":
    main()
