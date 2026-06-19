# Current MCIFT Status: v0.59 Cosmology + CERN Real-World Retest

**Status:** speculative real-data retest scaffold; not established physics.  
**Current layer:** v0.59 cosmology + CERN/LHC public-data retest/audit.  
**Previous layer:** v0.58 3D unified real-data retest.

---

## One-sentence status

```text
MCIFT v0.59 retests the current v0.58 3D output against cosmology and CERN/LHC anchors. Raw 3D particle channels still fail the all-channel criterion, especially gamma, Zgamma, and cc. Raw 3D cosmology still over-expands. Transfer/smoothing and kappa/clock bridges remain useful scaffolds, but they are not independent physical predictions.
```

---

## v0.59 verdict

```text
REALDATA_RETEST_FAILS_RAW_BUT_IDENTIFIES_NEXT_IMPLEMENTATION_TARGETS
```

Detailed verdict:

```text
COSMOLOGY_RAW_FAIL_TRANSFER_PASS_SCAFFOLD
CERN_RAW_FAIL_BRIDGE_COMPATIBLE_NOT_PREDICTIVE
INVERSE_TIMEFLOW_BACKPROP_LOSS_NOT_IMPLEMENTED
```

---

## Cosmology result

```text
Planck-style baryon/CDM ratio = 0.186417

visible_dark_2B = 0.195224
visible_dark_2B_fractional_error_vs_planck_ratio = 0.047245

visible_dark_5B = 0.153635
visible_dark_5B_fractional_error_vs_planck_ratio = 0.175852

v0.20 final BAO/global peak = 152.29 Mpc
fractional_error_vs_rd_147.09 = 0.035353

v0.58 H075_raw_3d = 156.663819
v0.58 H075_raw_delta_pct_vs_reference = 50.883364

v0.58 H075_transfer_3d = 103.897709
v0.58 H075_transfer_delta_pct_vs_reference = 0.064175
v0.58 H075_transfer_residual_sigma_vs_CC_obs = -0.102478
```

Strict status:

```text
Raw 3D cosmology: FAIL / over-expands
Transfer 3D cosmology: PASS-LIKE as calibrated scaffold
Full CMB / BAO ladder / BBN / w0-wa fit: NOT_IMPLEMENTED
```

---

## CERN/LHC result

```text
BR_L1_raw_vs_SM = 0.092428
max_abs_BR_delta_pct_raw_vs_SM = 100.000000
failed_CERN_channels_10pct = gg,tau,cc,gamma,Zgamma,mumu
```

Raw channel status:

```text
bb, WW, ZZ: within 10 percent
gg, tau, cc, gamma, Zgamma, mumu: fail 10 percent criterion
```

Bridge status:

```text
v0.52 channel-clock bridge:
  Gamma_lab_channel_clock_MeV = 3.965184
  width_delta_fraction_vs_4.07 = 0.025753
  max_abs_BR_delta_pct_after_channel_clock = 3.313884
  max_abs_signal_strength_delta_pct_after_channel_clock = 5.205441

v0.53 sound-spread bridge:
  Gamma_lab_sound_raw_MeV = 3.964892
  width_delta_fraction_vs_4.07 = 0.025825
  max_abs_BR_delta_pct_after_sound = 4.913465
  max_abs_signal_strength_delta_pct_after_sound = 7.790001
```

Strict status:

```text
Raw CERN channel model: FAIL
Calibrated / bridge layers: compatible scaffolds, not predictions
```

---

## Inverse timeflow backpropagation status

```text
forward timeflow/clock formulas: PRESENT
inverse-timeflow backprop loss: NOT_IMPLEMENTED
```

The intended AI-style layer is:

```text
observed lab residual -> inverse timeflow loss -> gradients/updates into hidden MCIFT parameters
```

This is documented as a future implementation target, not a completed trained model.

---

## Analysis result files

```text
analysis/results_v0.59/mcift_v0.59_cosmology_cern_retest_report.md
analysis/results_v0.59/mcift_v0.59_cosmology_cern_retest_metrics.csv

analysis/results_v0.58/mcift_v0.58_3d_realdata_retest_report.md
analysis/results_v0.58/mcift_v0.58_3d_realdata_metrics.csv
analysis/results_v0.58/mcift_v0.58_cern_channels.csv
analysis/results_v0.58/mcift_v0.58_reference_comparison.csv
```

---

## Safe wording

```text
v0.59 is a real-data retest/audit. It does not pass raw CERN channel comparison and does not pass raw cosmology. It shows that loop/surface particle channels, cc projection, full cosmology observables, and an implemented inverse-timeflow loss are the next required steps.
```
