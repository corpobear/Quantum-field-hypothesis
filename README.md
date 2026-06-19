# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.52 channel-clock / rotation bridge

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has four bridge layers:

```text
1. v0.49 internal scaffold:
   dense entanglement, visible/hidden split, rotating-core load feedback

2. v0.50 kappa bridge:
   explicit kappa modifiers, partial widths, branching ratios, and rate modifiers

3. v0.51 common time bridge:
   core-clock to lab-clock conversion for total width/rate comparison

4. v0.52 channel-clock bridge:
   time-dilated rotation modifies channel formation clocks and branching ratios
```

Current bridge verdict:

```text
v0.52 channel-clock rotation bridge = PASS_CHANNEL_CLOCK_ROTATION_BRIDGE
```

This is an internal-clock bridge, not a full general-relativistic calculation.

---

## v0.52 result

```text
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

Branching-ratio shifts after channel clock:

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

## Key math

```text
omega_lab = tau_core_to_lab * omega_proper
rotation_speed_shift = 1 - tau_core_to_lab
tau_depth,i = 1 - (1 - tau_core_to_lab) depth_i
tau_channel,i = tau_depth,i * (1 + spin_sensitivity_i * rotation_speed_shift)
Gamma_i,lab = tau_channel,i Gamma_i,proper
```

A common time factor changes only total width/rate scale. A channel-specific clock can change branching ratios.

---

## Analysis result files

```text
CURRENT_STATUS.md
models/channel_clock_rotation_bridge_v0.52.md
analysis/results_v0.52/mcift_v0.52_channel_clock_rotation_report.md
analysis/results_v0.52/mcift_v0.52_channel_clock_rotation_metrics.csv
analysis/results_v0.52/mcift_v0.52_channel_clock_widths.csv
analysis/results_v0.52/mcift_v0.52_signal_summary.csv
```

---

## Important limitation

```text
v0.52 is an internal channel-clock bridge. It is not a full general-relativistic calculation or collider evidence. The channel depth and spin-sensitivity map is still a scaffold rule.
```

---

## Research roadmap

Next required tests:

```text
1. Derive channel depth and spin sensitivity from the 3D phase field.
2. Test channel-specific clocks without assigning them by hand.
3. Keep visible and hidden branches separate before channel projection.
4. Derive kappa values from geometry rather than fitting to reference widths.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
