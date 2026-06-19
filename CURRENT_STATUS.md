# Current MCIFT Status: v0.53 Sound / Acoustic Spread Bridge

**Status:** speculative theoretical framework / toy collider scaffold; not established physics.  
**Current bridge test:** v0.53 sound / acoustic spread bridge.  
**Previous bridge test:** v0.52 channel-specific clock / rotation bridge.

---

## One-sentence status

```text
MCIFT v0.53 adds an internal sound/pressure-wave bridge. In this scaffold, sound means a pressure or phonon-like wave inside the dense field medium, not ordinary air sound. The acoustic mode changes shell spread and gives channels additional sound-specific width factors, so branching ratios shift beyond v0.52.
```

---

## v0.53 result

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

Branching-ratio changes after sound spread:

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

---

## Analysis result files

```text
models/sound_spread_bridge_v0.53.md
analysis/results_v0.53/mcift_v0.53_sound_spread_report.md
analysis/results_v0.53/mcift_v0.53_sound_spread_metrics.csv
analysis/results_v0.53/mcift_v0.53_sound_channel_widths.csv
analysis/results_v0.53/mcift_v0.53_sound_signal_summary.md
analysis/results_v0.53/mcift_v0.53_sound_spread_criteria.csv
```

The plots and full signal-strength matrix are in the local output bundle.

---

## Safe wording

```text
v0.53 is an internal acoustic-spread bridge. It is not ordinary sound in air, not a full quantum field calculation, and not collider evidence. It shows that a pressure-wave scaffold can influence shell spread and branching ratios inside MCIFT.
```
