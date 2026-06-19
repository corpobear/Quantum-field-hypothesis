# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, cosmology, and weak-field gravity scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.83 lattice source conservation test

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Start here

```text
docs/mcift_findings_v0.1_to_v0.80.md    consolidated project findings history
docs/documentation_gap_audit.md          missing/stale documentation audit
CURRENT_STATUS.md                        current repo status
models/mcift_v0.83_lattice_source_note.md
analysis/results_v0.83/v083_lattice_metrics.csv
analysis/results_v0.83/v083_lattice_tests.csv
```

---

## Current focus

The main branch now tests Option C source bookkeeping on a periodic cell lattice:

```text
source = visible projection + hidden/information projection
```

Current verdict:

```text
v0.83 = LATTICE_COMBINED_SOURCE_CONSERVATION_PASSES_TOY_LOCAL_AND_GLOBAL_CHECKS_FULL_GR_STILL_NOT_DERIVED
```

---

## v0.83 result

```text
visible-only local residual = 0.022500
visible-only global residual = 0.000000
combined local residual = 0.000000
combined global residual = 0.000000
cellwise exchange balance residual = 0.000000
```

---

## Strict status

```text
passes: combined source closes local and global toy lattice residuals, preserves v0.82 compact result and v0.81 tensor bridge
fails as expected: visible-only source does not close locally
missing: full nonlinear GR, covariant conservation, observational test
```

---

## Next version target

```text
v0.84 should make the lattice dynamic: update cells over time and test conservation across multiple time steps, not just one static lattice residual.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
