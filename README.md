# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.37 line-chain spin-drill Higgs test

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now tests a collider-style line-chain mechanism:

```text
connect cube centers in a line
send opposite information/phase flows toward the center
measure spin/twist over time
watch whether a localized dent/drill/sink forms
measure mass proxy and decay/leakage
```

Verdict:

```text
v0.37 line-chain spin-drill Higgs test = PASS-LIKE, 7/7 strict toy criteria
```

---

## v0.37 result

```text
verdict = PASS-LIKE
criteria_pass_count = 7/7
peak_B = 10.403389
peak_B_step = 426
peak_B_distance_from_center = 4 cells
B_localization_ratio_at_peak = 0.366080
peak_Dent = 2.995342
peak_window_mass_GeV_proxy = 0.603444
peak_window_mass_distance_from_center = 7 cells
sink_halfmax_lifetime_steps = 140
sink_halfmax_lifetime_time = 2.800000
center_B_final_over_peak = 0.338235
```

---

## Key line-chain math

```text
delta_phi_i = phi_(i+1) - phi_i
omega_i = d(delta_phi_i)/dt
Theta_i = phi_(i+1) - 2 phi_i + phi_(i-1)
A_i = sqrt(a_i a_(i+1))
chi_i = A_i P_phase P_timing P_match
Omega_i = H_i sigma(chi_i - chi_c)
m_i = m_scale Omega_i A_i
D_i = alpha_spin |omega_i| + alpha_twist |Theta_i| + alpha_Omega Omega_i
S_i = Coh_i - q_i - D_i
dB_i/dt = gamma_B max(0,-S_i) - decay_B B_i
```

---

## Key files

```text
analysis/results_v0.37/mcift_v0.37_line_chain_spin_drill_report.md
analysis/results_v0.37/mcift_v0.37_line_chain_spin_drill_metrics.csv
paper/v0.37_line_chain_spin_drill_addendum.md
analysis/mcift_cern_higgs_comparison_v0.36.py
analysis/results_v0.36/mcift_v0.36_cern_higgs_comparison_report.md
analysis/mcift_spatial_cubic_lattice_v0.35.py
models/first_principle_cubic_field_formula_v0.33.md
models/cube_face_higgs_vortex_mass_v0.32.md
models/cube_center_six_connector_knot_v0.31.md
```

---

## Important limitation

```text
v0.37 is a 1D collider-style toy stress test. It is not yet a detector-level CERN simulation and does not compute Standard Model branching fractions or cross sections.
```

---

## Wording correction

Earlier docs used **"no-fit"** too strongly. The current wording is:

```text
no parameter sweep / internally constrained heuristic closure
```

This means parameters were not swept to match the target, but the closure choices remain model assumptions.

---

## Research roadmap

Next required tests:

```text
1. Convert sink decay/leakage into channel fractions.
2. Map channel fractions to Higgs-like decay patterns.
3. Compare against Higgs width and branching-ratio patterns.
4. Keep the no per-channel tuning rule.
5. Then move toward coupling modifiers and signal strengths.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
