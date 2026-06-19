# Current MCIFT Status: v0.55 Q_i Transfer Network Comparison

**Status:** speculative theoretical framework / calibrated toy cosmology scaffold; not established physics.  
**Current layer:** v0.55 Q_i transfer-network background comparison.  
**Previous layer:** v0.54 cosmology coarse-graining test.

---

## One-sentence status

```text
MCIFT v0.55 adds a conservative Q_i transfer-network bridge. Raw v0.54 over-expands when local collision fractions are treated directly as present-day cosmic densities. The v0.55 transfer map moves excess branch energy into a smooth/lapse reservoir, then compares the resulting H(z) curve to Planck-like and cosmic-chronometer reference points.
```

---

## v0.55 result

```text
verdict = PASS_Q_TRANSFER_BACKGROUND_BRIDGE
criteria_pass_count = 12/12
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

Growth-kernel proxy:

```text
mu_eff(k=0.01) = 1.214990
mu_eff(k=0.1)  = 1.214007
mu_eff(k=1)    = 1.136847
mu_eff(k=10)   = 0.800982
```

---

## Analysis result files

```text
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

The plots are in the local output bundle.

---

## Safe wording

```text
v0.55 is a calibrated background bridge. It is not a successful observational cosmology fit. It shows that the raw coarse-grained branch fractions require a transfer/smoothing network before comparison with real-world H(z) data. DESI-style evolving-dark-energy behavior is not fitted yet.
```
