# Current MCIFT Status: v0.84 Dynamic Lattice Test

**Status:** speculative source-bookkeeping scaffold.  
**Current layer:** v0.84 dynamic lattice test.  
**Previous layer:** v0.83 static lattice test.

## Verdict

```text
DYNAMIC_LATTICE_CONSERVATION_MIXED
```

## Result

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

## Status

```text
passes: combined source closes local and global residuals across all tested steps
fails as expected: visible-only source does not close locally through time
missing: observational test and non-toy exchange rule
```

## Files

```text
models/mcift_v0.84_dynamic_lattice_note.md
analysis/results_v0.84/v084_metrics.csv
analysis/results_v0.84/v084_checks.csv
README.md
CURRENT_STATUS.md
```

## Next

```text
v0.85: derive the exchange rule from evolving cell variables
```
