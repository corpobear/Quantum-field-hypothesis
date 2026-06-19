import math
import numpy as np

M0 = 2.0
alpha_M = 0.05
r_core = 1.0
rho_floor = 0.1
epsilon_3 = 0.125
psi_3 = 0.0
R4 = 2.0
beta_3 = 1.0

n_theta = 181
n_phi = 360
shells = range(1, 11)

theta = (np.arange(n_theta) + 0.5) * math.pi / n_theta
phi = (np.arange(n_phi) + 0.5) * 2.0 * math.pi / n_phi
T, P = np.meshgrid(theta, phi, indexing="ij")
weight = np.sin(T)
weight = weight / weight.sum()

A3 = 1.0 + epsilon_3 * (np.sin(T) ** 2) * np.cos(3.0 * P + psi_3)


def wmean(x):
    return float((x * weight).sum() / weight.sum())


def wstd(x):
    m = wmean(x)
    return float(math.sqrt(wmean((x - m) ** 2)))


def rho(r):
    value = 1.0 - alpha_M * M0 / (r * r + r_core * r_core)
    return max(rho_floor, min(1.0, value))

rows = []
for shell in shells:
    rh = rho(float(shell))
    radius_scale = rh * A3
    D3 = 1.0 - radius_scale
    rows.append({
        "shell": shell,
        "rho": rh,
        "mean_radius_scale": wmean(radius_scale),
        "mean_D3": wmean(D3),
        "shear_proxy": wstd(D3),
        "mean_abs_lc": wmean(np.abs(D3)),
        "mean_null": wmean(1.0 - radius_scale ** 2),
        "threefold_amp": float(radius_scale.max() - radius_scale.min()),
    })

mean_rho = sum(row["rho"] for row in rows) / len(rows)
mean_D3 = sum(row["mean_D3"] for row in rows) / len(rows)
mean_shear = sum(row["shear_proxy"] for row in rows) / len(rows)
mean_amp = sum(row["threefold_amp"] for row in rows) / len(rows)
mean_abs_lc = sum(row["mean_abs_lc"] for row in rows) / len(rows)
mean_null = sum(row["mean_null"] for row in rows) / len(rows)
H_proxy = sum(row["mean_radius_scale"] / row["shell"] for row in rows) / sum(1.0 / row["shell"] for row in rows)

Amax = float(A3.max())
loop_phase = sum(abs(1.0 - row["rho"] * Amax) for row in rows) / len(rows)
loop_sum = 3.0 * beta_3 * loop_phase
beta4_needed = loop_sum / R4

print("mean_A3", wmean(A3))
print("A3_std", wstd(A3))
print("mean_rho", mean_rho)
print("mean_D3", mean_D3)
print("mean_shear", mean_shear)
print("mean_amp", mean_amp)
print("mean_abs_lc", mean_abs_lc)
print("mean_null", mean_null)
print("H_proxy", H_proxy)
print("loop_sum", loop_sum)
print("beta4_needed", beta4_needed)
