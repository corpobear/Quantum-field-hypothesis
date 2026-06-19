# MCIFT v0.59 Cosmology + CERN Real-World Retest

**Status:** public-data retest/audit layer; speculative MCIFT scaffold, not established physics.  
**Generated:** 2026-06-19  
**Scope:** retest the current v0.58 3D real-data outputs against cosmology and CERN/LHC reference results, with strict wording and no claim of physical validation.

---

## Purpose

v0.59 does not introduce a new physics proof. It updates the documentation layer after retesting the current MCIFT outputs against external reference data:

```text
A. Cosmology: Planck 2018 + DESI BAO / DESI DR2 context.
B. CERN/LHC: Higgs mass, total width, branching fractions, and signal-strength constraints.
C. Existing MCIFT outputs: v0.58 3D real-data retest, with earlier v0.20/v0.22/v0.25 cosmology context.
```

The retest keeps the distinction between:

```text
raw 3D MCIFT readout
transfer / smoothing scaffold
calibrated bridge
```

Only raw outputs can count as independent evidence. Transfer and calibrated layers remain scaffolds.

---

## External reference anchors

### Cosmology anchors

```text
Planck 2018 baseline:
  Omega_b h^2 ~= 0.02237
  Omega_c h^2 ~= 0.1200
  baryon/CDM ratio ~= 0.186417

DESI BAO context:
  DR1 BAO used tracers over 0.1 < z < 4.2.
  DESI Ly-alpha BAO used r_d = 147.09 Mpc as a reference sound horizon.
  DESI DR2 reports BAO measurements from more than 14 million galaxies and quasars.
  DESI DR2 flat-LambdaCDM BAO is broadly described by the data, but BAO+CMB shows mild tension,
  and w0-wa dynamical dark energy improves the fit in several combinations.
```

### CERN/LHC anchors

```text
Higgs mass:
  ATLAS+CMS Run 1 combined mass: m_H = 125.09 GeV.
  ATLAS Run 1+Run 2 mass: m_H = 125.11 +/- 0.11 GeV.

Higgs width:
  SM-like expectation near 125 GeV: Gamma_H ~= 4.1 MeV.
  CMS off-shell/on-shell width measurement: Gamma_H = 3.2 +2.4/-1.7 MeV.

Signal strength:
  ATLAS+CMS Run 1 combined signal yield: mu = 1.09 +/- 0.11.
  ATLAS 13 TeV combined result reported global signal strength mu = 1.11 +0.09/-0.08.
```

---

## Retest inputs from the repo

```text
analysis/results_v0.58/mcift_v0.58_3d_realdata_retest_report.md
analysis/results_v0.58/mcift_v0.58_3d_realdata_metrics.csv
analysis/results_v0.58/mcift_v0.58_cern_channels.csv
analysis/results_v0.58/mcift_v0.58_reference_comparison.csv
analysis/results_v0.20/mcift_v0.20_derived_scalelock_report.md
analysis/results_v0.22/mcift_v0.22_growth_transfer_report.md
analysis/results_v0.25/mcift_v0.25_first_principle_sinks_report.md
analysis/results_v0.50/mcift_v0.50_kappa_bridge_report.md
analysis/results_v0.52/mcift_v0.52_channel_clock_rotation_report.md
analysis/results_v0.53/mcift_v0.53_sound_spread_report.md
```

---

## Cosmology retest

### 1. Baryon/CDM ratio

Using the Planck-style physical-density ratio:

```text
Omega_b h^2 / Omega_c h^2 = 0.02237 / 0.1200 = 0.186417
```

Earlier MCIFT visible/dark weighted-ratio milestones remain:

| Milestone | MCIFT visible/dark | fractional error vs 0.186417 | verdict |
|---:|---:|---:|---|
| 1B | 1.018471 | 4.463412 | FAIL |
| 2B | 0.195224 | 0.047245 | PASS-LIKE |
| 3B | 0.162572 | 0.127911 | WEAK |
| 4B | 0.155448 | 0.166126 | WEAK |
| 5B | 0.153635 | 0.175852 | WEAK |

Result:

```text
Best ratio point: 2B, PASS-LIKE but time-selected.
Final 5B point: WEAK, about 17.6 percent low.
```

This is not enough for a cosmology pass.

### 2. BAO / sound-horizon scale

Using `r_d = 147.09 Mpc` as the external BAO scale anchor:

| MCIFT scale readout | value [Mpc] | fractional error vs 147.09 Mpc | verdict |
|---|---:|---:|---|
| v0.20 final BAO/global peak | 152.29 | 0.035353 | PASS-LIKE scale sanity check |
| v0.25 native global peak | 617.87 | 3.200625 | FAIL |
| v0.25 native BAO-window peak | 128.15 | 0.128765 | WEAK |
| v0.25 nearest BAO bin | 152.29 | 0.035353 | PASS-LIKE bin proximity |

Result:

```text
Scale-lock can land near the BAO scale.
The more native first-principle six-sink global peak does not.
```

### 3. Full cosmology status against Planck + DESI DR2

DESI DR2 sharpens the problem: it is not enough to match one scale. A real model must reproduce distance-redshift behavior, CMB acoustic structure, growth, and possibly w0-wa behavior.

Current MCIFT status:

```text
raw 3D background expansion: FAIL / over-expands
transfer 3D background at z=0.75: PASS-LIKE as a calibrated scaffold
CMB TT/TE/EE: NOT_IMPLEMENTED
BBN abundances: NOT_IMPLEMENTED
full BAO distance ladder: NOT_IMPLEMENTED
w0-wa dynamical-dark-energy fit: NOT_IMPLEMENTED
Boltzmann/radiation transfer solver: NOT_IMPLEMENTED
```

v0.58 gives:

```text
H075_raw_3d = 156.663819
H075_raw_delta_pct_vs_reference = 50.883364

H075_transfer_3d = 103.897709
H075_transfer_delta_pct_vs_reference = 0.064175
H075_transfer_residual_sigma_vs_CC_obs = -0.102478
```

Result:

```text
COSMOLOGY_RAW_FAIL_TRANSFER_PASS_SCAFFOLD
```

Meaning: MCIFT has a useful transfer/smoothing bridge, but the raw 3D cosmology does not yet pass real cosmology data.

---

## CERN / LHC retest

### 1. Raw v0.58 particle-channel result

The raw 3D readout still fails the all-channel 10 percent criterion:

```text
BR_L1_raw_vs_SM = 0.092428
max_abs_BR_delta_pct_raw_vs_SM = 100.000000
failed_CERN_channels_10pct = gg,tau,cc,gamma,Zgamma,mumu
```

Channel result:

| channel | raw delta vs SM [%] | verdict |
|---|---:|---|
| bb | +6.416978 | PASS_10PCT |
| WW | -0.230620 | PASS_10PCT |
| gg | -15.788351 | FAIL |
| tau | +13.658096 | FAIL |
| cc | -100.000000 | FAIL |
| ZZ | +0.950363 | PASS_10PCT |
| gamma | -99.924245 | FAIL |
| Zgamma | -99.960445 | FAIL |
| mumu | +13.075238 | FAIL |

Result:

```text
CERN_RAW_FAIL
```

The raw model is not yet a CERN/LHC quantitative pass. The central failures are missing loop/surface channels for gamma and Zgamma, and missing explicit cc projection.

### 2. Kappa and clock bridges

Earlier bridge layers remain useful but calibrated:

```text
v0.50 kappa bridge:
  PASS_KAPPA_BRIDGE_CALIBRATED
  Reproduces SM table by choosing kappa ~= 1.
  This is not an independent prediction.

v0.52 channel-clock bridge:
  Gamma_lab_channel_clock_MeV = 3.965184
  delta vs 4.07 MeV = -2.575329 percent
  max_abs_BR_delta_pct_after_channel_clock = 3.313884
  max_abs_signal_strength_delta_pct_after_channel_clock = 5.205441

v0.53 sound-spread bridge:
  Gamma_lab_sound_raw_MeV = 3.964892
  delta vs 4.07 MeV = -2.582506 percent
  max_abs_BR_delta_pct_after_sound = 4.913465
  max_abs_signal_strength_delta_pct_after_sound = 7.790001
```

Result:

```text
CERN_BRIDGE_COMPATIBLE_BUT_NOT_PREDICTIVE
```

The bridge layers sit in the few-percent regime and are not obviously excluded by broad Higgs-width and inclusive-signal-strength anchors, but the raw 3D channel model still fails.

---

## Inverse Timeflow Backpropagation Derivation status

For this retest, the inverse-timeflow/backpropagation layer is treated as a future loss-function layer, not as already implemented.

Correct AI-style interpretation:

```text
forward bridge:
  hidden/proper MCIFT state -> timeflow/channel correction -> predicted lab observable

inverse timeflow backpropagation derivation:
  observed lab residual -> loss function -> gradients/updates into hidden MCIFT parameters
```

Current repo status:

```text
forward timeflow/clock formulas: PRESENT
inverse-timeflow backprop loss: NOT_IMPLEMENTED
```

Required future formula class:

```text
L_ITB(theta) =
  sum_i w_i [log(Gamma_i,pred_lab(theta) / Gamma_i,obs)]^2
  + lambda_total [log(sum_i Gamma_i,pred_lab(theta) / Gamma_total,obs)]^2
  + regularization
```

v0.59 does not claim this has been trained.

---

## Overall v0.59 verdict

```text
COSMOLOGY_RAW_FAIL_TRANSFER_PASS_SCAFFOLD
CERN_RAW_FAIL_BRIDGE_COMPATIBLE_NOT_PREDICTIVE
INVERSE_TIMEFLOW_BACKPROP_LOSS_NOT_IMPLEMENTED
```

Short form:

```text
v0.59 = REALDATA_RETEST_FAILS_RAW_BUT_IDENTIFIES_NEXT_IMPLEMENTATION_TARGETS
```

---

## Required next work

```text
1. Implement explicit gamma and Zgamma loop/surface channel readouts.
2. Implement explicit cc projection.
3. Replace transfer/smoothing calibration with derived 3D dynamics.
4. Add full cosmology observables: H(z), D_M(z), D_H(z), BAO ladder, C_l, and growth.
5. Implement the inverse timeflow backpropagation loss as an actual optimization target.
6. Retest raw, transfer, and calibrated modes separately.
```

---

## Safe wording

Safe:

```text
MCIFT v0.59 retests current outputs against cosmology and CERN/LHC anchors.
The raw 3D model does not yet pass either full cosmology or full CERN channel tests.
The transfer and bridge layers are useful scaffolds but are not independent physical predictions.
```

Unsafe:

```text
MCIFT matches CERN.
MCIFT explains DESI.
MCIFT proves a new cosmology.
The inverse-timeflow backpropagation loss has already been trained.
```

---

## References

- Planck Collaboration, "Planck 2018 results. VI. Cosmological parameters", arXiv:1807.06209.
- DESI Collaboration, "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints", arXiv:2503.14738.
- DESI Collaboration, "DESI 2024 IV: Baryon Acoustic Oscillations from the Lyman-alpha Forest", arXiv:2404.03001.
- ATLAS and CMS Collaborations, "Combined Measurement of the Higgs Boson Mass in pp Collisions at sqrt(s)=7 and 8 TeV", arXiv:1503.07589.
- ATLAS Collaboration, "Combined measurement of the Higgs boson mass from H->gamma gamma and H->ZZ*->4l...", arXiv:2308.04775.
- ATLAS Collaboration, "Combined measurements of Higgs boson production and decay using up to 80 fb^-1...", arXiv:1909.02845.
- CMS Collaboration, "Measurement of the Higgs boson width and evidence of its off-shell contributions to ZZ production", arXiv:2202.06923.
