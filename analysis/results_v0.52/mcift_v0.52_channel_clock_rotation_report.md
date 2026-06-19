# MCIFT v0.52 Channel-Specific Clock / Rotation Bridge Report

**Status:** internal-clock/rotation bridge calculation; speculative MCIFT scaffold, not established physics.

## Purpose

v0.51 used one common core-clock factor, so it changed only the total width / rate scale. v0.52 applies the correction that if time dilation changes the observed rotation speed, channel formation geometry changes too. Different channels form at different core/shell depths and have different spin sensitivities, so they get different formation-time factors.

## Rotation-clock rule

```text
omega_lab = tau_core_to_lab * omega_proper
rotation_speed_shift = 1 - tau_core_to_lab
```

For each channel:

```text
tau_depth,i = 1 - (1 - tau_core_to_lab) depth_i
tau_channel,i = tau_depth,i * (1 + spin_sensitivity_i * rotation_speed_shift)
Gamma_i,lab = tau_channel,i Gamma_i,proper
```

A universal compensation can restore the total width scale:

```text
proper_width_scale = Gamma_SM_total / sum_i Gamma_i,lab
Gamma_i,comp = proper_width_scale * Gamma_i,lab
BR_i,comp = Gamma_i,comp / sum_j Gamma_j,comp
```

## Strict result

```text
verdict = PASS_CHANNEL_CLOCK_ROTATION_BRIDGE
tau_core_to_lab = 0.868528
omega_proper = 0.072027
omega_lab = 0.062559
rotation_speed_shift_pct = 13.147198
Gamma_lab_channel_clock_MeV = 3.965184
Gamma_lab_channel_clock_delta_pct = -2.575329
proper_width_scale_needed = 1.026434
universal_kappa_time_needed = 1.013131
max_abs_BR_delta_pct_after_channel_clock = 3.313884
max_abs_signal_strength_delta_pct_after_channel_clock = 5.205441
```

## Branching ratios after channel-specific clock

```text
channel  BR_lab_compensated  BR_delta_pct_compensated
bb       0.577371            -0.860789
WW       0.217607             1.830883
gg       0.082734             1.144792
tau      0.062453            -0.390957
cc       0.028808            -0.660675
ZZ       0.026883             1.830883
gamma    0.002345             3.313884
Zgamma   0.001585             2.909042
mumu     0.000215            -1.130329
```

## Interpretation

The correction works inside the scaffold: a common clock factor leaves branching ratios unchanged, but a time-dilated rotation speed creates channel-specific formation clocks. That changes partial widths and branching ratios. In this bridge the branching-ratio shifts remain bounded at about 3.31 percent, while representative signal-strength shifts reach about 5.21 percent.

## Limitation

This is still an internal-clock bridge, not a full general-relativistic or detector-level collider calculation. The channel depth and spin-sensitivity map is a scaffold rule. v0.53 should derive those depth/sensitivity values directly from the 3D vector phase field.
