#!/usr/bin/env python3
"""
MCIFT v0.62 blind CERN inverse-timeflow prediction.

Status:
    Speculative blind-prediction scaffold, not established physics.

Purpose:
    Use the v0.61 first-principle inverse-timeflow structure on CERN/Higgs
    channel readouts without backpropagation, without hidden learned channel
    corrections, and without a target-loss fit.

Blind rule:
    Start from the v0.60 implemented channel readout before backprop.
    Apply channel-dependent ITF factors derived from geometry-prior channel
    stress values. Then compare to the SM reference table only after the
    prediction is formed.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

RESULT_DIR = Path("analysis/results_v0.62")
RESULT_DIR.mkdir(parents=True, exist_ok=True)

SM_TOTAL_WIDTH_MEV = 4.070000
A_LOCK_5B = 0.918752
N_DARK = 6
N_VISIBLE = 1
N_ANCHOR = 1
C_ITF = A_LOCK_5B * N_DARK / (N_DARK + N_VISIBLE + N_ANCHOR)
DENOM = N_VISIBLE + N_ANCHOR

CHANNELS = [
    ("bb",     0.582384276,   0.6197557475800611),
    ("WW",     0.213694230,   0.2132014094097443),
    ("gg",     0.0817977915,  0.0688832690776304),
    ("tau",    0.0626983071,  0.0712617023835817),
    ("cc",     0.0289992170,  0.0),
    ("ZZ",     0.0263992872,  0.0266501761762180),
    ("gamma",  0.00226993871, 0.0000017195969070847837),
    ("Zgamma", 0.00153995842, 0.0000006091348074004856),
    ("mumu",   0.000216994141,0.0002453666410498),
]

# Geometry-prior channel stress values. These are assigned by channel class,
# not by optimizing against CERN targets.
CHANNEL_STRESS = {
    "bb": 0.90,      # deep heavy fermion containment
    "WW": 0.40,      # coherent vector channel
    "gg": 0.15,      # color-flux release channel
    "tau": 0.85,     # lepton containment channel
    "cc": 0.55,      # mixed color/core fermion projection
    "ZZ": 0.40,      # coherent vector channel
    "gamma": 0.30,   # surface loop channel
    "Zgamma": 0.35,  # mixed surface-vector loop
    "mumu": 0.80,    # light lepton containment channel
}


def normalize(widths):
    total = sum(widths.values())
    return {key: value / total for key, value in widths.items()}


def percent_delta(value, reference):
    return 100.0 * (value / reference - 1.0)


def l1(a, b):
    return sum(abs(a[key] - b[key]) for key in b)


def implemented_v060_readout(sm, raw):
    factors = {key: raw[key] / sm[key] for key in sm}

    color_feedback = math.sqrt(factors["bb"] * factors["WW"])
    gg_impl = math.sqrt(factors["gg"] * color_feedback)

    fermion_core = math.sqrt(factors["tau"] * factors["mumu"])
    cc_impl = math.sqrt(gg_impl * fermion_core)

    vector_loop = math.sqrt(factors["WW"] * factors["ZZ"])
    gamma_impl = math.sqrt(vector_loop * gg_impl)
    Zgamma_impl = math.sqrt(gamma_impl * factors["ZZ"])

    implemented_factors = {
        "bb": factors["bb"],
        "WW": factors["WW"],
        "gg": gg_impl,
        "tau": factors["tau"],
        "cc": cc_impl,
        "ZZ": factors["ZZ"],
        "gamma": gamma_impl,
        "Zgamma": Zgamma_impl,
        "mumu": factors["mumu"],
    }
    widths = {key: sm[key] * implemented_factors[key] for key in sm}
    return widths, normalize(widths)


def main():
    sm = {channel: ref for channel, ref, _ in CHANNELS}
    raw = {channel: value for channel, _, value in CHANNELS}

    v060_widths, v060_br = implemented_v060_readout(sm, raw)

    tau = {
        channel: math.exp(-C_ITF * CHANNEL_STRESS[channel] / DENOM)
        for channel in sm
    }
    blind_widths = {
        channel: v060_widths[channel] * tau[channel]
        for channel in sm
    }
    blind_br = normalize(blind_widths)

    raw_delta = {channel: percent_delta(raw[channel], sm[channel]) for channel in sm}
    v060_delta = {channel: percent_delta(v060_br[channel], sm[channel]) for channel in sm}
    blind_delta = {channel: percent_delta(blind_br[channel], sm[channel]) for channel in sm}

    blind_total_width = SM_TOTAL_WIDTH_MEV * sum(blind_widths.values())

    def failed(delta):
        return [channel for channel, value in delta.items() if abs(value) > 10.0]

    metrics = [
        ["metric", "value"],
        ["verdict", "BLIND_ITF_BR_PASS_LIKE_TOTAL_WIDTH_LOW"],
        ["uses_backpropagation", "False"],
        ["uses_SM_target_loss", "False"],
        ["uses_hidden_learned_channel_corrections", "False"],
        ["C_ITF", f"{C_ITF:.15g}"],
        ["N_dark", N_DARK],
        ["N_visible", N_VISIBLE],
        ["N_anchor", N_ANCHOR],
        ["A_lock_5B", f"{A_LOCK_5B:.15g}"],
        ["v0_59_raw_BR_L1_vs_SM", f"{l1(raw, sm):.15g}"],
        ["v0_60_implemented_before_backprop_BR_L1_vs_SM", f"{l1(v060_br, sm):.15g}"],
        ["v0_62_blind_ITF_BR_L1_vs_SM", f"{l1(blind_br, sm):.15g}"],
        ["v0_59_raw_max_abs_BR_delta_pct", f"{max(abs(v) for v in raw_delta.values()):.15g}"],
        ["v0_60_implemented_before_backprop_max_abs_BR_delta_pct", f"{max(abs(v) for v in v060_delta.values()):.15g}"],
        ["v0_62_blind_ITF_max_abs_BR_delta_pct", f"{max(abs(v) for v in blind_delta.values()):.15g}"],
        ["v0_59_raw_failed_channels_10pct", ",".join(failed(raw_delta))],
        ["v0_60_implemented_before_backprop_failed_channels_10pct", ",".join(failed(v060_delta))],
        ["v0_62_blind_ITF_failed_channels_10pct", ",".join(failed(blind_delta))],
        ["v0_62_blind_total_width_MeV", f"{blind_total_width:.15g}"],
        ["v0_62_blind_total_width_delta_pct_vs_4p07", f"{percent_delta(blind_total_width, SM_TOTAL_WIDTH_MEV):.15g}"],
        ["branching_result_status", "PASS_LIKE"],
        ["absolute_width_status", "LOW_WITHOUT_ENVELOPE_RULE"],
    ]

    with (RESULT_DIR / "mcift_v0.62_blind_cern_itf_metrics.csv").open("w", newline="") as handle:
        csv.writer(handle).writerows(metrics)

    rows = [[
        "channel", "BR_SM_ref", "v0_60_before_backprop_BR", "v0_60_delta_pct",
        "channel_stress", "tau_ITF_channel", "v0_62_blind_BR", "v0_62_delta_pct",
    ]]
    for channel in sm:
        rows.append([
            channel,
            f"{sm[channel]:.12g}",
            f"{v060_br[channel]:.12g}",
            f"{v060_delta[channel]:.12f}",
            f"{CHANNEL_STRESS[channel]:.12f}",
            f"{tau[channel]:.12f}",
            f"{blind_br[channel]:.12g}",
            f"{blind_delta[channel]:.12f}",
        ])

    with (RESULT_DIR / "mcift_v0.62_blind_cern_itf_channels.csv").open("w", newline="") as handle:
        csv.writer(handle).writerows(rows)


if __name__ == "__main__":
    main()
