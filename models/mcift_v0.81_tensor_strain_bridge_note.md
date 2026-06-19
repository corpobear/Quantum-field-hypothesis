# MCIFT v0.81 Tensor-Strain Bridge

**Status:** speculative linearized tensor bridge; not full GR.

## Purpose

v0.81 extends the v0.80 scalar weak-field metric into a linearized tensor scaffold.

## Tensor form

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

## Tests

```text
v0.80 weak-field regression: preserved
PPN gamma: 1
light bending: preserved
Mercury precession: preserved
Shapiro coefficient: preserved
h_0i shift mode: structurally nonzero
frame-dragging coefficient: normalized to 1
TT wave modes: plus and cross
GW speed: c by bridge equation
```

## Verdict

```text
TENSOR_STRAIN_EXTENSION_PRESERVES_WEAK_FIELD_LIMIT_ADDS_SHIFT_AND_TT_MODES_FULL_GR_STILL_NOT_DERIVED
```

## Strict limitation

```text
full nonlinear field equations: not derived
source conservation: not derived
contracted Bianchi identity: not derived
observational frame-dragging fit: not done
observational gravitational-wave waveform fit: not done
```

## Next target

v0.82 should derive source conservation and a linearized field equation from the MCIFT cell action instead of only declaring the tensor bridge structure.
