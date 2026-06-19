#!/usr/bin/env python3
"""
MCIFT v0.64 unified first-principle formula check.

Status:
    Speculative scaffold, not established physics.

Purpose:
    Recompute the consolidated v0.64 numbers from the sector-level formula:
      C_ITF, tau_ITF, O_DV, E_DV,
      v0.61 cosmology comparison,
      v0.62 blind branching result,
      v0.63 dark-visible width-envelope result.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

RESULT_DIR = Path("analysis/results_v0.64")
RESULT_DIR.mkdir(parents=True, exist_ok=True)

N_D = 6
N_V = 1
N_A = 1
A_LOCK = 0.918752

H075_RAW = 156.66381928473376
H075_V061 = 111.004443394536
H075_LCDM = 103.831075445288

WIDTH_REF = 4.07
WIDTH_V062 = 3.32598142936141
MAX_CHANNEL_DELTA_V062 = 8.24764893442693
BR_L1_V062 = 0.0523719944935826


def pct_delta(value: float, ref: float) -> float:
    return 100.0 * (value / ref - 1.0)


def main() -> None:
    c_itf = A_LOCK * N_D / (N_D + N_V + N_A)
    tau_itf = math.exp(-c_itf / (N_V + N_A))
    o_dv = 2.0 * math.sqrt(N_D * N_V) / (N_D + N_V + N_A)
    e_dv = math.exp(c_itf * o_dv / (N_V + N_A))
    width_v063 = WIDTH_V062 * e_dv

    rows = [
        ["metric", "value"],
        ["version", "v0.64"],
        ["C_ITF", f"{c_itf:.15g}"],
        ["tau_ITF", f"{tau_itf:.15g}"],
        ["O_DV", f"{o_dv:.15g}"],
        ["E_DV", f"{e_dv:.15g}"],
        ["H075_raw", f"{H075_RAW:.15g}"],
        ["H075_v061", f"{H075_V061:.15g}"],
        ["H075_LCDM", f"{H075_LCDM:.15g}"],
        ["H075_raw_delta_pct", f"{pct_delta(H075_RAW, H075_LCDM):.15g}"],
        ["H075_v061_delta_pct", f"{pct_delta(H075_V061, H075_LCDM):.15g}"],
        ["raw_to_v061_improvement", f"{abs(pct_delta(H075_RAW, H075_LCDM)) / abs(pct_delta(H075_V061, H075_LCDM)):.15g}"],
        ["width_v062", f"{WIDTH_V062:.15g}"],
        ["width_v062_delta_pct", f"{pct_delta(WIDTH_V062, WIDTH_REF):.15g}"],
        ["width_v063", f"{width_v063:.15g}"],
        ["width_v063_delta_pct", f"{pct_delta(width_v063, WIDTH_REF):.15g}"],
        ["max_channel_delta_v062_v063", f"{MAX_CHANNEL_DELTA_V062:.15g}"],
        ["BR_L1_v062_v063", f"{BR_L1_V062:.15g}"],
    ]

    out = RESULT_DIR / "mcift_v0.64_unified_formula_check.csv"
    with out.open("w", newline="") as handle:
        csv.writer(handle).writerows(rows)


if __name__ == "__main__":
    main()
