# MCIFT v0.73 Cell-Action Spatial Lapse Cosmology Retest

**Status:** speculative first-principle scaffold; not established physics.  
**Purpose:** replace the v0.72 bridge statement `sigma_X = E_DV^(1/3)` with a minimal cell-action derivation, then retest against expanded cosmology anchors.

---

## From patch to minimal action

v0.72 used:

```text
sigma_X = E_DV^(1/3)
```

v0.73 derives the same kind of ruler factor from a strain-energy equation.

Define a local spatial strain field:

```text
sigma_X = exp(phi_X)
```

Define a source from dark-visible stress:

```text
J_X = C_ITF * O_DV
```

Use the minimal one-zone strain action:

```text
F_X(phi_X) = 1/2 K_X phi_X^2 - J_X phi_X
```

The stationary point gives:

```text
partial F_X / partial phi_X = 0
K_X phi_X - J_X = 0
phi_X = J_X / K_X
```

For three spatial axes and two visible/anchor constraints:

```text
K_X = 3 (N_V + N_A) = 6
```

Therefore:

```text
phi_X = C_ITF * O_DV / [3 (N_V + N_A)]
sigma_X = exp(phi_X)
```

Numerically:

```text
C_ITF = 0.689064
O_DV = 0.612372436
K_X = 6
phi_X = 0.070040089
sigma_X = 1.072549870
```

---

## Cosmology retest

```text
H0_prediction = 67.163010
Planck_H0 residual = -0.364797 sigma
SH0ES_H0 residual = -5.650952 sigma
PantheonPlus_H0 residual = -5.760900 sigma
PantheonPlus_OmegaM residual = -1.038889 sigma

H075_prediction = 103.465987
H075_delta_vs_compact_LCDM = -0.351618 percent

DESI_LyA_DH/rd residual = +0.146909 sigma
DESI_LyA_DM/rd residual = +0.602802 sigma

BBN omega_b h2 residual = +0.345455 sigma
DESY3_S8 residual = +0.206750 sigma
Planck_S8 residual = -4.329115 sigma
```

---

## Verdict

```text
CELL_ACTION_SPATIAL_LAPSE_REPRODUCES_DISTANCE_CLOSES_BUT_FULL_COSMOLOGY_STILL_MIXED
```

Meaning:

```text
The spatial lapse is now derived from a minimal action instead of only asserted as a cube root.
The cosmology result remains close for Planck-like H0, H(z), DESI LyA, BBN, DES-Y3-style S8, and Pantheon+ OmegaM.
It still fails SH0ES/Pantheon+ local H0 and Planck S8 if the growth proxy is taken literally.
It still does not implement full CMB Cl, full SN distance-modulus residuals, full BAO covariance, or a BBN reaction network.
```

---

## Next target

v0.74 should move from one-zone action to actual cell-resolved action:

```text
F_X = sum_i [1/2 K_i phi_i^2 + 1/2 |grad phi_i|^2 - J_i phi_i]
J_i = O_DV(i) * max(0, q_i - Coh_i)^2 / [q_i^2 + Coh_i^2 + epsilon]
```

Then solve:

```text
(-nabla^2 + K_i) phi_i = J_i
```

and compute:

```text
sigma_X(a) = exp[weighted average of phi_i over the observed redshift shell]
```
