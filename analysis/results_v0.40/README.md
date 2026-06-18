# v0.40 Explicit 3D Spherical Leakage Results

**Status:** speculative toy/scaffold result set; not established physics.

This folder records the v0.40 explicit 3D spherical leakage collision test.

## Committed result files

```text
mcift_v0.40_explicit_3d_spherical_leakage_report.md
mcift_v0.40_explicit_3d_spherical_leakage_metrics.csv
mcift_v0.40_explicit_3d_spherical_leakage_channels.csv
```

## Local generated artifacts

The full local output bundle also contains time-history CSVs and PNG plots:

```text
mcift_v0.40_explicit_3d_spherical_leakage_history.csv
mcift_v0.40_explicit_3d_shell_snapshots.csv
mcift_v0.40_explicit_3d_center_shell.png
mcift_v0.40_explicit_3d_channels.png
mcift_v0.40_explicit_3d_shell_slices.png
```

These are included in the downloadable output bundle produced by the run.

## Headline result

```text
verdict = PASS-LIKE
criteria_pass_count = 11/11
max_center_drift_abs_cells = 0.000000
weighted_shell_peak_radius_cells = 3.500000
weighted_shell_halfmax_width_bins = 2.029847
weighted_sphericity = 0.782404
weighted_shape_anisotropy = 0.217596
```

## Channel result

```text
bb_like     = 0.783474  target ~ 0.582000
WZ_like     = 0.120174  target ~ 0.240000
gg_like     = 0.056984  target ~ 0.086000
tau_like    = 0.038445  target ~ 0.063000
gamma_like  = 0.000242  target ~ 0.002300
mumu_like   = 0.000681  target ~ 0.000220
```

## Interpretation

The explicit 3D geometry passes the shell/stability criteria, but the shape-derived channel hierarchy is not yet collider-good: compact mass retention is too high and coherent WZ-like shell leakage is too low against rough Higgs hierarchy targets.

## Next target

```text
v0.41:
derive kappa coupling modifiers from explicit 3D shell geometry and compute partial widths, total width, branching fractions, and signal strengths.
```
