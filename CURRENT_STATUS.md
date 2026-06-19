# Current MCIFT Status: v0.50 Kappa Bridge

**Status:** speculative theoretical framework / toy collider scaffold; not established physics.  
**Current bridge test:** v0.50 kappa / width bridge.  
**Previous feedback test:** v0.49 core load feedback test.

---

## One-sentence status

```text
MCIFT v0.50 adds an explicit kappa-framework bridge. It computes partial widths, branching ratios, and representative rate modifiers from kappa values. The current benchmark is calibrated to the SM-like reference point, so it is a compatibility bridge rather than a first-principle derivation.
```

---

## v0.50 result

```text
verdict = PASS_KAPPA_BRIDGE_CALIBRATED
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

Geometry-prior warning:

```text
geometry_prior_kappa_g = 1.1321962508
geometry_prior_kappa_gamma = 0.7373106620
geometry_prior_kappa_mu = 2.9745865530
```

---

## Analysis result files

```text
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

## Safe wording

```text
v0.50 is a calibrated bridge layer. It reproduces the SM-like reference table, but it does not yet derive kappa values from MCIFT first principles.
```
