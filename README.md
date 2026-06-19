# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.54 cosmology coarse-graining layer

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now lifts the local collision mechanics into a first cosmology-scale scaffold:

```text
v0.49 internal scaffold:
  dense entanglement, visible/hidden split, rotating-core load feedback

v0.50 kappa bridge:
  explicit kappa modifiers, partial widths, branching ratios, and rate modifiers

v0.51 common time bridge:
  core-clock to lab-clock conversion for total width/rate comparison

v0.52 channel-clock bridge:
  time-dilated rotation modifies channel formation clocks and branching ratios

v0.53 sound/acoustic bridge:
  internal pressure waves alter shell spread and channel partial widths

v0.54 cosmology layer:
  visible, hidden, rotation, radiation, and acoustic branches become coarse-grained density sectors
```

Current verdict:

```text
v0.54 cosmology coarse-grain = PASS_COSMOLOGY_COARSE_GRAIN_SCAFFOLD
```

This is a mathematical coarse-graining scaffold, not an observational cosmology fit.

---

## v0.54 result

```text
visible_gravity_fraction_normalized = 0.616356
hidden_gravity_fraction_normalized = 0.178592
rotation_gravity_fraction_normalized = 0.095371
radiation_fraction_normalized = 0.051573
acoustic_shell_fraction_normalized = 0.058107
c_sound_proxy = 0.582034
w_sound_proxy = 0.338764
lapse_N_at_a1 = 0.869985
H_lab_over_H_core_at_a1 = 1.149445
sound_horizon_proxy_at_a1 = 0.394142
inverse_sound_scale_proxy = 2.537156
```

Growth-kernel proxy:

```text
mu_eff(k=0.01) = 1.147401
mu_eff(k=0.1)  = 1.147026
mu_eff(k=1)    = 1.118137
mu_eff(k=10)   = 0.983284
```

---

## Key math

```text
rho_grav = rho_v + C_h rho_h + C_rot rho_rot + C_s rho_s + rho_r

H_core(a)^2 = sum_i Omega_i a^(-n_i)
N(a) = tau_rot / sqrt(1 + chi0 H_core(a)^2)
H_lab(a) = H_core(a) / N(a)

r_s(a) = integral_0^a c_s(a') / (a'^2 H_lab(a')) da'

dot(rho_i) + 3H(rho_i + p_i) = Q_i
sum_i Q_i = 0
```

The learned collision geometry becomes a cosmology language: hidden load becomes gravitational density, sound spread becomes acoustic pressure, time dilation becomes a lapse field, and rotation becomes vorticity/support.

---

## Analysis result files

```text
CURRENT_STATUS.md
models/cosmology_coarse_grain_v0.54.md
analysis/results_v0.54/mcift_v0.54_cosmology_coarse_grain_report.md
analysis/results_v0.54/mcift_v0.54_cosmology_coarse_grain_metrics.csv
analysis/results_v0.54/mcift_v0.54_components.csv
analysis/results_v0.54/mcift_v0.54_growth_kernel.csv
analysis/results_v0.54/mcift_v0.54_expansion_lapse_samples.csv
analysis/results_v0.54/mcift_v0.54_criteria.csv
```

---

## Important limitation

```text
v0.54 is a coarse-graining scaffold. It is not an observational cosmology fit and not a replacement for standard cosmology.
```

---

## Research roadmap

Next required tests:

```text
1. Implement the Q_i transfer network.
2. Test whether hidden/sound/rotation sectors evolve without hand-normalization.
3. Derive coarse-grained coefficients from the full 3D phase field.
4. Compare only later against H(z), growth, sound horizon, and lensing observables.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
