#!/usr/bin/env python3
"""
MCIFT 3D Spatial + Fibonacci Evolution — 5 billion year run

- True 3D volume (x, y, z)
- Fibonacci-Higgs resonance (golden ratio modulation)
- Elements/clusters forming inside the volume over long cosmic time
- One-point shadow anchor + visible/dark split
- Produces milestone screenshots at 1/2/3/4/5 billion years

Note: The original 1M-year toy dynamics are stretched across 5B years so that
billion-year milestones show the staged formation rather than a fully saturated
field at every frame.
"""

from __future__ import annotations

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


# Golden ratio for Fibonacci resonance
PHI = (1 + np.sqrt(5)) / 2

# Simulation timeline
BASE_TOY_YEARS = 1_000_000
TOTAL_YEARS = 5_000_000_000
TIME_STRETCH = TOTAL_YEARS / BASE_TOY_YEARS

# Grid / model parameters
N_SIDE = 60
FIELD_LIMIT = 5

# Output path can be overridden, otherwise it writes inside the repo tree.
DEFAULT_OUTPUT_DIR = Path(__file__).resolve().parent / "output" / "3d_fibonacci_5by"
OUTPUT_DIR = Path(os.environ.get("MCIFT_OUTPUT_DIR", DEFAULT_OUTPUT_DIR))
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

MILESTONES = [
    (1_000_000_000, "t=1B years - Early Billion-Year Pocket Structure"),
    (2_000_000_000, "t=2B years - Visible Axial + Dark Sinks Forming"),
    (3_000_000_000, "t=3B years - Mature 3D Resonance Structure"),
    (4_000_000_000, "t=4B years - Deep Coherent Cluster Formation"),
    (5_000_000_000, "t=5B years - Full 3D Pocket Universe"),
]


def scaled_t(actual_years: float) -> float:
    """Map the 5B-year run onto the original accelerated 1M-year toy dynamics."""
    return actual_years / TIME_STRETCH


def evolve_3d_field(actual_years: float, X: np.ndarray, Y: np.ndarray, Z: np.ndarray):
    """3D field evolution with Fibonacci resonance."""
    t = scaled_t(actual_years)
    r = np.sqrt(X**2 + Y**2 + Z**2)

    # Base coherence with Fibonacci modulation
    fib_mod = 1 + 0.15 * np.sin(2 * np.pi * np.log(r + 1e-6) / np.log(PHI))
    coherence = (1 - np.exp(-t / 40000)) * np.exp(-r**2 / (4 + 0.002 * t)) * fib_mod

    # One-point shadow anchor at center
    anchor = np.exp(-r**2 / (1.5 + 0.001 * t))

    # Visible axial component along z-axis
    if t > 40000:
        visible = 0.7 * (1 - np.exp(-(t - 40000) / 90000)) * np.exp(
            -((X) ** 2 + (Y) ** 2 + (Z - 2) ** 2) / 3
        )
    else:
        visible = np.zeros_like(X)

    # Dark side sinks distributed around the central anchor
    if t > 180000:
        dark_factor = 1 - np.exp(-(t - 180000) / 150000)
        dark = dark_factor * (
            np.exp(-((X - 2) ** 2 + (Y) ** 2 + (Z) ** 2) / 4)
            + np.exp(-((X + 2) ** 2 + (Y) ** 2 + (Z) ** 2) / 4)
            + np.exp(-((X) ** 2 + (Y - 2) ** 2 + (Z) ** 2) / 4)
            + np.exp(-((X) ** 2 + (Y + 2) ** 2 + (Z) ** 2) / 4)
        )
    else:
        dark = np.zeros_like(X)

    # Exchange + resonance
    exchange = 0.35 * np.tanh(t / 200000) * np.exp(-r**2 / 5)

    field = coherence + 0.6 * visible - 0.45 * dark + exchange + 0.3 * anchor

    return field, visible, dark, coherence


def safe_slug(title: str) -> str:
    return (
        title.replace("=", "")
        .replace(" ", "_")
        .replace(",", "")
        .replace("/", "-")
        .replace("+", "plus")
    )


def make_grid():
    axis = np.linspace(-FIELD_LIMIT, FIELD_LIMIT, N_SIDE)
    return np.meshgrid(axis, axis, axis, indexing="ij")


def render_milestone(actual_years: int, title: str, X: np.ndarray, Y: np.ndarray, Z: np.ndarray):
    field, visible, dark, coherence = evolve_3d_field(actual_years, X, Y, Z)

    fig = plt.figure(figsize=(16, 12))

    # Plot 1: 3D scatter of high field strength (forming elements)
    ax1 = fig.add_subplot(221, projection="3d")
    threshold = np.percentile(field, 92)
    mask = field > threshold
    scatter = ax1.scatter(X[mask], Y[mask], Z[mask], c=field[mask], cmap="plasma", s=8, alpha=0.6)
    ax1.set_title(f"Forming Elements (High Field)\n{title}")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    ax1.set_zlabel("z")
    fig.colorbar(scatter, ax=ax1, shrink=0.55, pad=0.1)

    # Plot 2: visible axial component (slice at z=0)
    ax2 = fig.add_subplot(222)
    mid_z = field.shape[2] // 2
    im2 = ax2.imshow(visible[:, :, mid_z], extent=[-5, 5, -5, 5], cmap="Greens", vmin=0, vmax=1.3)
    ax2.set_title("Visible-Manifest Slice (z=0)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    fig.colorbar(im2, ax=ax2, shrink=0.8)

    # Plot 3: dark side sinks
    ax3 = fig.add_subplot(223)
    im3 = ax3.imshow(dark[:, :, mid_z], extent=[-5, 5, -5, 5], cmap="Purples", vmin=0, vmax=1.1)
    ax3.set_title("Dark-Manifest Side Sinks Slice (z=0)")
    ax3.set_xlabel("x")
    ax3.set_ylabel("y")
    fig.colorbar(im3, ax=ax3, shrink=0.8)

    # Plot 4: total field contours with Fibonacci modulation visible
    ax4 = fig.add_subplot(224, projection="3d")
    ax4.contour(X[:, :, mid_z], Y[:, :, mid_z], field[:, :, mid_z], levels=8, cmap="RdBu_r")
    ax4.set_title("Total Field Contours + Fibonacci Influence")
    ax4.set_xlabel("x")
    ax4.set_ylabel("y")

    fig.suptitle(
        f"MCIFT 3D + Fibonacci Evolution\n{title} | scaled toy-time={scaled_t(actual_years):,.0f} years",
        fontsize=14,
    )
    fig.tight_layout()

    slug = safe_slug(title)
    png_path = OUTPUT_DIR / f"3d_fibonacci_{slug}.png"
    generated_paths = [png_path]

    fig.savefig(png_path, dpi=120, bbox_inches="tight")

    # Optional SVG export for repo-friendly vector figures. Disabled by default
    # because 3D scatter SVGs are large and slower to write.
    if os.environ.get("MCIFT_SAVE_SVG", "0") == "1":
        svg_path = OUTPUT_DIR / f"3d_fibonacci_{slug}.svg"
        fig.savefig(svg_path, bbox_inches="tight")
        generated_paths.append(svg_path)

    plt.close(fig)

    return generated_paths


def main():
    print("Running MCIFT 3D + Fibonacci Spatial Simulation...")
    print(f"Total simulated span: {TOTAL_YEARS:,} years")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Time stretch: {TIME_STRETCH:,.0f} actual years per original toy year")

    X, Y, Z = make_grid()

    generated = []
    for year, title in MILESTONES:
        print(f"Rendering milestone: {year:,} years")
        paths = render_milestone(year, title, X, Y, Z)
        generated.extend(paths)
        for path in paths:
            print(f"Saved: {path}")

    print("\n3D + Fibonacci 5B-year spatial simulation complete!")
    print("Generated files:")
    for path in generated:
        print(f"- {path}")


if __name__ == "__main__":
    main()
