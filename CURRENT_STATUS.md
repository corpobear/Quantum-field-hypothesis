# Current MCIFT Status: v0.82 Combined Source Test

**Status:** speculative source-bookkeeping scaffold; not full GR.  
**Current layer:** v0.82 combined source test.  
**Previous layer:** v0.81 tensor-strain bridge.

---

## One-sentence status

```text
MCIFT v0.82 implements Option C: the gravitational source is visible projection plus hidden/information projection. In the compact toy exchange test, visible-only conservation fails while the combined source closes the residual. This is source bookkeeping progress, not full covariant conservation or full GR.
```

---

## v0.82 verdict

```text
COMBINED_SOURCE_TOY_CONSERVATION_MIXED
```

---

## Source choice

```text
source = visible projection + hidden/information projection
```

---

## Test result

```text
visible-only residual = 0.030000
hidden projection residual = 0.030000
combined residual Linf = 0.000000
combined residual L1 = 0.000000
exchange balance residual = 0.000000
```

---

## Strict status

```text
passes: combined source closes the toy conservation residual and preserves v0.81 tensor bridge
fails as expected: visible-only source does not close
missing: full nonlinear GR, covariant conservation, observational test
```

---

## Main files on master

```text
models/mcift_v0.82_source_note.md
analysis/results_v0.82/v082_metrics.csv
analysis/results_v0.82/v082_tests.csv
README.md
CURRENT_STATUS.md
```

---

## Next target

```text
v0.83 should run the same combined-source conservation test on a cell lattice instead of a compact toy exchange.
```
