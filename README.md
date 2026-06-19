# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.73 cell-action spatial lapse cosmology retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

The main branch now retests cosmology after deriving the spatial scale-lapse from a minimal strain-energy action:

```text
v0.72: sigma_X was written as E_DV^(1/3)
v0.73: sigma_X is derived from a one-zone cell-action stationary point
```

Current verdict:

```text
v0.73 = CELL_ACTION_SPATIAL_LAPSE_REPRODUCES_DISTANCE_CLOSES_BUT_FULL_COSMOLOGY_STILL_MIXED
```

---

## Minimal cell-action derivation

```text
sigma_X = exp(phi_X)
J_X = C_ITF * O_DV
F_X(phi_X) = 1/2 K_X phi_X^2 - J_X phi_X
partial F_X / partial phi_X = 0
phi_X = J_X / K_X
K_X = 3 (N_V + N_A) = 6
```

Therefore:

```text
phi_X = C_ITF * O_DV / [3 (N_V + N_A)]
sigma_X = exp(phi_X)
```

Current values:

```text
C_ITF = 0.689064
O_DV = 0.612372436
K_X = 6
phi_X = 0.070040089
sigma_X = 1.072549870
```

---

## v0.73 cosmology retest

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

## Strict status

```text
close/pass-like: Planck-like H0, H(z=0.75), DESI LyA BAO, BBN baryon density, DES Y3-style S8, Pantheon+ OmegaM
fail/tension: SH0ES H0, Pantheon+ local-distance-ladder H0, Planck S8 if the growth proxy is literal
not implemented: full CMB Cl, full SN distance-modulus residuals, full BAO covariance, BBN reaction network
```

---

## Main documents

```text
models/mcift_v0.73_cell_action_spatial_lapse_note.md
analysis/results_v0.73/v073_cell_derived_spatial_lapse_metrics.csv
analysis/results_v0.73/v073_cell_derived_cosmology_tests.csv
main.md
CURRENT_STATUS.md
README.md
```

---

## Next version target

```text
v0.74 should move from one-zone action to cell-resolved action:
F_X = sum_i [1/2 K_i phi_i^2 + 1/2 |grad phi_i|^2 - J_i phi_i]
(-nabla^2 + K_i) phi_i = J_i
sigma_X(a) = exp[weighted average of phi_i over the observed redshift shell]
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
