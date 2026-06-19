# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.53 sound / acoustic spread bridge

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has five bridge layers:

```text
1. v0.49 internal scaffold:
   dense entanglement, visible/hidden split, rotating-core load feedback

2. v0.50 kappa bridge:
   explicit kappa modifiers, partial widths, branching ratios, and rate modifiers

3. v0.51 common time bridge:
   core-clock to lab-clock conversion for total width/rate comparison

4. v0.52 channel-clock bridge:
   time-dilated rotation modifies channel formation clocks and branching ratios

5. v0.53 sound/acoustic bridge:
   internal pressure waves alter shell spread and channel partial widths
```

Current bridge verdict:

```text
v0.53 sound spread bridge = PASS_SOUND_SPREAD_BRIDGE
```

This is an internal acoustic-spread bridge, not ordinary sound in air.

---

## v0.53 result

```text
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
max_abs_BR_delta_pct_after_sound = 4.913465
max_abs_signal_strength_delta_pct_after_sound = 7.790001
```

Branching-ratio shifts after sound spread:

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

## Key math

```text
c_sound = sqrt(Coh_feedback / (rho_ratio + G_load))
omega_sound = c_sound / R_shell
acoustic_resonance = exp[-((omega_lab - omega_sound)/(0.35 omega_sound))^2]
M_acoustic = v_core_lab / c_sound

tau_sound,i = 1 + s_sound,i A_sound resonance (1 + 0.25 M_acoustic)
Gamma_i,lab = tau_channel,i tau_sound,i Gamma_i,proper
```

Sound changes the spatial spread and channel partial widths in the scaffold.

---

## Analysis result files

```text
CURRENT_STATUS.md
models/sound_spread_bridge_v0.53.md
analysis/results_v0.53/mcift_v0.53_sound_spread_report.md
analysis/results_v0.53/mcift_v0.53_sound_spread_metrics.csv
analysis/results_v0.53/mcift_v0.53_sound_channel_widths.csv
analysis/results_v0.53/mcift_v0.53_sound_signal_summary.md
analysis/results_v0.53/mcift_v0.53_sound_spread_criteria.csv
```

---

## Important limitation

```text
v0.53 is an internal pressure-wave bridge. It is not real acoustic propagation in air, not a full quantum field calculation, and not collider evidence. The acoustic sensitivity map is still a scaffold rule.
```

---

## Research roadmap

Next required tests:

```text
1. Derive the acoustic sensitivity map from the 3D field.
2. Replace assigned channel sound sensitivities with field-measured couplings.
3. Keep visible and hidden branches separate before channel projection.
4. Derive kappa values from geometry rather than fitting to reference widths.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
