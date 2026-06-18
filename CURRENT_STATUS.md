# Current MCIFT Status: v0.43 Rhythm-Locked Entangled Merge Test

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current strict PASS/FLOP test:** v0.43 rhythm-locked entangled merge test.  
**Previous strict failure:** v0.42 entangled merge-sphere strict test.  
**Previous collision retest:** v0.41 spinning-sphere collision retest.  
**Previous explicit 3D retest:** v0.40 explicit 3D spherical leakage collision test.  
**Current collider comparison layer:** v0.36 CERN/LHC Higgs-sector comparison.

---

## One-sentence status

```text
MCIFT v0.43 adds rhythm-lock stabilization to the v0.42 entangled merge. Two internal heartbeats are compared first; only the synchronized part becomes the merged core heartbeat, while the mismatch becomes outward beat leakage. The strict verdict is PASS_STABILIZED: 15/15 criteria passed, core pressure stays below coherence capacity, total vibration decays instead of running away, and the rough channel hierarchy improves without direct per-channel tuning.
```

---

## v0.43 strict result

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

Shape result:

```text
weighted_shell_radius = 9.832114
weighted_shell_width = 1.894045
weighted_sphericity = 0.840701
weighted_anisotropy = 0.159299
core_fraction = 0.388466
inner_fraction = 0.502743
outer_fraction = 0.108791
```

Channel fractions:

```text
bb_like     = 0.572638  target ~ 0.582000
WZ_like     = 0.248455  target ~ 0.240000
gg_like     = 0.113869  target ~ 0.086000
tau_like    = 0.063330  target ~ 0.063000
gamma_like  = 0.000678  target ~ 0.002300
mumu_like   = 0.001031  target ~ 0.000220
```

---

## Math under test

```text
h_A(t) = A_A cos(omega_A t + phi_A)
h_B(t) = A_B cos(omega_B t + phi_B)
Z = A_A exp(i phi_A) + A_B exp(i phi_B)
A_merge = |Z|
phi_merge = arg(Z)
omega_merge = (E_A omega_A + E_B omega_B) / (E_A + E_B)
R_lock = phase_lock * frequency_lock * amplitude_match
E_core_seed = eta_core * R_lock * E_raw
E_beat_seed = (1 - R_lock) * E_raw
```

---

## Analysis result files

```text
analysis/results_v0.43/mcift_v0.43_rhythm_locked_merge_report.md
analysis/results_v0.43/mcift_v0.43_rhythm_locked_merge_metrics_summary.csv
```

The full channel table and time history are in the local output bundle.

---

## Limitation

```text
v0.43 is a toy rhythm-locked merge calculation, not a detector-level CERN simulation. PASS_STABILIZED means the stabilizer works inside this scaffold; it is not empirical confirmation.
```

---

## Next proof target

```text
v0.44 target:
carry the rhythm-lock rule into explicit 3D collision geometry and verify that heartbeat phase, frequency, and amplitude are derived from the 3D field rather than assigned as compact inputs.
```

---

## Safe wording

```text
v0.43 is a useful stabilization result: the merged sphere no longer explodes once raw vibration is split into locked core heartbeat and outward beat leakage. The next step is to derive those heartbeat quantities from the full 3D field.
```
