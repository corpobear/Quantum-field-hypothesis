# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.51 time-dilation / kappa-width bridge

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has three bridge layers:

```text
1. v0.49 internal scaffold:
   dense entanglement, visible/hidden split, rotating-core load feedback

2. v0.50 kappa bridge:
   explicit kappa modifiers, partial widths, branching ratios, and rate modifiers

3. v0.51 time bridge:
   core-clock to lab-clock conversion for width/rate comparison
```

Current bridge verdict:

```text
v0.51 time-dilation bridge = PASS_TIME_DILATION_BRIDGE_WITH_COMPENSATION
```

This is an internal-clock bridge, not a full general-relativistic calculation.

---

## v0.51 result

```text
G_load = 0.874502
R_hidden = 10.582795
R_dense = 6.198812
omega_final = 0.072027
v_core = 0.446482
tau_core_to_lab = 0.868528
time_slowdown_pct = 13.147198
```

Width bridge:

```text
Gamma_SM_total_MeV = 4.070000
Gamma_lab_uncompensated_MeV = 3.534909
Gamma_lab_uncompensated_delta_pct = -13.147198
universal_kappa_proper_needed = 1.073021
proper_width_scale_needed = 1.151373
Gamma_lab_compensated_MeV = 4.070000
```

---

## Key math

```text
chi_time = 2 beta_G G_load / R_hidden
tau_G = sqrt(1 - chi_time)
v_core = omega_final R_dense
tau_rot = sqrt(1 - v_core^2)
tau_core_to_lab = tau_G tau_rot
Gamma_i,lab = tau_core_to_lab Gamma_i,proper
```

A common time factor changes total width/rate scale, not branching ratios.

---

## Analysis result files

```text
CURRENT_STATUS.md
models/time_dilation_kappa_bridge_v0.51.md
analysis/results_v0.51/mcift_v0.51_time_dilation_report.md
analysis/results_v0.51/mcift_v0.51_time_dilation_metrics.csv
analysis/results_v0.51/mcift_v0.51_time_dilation_widths.csv
analysis/results_v0.51/mcift_v0.51_time_dilation_signal_summary.csv
```

---

## Important limitation

```text
v0.51 is an internal-clock bridge. It is not a full general-relativistic calculation. It does not yet derive channel-specific time factors.
```

---

## Research roadmap

Next required tests:

```text
1. Derive channel-specific formation-time factors from the 3D phase field.
2. Test whether channel-specific clocks modify branching ratios.
3. Keep visible and hidden branches separate before channel projection.
4. Derive kappa values from geometry rather than fitting to reference widths.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
