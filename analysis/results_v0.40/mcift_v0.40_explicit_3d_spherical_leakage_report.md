# MCIFT v0.40 Explicit 3D Spherical Leakage Collision Test Report

**Status:** explicit 3D cubic-field retest after v0.39; speculative scaffold, not established physics.

## Purpose

v0.40 runs the spherical leakage test in a real 3D cubic lattice rather than reconstructing a sphere from the 1D line-chain.

```text
six-direction packet collision -> central sink
mass gathered -> E = m c^2 vibration
vibration propagates as a 3D shell
center, shell, sphericity, anisotropy, and leakage are measured directly
```

## Setup

```text
grid = 48 x 48 x 48
steps = 260
collision = six-direction cubic packet collision
directions = +x, -x, +y, -y, +z, -z
tracked fields = B, E_vib, phase, vortex Omega, mass proxy
```

## Core formulas

```text
phi_mu(x,t) = A exp[-|x - x_mu(t)|^2 / 2 sigma^2] cos(k dot x - omega t)
chi_axis = sqrt(packet_plus packet_minus) P_phase P_timing
Omega = sigmoid(chi - chi_c) chi
m(x,t) = m_scale Omega
E_m(x,t) = eta_m m(x,t) c^2
E_vib evolves by damped 3D wave propagation
x_c(t) = sum_x x B(x,t)^2 / sum_x B(x,t)^2
R_shell(t) = argmax radial E_vib(r,t)
sphericity = 1 - anisotropy
```

## Result

```text
verdict = PASS-LIKE
criteria_pass_count = 11/11
max_center_drift_abs_cells = 0.000000
weighted_shell_peak_radius_cells = 3.500000
weighted_shell_halfmax_width_bins = 2.029847
weighted_sphericity = 0.782404
weighted_shape_anisotropy = 0.217596
weighted_core_fraction = 0.238897
weighted_inner_shell_fraction = 0.545301
weighted_outer_shell_fraction = 0.215802
channel_l1_distance_to_rough_higgs_targets = 0.377390
channel_log10_rms_to_rough_higgs_targets = 0.479895
```

## Shape-derived channel fractions

```text
bb_like     = 0.783474  target ~ 0.582000
WZ_like     = 0.120174  target ~ 0.240000
gg_like     = 0.056984  target ~ 0.086000
tau_like    = 0.038445  target ~ 0.063000
gamma_like  = 0.000242  target ~ 0.002300
mumu_like   = 0.000681  target ~ 0.000220
```

## Criteria

```text
center_track_stable_drift_lt_1p5_cells = True
dominant_shell_forms_radius_gt_3 = True
dominant_shell_not_far_radius_lt_12 = True
spherical_component_dominant = True
anisotropy_present_but_subdominant = True
shape_derived_leakage_positive = True
bb_like_largest_from_shape = True
WZ_like_second_or_third_from_shape = True
gg_like_visible_from_turbulence = True
gamma_and_mumu_suppressed = True
energy_finite_no_blowup = True
```

## Interpretation

```text
The explicit 3D cubic retest forms a central sink and a real 3D vibration shell. The center remains stable, shell formation is direct rather than reconstructed, the shell is mostly spherical with a small anisotropic/turbulent component, and shape-derived leakage remains led by compact mass retention, coherent spherical leakage, and visible turbulent leakage.
```

## Limitation

```text
This is still a toy 3D field calculation, not a detector-level CERN simulation. The rough Higgs target fractions are hierarchy targets, not measured detector likelihoods.
```

## Next target

```text
v0.41 target:
derive kappa coupling modifiers from the explicit 3D shell geometry and compute partial widths / branching fractions / signal strengths.
```
