# MCIFT v0.48 Visible/Dark Entanglement Split Report

**Status:** dark/sink branch separation after v0.47; speculative scaffold, not established physics.

## Purpose

v0.48 implements the correction that visible matter and dark/sink matter must be computed differently during entanglement. Visible matter is computed from face/vortex-coupled mass capture. Dark/sink matter is computed separately from density shadow, sink intake, hidden core retention, and rotation capture. The dark/sink branch is not added to the visible decay-like channels.

## Separate branch rules

```text
visible_capture_gate = face_visibility * vortex_capture_visibility
face_visibility = streamline_index * sphericity * (1 - 0.35 anisotropy)

sink_gate = sigmoid((sink_intake_index - streamline_index) / 0.12)
dark_capture_gate = sink_gate * [0.45 density_shadow + 0.35 hidden_core_retention + 0.20 rotation_capture]

E_dark_sink = E_event * 0.23 * dark_capture_gate
E_visible_pool = E_event - E_dark_sink - E_rotation - E_aero_bleed
```

## Strict result

```text
verdict = PASS_VISIBLE_DARK_SPLIT
criteria_pass_count = 15/15
face_visibility = 0.505352
vortex_capture_visibility = 0.768638
visible_capture_gate = 0.388433
density_shadow = 0.448632
hidden_core_retention = 0.702703
rotation_capture = 0.403382
sink_gate = 0.906765
dark_capture_gate = 0.479231
E_event = 0.933617
E_dark_sink = 0.102906
E_visible_pool = 0.605407
E_rotation_bound = 0.131844
E_radiation_thermal = 0.050657
core_pressure_after_dark_split = 0.727761
```

## Energy budget fractions

```text
visible_face_vortex = 0.648453
dark_sink_hidden = 0.110223
rotation_bound = 0.141219
radiation_thermal = 0.054259
aero_shell_bleed_nonthermal = 0.045846
```

## Visible branch channel split

```text
bb_like = 0.580984
WZ_like = 0.244118
gg_like = 0.107516
tau_like = 0.064210
gamma_like = 0.001302
mumu_like = 0.001870
```

## Criteria

```text
visible_branch_computed_from_face_vortex = True
dark_branch_computed_separately = True
dark_sink_not_added_to_visible_channels = True
dark_sink_positive = True
visible_pool_positive = True
budget_normalizes = True
core_pressure_below_capacity_after_dark_split = True
dark_fraction_nontrivial = True
visible_fraction_largest = True
rotation_retained = True
radiation_not_dominant = True
bb_like_largest_visible = True
WZ_visible_not_dominant = True
gg_visible_not_dominant = True
gamma_mumu_visible_suppressed = True
```

## Interpretation

```text
The dark/sink branch must be separated before visible channel projection. When this is done, the visible branch remains the face/vortex channel split while the hidden branch becomes a non-radiating sink component tied to density shadow and sink intake. In this toy run the separate dark/sink computation remains stable and does not spoil the v0.47 visible hierarchy.
```

## Limitation

```text
This is a toy split between visible-like and dark/sink-like energy, not a measured dark matter model and not detector-level collider physics.
```
