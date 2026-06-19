# MCIFT v0.82 Source Test

**Status:** speculative source-bookkeeping scaffold; not full GR.

## Implemented choice

```text
Option C: combined source
```

The source is treated as:

```text
visible projection + hidden/information projection
```

## Toy result

```text
visible-only residual = 0.030000
combined residual = 0.000000
exchange balance residual = 0.000000
```

## Meaning

The visible-only budget does not close. The combined budget closes in this toy exchange test.

## Verdict

```text
COMBINED_SOURCE_TOY_CONSERVATION_MIXED
```

## Limits

```text
full nonlinear GR: not derived
covariant conservation: not derived
observational test: not performed
```

## Next

v0.83 should run the same source test on a cell lattice instead of a compact toy exchange.
