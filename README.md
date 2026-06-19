# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.50 kappa / width bridge

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has two separate layers:

```text
1. v0.49 internal scaffold:
   dense entanglement, visible/hidden split, rotating-core load feedback

2. v0.50 collider bridge:
   explicit kappa modifiers, partial widths, branching ratios, and rate modifiers
```

Current bridge verdict:

```text
v0.50 kappa bridge = PASS_KAPPA_BRIDGE_CALIBRATED
```

This is a calibrated bridge, not a first-principle prediction of collider couplings.

---

## v0.50 result

```text
Gamma_SM_total_MeV = 4.070000
Gamma_fit_total_MeV = 4.070000
kappa_H_squared = 1.000000
BR_BSM_fit = 0.000000
max_abs_BR_delta_pct = 0.000000
max_abs_signal_strength_delta_pct = 0.000000
```

Kappa benchmark:

```text
kappa_b = 1
kappa_W = 1
kappa_Z = 1
kappa_g = 1
kappa_tau = 1
kappa_c = 1
kappa_gamma = 1
kappa_mu = 1
kappa_top = 1
```

---

## Key math

```text
Gamma_i = kappa_i^2 Gamma_i^SM
BR_i = Gamma_i / Gamma_total
mu(prod,decay) = kappa_prod^2 kappa_decay^2 / kappa_H^2
kappa_H^2 = Gamma_total / Gamma_total^SM
```

---

## Important boundary

The raw v0.49 geometry priors do not yet form a valid collider kappa prediction in all channels:

```text
geometry_prior_kappa_g = 1.1321962508
geometry_prior_kappa_gamma = 0.7373106620
geometry_prior_kappa_mu = 2.9745865530
```

So v0.50 deliberately separates:

```text
geometry prior = internal MCIFT shape/channel tendency
kappa fit = collider-compatible bridge
```

---

## Analysis result files

```text
CURRENT_STATUS.md
models/kappa_width_bridge_v0.50.md
paper/v0.50_kappa_width_bridge_addendum.md
analysis/results_v0.50/mcift_v0.50_kappa_bridge_report.md
analysis/results_v0.50/mcift_v0.50_kappa_bridge_metrics.csv
analysis/results_v0.50/mcift_v0.50_kappa_fit_values.csv
analysis/results_v0.50/mcift_v0.50_partial_widths_branching_ratios.csv
analysis/results_v0.50/mcift_v0.50_signal_strength_summary.csv
analysis/results_v0.50/mcift_v0.50_geometry_prior_vs_kappa_fit.csv
```

---

## Important limitation

```text
v0.50 is a calibrated bridge layer. It reproduces the SM-like kappa reference table, but it does not yet derive kappa values from MCIFT first principles.
```

---

## Research roadmap

Next required tests:

```text
1. Derive kappa values from the full 3D vector phase field.
2. Keep visible and hidden branches separate before channel projection.
3. Derive loop-sensitive channels without direct channel tuning.
4. Compute coupling modifiers and partial widths only after deriving kappa from geometry.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
