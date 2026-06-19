# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, cosmology, and weak-field gravity scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.84 dynamic lattice conservation test

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Start here

```text
docs/mcift_findings_v0.1_to_v0.80.md    consolidated project findings history
docs/documentation_gap_audit.md          missing/stale documentation audit
CURRENT_STATUS.md                        current repo status
models/mcift_v0.84_dynamic_lattice_note.md
analysis/results_v0.84/v084_metrics.csv
analysis/results_v0.84/v084_checks.csv
```

---

## Current focus

The main branch now tests Option C source bookkeeping across time on a periodic cell lattice:

```text
source = visible projection + hidden/information projection
```

Current verdict:

```text
v0.84 = DYNAMIC_LATTICE_CONSERVATION_MIXED
```

---

## v0.84 result

```text
cell_count = 8
time_steps = 16
boundary = periodic
visible local max = 0.024000
visible global max = 0.000000
combined local max = 0.000000
combined global max = 0.000000
combined L1 all steps = 0.000000
```

---

## Strict status

```text
passes: combined source closes local and global residuals across all tested steps
fails as expected: visible-only source does not close locally through time
missing: observational test and non-toy exchange rule
```

---

## Next version target

```text
v0.85 should make the exchange rule depend on evolving cell variables instead of a prescribed balanced exchange.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
