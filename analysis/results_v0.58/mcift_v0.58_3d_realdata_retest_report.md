# MCIFT v0.58 3D Real-Data Retest

**Status:** 3D unified-field retest; speculative scaffold, not established physics.

## Purpose

v0.58 compares the same v0.57 3D unified-field output in three modes:

```text
A. raw 3D field readout
B. 3D field plus transfer/smoothing
C. calibrated comparison layer
```

## Verdict

```text
CERN_RAW_FAIL_COSMOLOGY_TRANSFER_PASS_SCAFFOLD
```

## Particle-channel result

The raw 3D field does not pass the all-channel 10 percent criterion.

```text
BR_L1_raw_vs_SM = 0.092428
max_abs_BR_delta_pct_raw_vs_SM = 100.000000
failed_channels_10pct = gg,tau,cc,gamma,Zgamma,mumu
raw_gamma_delta_pct = -99.924245
raw_Zgamma_delta_pct = -99.960445
raw_cc_delta_pct = -100.000000
```

The main failure is the missing loop/surface channel mechanism and missing explicit cc readout.

## Background expansion result

```text
H075_raw_3d = 156.663819
H075_raw_delta_pct_vs_reference = 50.883364
H075_transfer_3d = 103.897709
H075_transfer_delta_pct_vs_reference = 0.064175
H075_transfer_residual_sigma_vs_CC_obs = -0.102478
```

Raw 3D branches over-expand. Transfer/smoothing remains close to the reference curve.

## Strict conclusion

```text
particle-channel raw 3D: FAIL
background raw 3D: FAIL / over-expands
background transfer 3D: PASS as calibrated scaffold
calibrated particle bridge: possible but not prediction
```

## Next target

v0.59 should add explicit 3D loop/surface readouts for gamma, Zgamma, and cc before any new particle-data pass claim.
