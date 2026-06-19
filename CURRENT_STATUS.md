# Current MCIFT Status: v0.49 Core Load Feedback Test

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current strict feedback test:** v0.49 core load feedback test.  
**Previous split test:** v0.48 visible/hidden branch split.  
**Previous shape-flow test:** v0.47 aero drill-sink stabilization test.

---

## One-sentence status

```text
MCIFT v0.49 feeds the separately computed hidden branch back into the rotating core as a local load. The visible branch remains separate. The strict verdict is PASS_CORE_LOAD_FEEDBACK: 18/18 criteria passed. The effective core load is 1.444487 times the visible-only load, but the feedback also raises coherence support, keeping core pressure below capacity.
```

---

## v0.49 strict result

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

## Analysis result files

```text
analysis/results_v0.49/mcift_v0.49_core_load_feedback_metrics.csv
analysis/results_v0.49/mcift_v0.49_budget.csv
analysis/results_v0.49/mcift_v0.49_criteria.csv
```

The full report, model note, plots, channels, and history are in the local output bundle because some text-heavy repo uploads were blocked by the connector filter.

---

## Safe wording

```text
v0.49 is a toy core-load feedback result. It treats the hidden branch as a separate local load on the rotating core and keeps it out of the visible channel split. It is not a measured dark-matter model, general-relativistic simulation, or collider evidence.
```
