# Current MCIFT Status: v0.40 Explicit 3D Spherical Leakage Collision Test

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current explicit 3D retest:** v0.40 explicit 3D spherical leakage collision test.  
**Previous geometric leakage retest:** v0.39 spherical leakage geometry retest.  
**Previous collider-style retest:** v0.38 mass-energy vibration channel retest.  
**Previous collider-style toy test:** v0.37 line-chain spin-drill Higgs test.  
**Current collider comparison layer:** v0.36 CERN/LHC Higgs-sector comparison.

---

## One-sentence status

```text
MCIFT v0.40 runs the spherical leakage test in an explicit 48^3 cubic lattice with a six-direction packet collision. The strict 3D toy verdict is PASS-LIKE: 11/11 geometry criteria passed. A central sink and real 3D vibration shell form directly, with stable center tracking, finite energy, mostly spherical shell geometry, subdominant anisotropy, and shape-derived leakage. However, the explicit 3D hierarchy shifts toward excessive compact mass retention: bb-like is high and WZ-like is low against rough Higgs hierarchy targets.
```

---

## v0.40 result

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

Shape-derived channel fractions:

```text
bb_like     = 0.783474  target ~ 0.582000
WZ_like     = 0.120174  target ~ 0.240000
gg_like     = 0.056984  target ~ 0.086000
tau_like    = 0.038445  target ~ 0.063000
gamma_like  = 0.000242  target ~ 0.002300
mumu_like   = 0.000681  target ~ 0.000220
```

---

## Math under test

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

---

## Analysis result files

```text
analysis/results_v0.40/mcift_v0.40_explicit_3d_spherical_leakage_report.md
analysis/results_v0.40/mcift_v0.40_explicit_3d_spherical_leakage_metrics.csv
analysis/results_v0.40/mcift_v0.40_explicit_3d_spherical_leakage_channels.csv
```

---

## Limitation

```text
v0.40 is a toy 3D field calculation, not a detector-level CERN simulation. The rough Higgs target fractions are hierarchy targets, not measured detector likelihoods.
```

---

## Next proof target

```text
v0.41 target:
derive kappa coupling modifiers from the explicit 3D shell geometry and compute partial widths, branching fractions, and signal strengths.
```

Before v0.41, inspect the geometric issue:

```text
Does the explicit 3D shell hold too much energy in the core/inner shell, suppressing coherent WZ-like leakage?
```

---

## Safe wording

```text
v0.40 shows that an explicit 3D cubic collision can form a stable central sink and real shell with PASS-LIKE geometry criteria, but the channel hierarchy is not yet a collider match and the model remains a toy scaffold.
```
