# MCIFT v0.88 Full Femtoscopy Table Attempt

**Status:** full-table validation attempted; numeric tables not yet loaded.

## Purpose

The goal was to move from v0.87 representative bins to all available published femtoscopy bins.

## What was found

The pp paper states that all 72 correlation functions were fitted.

The p-Pb paper states that 26 radii were extracted in each direction, giving 78 radius values across R_out, R_side, and R_long.

## Result

```text
full numeric table loaded = false
full residual table built = false
v0.87 representative-bin scaffold preserved = true
```

## Why no full residual table yet

The parsed paper text exposes the bin counts and trends, but not the complete machine-readable radius table. A full residual table requires HEPData/Durham numeric tables or manual transcription from the published data tables/figures.

## Next

v0.89 should ingest the HEPData numeric tables or add a manually transcribed table with provenance for every bin.
