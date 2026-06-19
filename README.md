# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.71 expanded cosmology benchmark

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

The main branch now expands the cosmology comparison beyond the v0.70 compact H(z=0.75) check:

```text
Planck-like H0
local SH0ES H0
H(z=0.75)
DESI LyA BAO D_H/r_d and D_M/r_d
BBN baryon density
S8 weak-lensing / growth-style proxy
BAO peak sanity check
```

Current verdict:

```text
v0.71 = EXPANDED_COSMOLOGY_MIXED_CLOSE_ON_EARLY_AND_LENSING_FAILS_LOCAL_H0
```

---

## Reworked formula

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
tau_ITF = exp[-C_ITF / (N_V + N_A)]
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

Current numerical values:

```text
N_D = 6
N_V = 1
N_A = 1
A_lock = 0.918752
C_ITF = 0.689064
tau_ITF = 0.708551878
O_DV = 0.612372436
E_DV = 1.234890003
E_DV^(1/3) = 1.072549870
```

---

## v0.71 expanded cosmology results

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

## Main documents

```text
models/mcift_v0.71_expanded_cosmology_note.md
analysis/results_v0.71/v071_expanded_cosmology_metrics.csv
analysis/results_v0.71/v071_expanded_cosmology_tests.csv
main.md
CURRENT_STATUS.md
README.md
```

---

## Next version target

```text
v0.72 should implement a proper cosmology data table and residual engine:
full BAO distance ladder
supernova distance-modulus residuals
compressed CMB likelihood
growth solver for f_sigma8 or S8 instead of one envelope proxy
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
