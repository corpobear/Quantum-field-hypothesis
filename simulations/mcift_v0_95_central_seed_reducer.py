import math

M0 = 2.0
alpha_M = 0.05
r_core = 1.0
rho_floor = 0.1

shells = range(1, 11)

def rho(r):
    value = 1.0 - alpha_M * M0 / (r * r + r_core * r_core)
    return max(rho_floor, min(1.0, value))

rows = []
for r in shells:
    rh = rho(float(r))
    deformation = 1.0 - rh
    rows.append((r, rh, deformation, deformation, r * deformation, 1.0 - rh * rh))

mean_rho = sum(row[1] for row in rows) / len(rows)
mean_deformation = sum(row[2] for row in rows) / len(rows)
max_deformation = max(row[2] for row in rows)
anisotropy_proxy = max(row[1] for row in rows) / min(row[1] for row in rows) - 1.0
mean_null_residual = sum(row[5] for row in rows) / len(rows)
weighted_h = sum(row[1] / row[0] for row in rows) / sum(1.0 / row[0] for row in rows)

print("mean_rho", mean_rho)
print("mean_deformation", mean_deformation)
print("max_deformation", max_deformation)
print("anisotropy_proxy", anisotropy_proxy)
print("mean_null_residual", mean_null_residual)
print("h_proxy_rel", weighted_h)
