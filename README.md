# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.72 spatial scale-lapse retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

The main branch now tests the missing spatial ruler correction:

```text
previous idea: inverse-timeflow changes the clock
v0.72 idea: gravity/dark-visible overlap also changes the effective ruler
```

Current verdict:

```text
v0.72 = SPATIAL_SCALE_LAPSE_IMPROVES_HZ_AND_DISTANCE_ANCHORS_BUT_NOT_LOCAL_H0_OR_RAW_BAO_PEAK
```

---

## Spatial scale-lapse formula

```text
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
sigma_X = E_DV^(1/3)
        = exp[C_ITF * O_DV / (3 (N_V + N_A))]
```

Current numerical values:

```text
C_ITF = 0.689064
O_DV = 0.612372436
E_DV = 1.234890003
sigma_X = 1.072549870
spatial_lapse = +7.254987 percent
```

Observable maps:

```text
H_lab = H_core / sigma_X
D_lab = sigma_X * D_core
k_lab = k_core / sigma_X
Gamma_lab = sigma_X^3 * tau_i * Gamma_core
```

---

## v0.72 retest results

```text
H075 before spatial lapse = 111.004443
H075 after spatial lapse = 103.465987
H075 delta vs compact LCDM = -0.351618 percent

Planck-like H0 residual = -0.364797 sigma
SH0ES H0 residual = -5.650952 sigma

DESI LyA D_H/r_d residual = +0.146909 sigma
DESI LyA D_M/r_d residual = +0.602802 sigma
```

Raw BAO peak check:

```text
raw BAO peak = 152.29 Mpc
reference r_d = 147.09 Mpc
raw fractional error = +0.035353

if divided by sigma_X: 141.987812 Mpc, fractional error = -0.034690
if multiplied by sigma_X: 163.340999 Mpc, fractional error = +0.110481
```

---

## Strict status

```text
works well: H(z=0.75), Planck-like H0, DESI LyA distance ratios
still fails: local SH0ES H0
not solved: raw BAO peak scale
not implemented: full BAO ladder covariance, SN distance moduli, full CMB Cl
```

---

## Main documents

```text
models/mcift_v0.72_spatial_scale_lapse_note.md
analysis/results_v0.72/v072_spatial_lapse_metrics.csv
analysis/results_v0.72/v072_spatial_lapse_tests.csv
main.md
CURRENT_STATUS.md
README.md
```

---

## Next version target

```text
v0.73 should implement a proper distance-ladder engine:
full BAO D_M, D_H, D_V table across redshifts
supernova distance-modulus residuals
compressed CMB distance priors
no per-dataset fitting of sigma_X
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
