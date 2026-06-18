# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.41 spinning-sphere collision retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now calculates collision geometry like a pool-ball collision:

```text
finite sphere A + finite sphere B
center, radius, velocity, spin, contact normal
normal impulse + tangential impulse
spin transfer at contact
E_dissipated + E_spin -> vibration seed
3D shell leakage from the collision
```

Verdict:

```text
v0.41 spinning-sphere collision retest = GEOMETRY_PASS_CHANNEL_WEAK, 11/13 criteria
```

---

## v0.41 result

```text
normal_impulse = 1.693458
tangent_impulse_mag = 0.156047
slip_ratio = 0.356799
spin_transfer = 0.130039
E_before = 2.319040
E_after = 1.766962
E_dissipated = 0.552078
E_vib_seed = 0.572343
momentum_error = 0.000000e+00
angular_momentum_error = 2.696865e-15
```

Shell result:

```text
max_center_drift_abs_cells = 0.000000
weighted_shell_peak_radius_cells = 8.922861
weighted_shell_halfmax_width_bins = 4.361015
weighted_sphericity = 0.845727
weighted_shape_anisotropy = 0.154273
weighted_core_fraction = 0.066127
weighted_inner_shell_fraction = 0.425236
weighted_outer_shell_fraction = 0.508637
```

Shape-derived channel fractions:

```text
bb_like     = 0.188928  target ~ 0.582000
WZ_like     = 0.518154  target ~ 0.240000
gg_like     = 0.249245  target ~ 0.086000
tau_like    = 0.019942  target ~ 0.063000
gamma_like  = 0.022681  target ~ 0.002300
mumu_like   = 0.001050  target ~ 0.000220
```

---

## Key math

```text
|x_A - x_B| <= R_A + R_B
n = (x_B - x_A) / |x_B - x_A|
u_A = v_A + omega_A x r_A
u_B = v_B + omega_B x r_B
u_rel = u_B - u_A
J_n = -(1+e)(u_rel . n) / D_n
J_t = clipped friction impulse from tangential contact velocity
J = J_n n + J_t
v_A' = v_A - J/m_A
v_B' = v_B + J/m_B
omega_A' = omega_A - I_A^-1 (r_A x J)
omega_B' = omega_B + I_B^-1 (r_B x J)
E_vib_seed = eta_c E_dissipated + eta_s E_spin
```

---

## Analysis result files

```text
analysis/results_v0.41/mcift_v0.41_spinning_sphere_collision_report.md
analysis/results_v0.41/mcift_v0.41_spinning_sphere_collision_metrics.csv
analysis/results_v0.41/mcift_v0.41_spinning_sphere_collision_channels_summary.csv
```

---

## Important limitation

```text
v0.41 is a toy rigid-sphere plus 3D shell calculation, not a detector-level CERN simulation. The rough Higgs fractions are hierarchy targets, not measured likelihoods.
```

---

## Research roadmap

Next required tests:

```text
1. Scan only physical collision geometry variables: impact parameter, spin orientation, restitution, friction.
2. Check whether a stable no-per-channel-tuning region balances compact mass retention and coherent shell leakage.
3. Then derive kappa coupling modifiers from the physical collision geometry.
4. Compute partial widths, total width, branching fractions, and signal strengths.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
