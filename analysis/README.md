# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current level

```text
Current geometric leakage retest: v0.39 spherical leakage geometry retest
Previous collider-style retest: v0.38 mass-energy vibration channel retest
Previous collider-style toy test: v0.37 line-chain spin-drill Higgs test
Current collider comparison: v0.36 CERN/LHC Higgs-sector comparison
Current spatial solver: v0.35 minimal spatial cubic lattice solver
Current field formula: v0.33 cubic cell-complex field formula
```

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The correct wording is "no parameter sweep / internally constrained heuristic closure", not strict no-fit proof.
```

---

## v0.39 spherical leakage geometry retest

The test reconstructs a spherical shell from the line-chain vibration profile and evaluates leakage from shape:

```text
x_c(t) = sum_x x B(x,t)^2 / sum_x B(x,t)^2
r = |x - x_c(t)|
R_shell(t) = argmax radial E_vib(r,t), for r greater than core radius
sphericity(t) = 1 - anisotropy(t)
```

Key result:

```text
verdict = PASS-LIKE
criteria_pass_count = 10/10
weighted_sphericity = 0.959336
weighted_shape_anisotropy = 0.040664
```

Shape-derived channel fractions:

```text
bb_like     = 0.505134
WZ_like     = 0.381469
gg_like     = 0.085943
tau_like    = 0.026958
gamma_like  = 0.000095
mumu_like   = 0.000402
```

Outputs:

```text
analysis/results_v0.39/mcift_v0.39_spherical_leakage_report.md
analysis/results_v0.39/mcift_v0.39_spherical_leakage_metrics.csv
analysis/results_v0.39/mcift_v0.39_spherical_leakage_channels.csv
```

---

## Next analysis target

```text
v0.40 target:
run the same center/shell/leakage test in an explicit 2D or 3D lattice so that shell anisotropy and leakage are measured directly rather than reconstructed from the line-chain.
```
