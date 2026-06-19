# Current MCIFT Status: v0.58 3D Real-Data Retest

**Status:** speculative 3D retest scaffold; not established physics.  
**Current layer:** v0.58 3D unified real-data retest.  
**Previous layer:** v0.57 executable unified-field run.

---

## One-sentence status

```text
MCIFT v0.58 retests particle-channel and cosmology readouts from the same v0.57 3D unified-field output. The raw 3D particle channels fail the all-channel criterion, especially gamma, Zgamma, and cc. Raw 3D cosmology over-expands. The transfer/smoothing mode remains close to the background H(z) reference as a calibrated scaffold.
```

---

## v0.58 verdict

```text
PARTICLE_RAW_FAIL_COSMOLOGY_TRANSFER_PASS_SCAFFOLD
```

Particle-channel result:

```text
BR_L1_raw_vs_ref = 0.092428
max_abs_BR_delta_pct_raw_vs_ref = 100.000000
failed_channels_10pct = gg,tau,cc,gamma,Zgamma,mumu
raw_gamma_delta_pct = -99.924245
raw_Zgamma_delta_pct = -99.960445
raw_cc_delta_pct = -100.000000
```

Background expansion result:

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
simulations/mcift_v0_58_3d_realdata_retest.py
analysis/results_v0.58/mcift_v0.58_3d_realdata_retest_report.md
analysis/results_v0.58/mcift_v0.58_3d_realdata_metrics.csv
analysis/results_v0.58/mcift_v0.58_cern_channels.csv
analysis/results_v0.58/mcift_v0.58_cern_calibration_needed.csv
analysis/results_v0.58/mcift_v0.58_cosmology_Hz.csv
analysis/results_v0.58/mcift_v0.58_reference_comparison.csv
analysis/results_v0.58/mcift_v0.58_criteria.csv
```

Plots and the full reference comparison table are in the local output bundle.

---

## Safe wording

```text
v0.58 is a strict 3D retest. It does not pass raw particle-channel comparison and it does not pass raw cosmology. It shows that loop/surface particle channels and cosmological transfer/smoothing remain necessary before any stronger claim.
```
