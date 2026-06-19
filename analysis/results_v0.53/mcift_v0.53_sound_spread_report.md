# MCIFT v0.53 Sound / Acoustic Spread Bridge Report

**Status:** internal acoustic-spread bridge; speculative MCIFT scaffold, not established physics.

## Purpose

v0.53 tests the correction that a dense rotating core can support a pressure/sound-like mode, and that this internal acoustic mode can influence the spread of the shell and the channel fractions.

In this scaffold, "sound" means an internal pressure/phonon-like wave in the dense field medium. It does not mean ordinary air sound.

## Acoustic rule

```text
c_sound = sqrt(Coh_feedback / (rho_ratio + G_load))
omega_sound = c_sound / R_shell
acoustic_resonance = exp[-((omega_lab - omega_sound)/(0.35 omega_sound))^2]
M_acoustic = v_core_lab / c_sound
```

A pressure-wave amplitude is computed from discarded vibration, clock slowdown, and acoustic Mach response:

```text
A_sound = 0.10 + 0.35 E_discarded/E_event + 0.08(1 - tau_core_to_lab) + 0.04 M_acoustic
```

## Strict result

```text
verdict = PASS_SOUND_SPREAD_BRIDGE
criteria_pass_count = 11/11
c_sound_proxy = 0.582034
omega_sound_proxy = 0.058545
omega_lab = 0.062558
acoustic_resonance = 0.962377
acoustic_mach = 0.666259
pressure_wave_amplitude = 0.207941
surface_ripple_index = 0.333447
radial_spread_factor = 1.094666
shell_radius_before_sound = 9.941601
shell_radius_after_sound = 10.882735
shell_width_before_sound = 2.640000
shell_width_after_sound = 3.088810
Gamma_lab_sound_raw_MeV = 3.964892
proper_width_scale_needed = 1.026510
universal_kappa_time_needed = 1.013168
max_abs_BR_delta_pct_after_sound = 4.913465
max_abs_signal_strength_delta_pct_after_sound = 7.790001
```

## Branching-ratio shifts after sound spread

```text
bb      -1.316439 %
WW      +2.741818 %
gg      +1.860716 %
tau     -0.523144 %
cc      -0.978220 %
ZZ      +2.741818 %
gamma   +4.913465 %
Zgamma  +4.238068 %
mumu    -1.538511 %
```

## Interpretation

The acoustic bridge changes the spatial spread and the channel distribution. Surface-ripple channels respond most strongly because sound waves couple naturally to shell/surface oscillation. Core-dominated channels are slightly compressed. This creates branching-ratio shifts beyond v0.52 while remaining bounded in this toy run.

## Limitation

This is not real acoustic propagation in air, not a full quantum field calculation, and not collider evidence. It is an internal MCIFT pressure-wave scaffold. v0.54 should derive the sound sensitivity map from the 3D field instead of assigning acoustic sensitivities by channel category.
