# MCIFT v0.44 Explicit 3D Rhythm-Lock Merge Test Report

**Status:** explicit 3D rhythm-lock stabilizer test after v0.43; speculative scaffold, not established physics.

## Purpose

v0.44 carries the rhythm-lock rule into an explicit 3D collision field. Heartbeat amplitude, phase, and frequency are not compact assigned inputs; they are extracted from the 3D complex field projection in the overlap/contact region before merge.

## 3D heartbeat extraction

```text
z_A(t) = sum_x W_A(x) exp[i phi_A(x,t)]
z_B(t) = sum_x W_B(x) exp[i phi_B(x,t)]
A_A = mean |z_A(t)|
A_B = mean |z_B(t)|
phi_A = arg z_A(t_merge)
phi_B = arg z_B(t_merge)
omega_A = slope unwrap(arg z_A(t))
omega_B = slope unwrap(arg z_B(t))
```

Rhythm-lock then follows:

```text
R_lock = phase_lock * frequency_lock * amplitude_match
E_core_seed = eta_core * R_lock * E_raw
E_beat_seed = (1 - R_lock) * E_raw
```

## Strict result

```text
verdict = FLOP_CORE_OVERLOCK
criteria_pass_count = 14/16
field_amplitude_A = 0.636285
field_amplitude_B = 0.636278
field_phase_A = 1.372184
field_phase_B = 1.072280
field_omega_A = 0.969237
field_omega_B = 1.035460
phase_lock = 0.977682
frequency_lock = 0.913374
amplitude_match = 1.000000
rhythm_lock = 0.892989
entanglement_score = 0.651470
entanglement_threshold = 0.280000
merged_mass = 2.000000
merged_radius = 7.559526
coherence_capacity = 0.640019
E_raw_vib_seed = 1.140500
E_core_seed_after_lock = 0.967532
E_beat_seed = 0.122046
core_pressure_0 = 1.511724
max_explosion_pressure = 1.522212
final_energy_over_peak = 0.356518
```

## Shape result

```text
weighted_shell_radius = 6.267193
weighted_shell_width = 1.281529
weighted_sphericity = 0.836267
weighted_anisotropy = 0.163733
core_fraction = 0.472421
inner_fraction = 0.366818
outer_fraction = 0.160761
```

## Channel fractions

```text
bb_like     = 0.573037  target ~ 0.582000
WZ_like     = 0.246305  target ~ 0.240000
gg_like     = 0.115613  target ~ 0.086000
tau_like    = 0.063336  target ~ 0.063000
gamma_like  = 0.000704  target ~ 0.002300
mumu_like   = 0.001005  target ~ 0.000220
```

## Criteria

```text
field_heartbeat_derived = True
entanglement_score_above_threshold = True
rhythm_lock_computed_positive = True
single_merged_heartbeat_forms = True
mass_added_correctly = True
core_vibration_below_capacity = False
beat_leakage_positive = True
final_energy_not_runaway = True
center_stable = True
shell_forms_after_merge = False
sphericity_remains_reasonable = True
bb_like_largest = True
WZ_like_visible_not_dominant = True
gg_like_visible_not_dominant = True
gamma_mumu_suppressed = True
channel_l1_below_0p20 = True
```

## Interpretation

```text
The explicit 3D rhythm-lock test removes the compact-input weakness of v0.43 by deriving heartbeat amplitude, phase, and frequency from the 3D field. But the result is stricter and fails: the derived heartbeats lock too strongly, so too much energy remains in the merged core heartbeat. Core pressure rises above coherence capacity and the shell does not detach beyond the merged radius. This is a useful flop: v0.43 stabilizes with compact rhythms, but direct 3D-derived rhythm-lock needs an adaptive bleed or coherence-capacity rule.
```

## Limitation

```text
This is not a detector-level CERN simulation. The channel fractions remain rough hierarchy diagnostics, not measured collider likelihoods.
```

## Next target

```text
v0.45 target:
derive coupling modifiers kappa_b, kappa_W, kappa_Z, kappa_g, kappa_tau, kappa_gamma, and kappa_mu from the explicit 3D rhythm-lock field, then compute partial widths and signal strengths.
```
