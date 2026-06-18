#!/usr/bin/env python3
"""MCIFT v0.25 first-principle sink-count retest.

This wraps the v0.24 coupled channel-exchange solver but replaces the inherited
four-sink Cartesian toy count with the deeper eight-sector / one-point-anchor
MCIFT sector count:

    C_3 = 8
    visible axial sector = 1
    anchor/opposite axial sector = 1
    N_dark = 8 - 1 - 1 = 6

No BBKS/Sugiyama/CLASS/CAMB transfer function is used inside the model. The
reference curve is used only for external scoring.
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
OUT = BASE / "results_v0.25"
OUT.mkdir(parents=True, exist_ok=True)

# First-principle MCIFT sector count.
C_THREE = 8
N_VISIBLE_AXIS = 1
N_ANCHOR_AXIS = 1
N_DARK_SINKS = C_THREE - N_VISIBLE_AXIS - N_ANCHOR_AXIS
P_DAMP = float(N_DARK_SINKS)

# Source-aperture math: A_tip from the existing source equation; A_side = 6*(1/56).
A_TIP = 0.01977858948
A_SIDE = N_DARK_SINKS * (1.0 / 56.0)
A_TOTAL = A_TIP + A_SIDE
F_VISIBLE = A_TIP / A_TOTAL
F_DARK = A_SIDE / A_TOTAL
APERTURE_RATIO = A_SIDE / A_TIP
GAMMA_EXCHANGE = APERTURE_RATIO / N_DARK_SINKS
RADIATION_DRAG_STRENGTH = 1.0 / F_VISIBLE
RADIATION_PRESSURE_STRENGTH = 2.0 * APERTURE_RATIO
DARK_SINK_RESISTANCE = APERTURE_RATIO

# Patch the v0.24 function globals so the same solver uses the first-principle count.
v24.update({
    "OUT": OUT,
    "N_DARK_SINKS": N_DARK_SINKS,
    "P_DAMP": P_DAMP,
    "A_TIP": A_TIP,
    "A_SIDE": A_SIDE,
    "A_TOTAL": A_TOTAL,
    "F_VISIBLE": F_VISIBLE,
    "F_DARK": F_DARK,
    "APERTURE_RATIO": APERTURE_RATIO,
    "GAMMA_EXCHANGE": GAMMA_EXCHANGE,
    "RADIATION_DRAG_STRENGTH": RADIATION_DRAG_STRENGTH,
    "RADIATION_PRESSURE_STRENGTH": RADIATION_PRESSURE_STRENGTH,
    "DARK_SINK_RESISTANCE": DARK_SINK_RESISTANCE,
})


def write_csv(path, rows):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader(); writer.writerows(rows)


def main():
    tracks, final_channels, R = v24["build_channel_tracks"]()
    r_s = v24["v20"]["sound_horizon_Mpc"]()
    k_cut_final = tracks[-1]["k_cut_1_per_Mpc"]

    raw_density = v24["v20"]["apply_anchor_damping"](
        v24["v20"]["density_proxy"](final_channels, R, r_s, locked=True),
        k_cut_final,
    )
    raw_rows = v24["v20"]["isotropic_power_spectrum"](raw_density, k_cut=k_cut_final, n_bins=44)
    k = np.array([row["k_1_per_Mpc"] for row in raw_rows], dtype=float)
    raw_power = np.array([row["power"] for row in raw_rows], dtype=float)

    T_growth, y_final = v24["derived_exchange_solver"](k, r_s, tracks)
    native_power = (np.maximum(k, 1e-12) / v24["K_PIVOT"]) ** v24["N_S"] * T_growth**2
    ref_power = v24["reference_pk"](k, r_s)
    score_mask = (k >= v24["K_MIN_SCORE"]) & (k <= v24["K_MAX_SCORE"]) & (native_power > 0) & (ref_power > 0)
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

    metrics = [
        {"metric":"first_principle_sinks_shape_rms_log_residual","value":rms,"unit":"ln_power","verdict":v24["verdict_shape"](rms)},
        {"metric":"first_principle_sinks_shape_mean_abs_log_residual","value":mean_abs,"unit":"ln_power","verdict":"diagnostic"},
        {"metric":"first_principle_sinks_shape_max_abs_log_residual","value":max_abs,"unit":"ln_power","verdict":"diagnostic"},
        {"metric":"v0.23_native_shape_rms_log_residual","value":4.147615292094368,"unit":"ln_power","verdict":"prior_FAIL"},
        {"metric":"improvement_vs_v0.23_rms","value":4.147615292094368-rms,"unit":"ln_power","verdict":"improved" if rms < 4.147615292094368 else "not_improved"},
        {"metric":"v0.24_four_sink_channel_exchange_rms","value":0.4685105160480104,"unit":"ln_power","verdict":"comparison_WEAK"},
        {"metric":"raw_geometric_global_peak","value":raw_peak["wavelength_Mpc"],"unit":"Mpc","verdict":v24["verdict_fractional_error"](abs(raw_peak["wavelength_Mpc"]-r_s)/r_s)},
        {"metric":"native_first_principle_sinks_global_peak","value":native_global_peak["wavelength_Mpc"],"unit":"Mpc","verdict":v24["verdict_fractional_error"](abs(native_global_peak["wavelength_Mpc"]-r_s)/r_s)},
        {"metric":"native_first_principle_sinks_BAO_window_peak","value":native_bao_peak["wavelength_Mpc"],"unit":"Mpc","verdict":v24["verdict_fractional_error"](abs(native_bao_peak["wavelength_Mpc"]-r_s)/r_s)},
        {"metric":"reference_scoring_peak","value":reference_peak["wavelength_Mpc"],"unit":"Mpc","verdict":"reference"},
        {"metric":"nearest_BAO_bin_wavelength","value":float(2.0*np.pi/k[nearest_bao_idx]),"unit":"Mpc","verdict":v24["verdict_fractional_error"](abs(2.0*np.pi/k[nearest_bao_idx]-r_s)/r_s)},
        {"metric":"nearest_BAO_bin_log_residual","value":float(log_residual[nearest_bao_idx]),"unit":"ln_power","verdict":"diagnostic"},
        {"metric":"sound_horizon_rs","value":r_s,"unit":"Mpc","verdict":"reference"},
        {"metric":"anchor_radius_R_A_5B","value":tracks[-1]["R_A_Mpc"],"unit":"Mpc","verdict":"derived"},
        {"metric":"derived_k_cut_5B","value":k_cut_final,"unit":"1/Mpc","verdict":"derived_not_fit"},
        {"metric":"derived_A_lock_5B","value":tracks[-1]["A_lock"],"unit":"fraction","verdict":"derived_not_fit"},
        {"metric":"C_3_sector_count","value":C_THREE,"unit":"sectors","verdict":"first_principle"},
        {"metric":"visible_axial_sector_count","value":N_VISIBLE_AXIS,"unit":"sector","verdict":"first_principle"},
        {"metric":"anchor_opposite_axial_sector_count","value":N_ANCHOR_AXIS,"unit":"sector","verdict":"first_principle"},
        {"metric":"N_dark_sinks_first_principle","value":N_DARK_SINKS,"unit":"sectors","verdict":"C3_minus_visible_minus_anchor"},
        {"metric":"A_tip","value":A_TIP,"unit":"source_aperture","verdict":"from_source_math"},
        {"metric":"A_side","value":A_SIDE,"unit":"source_aperture","verdict":"from_source_math"},
        {"metric":"aperture_ratio_A_side_over_A_tip","value":APERTURE_RATIO,"unit":"dimensionless","verdict":"from_source_math"},
        {"metric":"F_visible","value":F_VISIBLE,"unit":"fraction","verdict":"derived"},
        {"metric":"F_dark","value":F_DARK,"unit":"fraction","verdict":"derived"},
        {"metric":"gamma_exchange","value":GAMMA_EXCHANGE,"unit":"dimensionless","verdict":"A_side_over_A_tip_div_N_dark_sinks"},
        {"metric":"radiation_drag_strength","value":RADIATION_DRAG_STRENGTH,"unit":"dimensionless","verdict":"inverse_visible_fraction"},
        {"metric":"radiation_pressure_strength","value":RADIATION_PRESSURE_STRENGTH,"unit":"dimensionless","verdict":"two_transverse_modes_times_aperture_ratio"},
        {"metric":"dark_sink_resistance","value":DARK_SINK_RESISTANCE,"unit":"dimensionless","verdict":"aperture_ratio"},
        {"metric":"large_scale_slope_native_0.015_0.05","value":v24["slope"](k,native_power,0.015,0.05),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"large_scale_slope_reference_0.015_0.05","value":v24["slope"](k,ref_scaled,0.015,0.05),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"small_scale_slope_native_0.08_0.22","value":v24["slope"](k,native_power,0.08,0.22),"unit":"dlnP_dlnk","verdict":"diagnostic"},
        {"metric":"small_scale_slope_reference_0.08_0.22","value":v24["slope"](k,ref_scaled,0.08,0.22),"unit":"dlnP_dlnk","verdict":"diagnostic"},
    ]
    write_csv(OUT / "mcift_v0.25_first_principle_sinks_metrics.csv", metrics)

    residual_rows=[]
    for i,kval in enumerate(k):
        residual_rows.append({
            "k_1_per_Mpc":float(kval),
            "wavelength_Mpc":float(2.0*np.pi/kval),
            "raw_geometric_power":float(raw_power[i]),
            "T_growth_first_principle_sinks":float(T_growth[i]),
            "native_first_principle_sinks_power":float(native_power[i]),
            "reference_power_scaled":float(ref_scaled[i]),
            "log_residual":float(log_residual[i]),
            "score_window":bool(score_mask[i]),
            "delta_A_final":float(y_final[i,0]),
            "delta_V_final":float(y_final[i,1]),
            "delta_D_final":float(y_final[i,2]),
            "delta_R_final":float(y_final[i,3]),
        })
    write_csv(OUT / "mcift_v0.25_first_principle_sinks_residuals.csv", residual_rows)
    write_csv(OUT / "mcift_v0.25_first_principle_sinks_tracks.csv", tracks)

    plt.figure(figsize=(9.0,5.8))
    plt.loglog(k, raw_power/np.max(raw_power), marker="o", label="raw MCIFT geometry", alpha=0.65)
    plt.loglog(k, native_power/np.max(native_power), marker="s", label="v0.25 first-principle six sinks")
    plt.loglog(k, ref_scaled/np.max(ref_scaled), marker="^", label="external reference")
    plt.axvline(2.0*np.pi/r_s, linestyle="--", label="sound-horizon k")
    plt.xlabel("k [1/Mpc]"); plt.ylabel("normalized P(k)")
    plt.title(f"MCIFT v0.25 first-principle sinks: RMS={rms:.3f}, {v24['verdict_shape'](rms)}")
    plt.grid(True, which="both", alpha=0.25); plt.legend(); plt.tight_layout()
    plt.savefig(OUT / "mcift_v0.25_first_principle_sinks_comparison.png", dpi=140)
    plt.savefig(OUT / "mcift_v0.25_first_principle_sinks_comparison.svg")
    plt.close()

    report = f"""# MCIFT v0.25 First-Principle Six-Sink Retest Report\n\n**Status:** first-principle sink-count channel-exchange perturbation scaffold; not established physics and not a CLASS/CAMB replacement.  \n**Script:** `analysis/mcift_big_bang_first_principle_sinks_v0.25.py`  \n**Main change from v0.24:** derives the dark-sink count from the eight-sector / one-point-anchor MCIFT principle instead of inheriting the four-sink 3D Cartesian toy geometry.\n\n## First-principle sink-count derivation\n\n```text\nC_3 = 8 sectors\nvisible axial sector = 1\nanchor/opposite axial sector = 1\nN_dark_sinks = C_3 - 1 - 1 = 6\ndamping_power p = N_dark_sinks = 6\n```\n\n## Result\n\n```text\nv0.23 native-growth RMS = 4.148\nv0.24 four-sink channel-exchange RMS = 0.469\nv0.25 first-principle six-sink RMS = {rms:.3f}\nshape verdict = {v24['verdict_shape'](rms)}\nRMS improvement versus v0.23 = {4.147615292094368-rms:.3f}\n```\n\n## Scale diagnostics\n\n```text\nraw geometric global peak = {raw_peak['wavelength_Mpc']:.2f} Mpc\nnative first-principle six-sink global peak = {native_global_peak['wavelength_Mpc']:.2f} Mpc\nnative first-principle six-sink BAO-window peak = {native_bao_peak['wavelength_Mpc']:.2f} Mpc\nnearest BAO bin = {2.0*np.pi/k[nearest_bao_idx]:.2f} Mpc\nreference scoring peak = {reference_peak['wavelength_Mpc']:.2f} Mpc\nsound horizon r_s = {r_s:.2f} Mpc\n```\n\n## Interpretation\n\n```text\nv0.25 is more theoretically grounded than the four-sink Cartesian toy assumption.\nIt still improves strongly over v0.23, but it is weaker than the v0.24 four-sink scaffold.\nThis suggests the next issue is how six internal dark sectors project into the 3D cosmology field.\n```\n"""
    (OUT / "mcift_v0.25_first_principle_sinks_report.md").write_text(report, encoding="utf-8")

    zip_path = Path("/mnt/data/mcift_v0.25_first_principle_sinks_outputs.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file in OUT.iterdir():
            zf.write(file, arcname=file.name)
    print(f"v0.25 first-principle sinks RMS={rms:.3f}; verdict={v24['verdict_shape'](rms)}")
    print(f"ZIP: {zip_path}")


if __name__ == "__main__":
    main()
