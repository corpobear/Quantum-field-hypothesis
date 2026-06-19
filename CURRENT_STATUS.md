# Current MCIFT Status: v0.61 First-Principle Inverse-Timeflow Cosmology Retest

**Status:** speculative cosmology retest scaffold; not established physics.  
**Current layer:** v0.61 first-principle inverse-timeflow cosmology formula.  
**Previous layer:** v0.60 inverse-timeflow backpropagation and channel-readout implementation.

---

## One-sentence status

```text
MCIFT v0.61 implements a cosmology-specific inverse-timeflow formula. It reduces the v0.59 raw H(z=0.75) over-expansion without using reference-derived smoothing. The result improves the raw cosmology readout, but does not yet count as a full cosmology pass.
```

---

## v0.61 verdict

```text
FIRST_PRINCIPLE_ITF_IMPROVES_RAW_HZ_NOT_FULL_COSMOLOGY_PASS
```

---

## Formula summary

```text
C_ITF = A_lock * N_dark / (N_dark + N_visible + N_anchor)
tau_ITF = exp[-C_ITF / (N_visible + N_anchor)]
H_lab = tau_ITF * H_core
```

Numerical values:

```text
N_dark = 6
N_visible = 1
N_anchor = 1
A_lock_5B = 0.918752
C_ITF = 0.689064
tau_ITF = 0.708552
```

---

## H(z=0.75) comparison

```text
v0.59 raw H075_3d = 156.663819
v0.59 raw delta vs LCDM = +50.883364 percent
v0.59 raw residual vs CC = +4.803080 sigma

v0.60 transfer H075_3d = 103.897709
v0.60 transfer delta vs LCDM = +0.064175 percent
v0.60 transfer residual vs CC = -0.102478 sigma

v0.61 first-principle ITF H075 = 111.004443
v0.61 first-principle ITF delta vs LCDM = +6.908691 percent
v0.61 first-principle ITF residual vs CC = +0.558221 sigma
```

Improvement:

```text
raw_to_v061_delta_pct_improvement_factor = 7.364392x
```

---

## Strict status

```text
raw over-expansion: IMPROVED
reference-derived smoothing: NOT USED in v0.61 formula
full BAO ladder: NOT IMPLEMENTED
CMB power spectrum: NOT IMPLEMENTED
BBN network: NOT IMPLEMENTED
```

---

## Analysis result files

```text
simulations/mcift_v0_61_first_principle_cosmology_itf.py
analysis/results_v0.61/mcift_v0.61_first_principle_cosmology_metrics.csv
analysis/results_v0.61/mcift_v0.61_Hz_comparison.csv
```

---

## Next target

```text
v0.62 should make C_ITF redshift-dependent from actual 3D field cells using S_i = Coh_i - q_i, then score D_M(z), D_H(z), BAO, growth, and CMB-like spectra.
```
