# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, cosmology, and weak-field gravity scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.81 tensor-strain bridge

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Start here

```text
docs/mcift_findings_v0.1_to_v0.80.md    consolidated project findings history
docs/documentation_gap_audit.md          missing/stale documentation audit
CURRENT_STATUS.md                        current repo status
models/mcift_v0.81_tensor_strain_bridge_note.md
analysis/results_v0.81/v081_tensor_strain_metrics.csv
analysis/results_v0.81/v081_tensor_strain_tests.csv
```

---

## Current focus

The main branch now extends the v0.80 scalar weak-field metric bridge into a linearized tensor-strain scaffold:

```text
v0.80: scalar weak-field bridge
v0.81: tensor strain h_mu_nu with shift and TT modes
```

Current verdict:

```text
v0.81 = TENSOR_STRAIN_EXTENSION_PRESERVES_WEAK_FIELD_LIMIT_ADDS_SHIFT_AND_TT_MODES_FULL_GR_STILL_NOT_DERIVED
```

---

## Tensor bridge

```text
g_mu_nu = eta_mu_nu + h_mu_nu
h_00 = -2 psi
h_ij = 2 psi delta_ij + hTT_ij
h_0i = beta_i
```

Meaning:

```text
h_00: time strain
h_ij: spatial tensor strain
h_0i: shift / frame-dragging mode
hTT_ij: transverse-traceless wave mode
```

---

## v0.81 test result

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

## Documentation status

A consolidated history exists for v0.1 through v0.80. v0.81 is documented in its own model note and result files; the next full history update should extend the consolidated history through v0.81.

---

## Next version target

```text
v0.82 should derive source conservation and a linearized field equation from the MCIFT cell action instead of only declaring the tensor bridge structure.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
