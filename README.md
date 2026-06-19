# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, cosmology, and weak-field gravity scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.80 weak-field GR bridge

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

The main branch now tests whether MCIFT time-lapse and spatial-lapse can form a weak-field metric bridge:

```text
v0.73: cell-action spatial ruler correction
v0.80: weak-field metric bridge from time and space strain
```

Current verdict:

```text
v0.80 = WEAK_FIELD_GR_BRIDGE_PASSES_CLASSIC_LIMITS_FULL_GR_NOT_DERIVED
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

## v0.80 test result

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

## Main documents

```text
models/mcift_v0.80_weak_field_bridge_note.md
analysis/results_v0.80/v080_weak_field_gr_bridge_metrics.csv
analysis/results_v0.80/v080_weak_field_gr_bridge_tests.csv
CURRENT_STATUS.md
README.md
```

---

## Next version target

```text
v0.81 should move from one scalar bridge field to tensor strain:
g_mu_nu = eta_mu_nu + h_mu_nu
Then test frame dragging, gravitational waves, and conservation constraints.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
