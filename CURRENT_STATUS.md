# Current MCIFT Status: v0.41 Spinning-Sphere Collision Retest

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current collision retest:** v0.41 spinning-sphere collision retest.  
**Previous explicit 3D retest:** v0.40 explicit 3D spherical leakage collision test.  
**Previous geometric leakage retest:** v0.39 spherical leakage geometry retest.  
**Previous collider-style retest:** v0.38 mass-energy vibration channel retest.  
**Current collider comparison layer:** v0.36 CERN/LHC Higgs-sector comparison.

---

## One-sentence status

```text
MCIFT v0.41 replaces abstract packet overlap with two finite rotating spheres. Collision is calculated at the contact point like a pool-ball collision, including radius, center position, velocity, spin, contact normal, normal impulse, tangential impulse, and spin transfer. The rigid-body collision conserves momentum and angular momentum to numerical precision and forms a stable 3D shell, but the channel hierarchy is weak: compact mass retention becomes too low while coherent/turbulent shell leakage becomes too high.
```

---

## v0.41 collision result

```text
verdict = GEOMETRY_PASS_CHANNEL_WEAK
criteria_pass_count = 11/13
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

## Math under test

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

## Limitation

```text
v0.41 is a toy rigid-sphere plus 3D shell calculation, not a detector-level CERN simulation. The rough Higgs fractions are hierarchy targets, not measured likelihoods.
```

---

## Next proof target

```text
v0.42 target:
scan only physical collision geometry variables -- impact parameter, spin orientation, restitution, and friction -- to find whether a stable no-per-channel-tuning region naturally balances compact mass retention and coherent shell leakage.
```

---

## Safe wording

```text
v0.41 successfully implements pool-style collision geometry and spin transfer, but the decay hierarchy is not yet collider-like. The model now needs a physical-geometry scan, not per-channel tuning.
```
