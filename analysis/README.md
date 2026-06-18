# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current level

```text
Current collider comparison: v0.36 CERN/LHC Higgs-sector comparison
Current spatial solver: v0.35 minimal spatial cubic lattice solver
Current field formula: v0.33 cubic cell-complex field formula
Current mechanism layer: v0.32 cube-face Higgs vortex mass mechanism
Current geometry layer: v0.31 cube-center six-connector knot model
```

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The correct wording is "no parameter sweep / internally constrained heuristic closure", not strict no-fit proof.
```

---

## v0.36 CERN/LHC Higgs comparison

Run:

```bash
python analysis/mcift_cern_higgs_comparison_v0.36.py
```

Verdict:

```text
STRUCTURAL_ONLY_NOT_A_CERN_PASS
```

Scorecard:

```text
STRUCTURAL_PASS: scalar 0plus structural excitation; neutral/colorless structural representation
CALIBRATION_REQUIRED: Higgs mass scale
WEAK_QUALITATIVE: coupling hierarchy / mass-response idea
NOT_IMPLEMENTED: width, production rates, branching fractions, signal strengths, detector event distributions
CONSTRAINED: collider limit must reduce to SM-like Higgs behavior within current uncertainties
```

Outputs:

```text
analysis/results_v0.36/mcift_v0.36_cern_higgs_comparison_report.md
analysis/results_v0.36/mcift_v0.36_cern_higgs_comparison_metrics.csv
analysis/results_v0.36/mcift_v0.36_cern_higgs_summary.csv
```

---

## v0.35 spatial lattice solver

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

## Next analysis target

```text
v0.37 target:
Build a collider-Higgs effective model from MCIFT variables:
- derive coupling modifiers kappa_W, kappa_Z, kappa_t, kappa_b, kappa_tau, kappa_mu
- derive loop modifiers kappa_g and kappa_gamma
- compute partial widths and total width
- compute production times branching signal strengths
- compare to ATLAS/CMS likelihood-style targets
```
