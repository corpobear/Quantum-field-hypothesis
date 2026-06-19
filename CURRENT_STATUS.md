# Current MCIFT Status: v0.71 Expanded Cosmology Benchmark

**Status:** speculative expanded benchmark scaffold; not established physics.  
**Current layer:** v0.71 expanded cosmology comparison.  
**Previous layer:** v0.70 dual compact prediction test.

---

## One-sentence status

```text
MCIFT v0.71 expands the cosmology test beyond the compact H(z=0.75) check. It compares the same first-principle formula against Planck-like H0, local SH0ES H0, DESI LyA BAO, BBN baryon density, and S8-style weak-lensing/growth anchors. The result is mixed: close on early-universe and lensing-style anchors, but failing local H0.
```

---

## v0.71 verdict

```text
EXPANDED_COSMOLOGY_MIXED_CLOSE_ON_EARLY_AND_LENSING_FAILS_LOCAL_H0
```

---

## Key expanded benchmark results

```text
H0_prediction = 67.163010
Planck_H0 residual = -0.364797 sigma
SH0ES_H0 residual = -5.650952 sigma

H075_prediction = 103.465987
H075_delta_vs_compact_LCDM = -0.351618 percent
H075_residual_vs_CC = -0.142614 sigma

DESI_LyA_DH/rd prediction = 8.646895
DESI_LyA_DH/rd residual = +0.146909 sigma
DESI_LyA_DM/rd prediction = 39.311695
DESI_LyA_DM/rd residual = +0.602802 sigma

omega_b h2 prediction = 0.02237
BBN2024 residual = +0.345455 sigma

S8_prediction = 0.775722
DESY3_S8 residual = +0.206750 sigma
Planck_S8 residual = -4.329115 sigma
```

---

## Strict status

```text
close/pass-like: Planck-like H0, H(z=0.75), DESI LyA BAO, BBN baryon density, DES Y3-style S8
fail/tension: SH0ES local H0, Planck S8 if the growth proxy is taken literally
not implemented: full CMB Cl, full SN distance moduli, full BAO covariance, BBN reaction network
```

---

## Main files on master

```text
models/mcift_v0.71_expanded_cosmology_note.md
analysis/results_v0.71/v071_expanded_cosmology_metrics.csv
analysis/results_v0.71/v071_expanded_cosmology_tests.csv
main.md
README.md
CURRENT_STATUS.md
```

---

## Next target

```text
v0.72 should implement a proper cosmology data table and residual engine:
1. full BAO distance ladder table
2. supernova distance-modulus residuals
3. compressed CMB likelihood: theta_star, R, omega_b h2, omega_c h2
4. growth solver for f_sigma8 or S8 instead of one envelope proxy
```
