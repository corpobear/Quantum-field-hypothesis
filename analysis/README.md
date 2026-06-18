# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current level

```text
Current explicit 3D retest: v0.40 explicit 3D spherical leakage collision test
Previous geometric leakage retest: v0.39 spherical leakage geometry retest
Previous collider-style retest: v0.38 mass-energy vibration channel retest
Previous collider-style toy test: v0.37 line-chain spin-drill Higgs test
Current collider comparison: v0.36 CERN/LHC Higgs-sector comparison
Current spatial solver: v0.35 minimal spatial cubic lattice solver
```

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The correct wording is "no parameter sweep / internally constrained heuristic closure", not strict no-fit proof.
```

---

## v0.40 explicit 3D spherical leakage collision test

The test runs a six-direction cubic packet collision in a real 3D lattice:

```text
grid = 48 x 48 x 48
steps = 260
collision = six-direction cubic packet collision
directions = +x, -x, +y, -y, +z, -z
tracked fields = B, E_vib, phase, vortex Omega, mass proxy
```

Key result:

```text
verdict = PASS-LIKE
criteria_pass_count = 11/11
weighted_sphericity = 0.782404
weighted_shape_anisotropy = 0.217596
```

Shape-derived channel fractions:

```text
bb_like     = 0.783474
WZ_like     = 0.120174
gg_like     = 0.056984
tau_like    = 0.038445
gamma_like  = 0.000242
mumu_like   = 0.000681
```

Analysis result files:

```text
analysis/results_v0.40/mcift_v0.40_explicit_3d_spherical_leakage_report.md
analysis/results_v0.40/mcift_v0.40_explicit_3d_spherical_leakage_metrics.csv
analysis/results_v0.40/mcift_v0.40_explicit_3d_spherical_leakage_channels.csv
```

---

## Next analysis target

```text
v0.41 target:
derive kappa coupling modifiers from the explicit 3D shell geometry and compute partial widths, branching fractions, and signal strengths.
```

Before v0.41, inspect:

```text
Does the explicit 3D shell hold too much energy in the core/inner shell, suppressing coherent WZ-like leakage?
```
