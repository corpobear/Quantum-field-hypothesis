# MCIFT v0.71 Expanded Cosmology Benchmark

**Status:** speculative benchmark scaffold; not established physics.  
**Purpose:** compare the v0.70/v0.64 first-principle formula against more real-world cosmology anchors.

---

## Scope

v0.70 compared only a compact H(z=0.75) prediction plus a BAO sanity check. v0.71 expands the benchmark to:

```text
Planck-like H0
local SH0ES H0
H(z=0.75)
DESI LyA BAO D_H/r_d and D_M/r_d at z=2.33
BBN baryon density
S8 weak-lensing style check
BAO peak sanity check
```

It still does not implement a full Boltzmann CMB likelihood, full Pantheon+/DES SN likelihood, full BAO covariance, or BBN reaction network.

---

## Prediction rules

Expansion scaling:

```text
lambda_H = H075_v070 / H075_LCDM = 0.996483823
```

Growth proxy:

```text
S8_pred = S8_Planck / E_DV^(1/3)
```

DESI LyA BAO predictions are computed from the same scaled flat expansion curve.

---

## Results

```text
H0_prediction = 67.163010
Planck_H0 residual = -0.364797 sigma
SH0ES_H0 residual = -5.650952 sigma

H075_prediction = 103.465987
H075_delta_vs_LCDM = -0.351618 percent
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

## Verdict

```text
EXPANDED_COSMOLOGY_MIXED_CLOSE_ON_EARLY_AND_LENSING_FAILS_LOCAL_H0
```

Meaning:

```text
close/pass-like: Planck-like H0, H(z=0.75), DESI LyA BAO, BBN baryon density, DES Y3-style S8
fail/tension: SH0ES local H0, Planck S8 if the growth proxy is taken literally
not implemented: full CMB Cl, full SN distance moduli, full BAO covariance, BBN network
```

---

## Next target

v0.72 should stop using compact proxy observables and implement at least:

```text
1. full BAO distance ladder table with covariance-free residuals first
2. Pantheon+/DES/SN distance-modulus residuals
3. a growth solver for f_sigma8 or S8 instead of one envelope proxy
4. CMB compressed likelihood: theta_star, R, omega_b h2, omega_c h2
```
