# MCIFT v0.52 Channel-Clock / Rotation Bridge

**Status:** internal-clock bridge layer; speculative MCIFT scaffold, not established physics.

## Purpose

v0.51 used one common clock factor, so total widths changed but branching ratios did not. v0.52 adds the correction that a slowed core clock also changes the observed rotation speed. Since different channels form at different core/shell depths and have different spin sensitivity, their formation clocks can differ.

## Rotation-speed correction

```text
omega_lab = tau_core_to_lab * omega_proper
rotation_speed_shift = 1 - tau_core_to_lab
```

## Channel-clock rule

```text
tau_depth,i = 1 - (1 - tau_core_to_lab) depth_i
tau_channel,i = tau_depth,i * (1 + s_i * rotation_speed_shift)
Gamma_i,lab = tau_channel,i Gamma_i,proper
```

where `depth_i` is the schematic formation depth and `s_i` is the spin-sensitivity sign/weight.

## Result

```text
tau_core_to_lab = 0.868528
omega_proper = 0.072027
omega_lab = 0.062559
rotation_speed_shift_pct = 13.147198
Gamma_lab_channel_clock = 3.965184 MeV
proper_width_scale_needed = 1.026434
universal_kappa_time_needed = 1.013131
max_abs_BR_delta_pct_after_channel_clock = 3.313884
max_abs_signal_strength_delta_pct_after_channel_clock = 5.205441
```

## Meaning

A universal clock factor cannot change branching ratios. A channel-specific formation clock can change branching ratios because each partial width receives a different lab-time factor.

## Next target

v0.53 should derive `depth_i` and `s_i` from the full 3D vector phase field instead of assigning them by channel category.
