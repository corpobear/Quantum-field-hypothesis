# MCIFT v0.98 Cosmology Mapping Test

**Status:** first cosmology mapping test from the v0.97 shared threefold reducer. This is not a full cosmology validation.

## 1. Inputs from v0.97

```text
H_proxy_relative = 0.977215138494
mean_shear_proxy = 0.063915576742
```

## 2. Observational anchors used

```text
Planck H0 = 67.36 +/- 0.54
SH0ES H0 = 73.04 +/- 1.04
Planck S8 = 0.832
DES Y3 S8 = 0.776 +/- 0.017
```

DESI DR2 BAO is noted as a current BAO anchor, but not numerically scored in this version because v0.98 does not yet derive a BAO scale from the threefold reducer.

## 3. Mapping rules

One early-universe normalization is fitted:

```text
H0_norm = H0_planck / H_proxy_relative
```

Then:

```text
H0_early_model = H0_norm * H_proxy_relative
H0_local_model = H0_early_model * (1 + mean_shear_proxy)
S8_late_model = S8_planck * (1 - mean_shear_proxy)
```

## 4. Results

```text
H0_norm = 68.930573572376
H0_early_model = 67.36
H0_local_model = 71.665353249341
H0_local_residual_sigma = -1.321775721787
S8_late_model = 0.778822240151
S8_late_residual_sigma = 0.166014126510
```

## 5. Interpretation

The early H0 entry is a fitted anchor and is not an independent prediction.

The local H0 value is derived from the v0.97 shear proxy and lands within about 1.32 sigma of the SH0ES anchor using the quoted SH0ES uncertainty.

The late S8 value is derived from the same shear proxy and lands close to the DES Y3 value.

BAO, CMB acoustic scale, and BBN are not scored in v0.98.

## 6. Honesty labels

```text
H0_early_planck_anchor = fitted anchor
H0_local_shoes = derived from shear
S8_late_des_y3 = derived from shear
BAO = not tested
CMB acoustic scale = not tested
BBN = not tested
```

## 7. Next

v0.99 should either:

```text
1. build direct BAO/CMB/BBN mappings from the reducer, or
2. run the CERN mapping from the same v0.97 outputs.
```

A full joint cosmology-versus-CERN comparison should wait until both arms are mapped from the same reduced quantities.
