# MCIFT v0.39 Spherical Leakage Geometry Retest Report

**Status:** shape-derived leakage retest after v0.38; speculative scaffold, not established physics.

## Purpose

v0.39 tests the proposed geometric upgrade:

```text
track the sink center in time
let mass-energy vibration build a spherical shell
measure shell shape
evaluate leakage from the shape rather than direct proxy labels
```

Because the source data is the v0.37/v0.38 one-dimensional line-chain, the sphere is a rotational shell reconstruction from the line-chain vibration profile. This is not yet a full 3D detector simulation.

## Math under test

Center track:

```text
x_c(t) = sum_x x B(x,t)^2 / sum_x B(x,t)^2
```

Radial distance from the moving center:

```text
r = |x - x_c(t)|
```

Dominant shell radius:

```text
R_shell(t) = argmax radial E_vib(r,t), for r greater than core radius
```

Shape scores:

```text
sphericity(t)  = 1 - anisotropy(t)
anisotropy(t) = dipole_asymmetry + spin/twist distortion proxy
```

Shape-derived leakage families:

```text
core and compact inner-shell retention -> bb-like, tau-like, mumu-like
coherent spherical shell               -> WZ-like
anisotropic/turbulent shell             -> gg-like, gamma-like
```

## Result

```text
verdict = PASS-LIKE
criteria_pass_count = 10/10
max_center_drift_abs_cells = 0.434496
weighted_shell_peak_radius_cells = 3.655708
weighted_shell_halfmax_width_bins = 8.465637
weighted_sphericity = 0.959336
weighted_shape_anisotropy = 0.040664
weighted_core_fraction = 0.106027
weighted_inner_shell_fraction = 0.282291
weighted_outer_shell_fraction = 0.611682
channel_l1_distance_to_rough_higgs_targets = 0.256823
channel_log10_rms_to_rough_higgs_targets = 0.601039
```

## Shape-derived channel fractions

```text
bb_like     = 0.505134  target ~ 0.582000
WZ_like     = 0.381469  target ~ 0.240000
gg_like     = 0.085943  target ~ 0.086000
tau_like    = 0.026958  target ~ 0.063000
gamma_like  = 0.000095  target ~ 0.002300
mumu_like   = 0.000402  target ~ 0.000220
```

## Criteria

```text
center_track_stable_drift_lt_1_cell = True
dominant_shell_forms_radius_gt_3 = True
dominant_shell_not_far_radius_lt_8 = True
spherical_component_dominant = True
anisotropy_present_but_subdominant = True
shape_derived_leakage_positive = True
bb_like_largest_from_shape = True
WZ_like_second_from_shape = True
gg_like_visible_from_turbulence = True
gamma_and_mumu_suppressed = True
```

## Interpretation

```text
The center track remains stable, the dominant shell forms near the center, and the reconstructed shell is mostly spherical with a small but nonzero anisotropic/turbulent component. When leakage is evaluated from shape, the largest branch is compact mass-retention, the second branch is coherent spherical-shell leakage, and turbulence remains visible but subdominant. Gamma-like and mumu-like branches stay suppressed.
```

## Limitation

```text
This is a rotational spherical reconstruction from a 1D line-chain toy model. It is a stricter geometric leakage test than v0.38, but it is still not a full 3D event simulation and not a Standard Model branching-fraction calculation.
```

## Next target

```text
v0.40 target:
run the same center/shell/leakage test in an explicit 2D or 3D lattice so that shell anisotropy and leakage are measured directly rather than reconstructed from the line-chain.
```
