# Current MCIFT Status: v0.44 Explicit 3D Rhythm-Lock Merge Test

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current strict 3D test:** v0.44 explicit 3D rhythm-lock merge test.  
**Previous compact-input stabilizer:** v0.43 rhythm-locked entangled merge test.  
**Previous strict failure:** v0.42 entangled merge-sphere strict test.  
**Previous collision retest:** v0.41 spinning-sphere collision retest.  
**Current collider comparison layer:** v0.36 CERN/LHC Higgs-sector comparison.

---

## One-sentence status

```text
MCIFT v0.44 carries rhythm-lock into explicit 3D collision geometry and derives heartbeat amplitude, phase, and frequency from the 3D field. The strict verdict is FLOP_CORE_OVERLOCK: 14/16 criteria passed. The channel hierarchy remains close, but the field-derived rhythms lock too strongly, trapping too much energy in the merged core heartbeat; core pressure exceeds coherence capacity and the shell does not detach beyond the merged radius.
```

---

## v0.44 strict result

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

Shape result:

```text
weighted_shell_radius = 6.267193
weighted_shell_width = 1.281529
weighted_sphericity = 0.836267
weighted_anisotropy = 0.163733
core_fraction = 0.472421
inner_fraction = 0.366818
outer_fraction = 0.160761
```

Channel fractions:

```text
bb_like     = 0.573037  target ~ 0.582000
WZ_like     = 0.246305  target ~ 0.240000
gg_like     = 0.115613  target ~ 0.086000
tau_like    = 0.063336  target ~ 0.063000
gamma_like  = 0.000704  target ~ 0.002300
mumu_like   = 0.001005  target ~ 0.000220
```

---

## Math under test

```text
z_A(t) = sum_x W_A(x) exp[i phi_A(x,t)]
z_B(t) = sum_x W_B(x) exp[i phi_B(x,t)]
A_A = mean |z_A(t)|
A_B = mean |z_B(t)|
phi_A = arg z_A(t_merge)
phi_B = arg z_B(t_merge)
omega_A = slope unwrap(arg z_A(t))
omega_B = slope unwrap(arg z_B(t))
R_lock = phase_lock * frequency_lock * amplitude_match
E_core_seed = eta_core * R_lock * E_raw
E_beat_seed = (1 - R_lock) * E_raw
```

---

## Analysis result files

```text
analysis/results_v0.44/mcift_v0.44_explicit_3d_rhythm_lock_report.md
```

The metrics, channels, plots, and time history are in the local output bundle.

---

## Limitation

```text
v0.44 is not a detector-level CERN simulation. The channel fractions remain rough hierarchy diagnostics, not measured collider likelihoods. A flop here means the direct 3D-derived rhythm lock is over-locked under this rule.
```

---

## Next proof target

```text
v0.45 target:
add a first-principle adaptive beat-bleed or coherence-capacity rule so field-derived rhythm-lock does not trap too much core energy, then retest before moving to kappa partial widths.
```

---

## Safe wording

```text
v0.44 is a useful strict failure: compact-input rhythm lock stabilized v0.43, but direct 3D-derived heartbeat extraction over-locks the core. The missing piece is an adaptive outward bleed or capacity response, not per-channel tuning.
```
