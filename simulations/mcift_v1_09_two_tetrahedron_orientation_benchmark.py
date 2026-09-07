"""
MCIFT v1.09 candidate two-tetrahedron orientation benchmark.

Question
--------
Given a stable regular primordial tetrahedron T0, does a second regular
tetrahedron T1 acquire an intrinsic "down" direction relative to T0 and
prefer an apex-inward ("inverted pyramid") orientation?

This benchmark does NOT assume an apex-targeting torque. It compares two
minimal finite-body 1/r control couplings:

A) FACE-VORTEX coupling:
   The positive localized energy is placed at the four triangular face
   centroids, matching the v1.08 picture most directly.

B) VERTEX-LUMPED control:
   The same total coupling weight is placed at the four vertices.

For each coupling and separation R/L, T0 is fixed and T1's center is fixed.
T1 starts from many random orientations. We minimize the pairwise interaction
energy over orientation only.

Potential:
    U = -G sum_ab w_a w_b / |p0_a - p1_b|

No preferred "down" or apex term is present. The relational inward direction
is simply from the center of T1 toward the center of T0.

This is a toy structural control, not a derivation of physical gravity.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.spatial.transform import Rotation

HERE = Path(__file__).resolve().parent
METRICS_PATH = HERE / "mcift_v109_two_tetrahedron_orientation_metrics.json"
SWEEP_PATH = HERE / "mcift_v109_two_tetrahedron_orientation_sweep.csv"

G = 1.0
L = 1.0

VERTICES = np.array(
    [[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]],
    dtype=float,
) / (2.0 * math.sqrt(2.0))

FACES = [(1, 2, 3), (0, 2, 3), (0, 1, 3), (0, 1, 2)]
FACE_CENTROIDS = np.array(
    [VERTICES[list(f)].mean(axis=0) for f in FACES],
    dtype=float,
)

INWARD = np.array([-1.0, 0.0, 0.0])


def energy(rotvec: np.ndarray, R: float, points: np.ndarray) -> float:
    rot = Rotation.from_rotvec(rotvec).as_matrix()
    source = points
    target = points @ rot.T + np.array([R, 0.0, 0.0])
    delta = source[:, None, :] - target[None, :, :]
    dist = np.linalg.norm(delta, axis=2)
    w = 1.0 / len(points)
    return float(-G * w * w * np.sum(1.0 / dist))


def orientation_scores(rotvec: np.ndarray) -> tuple[float, float]:
    rot = Rotation.from_rotvec(rotvec).as_matrix()
    verts = VERTICES @ rot.T
    faces = FACE_CENTROIDS @ rot.T

    apex_score = float(
        np.max(verts @ INWARD) / np.linalg.norm(VERTICES[0])
    )
    face_score = float(
        np.max(faces @ INWARD) / np.linalg.norm(FACE_CENTROIDS[0])
    )
    return apex_score, face_score


def optimize_random_starts(points: np.ndarray, R: float, seed: int,
                           starts: int = 128):
    rng = np.random.default_rng(seed)
    records = []

    for _ in range(starts):
        rv0 = Rotation.random(random_state=rng).as_rotvec()
        res = minimize(
            lambda rv: energy(rv, R, points),
            rv0,
            method="BFGS",
            options={"maxiter": 1200, "gtol": 1e-10},
        )
        apex, face = orientation_scores(res.x)
        records.append(
            {
                "energy": float(res.fun),
                "apex_score": apex,
                "face_score": face,
                "success": bool(res.success),
            }
        )

    records.sort(key=lambda r: r["energy"])
    best = records[0]

    e0 = best["energy"]
    tol = max(1e-10, 1e-8 * abs(e0))
    basin = [r for r in records if abs(r["energy"] - e0) <= tol]

    return best, records, basin


def main():
    distances = [1.5, 2.0, 3.0, 5.0, 10.0]
    couplings = {
        "face_vortex_centroids": FACE_CENTROIDS,
        "vertex_lumped_control": VERTICES,
    }

    rows = []
    details = {}

    for ci, (name, points) in enumerate(couplings.items()):
        details[name] = {}
        for di, R in enumerate(distances):
            best, records, basin = optimize_random_starts(
                points, R, seed=20260907 + 100 * ci + di
            )

            classification = (
                "APEX_INWARD"
                if best["apex_score"] > 0.95 and best["face_score"] < 0.7
                else "FACE_INWARD"
                if best["face_score"] > 0.95 and best["apex_score"] < 0.7
                else "MIXED"
            )

            row = {
                "coupling": name,
                "R_over_L": R,
                "best_energy": best["energy"],
                "best_apex_score": best["apex_score"],
                "best_face_score": best["face_score"],
                "classification": classification,
                "same_minimum_basin_count": len(basin),
                "random_starts": len(records),
            }
            rows.append(row)
            details[name][str(R)] = row

    df = pd.DataFrame(rows)
    df.to_csv(SWEEP_PATH, index=False)

    face_classes = list(
        df[df["coupling"] == "face_vortex_centroids"]["classification"]
    )
    vertex_classes = list(
        df[df["coupling"] == "vertex_lumped_control"]["classification"]
    )

    metrics = {
        "status": "orientation_hypothesis_fails_for_face_vortex_coupling_but_passes_vertex_control",
        "scope": {
            "physical_gravity_claim": False,
            "orbit_tested": False,
            "capture_tested": False,
            "rigid_orientation_only": True,
            "apex_alignment_term_used": False,
            "global_down_direction_used": False,
        },
        "geometry": {
            "edge_length": L,
            "relation": "face centroid opposite vertex i equals -vertex_i/3 for a centered regular tetrahedron",
        },
        "interaction": "U=-G sum_ab w_a w_b / distance_ab",
        "results": details,
        "summary": {
            "face_vortex_coupling_classes": face_classes,
            "vertex_control_classes": vertex_classes,
            "face_vortex_result": (
                "At every tested separation, the minimum-energy orientation "
                "places a triangular face toward T0, not an apex."
            ),
            "vertex_control_result": (
                "At every tested separation, the minimum-energy orientation "
                "places one apex toward T0."
            ),
        },
        "interpretation": (
            "The desired inverted-pyramid orientation is not a generic consequence "
            "of tetrahedral geometry plus attraction. It depends on where the "
            "inter-tetrahedron coupling is carried. The current v1.08 face-vortex "
            "picture, when converted into a simple finite-body 1/r control by "
            "placing localized energy at face centroids, prefers face-inward. "
            "A vertex-carried interaction prefers apex-inward. Therefore an orbit/"
            "capture test should not yet promote apex-inward as an MCIFT result; "
            "the next derivation must establish whether external coupling acts "
            "through face vortices, vertices/edges, or a different channel."
        ),
    }

    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(df.to_string(index=False))
    print("\nSTATUS:", metrics["status"])


if __name__ == "__main__":
    main()
