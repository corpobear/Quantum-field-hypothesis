# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.40 explicit 3D spherical leakage collision test

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now tests spherical leakage directly in a 3D cubic field:

```text
six-direction packet collision
-> central sink
-> mass gathered
-> E = m c^2 vibration
-> real 3D shell propagation
-> direct center/shell/anisotropy/leakage measurement
```

Verdict:

```text
v0.40 explicit 3D spherical leakage test = PASS-LIKE, 11/11 strict toy criteria
```

Important result:

```text
The 3D shell forms and the center stays stable, but the channel hierarchy shifts toward excessive compact mass retention: bb-like is high and WZ-like is low against rough Higgs hierarchy targets.
```

---

## v0.40 result

```text
max_center_drift_abs_cells = 0.000000
weighted_shell_peak_radius_cells = 3.500000
weighted_shell_halfmax_width_bins = 2.029847
weighted_sphericity = 0.782404
weighted_shape_anisotropy = 0.217596
weighted_core_fraction = 0.238897
weighted_inner_shell_fraction = 0.545301
weighted_outer_shell_fraction = 0.215802
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

## Key math

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

## Important limitation

```text
v0.40 is a toy 3D field calculation, not a detector-level CERN simulation. The rough Higgs target fractions are hierarchy targets, not measured detector likelihoods.
```

---

## Research roadmap

Next required tests:

```text
1. Inspect why explicit 3D geometry retains too much core/inner-shell energy.
2. Derive kappa coupling modifiers from explicit 3D shell geometry.
3. Compute partial widths, total width, branching fractions, and signal strengths.
4. Compare to collider Higgs targets without per-channel tuning.
5. Move from toy shape hierarchy to collider observable formulas.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
