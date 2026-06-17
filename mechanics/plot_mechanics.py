#!/usr/bin/env python3
"""
Generate MCIFT mechanics diagrams through v0.14.

Goal:
    one SVG graph or diagram for every named mechanic in mechanics_v0.13.md.

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


def add_box(ax, xy, text, w=0.18, h=0.11, fontsize=9):
    x, y = xy
    ax.add_patch(
        FancyBboxPatch(
            (x - w / 2, y - h / 2),
            w,
            h,
            boxstyle="round,pad=0.02",
            fill=False,
            lw=1.3,
        )
    )
    ax.text(x, y, text, ha="center", va="center", fontsize=fontsize)


def add_arrow(ax, a, b, rad=0.0):
    ax.add_patch(
        FancyArrowPatch(
            a,
            b,
            arrowstyle="->",
            mutation_scale=12,
            lw=1.2,
            connectionstyle=f"arc3,rad={rad}",
        )
    )


def draw_mechanics_overview() -> None:
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.axis("off")
    rows = [
        ("1 Activation", "L visibility, H mass, G gravity, K coherence"),
        ("2 Complexity", "C_n = 2^n"),
        ("3 Stability", "S_n = a n - 2^n ; fourth mode fails"),
        ("4 Surface", "A_n = (C_n - 1)^Df"),
        ("5 Higgs window", "finite mass-capture response"),
        ("6 Exchange", "information, frequency, phase alignment"),
        ("7 Amplitude", "mass = amplitude squared"),
        ("8 Anchor", "one contact point gives 7/8 free fraction"),
        ("9 Source", "Fibonacci overlap, speed window, reservoir gate"),
        ("10 Dark sink", "six side intakes vs one tip intake"),
    ]
    for i, (title, desc) in enumerate(rows):
        y = 0.92 - i * 0.085
        add_box(ax, (0.17, y), title, w=0.22, h=0.055, fontsize=9)
        add_box(ax, (0.61, y), desc, w=0.58, h=0.055, fontsize=9)
        if i < len(rows) - 1:
            add_arrow(ax, (0.17, y - 0.03), (0.17, y - 0.055))
    ax.text(0.5, 0.995, "MCIFT mechanics overview through v0.14", ha="center", fontsize=14, weight="bold")
    savefig("mechanics_overview.svg")


def draw_activation_channels() -> None:
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.axis("off")
    nodes = {
        "Information\npoint": (0.08, 0.5),
        "Knot\ncoherence K": (0.28, 0.5),
        "Visibility\nL*K": (0.52, 0.78),
        "Mass\nH*K": (0.52, 0.5),
        "Gravity\nG*H*K": (0.52, 0.22),
        "Visible\nmanifest": (0.82, 0.78),
        "Dark\nmanifest": (0.82, 0.45),
        "Unmanifest": (0.82, 0.12),
    }
    for text, xy in nodes.items():
        add_box(ax, xy, text, w=0.16, h=0.12, fontsize=10)
    add_arrow(ax, nodes["Information\npoint"], nodes["Knot\ncoherence K"])
    add_arrow(ax, nodes["Knot\ncoherence K"], nodes["Visibility\nL*K"], 0.15)
    add_arrow(ax, nodes["Knot\ncoherence K"], nodes["Mass\nH*K"])
    add_arrow(ax, nodes["Knot\ncoherence K"], nodes["Gravity\nG*H*K"], -0.15)
    add_arrow(ax, nodes["Visibility\nL*K"], nodes["Visible\nmanifest"])
    add_arrow(ax, nodes["Mass\nH*K"], nodes["Visible\nmanifest"], 0.1)
    add_arrow(ax, nodes["Gravity\nG*H*K"], nodes["Visible\nmanifest"], -0.15)
    add_arrow(ax, nodes["Mass\nH*K"], nodes["Dark\nmanifest"], 0.05)
    add_arrow(ax, nodes["Gravity\nG*H*K"], nodes["Dark\nmanifest"], -0.05)
    add_arrow(ax, nodes["Information\npoint"], nodes["Unmanifest"], -0.25)
    ax.text(0.5, 0.98, "Activation mechanic: light controls visibility, not existence", ha="center", fontsize=13, weight="bold")
    savefig("activation_channels.svg")


def draw_complexity_growth() -> None:
    n = np.arange(1, 6)
    C = 2 ** n
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(n, C, marker="o", lw=2)
    ax.set_xlabel("mode n")
    ax.set_ylabel("complexity C_n")
    ax.set_title("Complexity mechanic: C_n = 2^n")
    for x, y in zip(n, C):
        ax.text(x, y + 0.8, f"{y}", ha="center", fontsize=9)
    savefig("complexity_growth.svg")


def draw_stability_modes() -> None:
    n = np.arange(1, 6)
    a = 3.5
    S = a * n - 2 ** n
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.axhline(0, lw=1)
    ax.bar(n, S)
    ax.set_xlabel("mode n")
    ax.set_ylabel("stability S_n")
    ax.set_title("Stability mechanic: S_n = a n - 2^n, a = 3.5")
    for x, y in zip(n, S):
        label = "stable" if y > 0 else "fails"
        ax.text(x, y + (0.25 if y >= 0 else -0.8), label, ha="center", fontsize=9)
    savefig("stability_modes.svg")


def draw_fractal_surface() -> None:
    C = np.arange(2, 17)
    Df_values = [2.5, 3.5, 4.0]
    fig, ax = plt.subplots(figsize=(7, 4))
    for Df in Df_values:
        ax.plot(C, (C - 1) ** Df, lw=2, label=f"Df={Df}")
    ax.set_xlabel("complexity C")
    ax.set_ylabel("catching surface A")
    ax.set_title("Fractal surface mechanic: A=(C-1)^Df")
    ax.set_yscale("log")
    ax.legend()
    savefig("fractal_surface.svg")


def draw_higgs_response_window() -> None:
    C = np.linspace(1.1, 20, 500)
    Cstar = 8
    w = 0.45
    H = np.exp(-((np.log(C) - np.log(Cstar)) ** 2) / (2 * w**2))
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(C, H, lw=2)
    ax.axvline(Cstar, ls="--", lw=1)
    ax.set_xlabel("complexity C")
    ax.set_ylabel("Higgs response H(C)")
    ax.set_title("Finite Higgs-response mechanic")
    ax.text(Cstar + 0.4, 0.9, "resonance window", fontsize=9)
    savefig("higgs_response_window.svg")


def draw_exchange_alignment() -> None:
    dI = np.linspace(-3, 3, 400)
    dw = np.linspace(-3, 3, 400)
    phase = np.linspace(0, np.pi, 400)
    gI = np.exp(-(dI**2) / 2)
    gw = np.exp(-(dw**2) / 2)
    gp = np.cos(phase) ** 2
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(dI, gI, label="information match")
    ax.plot(dw, gw, label="frequency match")
    ax.plot(phase - np.pi / 2, gp, label="phase cos^2")
    ax.set_xlabel("mismatch coordinate")
    ax.set_ylabel("exchange factor")
    ax.set_title("Exchange mechanic: alignment opens exchange")
    ax.legend()
    savefig("exchange_alignment.svg")


def draw_exchange_densification() -> None:
    Gamma = np.linspace(0, 3, 400)
    eta = 0.8
    X = np.exp(eta * Gamma)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(Gamma, X, lw=2)
    ax.set_xlabel("whole-knot exchange Gamma")
    ax.set_ylabel("densification X = exp(eta Gamma)")
    ax.set_title("Exchange densification mechanic")
    savefig("exchange_densification.svg")


def draw_amplitude_mass() -> None:
    A = np.linspace(-3, 3, 400)
    m = A**2
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(A, m, lw=2)
    ax.set_xlabel("amplitude A")
    ax.set_ylabel("mass m")
    ax.set_title("Amplitude-first mass mechanic: m = A^2")
    ax.text(0.1, 7.5, "sign/orientation can flip; mass stays positive", fontsize=9)
    savefig("amplitude_mass.svg")


def draw_shadow_correction() -> None:
    f = np.linspace(0, 1, 200)
    base = 1708.60405054
    s1 = 1 / 56
    s2 = 1 / 448
    m = base * (1 + s1 + f * s2) ** 2
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(f, m, lw=2)
    ax.axvline(7 / 8, ls="--", lw=1)
    ax.set_xlabel("shadow echo fraction f")
    ax.set_ylabel("tau-like mass result MeV")
    ax.set_title("Shadow amplitude correction mechanic")
    ax.text(0.76, m[np.argmin(abs(f - 7 / 8))] + 1, "f = 7/8", fontsize=9)
    savefig("shadow_correction.svg")


def draw_anchor_contacts() -> None:
    k = np.arange(0, 9)
    M = k * (k - 1) / 2
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.bar(k, M)
    ax.set_xlabel("contact count k")
    ax.set_ylabel("bridge count M(k)")
    ax.set_title("One-point anchor mechanic: M(k)=k(k-1)/2")
    ax.axvline(1, ls="--", lw=1)
    ax.text(1.15, 5, "k*=1 avoids bridges", fontsize=9)
    savefig("anchor_contacts.svg")


def draw_spin_vortex_fraction() -> None:
    C = np.arange(2, 17)
    B = (C - 1) / C
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(C, B, marker="o", lw=2)
    ax.axvline(8, ls="--", lw=1)
    ax.axhline(7 / 8, ls=":", lw=1)
    ax.set_xlabel("sector count C")
    ax.set_ylabel("free spin-vortex fraction B_C(1)")
    ax.set_title("Spin-vortex mechanic: B_C(1)=(C-1)/C")
    ax.text(8.2, 0.82, "C=8 gives 7/8", fontsize=9)
    savefig("spin_vortex_fraction.svg")


def draw_fibonacci_resonance() -> None:
    t = np.linspace(0, 8 * np.pi, 1000)
    phi = (1 + np.sqrt(5)) / 2
    r = 0.25
    omega = r * np.sin(phi * t)
    O = np.exp(-(omega**2) / 2)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t, O, lw=1.5)
    ax.set_xlabel("time")
    ax.set_ylabel("Higgs overlap O_phi")
    ax.set_title("Fibonacci-Higgs resonance mechanic")
    ax.text(1, 0.94, "golden wobble around resonance", fontsize=9)
    savefig("fibonacci_resonance.svg")


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
    ax.set_title("Funnel-speed capture mechanic")
    ax.text(0.45, 0.2, "too slow", ha="center", fontsize=9)
    ax.text(v[np.argmax(W)], 0.85, "capture", ha="center", fontsize=9)
    ax.text(3.35, 0.25, "too fast", ha="center", fontsize=9)
    ax.set_ylim(0, 1.1)
    savefig("capture_window.svg")


def draw_reservoir_gate() -> None:
    R = np.logspace(-3, 3, 400)
    Rgate = R / (R + 1)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.semilogx(R, Rgate, lw=2)
    ax.set_xlabel("reservoir strength R4/R*")
    ax.set_ylabel("bounded availability")
    ax.set_title("Fourth-mode reservoir gate mechanic")
    ax.axhline(1, ls=":", lw=1)
    ax.axvline(1, ls="--", lw=1)
    ax.text(20, 0.85, "saturates at 1", fontsize=9)
    ax.set_ylim(0, 1.05)
    savefig("reservoir_gate.svg")


def draw_field_source_pipeline() -> None:
    fig, ax = plt.subplots(figsize=(12, 3.2))
    ax.axis("off")
    labels = [
        "anchor",
        "vortex\nOmega or kappa",
        "speed\nW",
        "aperture\nP+BEO",
        "reservoir\nR gate",
        "core\ndelta",
        "source\nSigma",
        "mass\n(1+Sigma)^2",
    ]
    xs = np.linspace(0.06, 0.94, len(labels))
    for x, label in zip(xs, labels):
        add_box(ax, (x, 0.5), label, w=0.105, h=0.23, fontsize=8)
    for x1, x2 in zip(xs[:-1], xs[1:]):
        add_arrow(ax, (x1 + 0.055, 0.5), (x2 - 0.055, 0.5))
    ax.text(0.5, 0.9, "Field-source pipeline mechanic", ha="center", fontsize=13, weight="bold")
    savefig("field_source_pipeline.svg")


def draw_source_terms_bar() -> None:
    O = 0.9837806705
    vals = {
        "P=1/56": 1 / 56,
        "echo=(7/8)(1/448)O": (7 / 8) * (1 / 448) * O,
        "tip total": 1 / 56 + (7 / 8) * (1 / 448) * O,
        "side=6/56": 6 / 56,
    }
    fig, ax = plt.subplots(figsize=(8, 4))
    bars = ax.bar(range(len(vals)), list(vals.values()))
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(list(vals.keys()), rotation=20, ha="right")
    ax.set_ylabel("aperture/source contribution")
    ax.set_title("Source term mechanic: tip terms vs side-sink aperture")
    for bar, val in zip(bars, vals.values()):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.003, f"{val:.4f}", ha="center", fontsize=9)
    savefig("source_terms_bar.svg")


def draw_motion_exchange() -> None:
    G = np.linspace(0, 3, 400)
    eta = 1.0
    beta = np.tanh(eta * G)
    gamma = np.cosh(eta * G)
    fig, ax1 = plt.subplots(figsize=(7, 4))
    ax1.plot(G, beta, lw=2, label="beta=tanh(eta|Gamma|)")
    ax1.set_xlabel("directional exchange magnitude")
    ax1.set_ylabel("velocity proxy beta")
    ax2 = ax1.twinx()
    ax2.plot(G, gamma, lw=2, ls="--", label="gamma=cosh(eta|Gamma|)")
    ax2.set_ylabel("effective gamma factor")
    ax1.set_title("Motion mechanic: directional exchange creates velocity")
    savefig("motion_exchange.svg")


def draw_entanglement_shared_channel() -> None:
    dc = np.linspace(0, 4, 400)
    sigma = 1.0
    E = np.exp(-(dc**2) / (2 * sigma**2))
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(dc, E, lw=2)
    ax.set_xlabel("internal channel distance d_c")
    ax.set_ylabel("shared-channel strength")
    ax.set_title("Entanglement/shared-channel mechanic")
    ax.text(1.6, 0.6, "closer channels -> stronger shared amplitude", fontsize=9)
    savefig("entanglement_shared_channel.svg")


def draw_confinement_complexity() -> None:
    C = np.linspace(1, 40, 400)
    threshold = 20
    confinement = 1 / (1 + np.exp(-(C - threshold) / 3))
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(C, confinement, lw=2)
    ax.axvline(threshold, ls="--", lw=1)
    ax.set_xlabel("coherent complexity")
    ax.set_ylabel("confinement / channel separation proxy")
    ax.set_title("Confinement mechanic: high complexity separates channels")
    savefig("confinement_complexity.svg")


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
    ax.annotate("visible\naxis tip", xy=(0, 0.95), xytext=(0, 1.45), ha="center", arrowprops=dict(arrowstyle="->", lw=1.2), fontsize=9)
    ax.annotate("opposite\naxis", xy=(0, -0.95), xytext=(0, -1.35), ha="center", arrowprops=dict(arrowstyle="->", lw=1.2), fontsize=9)
    for ang in angles[[1, 2, 3, 5, 6, 7]]:
        x, y = np.cos(ang) * 1.25, np.sin(ang) * 1.25
        x2, y2 = np.cos(ang) * 0.9, np.sin(ang) * 0.9
        add_arrow(ax, (x, y), (x2, y2))
    ax.text(0, 0, "six lateral\nside intakes", ha="center", va="center", fontsize=10)
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.7, 1.7)
    ax.set_title("Eight-sector dark-sink geometry mechanic")
    savefig("eight_sector_sink_geometry.svg")


def draw_dark_visible_ratio() -> None:
    target = 0.120 / 0.0224
    O = 0.9837806705
    A_tip = 1 / 56 + (7 / 8) * (1 / 448) * O
    A_side = 6 / 56
    ratio = A_side / A_tip
    fig, ax = plt.subplots(figsize=(6, 4))
    vals = [ratio, target]
    labels = ["MCIFT\nside/tip", "Planck\nOmega_c/Omega_b"]
    bars = ax.bar(labels, vals)
    ax.set_ylabel("dark / visible ratio")
    ax.set_title("Dark-visible ratio mechanic")
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.05, f"{val:.3f}", ha="center", fontsize=10)
    ax.set_ylim(0, 6.2)
    savefig("dark_visible_ratio.svg")


def draw_cern_event_proxy() -> None:
    rng = np.random.default_rng(13)
    ht = rng.lognormal(mean=6.0, sigma=0.45, size=900)
    met_bg = rng.gamma(shape=2.0, scale=50.0, size=900)
    met_sig = rng.gamma(shape=3.5, scale=80.0, size=120)
    ratio_bg = met_bg / ht
    ratio_sig = met_sig / ht[:120]
    fig, ax = plt.subplots(figsize=(7, 4))
    bins = np.linspace(0, 1.5, 40)
    ax.hist(ratio_bg, bins=bins, histtype="step", label="SM-like proxy")
    ax.hist(ratio_sig, bins=bins, histtype="step", label="side-channel proxy")
    ax.set_xlabel("MET / HT")
    ax.set_ylabel("events")
    ax.set_title("CERN two-drill event proxy mechanic")
    ax.legend()
    savefig("cern_event_proxy.svg")


def draw_light_activation_gate() -> None:
    d = np.linspace(-3, 3, 400)
    L = np.exp(-(d**2) / 2)
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(d, L, lw=2)
    ax.set_xlabel("light-channel mismatch")
    ax.set_ylabel("visibility activation L")
    ax.set_title("Light-channel gate mechanic")
    ax.text(0.5, 0.8, "mismatch suppresses visibility only", fontsize=9)
    savefig("light_activation_gate.svg")


def main() -> None:
    # One figure per major mechanic.
    draw_mechanics_overview()
    draw_activation_channels()
    draw_light_activation_gate()
    draw_complexity_growth()
    draw_stability_modes()
    draw_fractal_surface()
    draw_higgs_response_window()
    draw_exchange_alignment()
    draw_exchange_densification()
    draw_amplitude_mass()
    draw_shadow_correction()
    draw_anchor_contacts()
    draw_spin_vortex_fraction()
    draw_fibonacci_resonance()
    draw_capture_window()
    draw_reservoir_gate()
    draw_field_source_pipeline()
    draw_source_terms_bar()
    draw_motion_exchange()
    draw_entanglement_shared_channel()
    draw_confinement_complexity()
    draw_eight_sector_geometry()
    draw_dark_visible_ratio()
    draw_cern_event_proxy()


if __name__ == "__main__":
    main()
