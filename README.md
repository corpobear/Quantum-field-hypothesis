# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.36 CERN/LHC Higgs-sector comparison

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT has paused cosmology-style testing and opened a collider-facing Higgs comparison.

v0.36 compares the cubic Higgs-vortex mass mechanism against core CERN/LHC Higgs-sector constraints.

Verdict:

```text
STRUCTURAL_ONLY_NOT_A_CERN_PASS
```

Meaning:

```text
MCIFT can structurally represent a scalar neutral Higgs-like mass-coupling excitation,
but it does not yet quantitatively predict the Higgs mass, width, production rates,
branching fractions, signal strengths, or detector-level event distributions.
```

---

## v0.36 Higgs comparison scorecard

```text
STRUCTURAL_PASS:
- scalar 0plus style central balanced excitation
- neutral/colorless structural representation

CALIBRATION_REQUIRED:
- Higgs mass scale

WEAK_QUALITATIVE:
- coupling hierarchy / mass-response idea

NOT_IMPLEMENTED:
- total width in MeV
- production rates: ggF, VBF, VH, ttH
- branching fractions: ZZ, WW, gamma gamma, tau tau, bb, mu mu
- signal-strength likelihood
- detector-level event distributions
```

---

## Key files

```text
analysis/mcift_cern_higgs_comparison_v0.36.py
analysis/results_v0.36/mcift_v0.36_cern_higgs_comparison_report.md
analysis/results_v0.36/mcift_v0.36_cern_higgs_comparison_metrics.csv
analysis/results_v0.36/mcift_v0.36_cern_higgs_summary.csv
paper/v0.36_cern_higgs_comparison_addendum.md
analysis/mcift_spatial_cubic_lattice_v0.35.py
models/first_principle_cubic_field_formula_v0.33.md
models/cube_face_higgs_vortex_mass_v0.32.md
models/cube_center_six_connector_knot_v0.31.md
```

---

## Latest spatial lattice result: v0.35

```text
v0.34 mode-level RMS = 0.302859
v0.35 spatial-lattice mapped RMS = 0.303948
shape verdict = PASS-LIKE
spatial pre-collapse peak = 617.87 Mpc, harmonic n=1
spatial post-collapse peak = 154.47 Mpc, harmonic n=4
mapped v0.35 global peak = 152.29 Mpc
mapped v0.35 BAO-window peak = 152.29 Mpc
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
1. Build a collider-Higgs effective model from MCIFT variables.
2. Derive coupling modifiers kappa_W, kappa_Z, kappa_t, kappa_b, kappa_tau, kappa_mu.
3. Derive loop modifiers kappa_g and kappa_gamma.
4. Compute partial widths and total width.
5. Compute production times branching signal strengths.
6. Compare to ATLAS/CMS likelihood-style targets.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
