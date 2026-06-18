# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current level

```text
Current collider-style retest: v0.38 mass-energy vibration channel retest
Previous collider-style toy test: v0.37 line-chain spin-drill Higgs test
Current collider comparison: v0.36 CERN/LHC Higgs-sector comparison
Current spatial solver: v0.35 minimal spatial cubic lattice solver
Current field formula: v0.33 cubic cell-complex field formula
Current mechanism layer: v0.32 cube-face Higgs vortex mass mechanism
```

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The correct wording is "no parameter sweep / internally constrained heuristic closure", not strict no-fit proof.
```

---

## v0.38 mass-energy vibration retest

The test adds:

```text
mass gathered by spin-drill sink -> E = m c^2 -> vibration energy -> channel proxies
```

Key result:

```text
verdict = PASS-LIKE
criteria_pass_count = 9/9
peak_E_vib_GeV_proxy = 0.023315
final_E_vib_over_peak = 0.187542
```

Channel fractions:

```text
bb_like     = 0.559140
WZ_like     = 0.316161
gg_like     = 0.100017
tau_like    = 0.024090
gamma_like  = 0.000402
mumu_like   = 0.000189
```

Outputs:

```text
analysis/results_v0.38/mcift_v0.38_mass_energy_vibration_report.md
analysis/results_v0.38/mcift_v0.38_mass_energy_vibration_metrics.csv
analysis/results_v0.38/mcift_v0.38_mass_energy_vibration_channels.csv
```

---

## Next analysis target

```text
v0.39 target:
replace proxy channel families with coupling modifiers kappa_W, kappa_Z, kappa_b, kappa_tau, kappa_mu, kappa_g, and kappa_gamma, then compute partial widths and signal strengths.
```
