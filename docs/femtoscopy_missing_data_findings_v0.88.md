# Femtoscopy Missing Data Findings — v0.88

**Status:** honesty-first data audit.

## Summary

v0.88 attempted to move from representative femtoscopy bins to all available published bins.

The result is blocked because the complete machine-readable numeric tables are not yet available inside the repository.

Without those tables, MCIFT cannot honestly claim a full all-bin prediction or validation for femtoscopy radii.

## What is known

```text
pp target: 72 fitted correlation functions
p-Pb target: 26 radii in each direction
p-Pb total: 78 radius values across R_out, R_side, and R_long
```

These targets are recorded in:

```text
analysis/results_v0.88/v088_full_table_inventory.csv
analysis/results_v0.88/v088_status.csv
models/mcift_v0.88_full_table_attempt_note.md
```

## What is missing

For a valid all-bin test, the repository needs the numeric tables for each published bin:

```text
system
energy
multiplicity bin
pair kT bin
R_out
R_side
R_long
lambda
statistical uncertainty
systematic uncertainty
source/provenance for each point
```

## What cannot be claimed yet

```text
full HEPData validation: no
all-bin residual table: no
full femtoscopy prediction: no
stable-particle entanglement: no
```

## What remains valid

```text
v0.86 trend-level cross-check: preserved
v0.87 representative-bin numeric scaffold: preserved
v0.88 all-bin attempt: blocked by missing numeric tables
```

## Next required step

Find and ingest the official HEPData/Durham/CERN numeric tables, or manually transcribe the published data with clear provenance for every point.

Only after that can the repo compute full all-bin residuals honestly.
