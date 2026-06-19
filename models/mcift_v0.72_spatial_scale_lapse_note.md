# MCIFT v0.72 Spatial Scale-Lapse Retest

**Status:** speculative cosmology scaffold; not established physics.  
**Purpose:** make the spatial ruler correction explicit and retest the expanded cosmology anchors.

---

## Motivation

Earlier versions accounted for time dilation / inverse-timeflow. v0.72 tests the complementary idea:

```text
gravity changes the effective ruler as well as the clock
```

The simulation scale and the observed measurement scale may not be identical.

---

## Formula

The dark-visible envelope from v0.64/v0.70 is:

```text
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

The spatial scale-lapse is defined as:

```text
sigma_X = E_DV^(1/3)
        = exp[C_ITF * O_DV / (3 (N_V + N_A))]
```

Current values:

```text
C_ITF = 0.689064
O_DV = 0.612372436
E_DV = 1.234890003
sigma_X = 1.072549870
spatial lapse = +7.254987 percent
```

---

## Observable maps

```text
H_lab = H_core / sigma_X
D_lab = sigma_X * D_core
k_lab = k_core / sigma_X
Gamma_lab = sigma_X^3 * tau_i * Gamma_core
```

This means the same dark-visible envelope that fixed the CERN width also defines the spatial ruler correction used in cosmology.

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

Raw BAO peak test:

```text
raw BAO peak = 152.29 Mpc
reference r_d = 147.09 Mpc
raw fractional error = +0.035353

if divided by sigma_X: 141.987812 Mpc, fractional error = -0.034690
if multiplied by sigma_X: 163.340999 Mpc, fractional error = +0.110481
```

So the spatial lapse improves H(z) and distance-style anchors, but it does not solve the raw BAO peak by itself.

---

## Verdict

```text
SPATIAL_SCALE_LAPSE_IMPROVES_HZ_AND_DISTANCE_ANCHORS_BUT_NOT_LOCAL_H0_OR_RAW_BAO_PEAK
```

Meaning:

```text
works well: H(z=0.75), Planck-like H0, DESI LyA distance ratios
still fails: local SH0ES H0
not solved: raw BAO peak scale
not implemented: full BAO ladder covariance, SN distance moduli, full CMB Cl
```

---

## Next target

v0.73 should implement a proper distance-ladder engine:

```text
1. compute D_M(z), D_H(z), D_V(z) over many BAO redshifts
2. compare against DESI/BOSS/eBOSS BAO tables
3. compute supernova distance-modulus residuals
4. keep sigma_X fixed by the formula, not fit per dataset
```
