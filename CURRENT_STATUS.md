# Current MCIFT Status: v0.60 Inverse-Timeflow Backpropagation Retest

**Status:** speculative implementation and retest scaffold; not established physics.  
**Current layer:** v0.60 inverse-timeflow backpropagation and channel-readout implementation.  
**Previous layer:** v0.59 cosmology + CERN/LHC public-data retest.

---

## One-sentence status

```text
MCIFT v0.60 implements the missing gamma/Zgamma loop-surface readouts, explicit cc projection, and inverse-timeflow backpropagation loss. It then retests against the v0.59 baseline. The particle-channel bridge improves strongly. Cosmology remains at transfer/smoothing scaffold level.
```

---

## v0.60 verdict

```text
IMPLEMENTED_BACKPROP_IMPROVES_CERN_BRIDGE_RAW_STILL_SCAFFOLD
```

Detailed status:

```text
gamma_Zgamma_loop_surface_readout: IMPLEMENTED
cc_projection: IMPLEMENTED
inverse_timeflow_backprop_loss: IMPLEMENTED
CERN implemented-readout before backprop: NEAR_PASS_WITH_GG_REMAINING
CERN after inverse-timeflow backprop: TRAINED_BRIDGE_PASS_LIKE
cosmology raw: STILL_FAIL
cosmology timeflow/transfer: PASS_LIKE_SCAFFOLD
```

---

## Comparison with v0.59

```text
v0.59 inverse_timeflow_backprop_loss = NOT_IMPLEMENTED
v0.60 inverse_timeflow_backprop_loss = IMPLEMENTED

v0.59 raw BR_L1_vs_SM = 0.092428
v0.60 implemented BR_L1_vs_SM = 0.037697
v0.60 after backprop BR_L1_vs_SM = 0.000938

v0.59 raw max_abs_BR_delta_pct = 100.000000
v0.60 implemented max_abs_BR_delta_pct = 10.502733
v0.60 after backprop max_abs_BR_delta_pct = 0.294487

v0.59 failed_CERN_channels_10pct = gg,tau,cc,gamma,Zgamma,mumu
v0.60 implemented failed_CERN_channels_10pct = gg
v0.60 after_backprop failed_CERN_channels_10pct = none
```

---

## CERN/LHC result

```text
Gamma_total_after_backprop = 4.071982 MeV
Gamma_total_delta_pct = +0.048698
tau_time_lab_factor = 0.975951
final_inverse_timeflow_loss = 0.001072518
```

---

## Cosmology result

```text
v0.59 raw H075_3d = 156.663819
v0.59 transfer H075_3d = 103.897709
v0.60 q_smoothing_derived_from_v0_59_transfer = 6.675682
v0.60 H075_after_timeflow = 103.897709
v0.60 H075_after_timeflow_delta_pct_vs_reference = 0.064175
```

---

## Analysis result files

```text
simulations/mcift_v0_60_inverse_timeflow_backprop_retest.py
analysis/results_v0.60/mcift_v0.60_inverse_timeflow_retest_report.md
analysis/results_v0.60/mcift_v0.60_inverse_timeflow_metrics.csv
analysis/results_v0.60/mcift_v0.60_cern_channels_before_after.csv
```

---

## Safe wording

```text
v0.60 implements the missing readout and inverse-timeflow loss layers and improves the CERN-channel comparison relative to v0.59. The post-backprop result is a trained bridge. Cosmology remains a transfer/smoothing scaffold.
```
