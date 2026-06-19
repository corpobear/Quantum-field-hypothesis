# Current MCIFT Status: v0.70 Dual First-Principle Prediction Test

**Status:** speculative compact prediction scaffold; not established physics.  
**Current layer:** v0.70 dual compact prediction test.  
**Previous layer:** v0.64 unified first-principle formula consolidation.

---

## One-sentence status

```text
MCIFT v0.70 runs two compact first-principle prediction tests from the same formula: one against CERN/Higgs width and branching-ratio anchors, and one against compact cosmology H(z=0.75) anchors. No backpropagation or target-loss fitting is used.
```

---

## v0.70 verdict

```text
DUAL_PREDICTION_CERN_PASSLIKE_COSMOLOGY_CLOSE
```

---

## Formula summary

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
tau_ITF = exp[-C_ITF / (N_V + N_A)]
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

Current values:

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

## Test 1: CERN/Higgs compact prediction

```text
width_prediction = 4.107221 MeV
width_delta_vs_4.07 = +0.914526 percent
max_channel_delta = 8.247649 percent
BR_L1 = 0.052372
```

Status:

```text
compact CERN/Higgs prediction: PASS-LIKE
backpropagation used: False
target-loss fit used: False
```

---

## Test 2: Cosmology compact prediction

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
compact H(z) prediction: CLOSE
full BAO ladder: not implemented
CMB spectra: not implemented
BBN network: not implemented
```

---

## Main files on master

```text
main.md
README.md
CURRENT_STATUS.md
models/mcift_v0.70_dual_prediction_note.md
models/mcift_first_principle_formula_v0.64.md
analysis/results_v0.70/v070_metrics.csv
analysis/results_v0.70/v070_collider_result.csv
analysis/results_v0.70/v070_cosmology_result.csv
```

---

## Next target

```text
v0.71 should move from compact sector-count rules to cell-resolved rules:
S_i = Coh_i - q_i
C_ITF(a) from weighted negative-stability stress
O_DV(a) from dark-visible density overlap
Then retest H(z), BAO, CERN total width, branching ratios, and signal-strength style observables separately.
```
