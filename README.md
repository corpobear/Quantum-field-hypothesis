# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.57 executable unified field

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has an executable unified-field scaffold:

```text
v0.56 formula:
  one extended field object defines collision, visible/hidden, rotation, clock, sound, channels, cosmology, and Q_i transfer readouts

v0.57 execution:
  a deterministic Python run instantiates node/link/face/cell fields and computes those readouts from one code path
```

Current verdict:

```text
v0.57 executable unified field = PASS_EXECUTABLE_UNIFIED_FIELD_SCAFFOLD
```

This is an executable closure test, not a completed physics model or observational fit.

---

## v0.57 result

```text
grid_n = 34
cells = 39304
mean_chi = 0.262683
mean_Omega = 0.381430
mean_E = 1.111738
mean_R_lock = 0.964146
mean_rho_ratio = 1.418517
mean_lapse_N = 0.830136
mean_omega_lab = 0.068444
mean_c_sound = 0.719971
collapse_fraction = 0.103908
```

Branch fractions from the field:

```text
visible_raw = 0.542599
hidden_raw = 0.446601
rotation_raw = 0.001410
sound_raw = 0.009269
radiation_raw = 0.000121
```

After-transfer readouts:

```text
Omega_visible_today = 0.172785
Omega_hidden_today = 0.142215
Omega_m_like_today = 0.315000
Omega_rotation_today = 0.000027
Omega_acoustic_today = 0.000336
Omega_radiation_today = 0.000000
Omega_smooth_lapse_reservoir_today = 0.684636
H075_model = 103.897709
H075_delta_pct_vs_reference = 0.064175
```

---

## Analysis result files

```text
CURRENT_STATUS.md
simulations/mcift_v0_57_unified_field.py
analysis/results_v0.57/mcift_v0.57_unified_field_report.md
analysis/results_v0.57/mcift_v0.57_unified_field_metrics.csv
analysis/results_v0.57/mcift_v0.57_unified_field_branches.csv
analysis/results_v0.57/mcift_v0.57_unified_field_channels.csv
analysis/results_v0.57/mcift_v0.57_unified_field_growth_kernel.csv
analysis/results_v0.57/mcift_v0.57_transfer_retention.csv
analysis/results_v0.57/mcift_v0.57_criteria.csv
```

---

## Important limitation

```text
v0.57 executes the unified scaffold, but it still contains assigned channel/retention coefficients. The next step is to replace those with measurements from the evolved 3D field geometry itself.
```

---

## Research roadmap

Next required tests:

```text
1. Remove assigned channel/category coefficients.
2. Measure channel weights W_c directly from field geometry.
3. Derive Q_i transfer rates dynamically from Psi_i evolution.
4. Rerun particle and cosmology outputs with no bridge calibration.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
