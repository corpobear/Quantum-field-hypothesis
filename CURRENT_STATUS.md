# Current MCIFT Status: v0.72 Spatial Scale-Lapse Retest

**Status:** speculative cosmology scaffold; not established physics.  
**Current layer:** v0.72 spatial scale-lapse retest.  
**Previous layer:** v0.71 expanded cosmology benchmark.

---

## One-sentence status

```text
MCIFT v0.72 makes the spatial ruler correction explicit. It tests whether gravity/dark-visible overlap changes the effective measurement scale of space as well as time. The spatial lapse improves H(z) and distance-style anchors, but it does not solve local SH0ES H0 or the raw BAO peak scale.
```

---

## v0.72 verdict

```text
SPATIAL_SCALE_LAPSE_IMPROVES_HZ_AND_DISTANCE_ANCHORS_BUT_NOT_LOCAL_H0_OR_RAW_BAO_PEAK
```

---

## Spatial scale-lapse formula

```text
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
sigma_X = E_DV^(1/3)
        = exp[C_ITF * O_DV / (3 (N_V + N_A))]
```

Current values:

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

## Retest results

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

## Main files on master

```text
models/mcift_v0.72_spatial_scale_lapse_note.md
analysis/results_v0.72/v072_spatial_lapse_metrics.csv
analysis/results_v0.72/v072_spatial_lapse_tests.csv
main.md
README.md
CURRENT_STATUS.md
```

---

## Next target

```text
v0.73 should implement a proper distance-ladder engine:
1. compute D_M(z), D_H(z), D_V(z) over many BAO redshifts
2. compare against DESI/BOSS/eBOSS BAO tables
3. compute supernova distance-modulus residuals
4. keep sigma_X fixed by the formula, not fit per dataset
```
