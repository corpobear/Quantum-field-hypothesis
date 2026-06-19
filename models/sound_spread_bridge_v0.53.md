# MCIFT v0.53 Sound / Acoustic Spread Bridge

**Status:** internal acoustic-spread bridge; speculative MCIFT scaffold, not established physics.

## Purpose

v0.53 tests whether a dense rotating core can support a pressure/sound-like mode, and whether that internal acoustic mode changes shell spread and channel fractions.

In this scaffold, sound means an internal pressure or phonon-like wave in the dense field medium. It does not mean ordinary air sound.

## Acoustic speed and resonance

```text
c_sound = sqrt(Coh_feedback / (rho_ratio + G_load))
omega_sound = c_sound / R_shell
acoustic_resonance = exp[-((omega_lab - omega_sound)/(0.35 omega_sound))^2]
M_acoustic = v_core_lab / c_sound
```

## Pressure-wave amplitude

```text
A_sound = 0.10 + 0.35 E_discarded/E_event + 0.08(1 - tau_core_to_lab) + 0.04 M_acoustic
```

## Spread rule

```text
radial_spread_factor = 1 + 0.24 A_sound resonance + 0.07 M_acoustic
shell_radius_sound = shell_radius_before * radial_spread_factor
```

## Channel-width rule

```text
tau_sound,i = 1 + s_sound,i A_sound resonance (1 + 0.25 M_acoustic)
Gamma_i,lab = tau_channel,i tau_sound,i Gamma_i,proper
```

## Meaning

The sound mode changes the spatial spread and creates channel-dependent partial-width shifts. Core-dominated channels are slightly compressed. Shell and surface-ripple channels spread more strongly.

## Next target

v0.54 should derive the acoustic sensitivity map directly from the 3D field rather than assigning it by channel category.
