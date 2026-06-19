# Current MCIFT Status: v0.81 Tensor-Strain Bridge

**Status:** speculative linearized tensor bridge; not full GR.  
**Current layer:** v0.81 tensor-strain bridge.  
**Previous layer:** v0.80 weak-field metric bridge.

---

## One-sentence status

```text
MCIFT v0.81 extends the v0.80 scalar weak-field metric into a linearized tensor scaffold. It preserves the v0.80 weak-field checks and adds structural shift/frame-dragging and transverse-traceless wave modes, but it still does not derive full nonlinear field equations or source conservation.
```

---

## v0.81 verdict

```text
TENSOR_STRAIN_EXTENSION_PRESERVES_WEAK_FIELD_LIMIT_ADDS_SHIFT_AND_TT_MODES_FULL_GR_STILL_NOT_DERIVED
```

---

## Tensor bridge

```text
g_mu_nu = eta_mu_nu + h_mu_nu
h_00 = -2 psi
h_ij = 2 psi delta_ij + hTT_ij
h_0i = beta_i
```

Interpretation:

```text
h_00: time strain
h_ij: spatial tensor strain
h_0i: shift / frame-dragging mode
hTT_ij: transverse-traceless wave mode
```

---

## Test result

```text
v0.80 weak-field regression: preserved
PPN gamma = 1.000000
light bending: preserved
Mercury precession: preserved
Shapiro coefficient: preserved
h_0i shift mode: structurally nonzero
frame-dragging coefficient: normalized to 1
TT wave modes: plus and cross
GW speed: c by bridge equation
```

---

## Strict status

```text
passes: preserves v0.80 weak-field limit, adds structural shift/frame-dragging mode, adds TT wave modes
missing: full nonlinear field equations, source conservation, contracted Bianchi identity, observational frame-dragging fit, observational GW waveform fit
```

---

## Main files on master

```text
simulations/mcift_v0_81_tensor_strain_bridge.py
models/mcift_v0.81_tensor_strain_bridge_note.md
analysis/results_v0.81/v081_tensor_strain_metrics.csv
analysis/results_v0.81/v081_tensor_strain_tests.csv
README.md
CURRENT_STATUS.md
```

---

## Next target

```text
v0.82 should derive source conservation and a linearized field equation from the MCIFT cell action instead of only declaring the tensor bridge structure.
```
