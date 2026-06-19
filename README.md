# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.55 Q_i transfer-network background comparison

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has a calibrated background-comparison layer:

```text
v0.54 cosmology layer:
  visible, hidden, rotation, radiation, and acoustic branches become coarse-grained density sectors

v0.55 transfer layer:
  conservative Q_i transfer map moves excess local branch energy into a smooth/lapse reservoir
  then compares raw and transfer-corrected H(z) against real-world reference checkpoints
```

Current verdict:

```text
v0.55 Q_i transfer network = PASS_Q_TRANSFER_BACKGROUND_BRIDGE
```

This is a calibrated transfer-network bridge, not a successful observational cosmology fit.

---

## v0.55 result

```text
Omega_visible_today = 0.244232
Omega_hidden_today = 0.070768
Omega_m_like_today = 0.315000
Omega_rotation_today = 0.001500
Omega_acoustic_today = 0.003500
Omega_radiation_today = 0.000090
Omega_smooth_lapse_reservoir_today = 0.679910
```

Real-world comparison checkpoint:

```text
H0_reference = 67.4
Omega_m_reference = 0.315
H075_observed = 105.0 ± 10.756
H075_model = 104.766
H075_residual_sigma = -0.022
```

Raw vs transfer at z=0.75:

```text
Planck_LCDM_reference_H075 = 103.831
v0.54_raw_no_transfer_H075 = 167.670
v0.55_transfer_H075 = 104.766
raw_H075_delta_pct = 61.483
transfer_H075_delta_pct = 0.901
```

---

## Key math

```text
dot(rho_i) + 3H(rho_i + p_i) = Q_i
sum_i Q_i = 0

rho_i(today) = R_i rho_i(v0.54)
rho_smooth(today) = sum_i (1 - R_i) rho_i(v0.54)
```

The raw coarse-grained branch fractions cannot be compared directly to H(z). A transfer/smoothing network is required before real-world background comparison.

---

## Analysis result files

```text
CURRENT_STATUS.md
models/q_transfer_network_v0.55.md
analysis/results_v0.55/mcift_v0.55_q_transfer_report.md
analysis/results_v0.55/mcift_v0.55_q_transfer_metrics.csv
analysis/results_v0.55/mcift_v0.55_components_after_transfer.csv
analysis/results_v0.55/mcift_v0.55_transfer_network.csv
analysis/results_v0.55/mcift_v0.55_Hz_comparison.csv
analysis/results_v0.55/mcift_v0.55_real_world_comparison.csv
analysis/results_v0.55/mcift_v0.55_growth_kernel.csv
analysis/results_v0.55/mcift_v0.55_criteria.csv
```

---

## Important limitation

```text
v0.55 is calibrated to Planck-like H0/Omega_m and is not a predictive cosmology fit. DESI-style evolving-dark-energy behavior is not fitted yet.
```

---

## Research roadmap

Next required tests:

```text
1. Replace present-day retention factors with dynamic Q_i rates.
2. Fit or derive evolving dark-energy behavior instead of a static smooth reservoir.
3. Compare against DESI BAO, supernova, H(z), growth, sound horizon, and lensing data.
4. Derive Q_i rates from the full 3D phase field.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
