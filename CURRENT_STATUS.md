# Current MCIFT Status: v0.99 CERN Mapping

**Status:** speculative source-bookkeeping and mapping scaffold.
**Current layer:** v0.99 CERN/collider mapping from the v0.97 shared threefold reducer.
**Previous layer:** v0.98 cosmology mapping from the same reducer.

## Verdict

```text
CERN_MAPPING_PASSLIKE_FOR_SELECTED_PROXIES_FULL_VALIDATION_NOT_CLAIMED
```

## Latest chain

```text
v0.92: bubble light-cone projection
v0.93: simplified first-principle bubble formula
v0.94: central failed-mode-4 seed
v0.95: central-seed reducer
v0.96: threefold bubble-knot formula
v0.97: shared threefold reducer
v0.98: cosmology mapping from shared reducer
v0.99: CERN/collider mapping from shared reducer
```

## v0.97 shared reducer outputs

```text
load_proxy = 0.009817928223
mean_shear_proxy = 0.063915576742
beta4_needed_for_balance = 0.170868625373
H_proxy_relative = 0.977215138494
```

## v0.99 result

```text
Gamma_model = 4.109958967868 MeV
mu_inclusive_model = 1.000000000000
CMS HZZ residual = 0.526 sigma
D_proxy = -0.504201958707
ATLAS D residual = 1.717 sigma
CMS D residual = -0.880 sigma
```

## Status

```text
passes: selected CMS HZZ and CMS top-entanglement proxy checks are pass-like
close: ATLAS top-entanglement D is close but not pass-claimed
reference-close: Higgs width proxy is near the SM reference but is not scored as direct experimental validation
missing: branching ratios, channel signal strengths, detector event shapes, full CERN validation
```

## Files

```text
reports/mcift_v0.99_cern_mapping_report.md
reports/mcift_v0.98_cosmology_mapping_report.md
reports/mcift_v0.97_threefold_reducer_report.md
models/mcift_v0.96_threefold_bubble_knot_first_principle.md
simulations/mcift_v0_99_cern_mapping.py
analysis/results_v0.99/v099_cern_score.csv
analysis/results_v0.99/v099_cern_inputs.csv
analysis/results_v0.99/v099_state.csv
docs/v0.99_offline_milestone_prep.md
```

## Next

```text
v1.00: create a joint v0.98/v0.99 scorecard with explicit labels for derived, fitted, assumed, placeholder, not tested, pass-like, close-not-pass, and fail entries.
```
