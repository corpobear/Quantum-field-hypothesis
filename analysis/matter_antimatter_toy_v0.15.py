#!/usr/bin/env python3
"""
MCIFT v0.15 matter-antimatter toy ratio calculator.

This is a speculative toy-model calculation, not established physics.
It treats antimatter as positive-mass, channel-reversed geometry rather than
negative mass.

Geometry used here:
    matter visible drill:
        central tip aperture + spin-vortex echo

    antimatter dark sink:
        one Higgs-response drop

    antimatter light drill:
        splash-ring intake with the middle discarded
        seven local splash units - one discarded middle = six captured splashes

The calculation asks whether this routing gives a matter formation/survival
aperture larger than the antimatter aperture.
"""

from __future__ import annotations

import csv
from pathlib import Path


O_PHI = 0.9837806705
C = 8
P8 = 1 / 56
E8 = 1 / 448
B8 = 7 / 8


def compute() -> dict[str, float]:
    matter_tip = P8 + B8 * E8 * O_PHI

    antimatter_hdrop = E8 * O_PHI
    antimatter_splash_total = 7 * E8 * O_PHI
    antimatter_mid_discard = E8 * O_PHI
    antimatter_splash_captured = antimatter_splash_total - antimatter_mid_discard
    antimatter_total = antimatter_hdrop + antimatter_splash_captured

    matter_to_antimatter = matter_tip / antimatter_total
    antimatter_to_matter = antimatter_total / matter_tip
    epsilon_mcift = (matter_tip - antimatter_total) / (matter_tip + antimatter_total)
    matter_excess = matter_tip - antimatter_total

    return {
        "C": C,
        "O_phi": O_PHI,
        "P8_primary_tip": P8,
        "E8_echo_unit": E8,
        "B8_free_spin_fraction": B8,
        "matter_effective_aperture": matter_tip,
        "antimatter_higgs_drop_aperture": antimatter_hdrop,
        "antimatter_splash_total_before_middle_discard": antimatter_splash_total,
        "antimatter_discarded_middle": antimatter_mid_discard,
        "antimatter_splash_captured": antimatter_splash_captured,
        "antimatter_effective_aperture": antimatter_total,
        "matter_to_antimatter_ratio": matter_to_antimatter,
        "antimatter_to_matter_ratio": antimatter_to_matter,
        "epsilon_MCIFT": epsilon_mcift,
        "matter_excess_aperture": matter_excess,
    }


def write_csv(results: dict[str, float], outpath: Path) -> None:
    outpath.parent.mkdir(parents=True, exist_ok=True)
    with outpath.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["quantity", "value"])
        for key, value in results.items():
            writer.writerow([key, f"{value:.15g}"])


def main() -> None:
    results = compute()
    outpath = Path("analysis/results_v0.15/matter_antimatter_toy_ratio.csv")
    write_csv(results, outpath)

    print("MCIFT v0.15 matter-antimatter toy ratio")
    print("status: speculative toy-model calculation; not established physics")
    print()
    for key, value in results.items():
        print(f"{key}: {value:.15g}")
    print()
    if results["matter_to_antimatter_ratio"] > 1:
        print("verdict: toy geometry gives more matter aperture than antimatter aperture")
    elif results["matter_to_antimatter_ratio"] < 1:
        print("verdict: toy geometry gives more antimatter aperture than matter aperture")
    else:
        print("verdict: toy geometry gives equal matter and antimatter apertures")


if __name__ == "__main__":
    main()
