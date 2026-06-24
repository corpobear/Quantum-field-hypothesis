import csv
import math
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "analysis" / "results_v1.00"


def weighted_mean(values, weights):
    return float((values * weights).sum() / weights.sum())


def weighted_std(values, weights):
    mean = weighted_mean(values, weights)
    return float(math.sqrt(weighted_mean((values - mean) ** 2, weights)))


def rho(shell, alpha_m=0.05, m0=2.0, r_core=1.0, rho_floor=0.1):
    value = 1.0 - alpha_m * m0 / (shell * shell + r_core * r_core)
    return max(rho_floor, min(1.0, value))


def compute_shared_state():
    m0 = 2.0
    r4 = 2.0
    alpha_m = 0.05
    r_core = 1.0
    rho_floor = 0.1
    epsilon_3 = 0.125
    psi_3 = 0.0
    beta_3 = 1.0
    n_theta = 181
    n_phi = 360
    shells = range(1, 11)

    theta = (np.arange(n_theta) + 0.5) * math.pi / n_theta
    phi = (np.arange(n_phi) + 0.5) * 2.0 * math.pi / n_phi
    theta_grid, phi_grid = np.meshgrid(theta, phi, indexing="ij")
    weight = np.sin(theta_grid)
    weight = weight / weight.sum()

    a3 = 1.0 + epsilon_3 * (np.sin(theta_grid) ** 2) * np.cos(
        3.0 * phi_grid + psi_3
    )

    shell_rows = []
    for shell in shells:
        rho_shell = rho(float(shell), alpha_m, m0, r_core, rho_floor)
        radius_scale = rho_shell * a3
        d3 = 1.0 - radius_scale
        shell_rows.append(
            {
                "shell": shell,
                "rho": rho_shell,
                "mean_radius_scale": weighted_mean(radius_scale, weight),
                "mean_D3": weighted_mean(d3, weight),
                "shear_proxy": weighted_std(d3, weight),
                "mean_abs_lc": weighted_mean(np.abs(d3), weight),
                "mean_null": weighted_mean(1.0 - radius_scale**2, weight),
                "threefold_amp": float(radius_scale.max() - radius_scale.min()),
            }
        )

    mean_rho = sum(row["rho"] for row in shell_rows) / len(shell_rows)
    mean_d3 = sum(row["mean_D3"] for row in shell_rows) / len(shell_rows)
    mean_shear = sum(row["shear_proxy"] for row in shell_rows) / len(shell_rows)
    mean_amp = sum(row["threefold_amp"] for row in shell_rows) / len(shell_rows)
    mean_abs_lc = sum(row["mean_abs_lc"] for row in shell_rows) / len(shell_rows)
    mean_null = sum(row["mean_null"] for row in shell_rows) / len(shell_rows)
    h_proxy = sum(row["mean_radius_scale"] / row["shell"] for row in shell_rows)
    h_proxy /= sum(1.0 / row["shell"] for row in shell_rows)

    a3_max = float(a3.max())
    loop_phase = sum(abs(1.0 - row["rho"] * a3_max) for row in shell_rows)
    loop_phase /= len(shell_rows)
    loop_sum = 3.0 * beta_3 * loop_phase
    beta4_needed = loop_sum / r4

    state = {
        "version": "v1.00",
        "source": "v0.97_shared_threefold_reducer",
        "M0": m0,
        "R4": r4,
        "alpha_M": alpha_m,
        "r_core": r_core,
        "rho_floor": rho_floor,
        "epsilon_3": epsilon_3,
        "psi_3": psi_3,
        "beta_3": beta_3,
        "mean_A3": weighted_mean(a3, weight),
        "A3_min": float(a3.min()),
        "A3_max": a3_max,
        "A3_std": weighted_std(a3, weight),
        "mean_rho": mean_rho,
        "load_proxy": mean_d3,
        "mean_D3": mean_d3,
        "mean_shear_proxy": mean_shear,
        "mean_threefold_amp": mean_amp,
        "mean_abs_lc_resid": mean_abs_lc,
        "mean_null_resid": mean_null,
        "H_proxy_relative": h_proxy,
        "loop_sum_beta3_1": loop_sum,
        "beta4_needed_for_balance": beta4_needed,
        "global_radius_min": min(row["rho"] for row in shell_rows) * float(a3.min()),
        "global_radius_max": max(row["rho"] for row in shell_rows) * a3_max,
    }
    state["global_anisotropy"] = (
        state["global_radius_max"] / state["global_radius_min"] - 1.0
    )
    return state, shell_rows


def write_outputs(state, shell_rows):
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    with (OUT_DIR / "shared_reducer_state.csv").open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["metric", "value", "label"])
        labels = {
            "epsilon_3": "assumed_from_symbol_strength",
            "psi_3": "assumed_phase_origin",
            "source": "provenance",
            "version": "provenance",
        }
        for key, value in state.items():
            label = labels.get(key, "derived")
            writer.writerow([key, value, label])

    with (OUT_DIR / "shared_reducer_shells.csv").open("w", newline="") as handle:
        fieldnames = [
            "shell",
            "rho",
            "mean_radius_scale",
            "mean_D3",
            "shear_proxy",
            "mean_abs_lc",
            "mean_null",
            "threefold_amp",
        ]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(shell_rows)


def main():
    state, shell_rows = compute_shared_state()
    write_outputs(state, shell_rows)
    for key in [
        "mean_A3",
        "load_proxy",
        "mean_shear_proxy",
        "mean_abs_lc_resid",
        "mean_null_resid",
        "H_proxy_relative",
        "beta4_needed_for_balance",
    ]:
        print(key, state[key])


if __name__ == "__main__":
    main()
