# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.49 core load feedback test

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now tests a dense entanglement collision with separate visible and hidden branches:

```text
two particles attempt to entangle
merged object becomes denser than simple mass addition
visible branch comes from face/vortex capture
hidden branch is computed separately
hidden branch feeds back as local rotating-core load
rotation and shape-flow support coherence
```

Current verdict:

```text
v0.49 core load feedback test = PASS_CORE_LOAD_FEEDBACK, 18/18 criteria
```

This is a scaffold pass, not empirical confirmation. The useful point is that hidden branch feedback now changes the rotating-core load while remaining outside the visible channel split.

---

## v0.49 result

```text
E_visible_pool = 0.605407
E_hidden_sink = 0.102906
E_rotation_bound = 0.131844
G_visible = 0.605407
G_hidden = 0.175419
G_rot = 0.093676
G_load = 0.874502
load_strength_vs_visible = 1.444487
capacity_before_feedback = 0.854501
capacity_after_feedback = 0.910654
core_pressure_before_feedback = 0.727761
core_pressure_after_feedback = 0.717440
```

Budget fractions:

```text
visible = 0.648453
hidden = 0.110223
rotation = 0.141219
radiation = 0.054259
shell = 0.045846
```

Visible branch:

```text
bb_like = 0.581674
WZ_like = 0.244245
gg_like = 0.104854
tau_like = 0.064263
gamma_like = 0.001234
mumu_like = 0.001920
```

---

## Key math

```text
G_visible = E_visible_pool
G_hidden = C_sink * E_hidden_sink
G_rot = xi_rot * E_rotation_bound
G_load = G_visible + G_hidden + G_rot
core_pressure_after_feedback = core_load_after_feedback / capacity_after_feedback
```

The visible branch is still computed separately from the hidden branch. The hidden branch contributes load/support feedback, not visible decay-like fractions.

---

## Analysis result files

```text
CURRENT_STATUS.md
models/dark_gravity_entanglement_feedback_v0.49.md
analysis/results_v0.49/mcift_v0.49_core_load_feedback_short_report.md
analysis/results_v0.49/mcift_v0.49_core_load_feedback_metrics.csv
analysis/results_v0.49/mcift_v0.49_budget.csv
analysis/results_v0.49/mcift_v0.49_source_loads.csv
analysis/results_v0.49/mcift_v0.49_visible_branch_channels.md
analysis/results_v0.49/mcift_v0.49_criteria.csv
```

Some longer report and plot artifacts are kept in local output bundles because the connector may block text-heavy uploads.

---

## Important limitation

```text
v0.49 is a toy core-load feedback result. It is not a measured dark-matter model, general-relativistic simulation, detector-level collider simulation, or empirical confirmation.
```

---

## Research roadmap

Next required tests:

```text
1. Derive the feedback coefficients from the full 3D vector phase field.
2. Keep visible and hidden branches separate before channel projection.
3. Retest without tuning visible channels directly.
4. Only after stability should the model derive coupling modifiers and partial widths.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
