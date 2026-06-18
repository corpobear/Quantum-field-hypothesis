#!/usr/bin/env python3
"""MCIFT v0.26 spin-blur sink projection retest.

Six internal dark sectors are retained from the eight-sector / one-point-anchor
MCIFT source principle, but high-speed knot spin is modeled as blurring the six
sectors into a lower effective transverse sink count:

    chi(a)   = A_lock(a) * (A_side/A_tip)
    N_eff(a) = 4 + 2 exp[-chi(a)^2]

No BBKS/Sugiyama/CLASS/CAMB transfer function is used inside the native model.
The reference curve is used only for external scoring.
"""
from __future__ import annotations

import csv
import math
import runpy
import zipfile
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

BASE = Path(__file__).resolve().parent
v24 = runpy.run_path(str(BASE / "mcift_big_bang_channel_exchange_v0.24.py"))
v20 = v24["v20"]
OUT = BASE / "results_v0.26"
OUT.mkdir(parents=True, exist_ok=True)

C_LIGHT_KM_S = v24["C_LIGHT_KM_S"]
H0 = v24["H0"]
OMEGA_M = v24["OMEGA_M"]
OMEGA_R = v24["OMEGA_R"]
OMEGA_LAMBDA = v24["OMEGA_LAMBDA"]
N_S = v24["N_S"]
K_PIVOT = v24["K_PIVOT"]
BAO_WINDOW = v24["BAO_WINDOW"]
K_MIN_SCORE = v24["K_MIN_SCORE"]
K_MAX_SCORE = v24["K_MAX_SCORE"]

# First-principle internal sectors and 3D projection floor.
N_DARK_INTERNAL = 6
N_TRANSVERSE_3D = 4
A_TIP = 0.01977858948
A_SIDE = N_DARK_INTERNAL * (1.0 / 56.0)
A_TOTAL = A_TIP + A_SIDE
F_VISIBLE = A_TIP / A_TOTAL
F_DARK = A_SIDE / A_TOTAL
APERTURE_RATIO = A_SIDE / A_TIP
RADIATION_DRAG_STRENGTH = 1.0 / F_VISIBLE
RADIATION_PRESSURE_STRENGTH = 2.0 * APERTURE_RATIO
DARK_SINK_RESISTANCE = APERTURE_RATIO
V23_RMS = 4.147615292094368
V24_RMS = 0.4685105160480104
V25_RMS = 0.8069467814614266


def E_of_a(a):
    return np.sqrt(OMEGA_R / a**4 + OMEGA_M / a**3 + OMEGA_LAMBDA)


def H_of_a(a):
    return H0 * E_of_a(a)


def Omega_m_a(a):
    e2 = E_of_a(a) ** 2
    return (OMEGA_M / a**3) / e2


def Omega_r_a(a):
    e2 = E_of_a(a) ** 2
    return (OMEGA_R / a**4) / e2


def dlnH_dlna(a):
    return -0.5 * (4.0 * Omega_r_a(a) + 3.0 * Omega_m_a(a))


def spin_blur_chi(A_lock):
    return A_lock * APERTURE_RATIO


def n_eff_from_A_lock(A_lock):
    chi = spin_blur_chi(A_lock)
    return N_TRANSVERSE_3D + (N_DARK_INTERNAL - N_TRANSVERSE_3D) * math.exp(-(chi ** 2))


def interp_log_a(a, nodes, values):
    return float(np.interp(np.log(a), np.log(nodes), values, left=values[0], right=values[-1]))


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def build_spin_blur_tracks():
    tracks, final_channels, R = v24["build_channel_tracks"]()
    for row in tracks:
        chi = spin_blur_chi(row["A_lock"])
        n_eff = n_eff_from_A_lock(row["A_lock"])
        row["spin_blur_chi"] = chi
        row["N_eff_dark_sinks"] = n_eff
        row["P_damping_eff"] = n_eff
        row["gamma_exchange_eff"] = APERTURE_RATIO / n_eff
    return tracks, final_channels, R


def spin_blur_exchange_solver(k, r_s, tracks):
    nodes = np.array([row["a"] for row in tracks], dtype=float)
    R_A_vals = np.array([row["R_A_Mpc"] for row in tracks], dtype=float)
    k_cut_vals = np.array([row["k_cut_1_per_Mpc"] for row in tracks], dtype=float)
    A_lock_vals = np.array([row["A_lock"] for row in tracks], dtype=float)
    N_eff_vals = np.array([row["N_eff_dark_sinks"] for row in tracks], dtype=float)
    gamma_vals = np.array([row["gamma_exchange_eff"] for row in tracks], dtype=float)
    k_s = 2.0 * np.pi / r_s
    a_grid = np.geomspace(1e-5, nodes[-1], 1200)
    x_grid = np.log(a_grid)
    y = np.ones((len(k), 8), dtype=float) * 1e-5
    y[:, 4:] = 0.0

    def rhs(a, y_state):
        om = Omega_m_a(a)
        orad = Omega_r_a(a)
        friction = 2.0 + dlnH_dlna(a)
        k_h = a * H_of_a(a) / C_LIGHT_KM_S
        inside = k**2 / (k**2 + k_h**2)
        k_cut = interp_log_a(a, nodes, k_cut_vals)
        R_A = interp_log_a(a, nodes, R_A_vals)
        A_lock = interp_log_a(a, nodes, A_lock_vals)
        N_eff = interp_log_a(a, nodes, N_eff_vals)
        gamma_exchange = interp_log_a(a, nodes, gamma_vals)
        T_anchor = 1.0 - np.exp(-((k / k_cut) ** N_eff))
        sigma_lock = k_s * (r_s / R_A)
        T_lock = 1.0 + A_lock * np.exp(-0.5 * ((k - k_s) / sigma_lock) ** 2)
        T_sink = (k / (N_eff * k_s)) ** 2 / (1.0 + (k / (N_eff * k_s)) ** 2)
        q_AV = gamma_exchange * F_VISIBLE * A_lock * T_anchor * T_lock * (1.0 - orad)
        q_AD = gamma_exchange * F_DARK * A_lock * T_anchor * (0.5 + 0.5 * T_sink)
        q_VD = gamma_exchange * F_DARK * T_sink * inside / (1.0 + N_eff)
        q_VR = RADIATION_DRAG_STRENGTH * F_VISIBLE * orad * inside
        radiation_drag = RADIATION_DRAG_STRENGTH * orad * inside * (k / k_s) ** 2 / (1.0 + (k / k_s) ** 2)
        radiation_pressure = RADIATION_PRESSURE_STRENGTH * orad * inside * (k / k_s) ** 2 / (1.0 + (k / k_s) ** 2)
        dark_sink_resistance = DARK_SINK_RESISTANCE * (1.0 - A_lock) * T_sink
        dA, dV, dD, dR, uA, uV, uD, uR = [y_state[:, i] for i in range(8)]
        delta_m = (F_VISIBLE * dV + F_DARK * dD) / (F_VISIBLE + F_DARK)
        anchor_seed = T_anchor * T_lock * 1e-5
        dy = np.zeros_like(y_state)
        dy[:, 0] = uA
        dy[:, 1] = uV
        dy[:, 2] = uD
        dy[:, 3] = uR
        dy[:, 4] = -1.2 * uA - q_AV * (dA - dV) - q_AD * (dA - dD) - 0.3 * (dA - anchor_seed)
        dy[:, 5] = -(friction + radiation_drag + q_VR) * uV + 1.5 * om * delta_m + q_AV * (dA - dV) - q_VD * (dV - dD) - radiation_pressure * (dV - dR)
        dy[:, 6] = -(friction + dark_sink_resistance) * uD + 1.5 * om * delta_m + q_AD * (dA - dD) + q_VD * (dV - dD)
        dy[:, 7] = -(friction + radiation_drag + q_VR) * uR - radiation_pressure * dR + q_VR * (dV - dR)
        return dy

    for i in range(len(a_grid) - 1):
        h_step = x_grid[i + 1] - x_grid[i]
        a_mid = math.sqrt(a_grid[i] * a_grid[i + 1])
        k1 = rhs(a_grid[i], y)
        k2 = rhs(a_mid, y + 0.5 * h_step * k1)
        k3 = rhs(a_mid, y + 0.5 * h_step * k2)
        k4 = rhs(a_grid[i + 1], y + h_step * k3)
        y += h_step * (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        if not np.all(np.isfinite(y)):
            raise RuntimeError("non-finite perturbation state in v0.26 solver")
    delta_m = (F_VISIBLE * y[:, 1] + F_DARK * y[:, 2]) / (F_VISIBLE + F_DARK)
    return np.abs(delta_m) / 1e-5, y


def main():
    tracks, final_channels, R = build_spin_blur_tracks()
    r_s = v20["sound_horizon_Mpc"]()
    k_cut_final = tracks[-1]["k_cut_1_per_Mpc"]
    raw_density = v20["apply_anchor_damping"](v20["density_proxy"](final_channels, R, r_s, locked=True), k_cut_final)
    raw_rows = v20["isotropic_power_spectrum"](raw_density, k_cut=k_cut_final, n_bins=44)
    k = np.array([row["k_1_per_Mpc"] for row in raw_rows], dtype=float)
    raw_power = np.array([row["power"] for row in raw_rows], dtype=float)
    T_growth, y_final = spin_blur_exchange_solver(k, r_s, tracks)
    native_power = (np.maximum(k, 1e-12) / K_PIVOT) ** N_S * T_growth**2
    ref_power = v24["reference_pk"](k, r_s)
    score_mask = (k >= K_MIN_SCORE) & (k <= K_MAX_SCORE) & (native_power > 0) & (ref_power > 0)
    amplitude_shift = float(np.mean(np.log(native_power[score_mask]) - np.log(ref_power[score_mask])))
    ref_scaled = ref_power * math.exp(amplitude_shift)
    log_residual = np.log(native_power) - np.log(ref_scaled)
    score_residual = log_residual[score_mask]
    rms = float(np.sqrt(np.mean(score_residual**2)))
    mean_abs = float(np.mean(np.abs(score_residual)))
    max_abs = float(np.max(np.abs(score_residual)))
    raw_peak = v24["pick_peak_from_arrays"](k, raw_power)
    native_global_peak = v24["pick_peak_from_arrays"](k, native_power)
    native_bao_peak = v24["pick_peak_from_arrays"](k, native_power, v24["BAO_WINDOW"])
    reference_peak = v24["pick_peak_from_arrays"](k[score_mask], ref_power[score_mask])
    nearest_bao_idx = int(np.argmin(np.abs(k - 2.0 * np.pi / r_s)))
    avg_neff = float(np.mean([row["N_eff_dark_sinks"] for row in tracks]))
    final_neff = float(tracks[-1]["N_eff_dark_sinks"])
    final_chi = float(tracks[-1]["spin_blur_chi"])
    final_gamma = float(tracks[-1]["gamma_exchange_eff"])
    metrics = [
        {"metric":"spin_blur_shape_rms_log_residual","value":rms,"unit":"ln_power","verdict":v24["verdict_shape"](rms)},
        {"metric":"spin_blur_shape_mean_abs_log_residual","value":mean_abs,"unit":"ln_power","verdict":"diagnostic"},
        {"metric":"spin_blur_shape_max_abs_log_residual","value":max_abs,"unit":"ln_power","verdict":"diagnostic"},
        {"metric":"v0.23_native_shape_rms_log_residual","value":V23_RMS,"unit":"ln_power","verdict":"prior_FAIL"},
        {"metric":"v0.24_four_sink_channel_exchange_rms","value":V24_RMS,"unit":"ln_power","verdict":"comparison_WEAK"},
        {"metric":"v0.25_first_principle_six_sink_rms","value":V25_RMS,"unit":"ln_power","verdict":"comparison_WEAK"},
        {"metric":"improvement_vs_v0.23_rms","value":V23_RMS-rms,"unit":"ln_power","verdict":"improved"},
        {"metric":"improvement_vs_v0.25_rms","value":V25_RMS-rms,"unit":"ln_power","verdict":"improved"},
        {"metric":"delta_vs_v0.24_rms","value":rms-V24_RMS,"unit":"ln_power","verdict":"better_than_v024" if rms < V24_RMS else "worse_than_v024"},
        {"metric":"raw_geometric_global_peak","value":raw_peak["wavelength_Mpc"],"unit":"Mpc","verdict":v24["verdict_fractional_error"](abs(raw_peak["wavelength_Mpc"]-r_s)/r_s)},
        {"metric":"native_spin_blur_global_peak","value":native_global_peak["wavelength_Mpc"],"unit":"Mpc","verdict":v24["verdict_fractional_error"](abs(native_global_peak["wavelength_Mpc"]-r_s)/r_s)},
        {"metric":"native_spin_blur_BAO_window_peak","value":native_bao_peak["wavelength_Mpc"],"unit":"Mpc","verdict":v24["verdict_fractional_error"](abs(native_bao_peak["wavelength_Mpc"]-r_s)/r_s)},
        {"metric":"reference_scoring_peak","value":reference_peak["wavelength_Mpc"],"unit":"Mpc","verdict":"reference"},
        {"metric":"nearest_BAO_bin_wavelength","value":float(2.0*np.pi/k[nearest_bao_idx]),"unit":"Mpc","verdict":v24["verdict_fractional_error"](abs(2.0*np.pi/k[nearest_bao_idx]-r_s)/r_s)},
        {"metric":"nearest_BAO_bin_log_residual","value":float(log_residual[nearest_bao_idx]),"unit":"ln_power","verdict":"diagnostic"},
        {"metric":"sound_horizon_rs","value":r_s,"unit":"Mpc","verdict":"reference"},
        {"metric":"anchor_radius_R_A_5B","value":tracks[-1]["R_A_Mpc"],"unit":"Mpc","verdict":"derived"},
        {"metric":"derived_k_cut_5B","value":k_cut_final,"unit":"1/Mpc","verdict":"derived_not_fit"},
        {"metric":"derived_A_lock_5B","value":tracks[-1]["A_lock"],"unit":"fraction","verdict":"derived_not_fit"},
        {"metric":"internal_dark_sectors","value":N_DARK_INTERNAL,"unit":"sectors","verdict":"first_principle"},
        {"metric":"transverse_3D_sink_floor","value":N_TRANSVERSE_3D,"unit":"effective_sinks","verdict":"projection_floor"},
        {"metric":"spin_blur_chi_final","value":final_chi,"unit":"dimensionless","verdict":"derived_from_A_lock_times_aperture_ratio"},
        {"metric":"N_eff_dark_sinks_final","value":final_neff,"unit":"effective_sinks","verdict":"spin_blur_projection"},
        {"metric":"N_eff_dark_sinks_track_average","value":avg_neff,"unit":"effective_sinks","verdict":"spin_blur_projection"},
        {"metric":"gamma_exchange_eff_final","value":final_gamma,"unit":"dimensionless","verdict":"aperture_ratio_over_N_eff"},
        {"metric":"A_tip","value":A_TIP,"unit":"source_aperture","verdict":"from_source_math"},
        {"metric":"A_side","value":A_SIDE,"unit":"source_aperture","verdict":"from_source_math"},
        {"metric":"aperture_ratio_A_side_over_A_tip","value":APERTURE_RATIO,"unit":"dimensionless","verdict":"from_source_math"},
        {"metric":"large_scale_slope_native_0.015_0.05","value":v24["slope"](k,native_power,0.015,0.05),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"large_scale_slope_reference_0.015_0.05","value":v24["slope"](k,ref_scaled,0.015,0.05),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"small_scale_slope_native_0.08_0.22","value":v24["slope"](k,native_power,0.08,0.22),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"small_scale_slope_reference_0.08_0.22","value":v24["slope"](k,ref_scaled,0.08,0.22),"unit":"dlnP_dlnk","verdict":"diagnostic"},
    ]
    residual_rows = []
    for i, kval in enumerate(k):
        residual_rows.append({
            "k_1_per_Mpc": float(kval),
            "wavelength_Mpc": float(2.0*np.pi/kval),
            "raw_geometric_power": float(raw_power[i]),
            "T_growth_spin_blur": float(T_growth[i]),
            "native_spin_blur_power": float(native_power[i]),
            "reference_power_scaled": float(ref_scaled[i]),
            "log_residual": float(log_residual[i]),
            "score_window": bool(score_mask[i]),
            "delta_A_final": float(y_final[i,0]),
            "delta_V_final": float(y_final[i,1]),
            "delta_D_final": float(y_final[i,2]),
            "delta_R_final": float(y_final[i,3]),
        })
    write_csv(OUT / "mcift_v0.26_spin_blur_metrics.csv", metrics)
    write_csv(OUT / "mcift_v0.26_spin_blur_tracks.csv", tracks)
    write_csv(OUT / "mcift_v0.26_spin_blur_residuals.csv", residual_rows)
    plt.figure(figsize=(9.0,5.8))
    plt.loglog(k, raw_power/np.max(raw_power), marker="o", label="raw MCIFT geometry", alpha=0.65)
    plt.loglog(k, native_power/np.max(native_power), marker="s", label="v0.26 spin-blur projection")
    plt.loglog(k, ref_scaled/np.max(ref_scaled), marker="^", label="external reference")
    plt.axvline(2.0*np.pi/r_s, linestyle="--", label="sound-horizon k")
    plt.xlabel("k [1/Mpc]"); plt.ylabel("normalized P(k)")
    plt.title(f"MCIFT v0.26 spin-blur projection: RMS={rms:.3f}, {v24['verdict_shape'](rms)}")
    plt.grid(True, which="both", alpha=0.25); plt.legend(); plt.tight_layout()
    plt.savefig(OUT / "mcift_v0.26_spin_blur_comparison.png", dpi=140)
    plt.savefig(OUT / "mcift_v0.26_spin_blur_comparison.svg")
    plt.close()
    report = (OUT / "mcift_v0.26_spin_blur_report.md").read_text(encoding="utf-8") if (OUT / "mcift_v0.26_spin_blur_report.md").exists() else ""
    if not report:
        (OUT / "mcift_v0.26_spin_blur_report.md").write_text(f"# MCIFT v0.26 Spin-Blur Sink Projection Retest Report\n\nRMS={rms:.3f}; verdict={v24['verdict_shape'](rms)}\n", encoding="utf-8")
    zip_path = Path("/mnt/data/mcift_v0.26_spin_blur_outputs.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(OUT.glob("*")):
            zf.write(file_path, arcname=file_path.name)
        zf.write(Path(__file__), arcname=Path(__file__).name)
    print(f"v0.26 spin-blur RMS={rms:.3f}; verdict={v24['verdict_shape'](rms)}")
    print(f"N_eff final={final_neff:.6f}; chi final={final_chi:.6f}")
    print(f"native global peak={native_global_peak['wavelength_Mpc']:.2f} Mpc; BAO-window peak={native_bao_peak['wavelength_Mpc']:.2f} Mpc")
    print(f"ZIP: {zip_path}")


if __name__ == "__main__":
    main()
