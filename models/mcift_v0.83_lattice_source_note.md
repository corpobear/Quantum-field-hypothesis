# MCIFT v0.83 Lattice Source Conservation Test

**Status:** speculative lattice conservation scaffold; not full GR.

## Purpose

v0.83 tests the v0.82 Option C source on a periodic cell lattice.

```text
source = visible projection + hidden/information projection
```

## Result

```text
cell_count = 8
boundary = periodic
visible-only local residual = 0.022500
visible-only global residual = 0.000000
combined local residual = 0.000000
combined global residual = 0.000000
```

## Meaning

Visible-only source can balance globally while still failing local conservation. The combined source closes both local and global residuals in this toy lattice.

## Verdict

```text
LATTICE_COMBINED_SOURCE_CONSERVATION_PASSES_TOY_LOCAL_AND_GLOBAL_CHECKS_FULL_GR_STILL_NOT_DERIVED
```

## Limits

```text
full nonlinear GR: not derived
covariant conservation: not derived
observational test: not performed
```

## Next

v0.84 should make the lattice dynamic: update cells over time and test conservation across multiple time steps, not just one static lattice residual.
