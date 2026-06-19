# MCIFT v0.49 Hidden-Load Rotating-Core Feedback Report

**Status:** speculative toy/scaffold test, not established physics.

## Purpose

v0.49 retests v0.48 with hidden branch feedback. The hidden branch is still separate from visible face/vortex matter, but now it contributes an additional bound load to the rotating dense core. Bound rotation is included as part of the effective rotating-core load.

## Rule summary

```text
G_visible = E_visible_pool
C_hidden = 1 + 0.45 density_shadow + 0.35 sink_gate + 0.20 hidden_core_retention
G_hidden = C_hidden E_hidden_sink
G_rotation = C_rot E_rotation_bound
G_total = G_visible + G_hidden + G_rotation
```

Core feedback:

```text
R_feedback = R_dense * (1 - radius_tightening_fraction)
I_feedback = (2/5) M_eff R_feedback^2
omega_feedback = L_discarded / I_feedback
Coh_feedback = Coh_aero + hidden_load_gain
pressure_feedback = (core_numerator + hidden_load_pressure) / Coh_feedback
```

## Strict result

```text
verdict = PASS_DARK_GRAVITY_FEEDBACK
criteria_pass_count = 17/17
G_visible_only = 0.605407
G_visible_plus_hidden = 0.776210
G_total_visible_hidden_rotation = 0.884322
gravity_gain_visible_plus_hidden = 1.282129
gravity_gain_total = 1.460706
C_sink = 1.659793
dark_gravity_fraction = 0.193145
R_dense_before_dark_gravity = 6.198812
R_core_after_dark_gravity = 6.088726
I_before_dark_gravity = 47.549827
I_after_dark_gravity = 48.206567
omega_before_dark_gravity = 0.072027
omega_after_dark_gravity = 0.071017
coherence_capacity_before_dark_gravity = 0.854501
coherence_capacity_after_dark_gravity = 0.882377
core_pressure_before_dark_gravity = 0.727761
core_pressure_after_dark_gravity = 0.733320
```

## Budget fractions after feedback

```text
visible_face_vortex = 0.642328
hidden_sink_gravity = 0.116817
rotation_bound = 0.140673
radiation_thermal = 0.053892
shell_bleed = 0.046289
```

## Visible channel branch

```text
bb_like = 0.586240
WZ_like = 0.240486
gg_like = 0.106102
tau_like = 0.064482
gamma_like = 0.001028
mumu_like = 0.001662
channel_l1_distance_to_rough_targets = 0.029024
```

## Criteria

```text
hidden_sink_gravity_computed_separately = True
hidden_sink_adds_to_gravity_not_visible_channels = True
visible_only_gravity_load_recorded = True
visible_dark_gravity_load_above_visible_only = True
rotation_energy_contributes_to_gravity = True
effective_gravity_load_above_visible_only = True
rotating_core_radius_tightens = True
moment_of_inertia_updated = True
omega_final_changes = True
core_pressure_below_capacity_after_dark_gravity = True
dark_gravity_fraction_nontrivial = True
visible_fraction_largest = True
radiation_not_dominant = True
bb_like_largest_visible = True
WZ_visible_not_dominant = True
gg_visible_not_dominant = True
channel_l1_below_0p08 = True
```

## Interpretation

The hidden branch now changes the rotating core instead of only appearing in the event budget. Relative to visible-only load, the hidden branch raises the load by about 28.2%. Including bound rotation raises the effective rotating-core load by about 46.1%. The core tightens slightly, final angular speed drops slightly, and containment remains stable in this scaffold.

## Limitation

This remains a toy field calculation, not a measured dark-matter model and not collider evidence.
