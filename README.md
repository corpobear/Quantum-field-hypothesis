# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.58 3D real-data retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has a strict 3D retest layer:

```text
v0.57 execution:
  one deterministic 3D unified-field run produces channels, branches, transfer, and background readouts

v0.58 retest:
  the same 3D output is compared in raw, transfer, and calibrated modes
```

Current verdict:

```text
v0.58 3D retest = PARTICLE_RAW_FAIL_COSMOLOGY_TRANSFER_PASS_SCAFFOLD
```

This is a retest scaffold, not a completed particle or cosmology fit.

---

## v0.58 particle-channel result

```text
BR_L1_raw_vs_ref = 0.092428
max_abs_BR_delta_pct_raw_vs_ref = 100.000000
failed_channels_10pct = gg,tau,cc,gamma,Zgamma,mumu
raw_gamma_delta_pct = -99.924245
raw_Zgamma_delta_pct = -99.960445
raw_cc_delta_pct = -100.000000
```

## v0.58 background result

```text
H075_raw_3d = 156.663819
H075_raw_delta_pct_vs_reference = 50.883364
H075_transfer_3d = 103.897709
H075_transfer_delta_pct_vs_reference = 0.064175
H075_transfer_residual_sigma_vs_CC_obs = -0.102478
```

---

## Analysis result files

```text
CURRENT_STATUS.md
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
v0.58 does not pass raw particle-channel comparison and does not pass raw cosmology. It shows exactly where the 3D model still needs work: loop/surface particle channels, cc projection, and transfer/smoothing dynamics.
```

---

## Research roadmap

Next required tests:

```text
1. Add explicit 3D loop/surface readouts for gamma and Zgamma.
2. Add explicit cc channel projection.
3. Derive Q_i smoothing dynamically instead of using retained factors.
4. Rerun raw 3D particle and cosmology tests before any calibrated comparison.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
