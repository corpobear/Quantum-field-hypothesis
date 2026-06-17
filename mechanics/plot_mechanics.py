#!/usr/bin/env python3
"""
Generate MCIFT mechanics diagrams through v0.13.

Usage:
    python mechanics/plot_mechanics.py

Outputs:
    mechanics/figures/*.svg
"""

from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Circle, Wedge, FancyBboxPatch

OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(parents=True, exist_ok=True)


def savefig(name: str) -> None:
    plt.savefig(OUT / name, format="svg", bbox_inches="tight")
    plt.close()


def draw_activation_channels() -> None:
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.axis("off")
    nodes = {
        "Information\npoint": (0.05, 0.5),
        "Knot\ncoherence K": (0.25, 0.5),
        "Visibility\nL·K": (0.5, 0.78),
        "Mass\nH·K": (0.5, 0.5),
        "Gravity\nG·H·K": (0.5, 0.22),
        "Visible-\nmanifest": (0.78, 0.78),
        "Dark-\nmanifest": (0.78, 0.38),
        "Unmanifest": (0.78, 0.08),
    }
    for text, (x, y) in nodes.items():
        ax.add_patch(
            FancyBboxPatch(
                (x - 0.075, y - 0.065),
                0.15,
                0.13,
                boxstyle="round,pad=0.02",
                fill=False,
                lw=1.5,
            )
        )
        ax.text(x, y, text, ha="center", va="center", fontsize=10)

    def arr(a: str, b: str, rad: float = 0) -> None:
        ax.add_patch(
            FancyArrowPatch(
                nodes[a],
                nodes[b],
                arrowstyle="->",
                mutation_scale=12,
                lw=1.2,
                connectionstyle=f"arc3,rad={rad}",
            )
        )

    arr("Information\npoint", "Knot\ncoherence K")
    arr("Knot\ncoherence K", "Visibility\nL·K", 0.15)
    arr("Knot\ncoherence K", "Mass\nH·K")
    arr("Knot\ncoherence K", "Gravity\nG·H·K", -0.15)
    arr("Visibility\nL·K", "Visible-\nmanifest")
    arr("Mass\nH·K", "Visible-\nmanifest", 0.15)
    arr("Gravity\nG·H·K", "Visible-\nmanifest", -0.15)
    arr("Mass\nH·K", "Dark-\nmanifest", 0.1)
    arr("Gravity\nG·H·K", "Dark-\nmanifest", -0.1)
    arr("Information\npoint", "Unmanifest", -0.25)
    ax.text(
        0.5,
        0.98,
        "Channel-specific activation: light controls visibility, not existence",
        ha="center",
        fontsize=13,
        weight="bold",
    )
    ax.text(0.78, 0.58, "Dark-manifest:\nL≈0, H>0, G>0, K>0", ha="center", fontsize=9)
    savefig("activation_channels.svg")


def draw_field_source_pipeline() -> None:
    fig, ax = plt.subplots(figsize=(12, 3))
    ax.axis("off")
    labels = [
        "Knot/shadow\nanchor",
        "Vortex\nΩ or κ",
        "Speed\nwindow W",
        "Higgs\nresonance O",
        "Reservoir\ngate R",
        "Finite\ncore δ",
        "Integrated\nsource Σ",
        "Mass\nm=m₀(1+Σ)²",
    ]
    xs = np.linspace(0.06, 0.94, len(labels))
    for x, label in zip(xs, labels):
        ax.add_patch(
            FancyBboxPatch(
                (x - 0.055, 0.38),
                0.11,
                0.24,
                boxstyle="round,pad=0.02",
                fill=False,
                lw=1.4,
            )
        )
        ax.text(x, 0.5, label, ha="center", va="center", fontsize=9)
    for x1, x2 in zip(xs[:-1], xs[1:]):
        ax.add_patch(
            FancyArrowPatch(
                (x1 + 0.055, 0.5),
                (x2 - 0.055, 0.5),
                arrowstyle="->",
                mutation_scale=12,
                lw=1.2,
            )
        )
    ax.text(0.5, 0.88, "Current field-source mechanics", ha="center", fontsize=13, weight="bold")
    ax.text(
        0.5,
        0.17,
        "Sₐ = λₐ Ωₐ Wᵥ [P + B·E·⟨Oφ⟩] R₄ᵍᵃᵗᵉ δₐ ; integrate Sₐ to get amplitude source Σ",
        ha="center",
        fontsize=10,
    )
    savefig("field_source_pipeline.svg")


def draw_capture_window() -> None:
    v = np.linspace(0, 4, 400)
    vmin = 0.8
    vscatter = 2.6
    W = (1 - np.exp(-(v / vmin) ** 2)) * np.exp(-(v / vscatter) ** 2)
    W = W / W.max()

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(v, W, lw=2)
    ax.axvline(v[np.argmax(W)], ls="--", lw=1)
    ax.set_xlabel("normalized tip/side speed")
    ax.set_ylabel("capture window W")
    ax.set_title("Funnel-speed capture window: too slow / capture / too fast")
    ax.text(0.45, 0.2, "too slow\nno connection", ha="center", fontsize=9)
    ax.text(v[np.argmax(W)], 0.85, "capture", ha="center", fontsize=9)
    ax.text(3.35, 0.25, "too fast\nscattering", ha="center", fontsize=9)
    ax.set_ylim(0, 1.1)
    savefig("capture_window.svg")


def draw_reservoir_gate() -> None:
    R = np.logspace(-3, 3, 400)
    Rgate = R / (R + 1)

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.semilogx(R, Rgate, lw=2)
    ax.set_xlabel("reservoir strength R₄ / R*")
    ax.set_ylabel("bounded availability R₄ᵍᵃᵗᵉ")
    ax.set_title("Fourth-mode reservoir gate: large supply saturates")
    ax.axhline(1, ls=":", lw=1)
    ax.axvline(1, ls="--", lw=1)
    ax.text(0.02, 0.2, "weak reservoir", fontsize=9)
    ax.text(20, 0.85, "saturated availability\nnot infinite mass", fontsize=9)
    ax.set_ylim(0, 1.05)
    savefig("reservoir_gate.svg")


def draw_eight_sector_geometry() -> None:
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={"aspect": "equal"})
    ax.axis("off")
    for i in range(8):
        theta1 = 90 - i * 45 - 22.5
        theta2 = 90 - i * 45 + 22.5
        ax.add_patch(Wedge((0, 0), 1.0, theta1, theta2, width=0.35, fill=False, lw=1.5))

    angles = np.deg2rad(90 - np.arange(8) * 45)
    pts = np.c_[np.cos(angles) * 0.82, np.sin(angles) * 0.82]
    for idx, (x, y) in enumerate(pts):
        ax.add_patch(Circle((x, y), 0.045, fill=False, lw=1.2))
        ax.text(x, y, str(idx + 1), ha="center", va="center", fontsize=8)

    ax.annotate(
        "visible\naxial tip\n1 sector",
        xy=(0, 0.95),
        xytext=(0, 1.45),
        ha="center",
        arrowprops=dict(arrowstyle="->", lw=1.2),
        fontsize=9,
    )
    ax.annotate(
        "opposite\naxis",
        xy=(0, -0.95),
        xytext=(0, -1.35),
        ha="center",
        arrowprops=dict(arrowstyle="->", lw=1.2),
        fontsize=9,
    )

    for ang in angles[[1, 2, 3, 5, 6, 7]]:
        x, y = np.cos(ang) * 1.25, np.sin(ang) * 1.25
        x2, y2 = np.cos(ang) * 0.9, np.sin(ang) * 0.9
        ax.add_patch(FancyArrowPatch((x, y), (x2, y2), arrowstyle="->", mutation_scale=12, lw=1.0))

    ax.text(0, 0, "six lateral\nside intakes", ha="center", va="center", fontsize=10)
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.7, 1.7)
    ax.set_title("Eight-sector knot/shadow geometry: tip vs six-side sink")
    savefig("eight_sector_sink_geometry.svg")


def draw_dark_visible_ratio() -> None:
    target = 0.120 / 0.0224
    O = 0.9837806705
    A_tip = 1 / 56 + (7 / 8) * (1 / 448) * O
    A_side = 6 / 56
    ratio = A_side / A_tip

    fig, ax = plt.subplots(figsize=(6, 4))
    vals = [ratio, target]
    labels = ["MCIFT side/tip\n6-sector sink", "Planck ratio\nΩc/Ωb"]
    bars = ax.bar(labels, vals)
    ax.set_ylabel("dark / visible ratio")
    ax.set_title("v0.13 dark-manifest ratio comparison")
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.05, f"{val:.3f}", ha="center", fontsize=10)
    ax.set_ylim(0, 6.2)
    savefig("dark_visible_ratio.svg")


def draw_mechanics_overview() -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis("off")
    rows = [
        ("Activation", "L visibility, H mass, G gravity, K coherence"),
        ("Complexity", "Cₙ=2ⁿ ; Sₙ=a n−2ⁿ ; mode 4 fails"),
        ("Exchange", "Γᵢⱼ: info, frequency, phase alignment ; X=e^{ηΓ}"),
        ("Amplitude", "A=I−Iˢ ; m=A² ; Δ corrections square into mass"),
        ("Anchor", "k*=1 ; B_C(1)=(C−1)/C ; B₈=7/8"),
        ("Source", "Fibonacci-Higgs overlap + capture window + reservoir gate"),
        ("Visible", "one axial tip intake"),
        ("Dark", "six lateral side intakes ; light suppressed, mass/gravity active"),
    ]

    for i, (title, desc) in enumerate(rows):
        y = 0.9 - i * 0.105
        ax.add_patch(
            FancyBboxPatch((0.05, y - 0.035), 0.18, 0.07, boxstyle="round,pad=0.015", fill=False, lw=1.2)
        )
        ax.text(0.14, y, title, ha="center", va="center", fontsize=10, weight="bold")
        ax.add_patch(
            FancyBboxPatch((0.32, y - 0.035), 0.62, 0.07, boxstyle="round,pad=0.015", fill=False, lw=1.2)
        )
        ax.text(0.63, y, desc, ha="center", va="center", fontsize=9)
        if i < len(rows) - 1:
            ax.add_patch(
                FancyArrowPatch((0.23, y - 0.035), (0.23, y - 0.07), arrowstyle="->", mutation_scale=10, lw=1)
            )

    ax.text(0.5, 0.99, "MCIFT mechanics overview through v0.13", ha="center", fontsize=14, weight="bold")
    savefig("mechanics_overview.svg")


def main() -> None:
    draw_activation_channels()
    draw_field_source_pipeline()
    draw_capture_window()
    draw_reservoir_gate()
    draw_eight_sector_geometry()
    draw_dark_visible_ratio()
    draw_mechanics_overview()


if __name__ == "__main__":
    main()
