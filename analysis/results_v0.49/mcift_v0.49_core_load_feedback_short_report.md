# MCIFT v0.49 Core Load Feedback Short Report

**Status:** speculative MCIFT scaffold result.

## Purpose

v0.49 keeps the visible branch separate from the hidden branch, then feeds the hidden branch back as local rotating-core load.

## Rule

```text
G_visible = E_visible_pool
G_hidden = C_sink * E_hidden_sink
G_rot = xi_rot * E_rotation_bound
G_load = G_visible + G_hidden + G_rot
core_pressure_after_feedback = core_load_after_feedback / capacity_after_feedback
```

## Result

```text
verdict = PASS_CORE_LOAD_FEEDBACK
criteria_pass_count = 18/18
G_visible = 0.605407
G_hidden = 0.175419
G_rot = 0.093676
G_load = 0.874502
load_strength_vs_visible = 1.444487
hidden_fraction_of_load = 0.200593
rotation_fraction_of_load = 0.107119
capacity_before_feedback = 0.854501
capacity_after_feedback = 0.910654
core_pressure_before_feedback = 0.727761
core_pressure_after_feedback = 0.717440
```

## Visible branch

```text
bb_like = 0.581674
WZ_like = 0.244245
gg_like = 0.104854
tau_like = 0.064263
gamma_like = 0.001234
mumu_like = 0.001920
```
