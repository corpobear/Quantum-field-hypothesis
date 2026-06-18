# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.39 spherical leakage geometry retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now evaluates leakage from geometry:

```text
track sink center in time
reconstruct spherical vibration shell
measure shell radius, width, sphericity, and anisotropy
derive leakage fractions from shape classes
```

Verdict:

```text
v0.39 spherical leakage geometry retest = PASS-LIKE, 10/10 strict toy criteria
```

---

## v0.39 result

```text
max_center_drift_abs_cells = 0.434496
weighted_shell_peak_radius_cells = 3.655708
weighted_shell_halfmax_width_bins = 8.465637
weighted_sphericity = 0.959336
weighted_shape_anisotropy = 0.040664
weighted_core_fraction = 0.106027
weighted_inner_shell_fraction = 0.282291
weighted_outer_shell_fraction = 0.611682
```

Shape-derived channel fractions:

```text
bb_like     = 0.505134  target ~ 0.582000
WZ_like     = 0.381469  target ~ 0.240000
gg_like     = 0.085943  target ~ 0.086000
tau_like    = 0.026958  target ~ 0.063000
gamma_like  = 0.000095  target ~ 0.002300
mumu_like   = 0.000402  target ~ 0.000220
```

---

## Key math

```text
x_c(t) = sum_x x B(x,t)^2 / sum_x B(x,t)^2
r = |x - x_c(t)|
R_shell(t) = argmax radial E_vib(r,t), for r greater than core radius
sphericity(t) = 1 - anisotropy(t)
anisotropy(t) = dipole_asymmetry + spin/twist distortion proxy
```

---

## Key files

```text
analysis/results_v0.39/mcift_v0.39_spherical_leakage_report.md
analysis/results_v0.39/mcift_v0.39_spherical_leakage_metrics.csv
analysis/results_v0.39/mcift_v0.39_spherical_leakage_channels.csv
paper/v0.39_spherical_leakage_geometry_addendum.md
analysis/results_v0.38/mcift_v0.38_mass_energy_vibration_report.md
analysis/results_v0.37/mcift_v0.37_line_chain_spin_drill_report.md
models/first_principle_cubic_field_formula_v0.33.md
models/cube_face_higgs_vortex_mass_v0.32.md
```

---

## Important limitation

```text
v0.39 is a rotational spherical reconstruction from the 1D line-chain toy model. It is stricter than v0.38 because leakage is evaluated from shape, but it is still not a full 3D event simulation or a Standard Model branching-fraction calculation.
```

---

## Research roadmap

Next required tests:

```text
1. Run the same center/shell/leakage test in an explicit 2D or 3D lattice.
2. Measure shell anisotropy and leakage directly instead of reconstructing from the line-chain.
3. Derive leakage fractions from measured shell geometry.
4. Compare hierarchy without per-channel tuning.
5. Then replace proxy channel families with coupling modifiers and partial widths.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
