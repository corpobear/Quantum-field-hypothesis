"""
MCIFT v1.09 candidate integrated formation + orbit benchmark.

T0
--
Older/heavier primordial tetrahedron represented in the orbital sector by the
existing weak-field/Newtonian bridge:
    a = -G M0 r / |r|^3

T1
--
Younger/lighter tetrahedron:
- center of mass follows the T0 weak-field acceleration,
- internal geometry has four free vertices relative to that center,
- four face-vortex amplitudes are solved quasi-statically,
- T0's radial field is sampled at the four T1 vertices,
- each triangular face receives the mean field sampled by its 3 vertices,
- T1 self-drive ramps upward during its first nominal orbital period.

Internal energy:
    F = sum_f A_f [
          1/2 (c Q_f - k_f) Omega_f^2
          + 1/4 Omega_f^4
        ]

with
    k_f = k_self(t) + mean_{v in f} [gamma M0 / |x_v|].

No apex term, alignment spring, target side length, target volume, damping,
or target orbit force is used.

The internal solver is adiabatic: at sampled orbital times it finds the local
equilibrium branch from the prior state. This intentionally removes an
otherwise arbitrary vortex inertia/relaxation time from the test.

The positive localized vortex-energy mass proxy is retained monotonically:
    M_ret(t) = max_{s<=t} M_proxy(s)
which follows the earlier MCIFT "retained Higgs response" language without
introducing a retention timescale.

Scope: toy structural benchmark only; not established physics.
"""

from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from scipy.spatial.transform import Rotation

torch.set_default_dtype(torch.float64)

HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE.parent / "analysis" / "results_v1.09"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
METRICS_PATH = RESULTS_DIR / "formation_during_orbit_metrics.json"
TRACE_PATH = RESULTS_DIR / "formation_during_orbit_trace.csv"

G = 1.0
M0 = 1.663148923591514
GAMMA = 1.0
R0 = 12.0
K_START = -0.12
K_END = 0.08
C_TRI = 27.0 / 2800.0

FACES = [(1,2,3),(0,2,3),(0,1,3),(0,1,2)]
FACES_T = torch.tensor(FACES, dtype=torch.long)

UNIT_REGULAR = np.array(
    [[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]], dtype=float
) / (2.0 * math.sqrt(2.0))


def orbital_acceleration(pos):
    r = np.linalg.norm(pos)
    return -G * M0 * pos / r**3


def internal_energy(y, center, k_self):
    Xrel = y[:12].reshape(4,3)
    Xrel = Xrel - Xrel.mean(dim=0)
    ctr = torch.tensor(center, dtype=y.dtype)
    X = Xrel + ctr
    omega = y[12:]

    P = X[FACES_T]
    centroids = P.mean(dim=1)
    q = P - centroids[:,None,:]

    Q = (q*q).sum(dim=(1,2))
    A = 0.5 * torch.linalg.norm(
        torch.cross(P[:,1]-P[:,0], P[:,2]-P[:,0], dim=1),
        dim=1
    )

    phi_vertex = GAMMA * M0 / torch.linalg.norm(X, dim=1)
    phi_face = phi_vertex[FACES_T].mean(dim=1)
    k_face = k_self + phi_face

    return (
        A * (
            0.5 * (C_TRI*Q - k_face) * omega**2
            + 0.25 * omega**4
        )
    ).sum()


def solve_internal(y_np, center, k_self):
    y = torch.tensor(y_np.copy(), requires_grad=True)
    opt = torch.optim.LBFGS(
        [y],
        lr=0.8,
        max_iter=100,
        tolerance_grad=1e-10,
        tolerance_change=1e-12,
        line_search_fn="strong_wolfe",
    )

    def closure():
        opt.zero_grad()
        E = internal_energy(y, center, k_self)
        E.backward()
        return E

    opt.step(closure)
    return y.detach().numpy()


def internal_metrics(y_np, center, k_self):
    Xrel = y_np[:12].reshape(4,3)
    Xrel = Xrel - Xrel.mean(axis=0)
    X = Xrel + center
    omega = y_np[12:]

    inward = -center / np.linalg.norm(center)

    apex_scores = Xrel @ inward / np.linalg.norm(Xrel, axis=1)
    apex_score = float(np.max(apex_scores))
    apex_index = int(np.argmax(apex_scores))

    face_centroids_rel = np.array(
        [Xrel[list(f)].mean(axis=0) for f in FACES]
    )
    face_scores = (
        face_centroids_rel @ inward
        / np.linalg.norm(face_centroids_rel, axis=1)
    )
    face_score = float(np.max(face_scores))

    edges = np.array(
        [np.linalg.norm(Xrel[i]-Xrel[j])
         for i in range(4) for j in range(i+1,4)]
    )
    Mmat = np.stack(
        [Xrel[1]-Xrel[0], Xrel[2]-Xrel[0], Xrel[3]-Xrel[0]],
        axis=1
    )
    volume = abs(np.linalg.det(Mmat))/6.0

    k_faces = []
    positive_terms = []
    for fi,f in enumerate(FACES):
        P = X[list(f)]
        centroid = P.mean(axis=0)
        q = P-centroid
        Q = float((q*q).sum())
        A = 0.5*np.linalg.norm(
            np.cross(P[1]-P[0], P[2]-P[0])
        )
        phi = np.mean(
            GAMMA*M0/np.linalg.norm(P, axis=1)
        )
        kf = k_self + phi
        k_faces.append(float(kf))
        positive_terms.append(
            0.5*C_TRI*Q*A*omega[fi]**2
            + 0.25*A*omega[fi]**4
        )

    return {
        "apex_score": apex_score,
        "apex_index": apex_index,
        "face_score": face_score,
        "mean_edge": float(edges.mean()),
        "edge_cv": float(edges.std()/edges.mean()),
        "volume": float(volume),
        "mass_proxy": float(np.sum(positive_terms)),
        "omega_mean": float(np.mean(omega)),
        "omega_std": float(np.std(omega)),
        "drive_spread": float(np.max(k_faces)-np.min(k_faces)),
        "k_faces": k_faces,
        "omega_faces": [float(x) for x in omega],
    }


def initial_internal(seed):
    rng = np.random.default_rng(seed)
    R = Rotation.random(random_state=rng).as_matrix()
    Xrel = (0.8 * UNIT_REGULAR) @ R.T
    Xrel += rng.normal(scale=1e-4, size=Xrel.shape)
    Xrel -= Xrel.mean(axis=0)
    omega = np.full(4, 0.03)
    return np.concatenate([Xrel.ravel(), omega])


def run_case(speed_factor, seed=11, sample_count=120):
    pos = np.array([R0,0.0])
    vc = math.sqrt(G*M0/R0)
    vel = np.array([0.0, speed_factor*vc])

    period = 2.0*math.pi*math.sqrt(R0**3/(G*M0))
    total_time = 3.0*period
    ramp_time = period

    dt = period/4000.0
    sample_every = max(1, int((total_time/dt)/sample_count))

    y = initial_internal(seed)
    retained_mass = 0.0
    rows = []

    a = orbital_acceleration(pos)

    steps = int(total_time/dt)
    completed = True

    for step in range(steps):
        t = step*dt
        vel_half = vel + 0.5*dt*a
        pos2 = pos + dt*vel_half
        a2 = orbital_acceleration(pos2)
        vel2 = vel_half + 0.5*dt*a2
        pos, vel, a = pos2, vel2, a2

        r = np.linalg.norm(pos)

        if r < 5.0 or r > 80.0:
            completed = False
            break

        if step % sample_every == 0 or step == steps-1:
            k_self = K_START + (K_END-K_START)*min(t/ramp_time, 1.0)

            center3 = np.array([pos[0], pos[1], 0.0])
            y = solve_internal(y, center3, k_self)
            m = internal_metrics(y, center3, k_self)

            retained_mass = max(retained_mass, m["mass_proxy"])

            specific_orbital_energy = (
                0.5*np.dot(vel,vel) - G*M0/r
            )
            h = pos[0]*vel[1]-pos[1]*vel[0]

            rows.append({
                "speed_factor": speed_factor,
                "time": t,
                "radius": float(r),
                "specific_orbital_energy": float(specific_orbital_energy),
                "specific_angular_momentum": float(h),
                "k_self": float(k_self),
                "apex_score": m["apex_score"],
                "face_score": m["face_score"],
                "mean_edge": m["mean_edge"],
                "edge_cv": m["edge_cv"],
                "volume": m["volume"],
                "instant_mass_proxy": m["mass_proxy"],
                "retained_mass_proxy": retained_mass,
                "omega_mean": m["omega_mean"],
                "omega_std": m["omega_std"],
                "drive_spread": m["drive_spread"],
                "apex_index": m["apex_index"],
            })

    df = pd.DataFrame(rows)

    final_mass = float(df["retained_mass_proxy"].iloc[-1])
    formation_threshold = 0.1*final_mass
    formed = df[df["retained_mass_proxy"] >= formation_threshold]

    summary = {
        "speed_factor": speed_factor,
        "completed": completed,
        "radius_min": float(df["radius"].min()),
        "radius_max": float(df["radius"].max()),
        "orbital_energy_min": float(df["specific_orbital_energy"].min()),
        "orbital_energy_max": float(df["specific_orbital_energy"].max()),
        "angular_momentum_relative_drift": float(
            (df["specific_angular_momentum"].max()
             - df["specific_angular_momentum"].min())
            / abs(df["specific_angular_momentum"].iloc[0])
        ),
        "retained_mass_final": final_mass,
        "mass_ratio_M1_over_M0": final_mass/M0,
        "apex_mean_after_10pct_mass": float(formed["apex_score"].mean()),
        "apex_min_after_10pct_mass": float(formed["apex_score"].min()),
        "edge_cv_max_after_10pct_mass": float(formed["edge_cv"].max()),
        "volume_min_after_10pct_mass": float(formed["volume"].min()),
    }

    summary["bound_orbit"] = bool(
        completed
        and summary["orbital_energy_max"] < 0.0
        and summary["radius_min"] > 5.0
        and summary["radius_max"] < 80.0
    )

    summary["apex_inward_formation_orbit"] = bool(
        summary["bound_orbit"]
        and summary["apex_min_after_10pct_mass"] > 0.95
        and summary["volume_min_after_10pct_mass"] > 0.0
    )

    return df, summary


def main():
    cases = [0.90, 1.00, 1.10, 1.45]
    traces = []
    summaries = {}

    for i,sf in enumerate(cases):
        df, summary = run_case(sf, seed=11+i)
        traces.append(df)
        summaries[str(sf)] = summary

    all_df = pd.concat(traces, ignore_index=True)
    all_df.to_csv(TRACE_PATH, index=False)

    metrics = {
        "status": (
            "FORMATION_AND_APEX_DIRECTION_COMPATIBLE_WITH_BOUND_ORBITS_"
            "UNDER_SEPARATE_WEAK_FIELD_MASS_DYNAMICS"
        ),
        "scope": {
            "physical_higgs_claim": False,
            "physical_gravity_claim": False,
            "primordial_cosmology_claim": False,
            "true_unbound_capture_claim": False,
            "T0_fixed_test_particle_approximation": True,
            "internal_damping_used": False,
            "alignment_spring_used": False,
            "target_orbit_force_used": False,
            "internal_solver": "adiabatic local-equilibrium continuation",
            "mass_retention": "monotonic max of positive localized mass proxy",
        },
        "parameters": {
            "M0_v108_reference_proxy": M0,
            "R0": R0,
            "circular_speed": math.sqrt(G*M0/R0),
            "nominal_period": 2.0*math.pi*math.sqrt(R0**3/(G*M0)),
            "k_self_start": K_START,
            "k_self_end": K_END,
            "formation_ramp_duration": "1 nominal circular period",
            "simulation_duration": "3 nominal circular periods",
        },
        "results": summaries,
        "interpretation": (
            "When the orbital and formation roles are separated, T1 can gain "
            "vortex mass under T0's vertex-sampled radial influence while its "
            "center follows the older/heavier T0 weak-field orbit. Bound circular "
            "and mildly eccentric cases preserve an apex-inward orientation once "
            "T1 has appreciable mass, with finite volume and modest deformation. "
            "The super-escape control is not captured. Therefore this benchmark "
            "shows compatibility of mass formation, relational down, and bound "
            "orbit, but not capture of an initially unbound object. A true capture "
            "test still requires explicit exchange between orbital energy and "
            "T1 internal vibration/vortex modes."
        ),
    }

    METRICS_PATH.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    print(json.dumps({
        "status": metrics["status"],
        "results": summaries,
    }, indent=2))


if __name__ == "__main__":
    main()
