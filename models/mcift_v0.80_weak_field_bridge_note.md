# MCIFT v0.80 Weak-Field Bridge

**Status:** speculative weak-field bridge; not full GR.

## Purpose

v0.80 tests whether MCIFT time-lapse and spatial-lapse can be combined into a weak-field spacetime metric.

## Bridge metric

```text
psi = GM / (c^2 r)
ds^2 = -exp(-2 psi) c^2 dt^2 + exp(2 psi) (dx^2 + dy^2 + dz^2)
```

Weak field:

```text
g_00 ~= -(1 - 2 psi)
g_ij ~= (1 + 2 psi) delta_ij
PPN gamma = 1
```

## Test result

```text
Newtonian limit: pass
redshift coefficient: pass
light bending at solar limb: 1.751243 arcsec
Mercury precession: 42.981975 arcsec / century
Shapiro coefficient: 2.000000
```

## Strict limitation

```text
full field equations: not derived
frame dragging: not implemented
gravity waves: not implemented
anisotropic metric tensor: not implemented
cosmological field equation from action: not derived
```

## Verdict

```text
WEAK_FIELD_GR_BRIDGE_PASSES_CLASSIC_LIMITS_FULL_GR_NOT_DERIVED
```

## Next target

v0.81 should move from one scalar bridge field to a tensor strain field:

```text
g_mu_nu = eta_mu_nu + h_mu_nu
```

and test the missing tensor modes.
