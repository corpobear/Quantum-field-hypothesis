# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.59 cosmology + CERN real-world retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has a strict real-data retest layer:

```text
v0.57 execution:
  one deterministic 3D unified-field run produces channels, branches, transfer, and background readouts

v0.58 retest:
  the same 3D output is compared in raw, transfer, and calibrated modes

v0.59 audit:
  the v0.58 outputs are retested/documented against current cosmology and CERN/LHC anchors,
  including Planck 2018, DESI BAO / DESI DR2 context, and Higgs mass/width/signal-strength constraints
```

Current verdict:

```text
v0.59 = REALDATA_RETEST_FAILS_RAW_BUT_IDENTIFIES_NEXT_IMPLEMENTATION_TARGETS
```

This is a retest scaffold, not a completed particle or cosmology fit.

---

## v0.59 cosmology result

```text
COSMOLOGY_RAW_FAIL_TRANSFER_PASS_SCAFFOLD

H075_raw_3d = 156.663819
H075_raw_delta_pct_vs_reference = 50.883364

H075_transfer_3d = 103.897709
H075_transfer_delta_pct_vs_reference = 0.064175
H075_transfer_residual_sigma_vs_CC_obs = -0.102478
```

Interpretation:

```text
The raw 3D background over-expands.
The transfer/smoothing layer remains close to the reference curve,
but this is a calibrated scaffold rather than an independent cosmology derivation.
```

---

## v0.59 CERN/LHC result

```text
CERN_RAW_FAIL_BRIDGE_COMPATIBLE_NOT_PREDICTIVE

BR_L1_raw_vs_SM = 0.092428
max_abs_BR_delta_pct_raw_vs_SM = 100.000000
failed_channels_10pct = gg,tau,cc,gamma,Zgamma,mumu
```

The bridge layers remain numerically useful but are not independent predictions:

```text
v0.52 channel-clock bridge:
  Gamma_lab_channel_clock_MeV = 3.965184
  max_abs_BR_delta_pct_after_channel_clock = 3.313884
  max_abs_signal_strength_delta_pct_after_channel_clock = 5.205441

v0.53 sound-spread bridge:
  Gamma_lab_sound_raw_MeV = 3.964892
  max_abs_BR_delta_pct_after_sound = 4.913465
  max_abs_signal_strength_delta_pct_after_sound = 7.790001
```

---

## Inverse timeflow backpropagation status

```text
forward timeflow/clock formulas: PRESENT
inverse-timeflow backprop loss: NOT_IMPLEMENTED
```

The inverse timeflow backpropagation derivation is now documented as a future AI-style loss-function layer, not as an already-trained result.

---

## Analysis result files

```text
CURRENT_STATUS.md
analysis/results_v0.59/mcift_v0.59_cosmology_cern_retest_report.md
analysis/results_v0.59/mcift_v0.59_cosmology_cern_retest_metrics.csv

simulations/mcift_v0_58_3d_realdata_retest.py
analysis/results_v0.58/mcift_v0.58_3d_realdata_retest_report.md
analysis/results_v0.58/mcift_v0.58_3d_realdata_metrics.csv
analysis/results_v0.58/mcift_v0.58_cern_channels.csv
analysis/results_v0.58/mcift_v0.58_cern_calibration_needed.csv
analysis/results_v0.58/mcift_v0.58_cosmology_Hz.csv
analysis/results_v0.58/mcift_v0.58_reference_comparison.csv
analysis/results_v0.58/mcift_v0.58_criteria.csv
```

---

## Important limitation

```text
v0.59 does not pass raw particle-channel comparison and does not pass raw cosmology.
It confirms the earlier v0.58 problem with stricter external-data language:
loop/surface particle channels, cc projection, and transfer/smoothing dynamics remain necessary.
```

---

## Research roadmap

Next required tests:

```text
1. Add explicit 3D loop/surface readouts for gamma and Zgamma.
2. Add explicit cc channel projection.
3. Derive Q_i smoothing dynamically instead of using retained factors.
4. Implement full cosmology observables: H(z), D_M(z), D_H(z), BAO ladder, C_l, and growth.
5. Implement inverse timeflow backpropagation as an actual loss function.
6. Rerun raw 3D particle and cosmology tests before any calibrated comparison.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
