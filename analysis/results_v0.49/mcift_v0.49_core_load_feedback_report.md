# MCIFT v0.49 Core Load Feedback Report

**Status:** speculative toy/scaffold result, not established physics.

## Purpose

v0.49 retests the visible/hidden split by feeding the hidden branch back into the rotating core as a separate local load. The visible branch remains separate and is not merged with the hidden branch before channel projection.

## Rule summary

```text
G_visible = E_visible_pool
G_hidden = C_sink * E_hidden_sink
G_rot = xi_rot * E_rotation_bound
G_load = G_visible + G_hidden + G_rot
```

The added local load changes the rotating core by increasing confinement support and adding a smaller pressure penalty.

```text
capacity_after_feedback = capacity_before_feedback + confinement_gain
core_load_after_feedback = core_load_before_feedback + pressure_penalty
core_pressure_after_feedback = core_load_after_feedback / capacity_after_feedback
```

## Strict result

```text
verdict = PASS_CORE_LOAD_FEEDBACK
criteria_pass_count = 18/18
E_visible_pool = 0.605407
E_hidden_sink = 0.102906
E_rotation_bound = 0.131844
C_sink = 1.704656
xi_rot = 0.710507
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
shell_radius_after_feedback = 9.941601
outer_hidden_radius = 10.582795
```

## Budget fractions

```text
visible = 0.648453
hidden = 0.110223
rotation = 0.141219
radiation = 0.054259
shell = 0.045846
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

## Interpretation

The hidden branch now contributes to the local rotating-core load. The effective load is 1.444487 times the visible-only load. Because confinement support rises more than the added pressure penalty, core pressure remains below capacity. This is a scaffold pass, not a measured hidden-matter or collider result.
