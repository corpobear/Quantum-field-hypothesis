#!/usr/bin/env python3
"""
MCIFT v0.14 two-drill collider event-shape test scaffold.

This script is intentionally data-format-light. It expects CSV files already
converted from ATLAS/CMS open data or derived ntuples.

Minimum expected columns:
    event_id
    sample        data or mc label, optional if passed separately
    weight        optional, defaults to 1
    met
    met_phi
    jet_pt        semicolon-separated jet pT list, e.g. "320;91;45"
    jet_phi       semicolon-separated jet phi list
    n_lep         optional, defaults to 0
    n_photon      optional, defaults to 0

Example:
    python analysis/cern_two_drill_event_shape_test.py \
        --data data.csv \
        --mc sm_mc.csv \
        --out analysis/results_v0.14

Outputs:
    data_vs_mc_summary.csv
    hist_met_over_ht.png
    hist_delta_phi_min.png
    hist_njets.png

Interpretation:
    MCIFT side-channel candidates would appear as a structured excess in
    high MET/HT and angular-imbalance bins after Standard Model comparison.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


EPS = 1e-9


def parse_list(value: object) -> list[float]:
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return []
    if isinstance(value, (int, float)):
        return [float(value)]
    text = str(value).strip()
    if not text:
        return []
    return [float(x) for x in text.replace(",", ";").split(";") if x.strip()]


def delta_phi(a: float, b: float) -> float:
    d = (a - b + np.pi) % (2 * np.pi) - np.pi
    return abs(d)


def add_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    if "weight" not in out.columns:
        out["weight"] = 1.0
    if "n_lep" not in out.columns:
        out["n_lep"] = 0
    if "n_photon" not in out.columns:
        out["n_photon"] = 0

    hts = []
    njets = []
    leading_pts = []
    dphi_mins = []

    for _, row in out.iterrows():
        pts = parse_list(row.get("jet_pt"))
        phis = parse_list(row.get("jet_phi"))
        met_phi = float(row.get("met_phi", 0.0))

        hts.append(float(np.sum(pts)) if pts else 0.0)
        njets.append(len([p for p in pts if p > 30.0]))
        leading_pts.append(max(pts) if pts else 0.0)

        if phis:
            dphi_mins.append(min(delta_phi(phi, met_phi) for phi in phis))
        else:
            dphi_mins.append(np.nan)

    out["ht"] = hts
    out["njets"] = njets
    out["leading_jet_pt"] = leading_pts
    out["delta_phi_min"] = dphi_mins
    out["met_over_ht"] = out["met"] / (out["ht"] + EPS)
    return out


def select_monojet_like(df: pd.DataFrame) -> pd.DataFrame:
    return df[
        (df["leading_jet_pt"] > 150.0)
        & (df["met"] > 200.0)
        & (df["n_lep"] == 0)
        & (df["n_photon"] == 0)
    ].copy()


def weighted_hist(values: Iterable[float], weights: Iterable[float], bins: np.ndarray) -> np.ndarray:
    hist, _ = np.histogram(list(values), bins=bins, weights=list(weights))
    return hist.astype(float)


def write_summary(data: pd.DataFrame, mc: pd.DataFrame, outdir: Path) -> None:
    regions = {
        "inclusive_loaded": (data, mc),
        "monojet_like": (select_monojet_like(data), select_monojet_like(mc)),
        "high_met_over_ht": (
            data[data["met_over_ht"] > 0.5],
            mc[mc["met_over_ht"] > 0.5],
        ),
        "side_channel_candidate": (
            data[(data["met_over_ht"] > 0.5) & (data["delta_phi_min"] > 0.4)],
            mc[(mc["met_over_ht"] > 0.5) & (mc["delta_phi_min"] > 0.4)],
        ),
    }

    rows = []
    for name, (d, m) in regions.items():
        d_yield = float(d["weight"].sum())
        m_yield = float(m["weight"].sum())
        ratio = d_yield / m_yield if m_yield > 0 else np.nan
        rows.append(
            {
                "region": name,
                "data_weighted_yield": d_yield,
                "mc_weighted_yield": m_yield,
                "data_over_mc": ratio,
                "data_events": len(d),
                "mc_events": len(m),
            }
        )
    pd.DataFrame(rows).to_csv(outdir / "data_vs_mc_summary.csv", index=False)


def plot_comparison(data: pd.DataFrame, mc: pd.DataFrame, column: str, bins: np.ndarray, outpath: Path, xlabel: str) -> None:
    plt.figure(figsize=(7, 4))
    plt.hist(mc[column].dropna(), bins=bins, weights=mc.loc[mc[column].notna(), "weight"], histtype="step", label="SM MC")
    plt.hist(data[column].dropna(), bins=bins, weights=data.loc[data[column].notna(), "weight"], histtype="step", label="Data")
    plt.xlabel(xlabel)
    plt.ylabel("weighted events")
    plt.title(f"MCIFT v0.14 collider proxy: {xlabel}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(outpath)
    plt.close()


def run(data_path: Path, mc_path: Path, outdir: Path) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    data = add_features(pd.read_csv(data_path))
    mc = add_features(pd.read_csv(mc_path))

    write_summary(data, mc, outdir)

    plot_comparison(data, mc, "met_over_ht", np.linspace(0, 2, 41), outdir / "hist_met_over_ht.png", "MET / HT")
    plot_comparison(data, mc, "delta_phi_min", np.linspace(0, np.pi, 41), outdir / "hist_delta_phi_min.png", "min delta phi(jet, MET)")
    plot_comparison(data, mc, "njets", np.arange(0, 16) - 0.5, outdir / "hist_njets.png", "N jets")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, type=Path, help="CSV file for collision data")
    parser.add_argument("--mc", required=True, type=Path, help="CSV file for Standard Model MC")
    parser.add_argument("--out", default=Path("analysis/results_v0.14"), type=Path, help="Output directory")
    args = parser.parse_args()
    run(args.data, args.mc, args.out)


if __name__ == "__main__":
    main()
