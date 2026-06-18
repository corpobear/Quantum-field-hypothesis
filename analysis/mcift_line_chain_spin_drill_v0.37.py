#!/usr/bin/env python3
"""MCIFT v0.37 line-chain spin-drill Higgs toy test.

Connect cube centers in a 1D line, drive counter-propagating phase/information
flows, measure spin/twist, and test whether a localized dent/drill/sink forms.
Speculative scaffold, not established physics.
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

OUT = Path("analysis/results_v0.37")
OUT.mkdir(parents=True, exist_ok=True)

N = 401
CENTER = N // 2
X = np.arange(N)
T = 900
DT = 0.02
CENTER_WINDOW = 12
SIGMA_PACKET = 45.0
V_PACKET = 0.42
K0 = 0.45
DRIVE_OMEGA = 0.04
CHI_C = 1 / np.sqrt(2)
KAPPA = 9.0
M_SCALE_GEV = 21.460118674437688
Q_BASE0 = 0.18
CAP_SCALE = 2.60
MASS_ALPHA = 0.25
GRAD_OMEGA_ALPHA = 0.04
DENT_SPIN_ALPHA = 0.50
DENT_TWIST_ALPHA = 0.80
DENT_VORTEX_ALPHA = 0.90
GAMMA_B = 0.35
DECAY_B = 0.022


def sigmoid(y):
    return 0.5 * (1 + np.tanh(KAPPA * y))


def wrap_phase(d):
    return np.angle(np.exp(1j * d))


def link_to_node(arr):
    out = np.zeros(N)
    out[:-1] += 0.5 * arr
    out[1:] += 0.5 * arr
    return out


def packet_state(step):
    xl = 35 + V_PACKET * step
    xr = (N - 36) - V_PACKET * step
    L = np.exp(-0.5 * ((X - xl) / SIGMA_PACKET) ** 2)
    R = np.exp(-0.5 * ((X - xr) / SIGMA_PACKET) ** 2)
    psi = L * np.exp(1j * (K0 * (X - xl) - DRIVE_OMEGA * step))
    psi += R * np.exp(1j * (-K0 * (X - xr) - DRIVE_OMEGA * step))
    psi += 0.01 * np.exp(1j * 0.01 * X)
    return np.abs(psi), np.unwrap(np.angle(psi)), L, R


def main():
    B = np.zeros(N)
    prev_delta_phi = np.zeros(N - 1)
    history = []
    snapshots = {}

    for step in range(T):
        K_abs, phi, L, R = packet_state(step)
        delta_phi = wrap_phase(np.diff(phi))
        omega_link = np.clip((delta_phi - prev_delta_phi) / DT, -40.0, 40.0)
        prev_delta_phi = delta_phi.copy()

        K_left, K_right = K_abs[:-1], K_abs[1:]
        A_link = np.sqrt(np.clip(K_left * K_right, 0, None))
        A_link = np.clip(A_link / (1 + A_link) * np.exp(-0.08 * (B[:-1] + B[1:])), 0, 1)

        L_link = 0.5 * (L[:-1] + L[1:])
        R_link = 0.5 * (R[:-1] + R[1:])
        collision_link = 4 * L_link * R_link / ((L_link + R_link) ** 2 + 1e-9)
        collision_node = 4 * L * R / ((L + R) ** 2 + 1e-9)

        P_phase = np.cos(delta_phi) ** 2
        P_timing = np.exp(-0.00045 * omega_link ** 2)
        P_match = np.exp(-((K_right - K_left) ** 2) / (0.45 ** 2))
        chi_link = A_link * P_phase * P_timing * P_match

        H_link = np.clip(0.25 + A_link, 0, 1)
        Omega_link = H_link * sigmoid(chi_link - CHI_C) * collision_link
        mass_link = M_SCALE_GEV * Omega_link * A_link

        chi_node = link_to_node(chi_link)
        Omega_node = link_to_node(Omega_link)
        mass_node = link_to_node(mass_link)
        omega_node = link_to_node(np.abs(omega_link))

        Theta = np.zeros(N)
        Theta[1:-1] = wrap_phase(phi[2:] - 2 * phi[1:-1] + phi[:-2])
        grad_Omega = np.zeros(N)
        grad_Omega[1:-1] = np.abs(Omega_link[1:] - Omega_link[:-1])

        leftA, rightA = np.zeros(N), np.zeros(N)
        leftA[1:] = A_link
        rightA[:-1] = A_link
        a_mean = 0.5 * (leftA + rightA)
        delta_line = np.abs(leftA - rightA)
        Coh = CAP_SCALE * a_mean - 0.25 * delta_line

        q = Q_BASE0 + 0.12 * K_abs ** 2 + MASS_ALPHA * (mass_node / M_SCALE_GEV) + GRAD_OMEGA_ALPHA * grad_Omega
        Dent = DENT_SPIN_ALPHA * (omega_node / 40.0) + DENT_TWIST_ALPHA * np.abs(Theta) + DENT_VORTEX_ALPHA * Omega_node
        S = Coh - q - Dent
        collapse = np.maximum(0, -S)
        B = (1 - DECAY_B) * B + GAMMA_B * collapse * (K_abs / (1 + K_abs)) * collision_node

        if step in [0, 180, 300, 380, 426, 520, 650, 899]:
            snapshots[step] = (Dent.copy(), B.copy(), mass_node.copy())

        w = slice(CENTER - CENTER_WINDOW, CENTER + CENTER_WINDOW + 1)
        peak_B_idx = int(np.argmax(B))
        peak_D_idx = int(np.argmax(Dent))
        local_mass_idx = int(np.argmax(mass_node[w]) + CENTER - CENTER_WINDOW)
        history.append({
            "step": step,
            "t": step * DT,
            "center_B": float(B[CENTER]),
            "peak_B": float(B[peak_B_idx]),
            "peak_B_idx": peak_B_idx,
            "peak_B_distance_from_center": abs(peak_B_idx - CENTER),
            "B_localization_ratio": float(B[w].sum() / (B.sum() + 1e-12)),
            "peak_Dent": float(Dent[peak_D_idx]),
            "peak_Dent_idx": peak_D_idx,
            "peak_window_mass_GeV_proxy": float(np.max(mass_node[w])),
            "peak_window_mass_idx": local_mass_idx,
            "peak_window_mass_distance_from_center": abs(local_mass_idx - CENTER),
            "center_S": float(S[CENTER]),
            "negative_S_fraction": float((S < 0).mean()),
        })

    hist = pd.DataFrame(history)
    hist.to_csv(OUT / "mcift_v0.37_line_chain_spin_drill_history.csv", index=False)

    peakB = hist.iloc[hist.peak_B.idxmax()]
    peakD = hist.iloc[hist.peak_Dent.idxmax()]
    peakM = hist.iloc[hist.peak_window_mass_GeV_proxy.idxmax()]

    half = 0.5 * hist.center_B.max()
    above = (hist.center_B >= half).values
    segments = []
    start = None
    for idx, flag in enumerate(above):
        if flag and start is None:
            start = idx
        if (not flag or idx == len(above) - 1) and start is not None:
            end = idx - 1 if not flag else idx
            segments.append((start, end))
            start = None
    life = max([e - s + 1 for s, e in segments], default=0)

    criteria = {
        "localized_sink_center_distance_le_5": bool(peakB.peak_B_distance_from_center <= 5),
        "sink_localization_ratio_peak_window_gt_0p35": bool(peakB.B_localization_ratio > 0.35),
        "central_spin_drill_forms": bool(peakD.peak_Dent > 0.85),
        "central_region_mass_gathers": bool(hist.peak_window_mass_GeV_proxy.max() > 0.50),
        "finite_lifetime_halfmax": bool(0 < life < T),
        "post_peak_decay_present": bool(hist.center_B.iloc[-1] < 0.9 * hist.center_B.max()),
        "not_global_everywhere_first_half": bool(hist.negative_S_fraction.iloc[:T // 2].max() < 0.95),
    }
    score = sum(criteria.values())
    verdict = "PASS-LIKE" if score >= 5 else "WEAK" if score >= 3 else "FAIL"

    rows = [
        ["verdict", verdict, "category", f"{score}/7 criteria"],
        ["criteria_pass_count", score, "count", "strict toy criteria"],
        ["peak_B", peakB.peak_B, "sink_proxy", "max reservoir dent"],
        ["peak_B_step", int(peakB.step), "step", "when sink peaked"],
        ["peak_B_distance_from_center", int(peakB.peak_B_distance_from_center), "cells", "localization"],
        ["B_localization_ratio_at_peak", peakB.B_localization_ratio, "fraction", "center +/- 12 cells"],
        ["peak_Dent", peakD.peak_Dent, "drill_proxy", "max dent/drill strength"],
        ["peak_Dent_step", int(peakD.step), "step", "when dent peaked"],
        ["peak_window_mass_GeV_proxy", hist.peak_window_mass_GeV_proxy.max(), "GeV_proxy", "mass gathered in center drill region"],
        ["peak_window_mass_step", int(peakM.step), "step", "when center-window mass peaked"],
        ["peak_window_mass_distance_from_center", int(peakM.peak_window_mass_distance_from_center), "cells", "mass localization"],
        ["sink_halfmax_lifetime_steps", life, "steps", "finite lifetime"],
        ["sink_halfmax_lifetime_time", life * DT, "sim_time", "finite lifetime"],
        ["center_B_final_over_peak", hist.center_B.iloc[-1] / (hist.center_B.max() + 1e-12), "ratio", "decay check"],
        ["max_negative_S_fraction", hist.negative_S_fraction.max(), "fraction", "collapse spread"],
        ["initial_negative_S_fraction", hist.negative_S_fraction.iloc[0], "fraction", "collapse spread"],
        ["final_negative_S_fraction", hist.negative_S_fraction.iloc[-1], "fraction", "collapse spread"],
    ] + [[k, int(v), "bool", "criterion"] for k, v in criteria.items()]
    pd.DataFrame(rows, columns=["metric", "value", "unit", "notes"]).to_csv(OUT / "mcift_v0.37_line_chain_spin_drill_metrics.csv", index=False)

    # lightweight plots
    plt.figure(figsize=(11, 6))
    plt.plot(hist.step, hist.center_B, label="center B")
    plt.plot(hist.step, hist.peak_Dent, label="peak dent")
    plt.plot(hist.step, hist.peak_window_mass_GeV_proxy / max(hist.peak_window_mass_GeV_proxy.max(), 1e-9), label="mass window norm")
    plt.legend(); plt.tight_layout()
    plt.savefig(OUT / "mcift_v0.37_line_chain_spin_drill_history.png", dpi=150)
    plt.close()

    print(f"v0.37 {verdict}; score={score}/7; peak_B={peakB.peak_B:.6f}; peak_mass={hist.peak_window_mass_GeV_proxy.max():.6f}")


if __name__ == "__main__":
    main()
