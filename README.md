# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.70 dual first-principle prediction test

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

The main branch now runs two compact v0.70 prediction tests from the same v0.64/v0.70 first-principle formula:

```text
Test 1: CERN/Higgs width and branching-ratio prediction
Test 2: cosmology H(z=0.75) prediction
```

Current verdict:

```text
v0.70 = DUAL_PREDICTION_CERN_PASSLIKE_COSMOLOGY_CLOSE
```

---

## Reworked formula

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
tau_ITF = exp[-C_ITF / (N_V + N_A)]
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

Current numerical values:

```text
N_D = 6
N_V = 1
N_A = 1
A_lock = 0.918752
C_ITF = 0.689064
tau_ITF = 0.708551878
O_DV = 0.612372436
E_DV = 1.234890003
E_DV^(1/3) = 1.072549870
```

---

## v0.70 CERN/Higgs prediction

```text
width_prediction = 4.107221 MeV
width_delta_vs_4.07 = +0.914526 percent
max_channel_delta = 8.247649 percent
BR_L1 = 0.052372
```

Status:

```text
compact CERN/Higgs prediction: pass-like
backpropagation used: False
target-loss fit used: False
```

---

## v0.70 cosmology prediction

```text
H075_prediction = 103.465987
H075_compact_LCDM_anchor = 103.831075
H075_delta = -0.351618 percent
H075_residual_vs_CC = -0.142614 sigma
raw_to_v0.70_improvement = 144.712194x
```

BAO sanity check:

```text
BAO_peak = 152.29 Mpc
BAO_reference_rd = 147.09 Mpc
fractional_error = 0.035353
```

Status:

```text
compact H(z) prediction: close
full BAO ladder: not implemented
CMB spectra: not implemented
BBN network: not implemented
```

---

## Main documents

```text
main.md
models/mcift_v0.70_dual_prediction_note.md
models/mcift_first_principle_formula_v0.64.md
CURRENT_STATUS.md
analysis/results_v0.70/v070_metrics.csv
analysis/results_v0.70/v070_collider_result.csv
analysis/results_v0.70/v070_cosmology_result.csv
```

---

## Next version target

```text
v0.71 should move from compact sector-count predictions to cell-resolved predictions:
S_i = Coh_i - q_i
C_ITF(a) from weighted negative-stability stress
O_DV(a) from dark-visible density overlap
Then retest H(z), BAO, CERN total width, branching ratios, and signal-strength style observables separately.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
