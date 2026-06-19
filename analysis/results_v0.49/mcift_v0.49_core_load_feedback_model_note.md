# MCIFT v0.49 Core Load Feedback Model Note

**Status:** speculative scaffold note.

## Correction implemented

The hidden branch is not only an energy-budget output. It also changes the rotating core through a separate local load.

## Visible branch

```text
E_visible_pool -> face/vortex visible channels
```

## Hidden branch

```text
E_hidden_sink -> separate bound local load
```

## Core-load rule

```text
G_visible = E_visible_pool
G_hidden = C_sink * E_hidden_sink
G_rot = xi_rot * E_rotation_bound
G_load = G_visible + G_hidden + G_rot
```

## Feedback rule

```text
capacity_after_feedback = capacity_before_feedback + confinement_gain
core_load_after_feedback = core_load_before_feedback + pressure_penalty
core_pressure_after_feedback = core_load_after_feedback / capacity_after_feedback
```

## v0.49 result

```text
G_visible = 0.605407
G_load = 0.874502
load_strength_vs_visible = 1.444487
core_pressure_after_feedback = 0.717440
```

The hidden branch therefore strengthens the rotating core load by 44.45% relative to visible-only load in this scaffold run, while the feedback rule keeps the core below capacity.
