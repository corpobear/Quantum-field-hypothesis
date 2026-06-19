# Current MCIFT Status: v0.52 Channel-Clock Rotation Bridge

**Status:** speculative theoretical framework / toy collider scaffold; not established physics.  
**Current bridge test:** v0.52 channel-specific clock / rotation bridge.  
**Previous bridge test:** v0.51 time-dilation / kappa-width bridge.

---

## One-sentence status

```text
MCIFT v0.52 adds the correction that time dilation changes the observed rotation speed, and the changed rotation speed gives each channel a different formation-time factor. Unlike v0.51's common clock factor, this channel-specific clock changes partial widths and branching ratios.
```

---

## v0.52 result

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

Branching-ratio changes after channel clock:

```text
bb    -0.860789 %
WW    +1.830883 %
gg    +1.144792 %
tau   -0.390957 %
cc    -0.660675 %
ZZ    +1.830883 %
gamma +3.313884 %
Zgamma +2.909042 %
mumu  -1.130329 %
```

---

## Analysis result files

```text
models/channel_clock_rotation_bridge_v0.52.md
analysis/results_v0.52/mcift_v0.52_channel_clock_rotation_report.md
analysis/results_v0.52/mcift_v0.52_channel_clock_rotation_metrics.csv
analysis/results_v0.52/mcift_v0.52_channel_clock_widths.csv
analysis/results_v0.52/mcift_v0.52_signal_summary.csv
```

The plots and full signal-strength matrix are in the local output bundle.

---

## Safe wording

```text
v0.52 is an internal channel-clock bridge. It shows that rotation-modified time dilation can influence branching ratios inside the scaffold. It is not a full general-relativistic calculation or collider evidence.
```
