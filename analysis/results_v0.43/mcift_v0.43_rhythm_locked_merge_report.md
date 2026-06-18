# MCIFT v0.43 Rhythm-Locked Entangled Merge Test Report

**Status:** strict PASS/FLOP rhythm-lock stabilizer test after v0.42; speculative scaffold, not established physics.

## Purpose

v0.43 tests the proposed correction to the v0.42 failure: two particles first compare internal rhythms, like heartbeats. Only the synchronized part becomes the merged core heartbeat. The mismatch becomes outward beat/leakage instead of being trapped as raw inner vibration.

## Rhythm merge rule

```text
h_A(t) = A_A cos(omega_A t + phi_A)
h_B(t) = A_B cos(omega_B t + phi_B)
Z = A_A exp(i phi_A) + A_B exp(i phi_B)
A_merge = |Z|
phi_merge = arg(Z)
omega_merge = (E_A omega_A + E_B omega_B) / (E_A + E_B)
```

Rhythm lock:

```text
R_lock = phase_lock * frequency_lock * amplitude_match
E_core_seed = eta_core * R_lock * E_raw
E_beat_seed = (1 - R_lock) * E_raw
```

## Strict result

```text
verdict = PASS_STABILIZED
criteria_pass_count = 15/15
entanglement_score = 0.292811
entanglement_threshold = 0.280000
phase_lock = 0.533301
frequency_lock = 0.778801
amplitude_match = 0.921610
rhythm_lock = 0.382777
merged_mass = 2.000000
merged_radius = 7.559526
coherence_capacity = 0.526780
E_raw_vib_seed_v42 = 1.139518
E_core_seed_after_lock = 0.414315
E_beat_seed = 0.703281
core_pressure_0 = 0.786615
max_explosion_pressure = 0.786615
final_energy_over_peak = 0.428634
```

## Shape result

```text
weighted_shell_radius = 9.832114
weighted_shell_width = 1.894045
weighted_sphericity = 0.840701
weighted_anisotropy = 0.159299
core_fraction = 0.388466
inner_fraction = 0.502743
outer_fraction = 0.108791
```

## Channel fractions

```text
bb_like     = 0.572638  target ~ 0.582000
WZ_like     = 0.248455  target ~ 0.240000
gg_like     = 0.113869  target ~ 0.086000
tau_like    = 0.063330  target ~ 0.063000
gamma_like  = 0.000678  target ~ 0.002300
mumu_like   = 0.001031  target ~ 0.000220
```

## Criteria

```text
entanglement_score_above_threshold = True
rhythm_lock_computed_positive = True
single_merged_heartbeat_forms = True
mass_added_correctly = True
core_vibration_below_capacity = True
beat_leakage_positive = True
final_energy_not_runaway = True
center_stable = True
shell_forms_after_merge = True
sphericity_remains_reasonable = True
bb_like_largest = True
WZ_like_visible_not_dominant = True
gg_like_visible_not_dominant = True
gamma_mumu_suppressed = True
channel_l1_below_0p20 = True
```

## Interpretation

```text
The rhythm-lock correction stabilizes the v0.42 entangled merge. The particles still pass the entanglement threshold and become one merged sphere, but the merged vibration is no longer added as raw trapped energy. The synchronized heartbeat becomes core vibration, while the mismatch becomes outward beat leakage. Core pressure stays below capacity, the total vibration decays instead of running away, and the channel hierarchy becomes much closer to the rough Higgs-like hierarchy without per-channel tuning.
```

## Limitation

```text
This is a toy rhythm-locked merge calculation, not a detector-level CERN simulation. PASS_STABILIZED means the stabilizer works inside this scaffold; it is not empirical confirmation.
```

## Next target

```text
v0.44 target:
carry the rhythm-lock rule into explicit 3D collision geometry and verify that heartbeat phase, frequency, and amplitude are derived from the 3D field rather than assigned as compact inputs.
```
