# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current level

```text
Current collider-style toy test: v0.37 line-chain spin-drill Higgs test
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

## v0.37 line-chain spin-drill test

The test connects cube centers in a straight line and drives opposite phase/information flows toward the center.

```text
line length N = 401
steps = 900
collision center = 200
two counter-propagating information packets
tracked variables = spin, twist, vortex, mass proxy, dent, stability, reservoir B
```

Key result:

```text
verdict = PASS-LIKE
criteria_pass_count = 7/7
peak_B = 10.403389
peak_B_distance_from_center = 4 cells
B_localization_ratio_at_peak = 0.366080
peak_window_mass_GeV_proxy = 0.603444
sink_halfmax_lifetime_time = 2.800000
center_B_final_over_peak = 0.338235
```

Outputs:

```text
analysis/results_v0.37/mcift_v0.37_line_chain_spin_drill_report.md
analysis/results_v0.37/mcift_v0.37_line_chain_spin_drill_metrics.csv
```

---

## v0.36 CERN/LHC Higgs comparison

Verdict:

```text
STRUCTURAL_ONLY_NOT_A_CERN_PASS
```

---

## Next analysis target

```text
v0.38 target:
convert sink decay/leakage into channel fractions, then compare the line-chain excitation to Higgs width and branching-ratio patterns.
```
