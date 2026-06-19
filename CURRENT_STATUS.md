# Current MCIFT Status: v0.80 Weak-Field GR Bridge

**Status:** speculative weak-field bridge; not full GR.  
**Current layer:** v0.80 weak-field metric bridge.  
**Previous layer:** v0.73 cell-action spatial lapse cosmology retest.

---

## One-sentence status

```text
MCIFT v0.80 combines time-lapse and spatial-lapse into an isotropic weak-field metric. It reproduces the classic weak-field checks by construction, but it does not derive the full field equations, tensor modes, frame dragging, or gravitational waves.
```

---

## v0.80 verdict

```text
WEAK_FIELD_GR_BRIDGE_PASSES_CLASSIC_LIMITS_FULL_GR_NOT_DERIVED
```

---

## Metric bridge

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

---

## Test result

```text
PPN gamma = 1.000000
Newtonian inverse-square limit = recovered
gravitational redshift coefficient = 1.000000
solar-limb light bending = 1.751243 arcsec
Mercury perihelion precession = 42.981975 arcsec / century
Shapiro delay coefficient = 2.000000
```

---

## Strict status

```text
passes: Newtonian limit, redshift coefficient, PPN gamma, light bending, Mercury precession, Shapiro delay coefficient
missing: full field equations, anisotropic metric tensor, frame dragging, gravitational waves, cosmological field equation from action
```

---

## Main files on master

```text
models/mcift_v0.80_weak_field_bridge_note.md
analysis/results_v0.80/v080_weak_field_gr_bridge_metrics.csv
analysis/results_v0.80/v080_weak_field_gr_bridge_tests.csv
CURRENT_STATUS.md
```

---

## Next target

```text
v0.81 should move from one scalar bridge field to tensor strain:
g_mu_nu = eta_mu_nu + h_mu_nu
Then test frame dragging, gravitational waves, and conservation constraints.
```
