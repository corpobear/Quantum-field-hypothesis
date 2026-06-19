# MCIFT v0.84 Dynamic Lattice Test

**Status:** speculative dynamic lattice scaffold.

## Purpose

v0.84 repeats the v0.83 source test across time.

```text
source = visible projection + hidden/information projection
```

## Setup

```text
cell_count = 8
time_steps = 16
boundary = periodic
```

## Result

```text
visible local max = 0.024000
visible global max = 0.000000
combined local max = 0.000000
combined global max = 0.000000
combined L1 all steps = 0.000000
```

## Meaning

Visible-only balance can look closed globally while still failing locally. The combined source closes local and global residuals at every tested step.

## Verdict

```text
DYNAMIC_LATTICE_CONSERVATION_MIXED
```

## Next

v0.85 should make the exchange rule depend on evolving cell variables instead of a prescribed balanced exchange.
