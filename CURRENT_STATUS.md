# Current MCIFT Status: v0.39 Spherical Leakage Geometry Retest

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current geometric leakage retest:** v0.39 spherical leakage geometry retest.  
**Previous collider-style retest:** v0.38 mass-energy vibration channel retest.  
**Previous collider-style toy test:** v0.37 line-chain spin-drill Higgs test.  
**Current collider comparison layer:** v0.36 CERN/LHC Higgs-sector comparison.  
**Current spatial tested layer:** v0.35 minimal spatial cubic lattice solver.

---

## One-sentence status

```text
MCIFT v0.39 tracks the sink center in time, reconstructs a spherical shell from the mass-energy vibration field, measures shell shape, and evaluates leakage from geometry rather than direct proxy labels. The strict toy verdict is PASS-LIKE: 10/10 criteria passed, with stable center tracking, dominant near-center shell formation, high sphericity, subdominant anisotropy, and shape-derived leakage led by compact mass retention, coherent spherical-shell leakage, and visible turbulent leakage.
```

---

## v0.39 result

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

## Math under test

```text
x_c(t) = sum_x x B(x,t)^2 / sum_x B(x,t)^2
r = |x - x_c(t)|
R_shell(t) = argmax radial E_vib(r,t), for r greater than core radius
sphericity(t) = 1 - anisotropy(t)
anisotropy(t) = dipole_asymmetry + spin/twist distortion proxy
```

Shape-derived leakage families:

```text
core and compact inner-shell retention -> bb-like, tau-like, mumu-like
coherent spherical shell               -> WZ-like
anisotropic/turbulent shell             -> gg-like, gamma-like
```

---

## Limitation

```text
v0.39 is a rotational spherical reconstruction from the 1D line-chain toy model. It is stricter than v0.38 because leakage is evaluated from shape, but it is still not a full 3D event simulation or a Standard Model branching-fraction calculation.
```

---

## Next proof target

```text
v0.40 target:
run the same center/shell/leakage test in an explicit 2D or 3D lattice so that shell anisotropy and leakage are measured directly rather than reconstructed from the line-chain.
```

Required direction:

```text
- initialize an explicit 2D/3D cubic field around the collision center
- evolve mass-energy vibration outward from the sink
- measure center drift, shell radius, shell thickness, sphericity, and anisotropy directly
- derive leakage fractions from measured shell geometry
- compare hierarchy without per-channel tuning
```

---

## Safe wording

```text
v0.39 shows that a rotational spherical reconstruction of the line-chain vibration gives a PASS-LIKE shape-derived leakage hierarchy, but it is not yet a full 3D collider event model.
```
