"""
MCIFT v1.07 toy benchmark:
Symmetric four-facet mass overload and collapse breakpoint.

Goal
----
Test a hunch within a nonlinear toy model:
    as central mass grows, the tetrahedral cell first breathes,
    but beyond a breakpoint the core collapses inward into an inner channel.

Important scope
---------------
This is not a physical black-hole or big-bang model.
It is a benchmark of one falsifiable toy hypothesis.

Model choices
-------------
- Four facet inputs are perfectly symmetric, so no directional sink is present.
- Core mass M gathers from the symmetric mode J0.
- The preferred radius first expands with moderate mass and then shrinks
  at high mass:
      R_eq(M) = R0 * (1 + a dM - b dM^2)
- Once R crosses a collapse threshold, the dynamics switch to an
  inner-channel target radius R_inner.
- Under symmetric loading this benchmark only tests stable breathing vs
  inward collapse. It does NOT test shell break from asymmetry.

Outputs
-------
mcift_v107_mass_breakpoint_benchmark.gif
mcift_v107_mass_breakpoint_benchmark_metrics.json
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter


HERE = Path(__file__).resolve().parent
GIF_PATH = HERE / "mcift_v107_mass_breakpoint_benchmark.gif"
METRICS_PATH = HERE / "mcift_v107_mass_breakpoint_benchmark_metrics.json"

DT = 0.004
DURATION = 14.0
SAVE_EVERY = 28

M0 = 1.0
R0 = 0.16

ETA_M = 0.85
LAMBDA_M = 0.42
BASE_FLUX = LAMBDA_M * M0 / (4.0 * ETA_M)

A_EXPAND = 0.34
B_SHRINK = 0.18
K_R = 17.0
GAMMA_R = 0.42

R_COLLAPSE = 0.060
R_INNER = 0.036
K_COLLAPSE = 24.0
GAMMA_COLLAPSE = 0.60

PULSE_CENTER = 5.0
PULSE_WIDTH = 0.95

EDGES = [(i, j) for i in range(4) for j in range(i + 1, 4)]


def regular_tetrahedron(edge_length: float = 1.0) -> np.ndarray:
    vertices = np.array(
        [
            [1.0, 1.0, 1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [-1.0, -1.0, 1.0],
        ],
        dtype=float,
    )
    return vertices * edge_length / (2.0 * math.sqrt(2.0))


def gaussian_pulse(t: float, amplitude: float) -> float:
    return amplitude * math.exp(-0.5 * ((t - PULSE_CENTER) / PULSE_WIDTH) ** 2)


def simulate(amplitude: float, duration: float = DURATION) -> dict:
    steps = int(duration / DT)

    mass = M0
    radius = R0
    radial_velocity = 0.0
    collapsed = False
    collapse_time = None

    history = {
        "time": [],
        "mass": [],
        "radius": [],
        "radius_eq": [],
        "radial_velocity": [],
        "radial_energy": [],
        "collapsed": [],
        "pulse": [],
    }

    for step in range(steps + 1):
        t = step * DT
        pulse = gaussian_pulse(t, amplitude)
        j0 = BASE_FLUX + pulse

        mass_rate = 4.0 * ETA_M * j0 - LAMBDA_M * mass
        mass += mass_rate * DT
        delta_m = mass - M0

        radius_eq = R0 * (1.0 + A_EXPAND * delta_m - B_SHRINK * delta_m**2)

        if (not collapsed) and (radius < R_COLLAPSE):
            collapsed = True
            collapse_time = t

        if collapsed:
            radial_acc = (
                -K_COLLAPSE * (radius - R_INNER)
                - GAMMA_COLLAPSE * radial_velocity
            )
        else:
            radial_acc = (
                -K_R * (radius - radius_eq)
                - GAMMA_R * radial_velocity
            )

        radial_velocity += radial_acc * DT
        radius += radial_velocity * DT
        radius = max(radius, 0.0)

        if step % SAVE_EVERY == 0:
            target = R_INNER if collapsed else radius_eq
            energy = 0.5 * radial_velocity**2 + 0.5 * (
                (K_COLLAPSE if collapsed else K_R) * (radius - target) ** 2
            )

            history["time"].append(t)
            history["mass"].append(mass)
            history["radius"].append(radius)
            history["radius_eq"].append(radius_eq)
            history["radial_velocity"].append(radial_velocity)
            history["radial_energy"].append(energy)
            history["collapsed"].append(collapsed)
            history["pulse"].append(pulse)

    for key in history:
        history[key] = np.asarray(history[key])

    history["amplitude"] = amplitude
    history["collapse_time"] = collapse_time
    return history


def benchmark(amplitudes: np.ndarray) -> list[dict]:
    rows = []

    for amplitude in amplitudes:
        history = simulate(float(amplitude))
        collapsed = bool(np.any(history["collapsed"]))
        collapse_indices = np.where(history["collapsed"])[0]
        collapse_time = (
            float(history["time"][collapse_indices[0]])
            if len(collapse_indices) > 0
            else None
        )
        rows.append(
            {
                "amplitude": float(amplitude),
                "peak_mass": float(np.max(history["mass"])),
                "peak_radius": float(np.max(history["radius"])),
                "min_radius": float(np.min(history["radius"])),
                "collapsed": collapsed,
                "collapse_time": collapse_time,
            }
        )

    return rows


def sphere_lines(
    center: np.ndarray,
    radius: float,
    count: int = 48,
) -> list[np.ndarray]:
    angle = np.linspace(0.0, 2.0 * math.pi, count)
    return [
        np.column_stack(
            [
                center[0] + radius * np.cos(angle),
                center[1] + radius * np.sin(angle),
                np.full_like(angle, center[2]),
            ]
        ),
        np.column_stack(
            [
                center[0] + radius * np.cos(angle),
                np.full_like(angle, center[1]),
                center[2] + radius * np.sin(angle),
            ]
        ),
        np.column_stack(
            [
                np.full_like(angle, center[0]),
                center[1] + radius * np.cos(angle),
                center[2] + radius * np.sin(angle),
            ]
        ),
    ]


def make_animation(
    animated: dict,
    subcritical: dict,
    supercritical: dict,
    bench_rows: list[dict],
    threshold_amplitude: float,
) -> None:
    fig = plt.figure(figsize=(12.3, 7.1))
    ax3d = fig.add_subplot(2, 2, 1, projection="3d")
    axtime = fig.add_subplot(2, 2, 2)
    axbench = fig.add_subplot(2, 2, 3)
    axmass = fig.add_subplot(2, 2, 4)

    vertices = regular_tetrahedron()
    times = animated["time"]
    center = np.zeros(3)

    amplitudes = np.array([row["amplitude"] for row in bench_rows])
    min_radii = np.array([row["min_radius"] for row in bench_rows])
    peak_masses = np.array([row["peak_mass"] for row in bench_rows])
    collapsed_mask = np.array([row["collapsed"] for row in bench_rows], dtype=bool)

    def update(frame: int):
        ax3d.cla()
        axtime.cla()
        axbench.cla()
        axmass.cla()

        t = times[frame]
        radius = float(animated["radius"][frame])
        radius_eq = float(animated["radius_eq"][frame])
        mass = float(animated["mass"][frame])
        pulse = float(animated["pulse"][frame])
        collapsed = bool(animated["collapsed"][frame])

        for i, j in EDGES:
            ax3d.plot(
                [vertices[i, 0], vertices[j, 0]],
                [vertices[i, 1], vertices[j, 1]],
                [vertices[i, 2], vertices[j, 2]],
                linewidth=2.0,
            )

        ax3d.scatter(
            vertices[:, 0],
            vertices[:, 1],
            vertices[:, 2],
            s=48,
            depthshade=True,
        )

        for circle in sphere_lines(center, radius):
            ax3d.plot(circle[:, 0], circle[:, 1], circle[:, 2], linewidth=1.8)

        for circle in sphere_lines(center, R_INNER):
            ax3d.plot(
                circle[:, 0],
                circle[:, 1],
                circle[:, 2],
                linewidth=1.0,
                alpha=0.45,
            )

        ax3d.scatter(
            [0.0],
            [0.0],
            [0.0],
            s=70 + 900 * radius**2,
            marker="o",
            depthshade=False,
        )

        ax3d.set_xlim(-0.7, 0.7)
        ax3d.set_ylim(-0.7, 0.7)
        ax3d.set_zlim(-0.7, 0.7)
        ax3d.set_box_aspect((1, 1, 1))
        ax3d.set_xlabel("x")
        ax3d.set_ylabel("y")
        ax3d.set_zlabel("z")
        ax3d.view_init(elev=23, azim=35 + frame * 0.28)
        ax3d.set_title("Symmetric overload run")

        phase = "stable breathing" if not collapsed else "inner-channel collapse branch"
        ax3d.text2D(0.02, 0.96, phase, transform=ax3d.transAxes)
        ax3d.text2D(
            0.02,
            0.88,
            (
                f"t = {t:.2f}\n"
                f"pulse amplitude A = {animated['amplitude']:.3f}\n"
                f"facet inflow pulse = {pulse:.3f}\n"
                f"core mass M = {mass:.3f}\n"
                f"radius R = {radius:.3f}\n"
                f"preferred R_eq = {radius_eq:.3f}"
            ),
            transform=ax3d.transAxes,
            va="top",
            family="monospace",
        )
        ax3d.text2D(
            0.02,
            0.03,
            "Symmetric input only: this tests breathing vs inward collapse.",
            transform=ax3d.transAxes,
        )

        axtime.plot(
            subcritical["time"],
            subcritical["radius"],
            label=f"stable A={subcritical['amplitude']:.3f}",
        )
        axtime.plot(
            animated["time"],
            animated["radius"],
            label=f"threshold A={animated['amplitude']:.3f}",
        )
        axtime.plot(
            supercritical["time"],
            supercritical["radius"],
            label=f"collapse A={supercritical['amplitude']:.3f}",
        )
        axtime.axhline(R_COLLAPSE, linestyle="--", linewidth=1.0, label="collapse radius")
        axtime.axhline(R_INNER, linestyle=":", linewidth=1.0, label="inner channel radius")
        axtime.axvline(t, linewidth=1.0, alpha=0.65)
        axtime.set_xlabel("time")
        axtime.set_ylabel("core radius")
        axtime.set_title("Radius histories around the breakpoint")
        axtime.grid(True, alpha=0.25)
        axtime.legend(fontsize=7, loc="upper right")

        if np.any(~collapsed_mask):
            axbench.plot(
                amplitudes[~collapsed_mask],
                min_radii[~collapsed_mask],
                marker="o",
                linewidth=1.6,
            )
        if np.any(collapsed_mask):
            axbench.plot(
                amplitudes[collapsed_mask],
                min_radii[collapsed_mask],
                marker="o",
                linewidth=1.6,
            )
        axbench.axhline(R_COLLAPSE, linestyle="--", linewidth=1.0, label="collapse threshold")
        axbench.axvline(
            threshold_amplitude,
            linestyle="--",
            linewidth=1.0,
            label=f"first collapse A≈{threshold_amplitude:.3f}",
        )
        axbench.axvline(animated["amplitude"], linewidth=1.0, alpha=0.65)
        axbench.set_xlabel("symmetric pulse amplitude A")
        axbench.set_ylabel("minimum radius during run")
        axbench.set_title("Benchmark sweep")
        axbench.grid(True, alpha=0.25)
        axbench.legend(fontsize=7, loc="upper right")

        axmass.plot(amplitudes, peak_masses, marker="o", linewidth=1.6)
        axmass.axvline(threshold_amplitude, linestyle="--", linewidth=1.0)
        axmass.axvline(animated["amplitude"], linewidth=1.0, alpha=0.65)
        axmass.set_xlabel("symmetric pulse amplitude A")
        axmass.set_ylabel("peak core mass")
        axmass.set_title("Peak mass at each benchmark point")
        axmass.grid(True, alpha=0.25)

        fig.suptitle(
            "MCIFT toy benchmark — central mass breakpoint under symmetric four-facet loading",
            y=0.98,
        )
        fig.tight_layout(rect=[0, 0, 1, 0.95])
        return []

    animation = FuncAnimation(
        fig,
        update,
        frames=len(times),
        interval=90,
        blit=False,
    )
    animation.save(
        GIF_PATH,
        writer=PillowWriter(fps=10),
        dpi=80,
    )
    plt.close(fig)


def summarize(
    bench_rows: list[dict],
    threshold_amplitude: float,
    subcritical: dict,
    critical: dict,
    supercritical: dict,
) -> dict:
    threshold_row = next(
        row
        for row in bench_rows
        if abs(row["amplitude"] - threshold_amplitude) < 1e-12
    )
    return {
        "status": "toy_nonlinear_breakpoint_benchmark_only",
        "model_scope": {
            "symmetric_four_facet_input_only": True,
            "directional_sink_tested": False,
            "breakup_mode_tested": False,
            "inward_collapse_mode_tested": True,
            "physical_big_bang_or_black_hole_claim": False,
        },
        "nonlinear_radius_law": {
            "R0": R0,
            "R_eq_formula": "R0 * (1 + a*dM - b*dM^2)",
            "a": A_EXPAND,
            "b": B_SHRINK,
            "collapse_radius": R_COLLAPSE,
            "inner_channel_radius": R_INNER,
        },
        "benchmark": {
            "amplitudes_tested": [row["amplitude"] for row in bench_rows],
            "collapsed_count": int(sum(row["collapsed"] for row in bench_rows)),
            "first_collapse_amplitude": threshold_amplitude,
            "threshold_row": threshold_row,
        },
        "reference_runs": {
            "last_stable": {
                "amplitude": subcritical["amplitude"],
                "peak_mass": float(np.max(subcritical["mass"])),
                "min_radius": float(np.min(subcritical["radius"])),
                "collapsed": bool(np.any(subcritical["collapsed"])),
            },
            "first_collapse": {
                "amplitude": critical["amplitude"],
                "peak_mass": float(np.max(critical["mass"])),
                "min_radius": float(np.min(critical["radius"])),
                "collapse_time": float(
                    critical["time"][np.where(critical["collapsed"])[0][0]]
                ),
                "collapsed": True,
            },
            "next_supercritical": {
                "amplitude": supercritical["amplitude"],
                "peak_mass": float(np.max(supercritical["mass"])),
                "min_radius": float(np.min(supercritical["radius"])),
                "collapse_time": float(
                    supercritical["time"][np.where(supercritical["collapsed"])[0][0]]
                ),
                "collapsed": True,
            },
        },
        "interpretation": (
            "Within this toy nonlinear closure law, a finite overload breakpoint "
            "does appear: below it the cell breathes and remains on the outer branch; "
            "above it the core crosses the collapse radius and is redirected onto an "
            "inner-channel collapse branch."
        ),
    }


def main() -> None:
    amplitudes = np.linspace(0.00, 1.00, 28)
    bench_rows = benchmark(amplitudes)

    collapse_rows = [row for row in bench_rows if row["collapsed"]]
    stable_rows = [row for row in bench_rows if not row["collapsed"]]

    if not collapse_rows or not stable_rows:
        raise RuntimeError("Parameter range did not bracket a breakpoint.")

    threshold_amplitude = collapse_rows[0]["amplitude"]
    last_stable_amplitude = stable_rows[-1]["amplitude"]
    next_supercritical_amplitude = collapse_rows[
        min(1, len(collapse_rows) - 1)
    ]["amplitude"]

    subcritical = simulate(last_stable_amplitude)
    critical = simulate(threshold_amplitude)
    supercritical = simulate(next_supercritical_amplitude)

    make_animation(
        critical,
        subcritical,
        supercritical,
        bench_rows,
        threshold_amplitude,
    )

    summary = summarize(
        bench_rows,
        threshold_amplitude,
        subcritical,
        critical,
        supercritical,
    )
    METRICS_PATH.write_text(
        json.dumps(summary, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))
    print(f"GIF: {GIF_PATH}")
    print(f"Metrics: {METRICS_PATH}")


if __name__ == "__main__":
    main()
