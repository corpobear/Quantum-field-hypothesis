# MCIFT v0.70 Dual First-Principle Prediction Test

**Status:** speculative prediction scaffold; not established physics.  
**Purpose:** run two compact tests from the same v0.64 first-principle formula.

---

## Rule

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
tau_ITF = exp[-C_ITF / (N_V + N_A)]
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

Current values:

```text
C_ITF = 0.689064
tau_ITF = 0.708551878
O_DV = 0.612372436
E_DV = 1.234890003
E_DV^(1/3) = 1.072549870
```

---

## Test 1: collider/Higgs-width prediction

The v0.70 collider prediction keeps the v0.62 blind branching pattern and applies the dark-visible envelope to the total width.

```text
width_prediction = 4.107221 MeV
width_delta_vs_4.07 = +0.914526 percent
max_channel_delta = 8.247649 percent
BR_L1 = 0.052372
```

Status:

```text
pass-like compact prediction
no backpropagation
no target-loss fit
```

---

## Test 2: cosmology prediction

The v0.70 cosmology prediction applies the dark-visible envelope as a 3D expansion projection:

```text
H075_v070 = H075_v061 / E_DV^(1/3)
```

Result:

```text
H075_prediction = 103.465987
H075_compact_LCDM_anchor = 103.831075
H075_delta = -0.351618 percent
H075_residual_vs_CC = -0.142614 sigma
raw_to_v070_improvement = 144.712194x
```

BAO sanity check remains:

```text
BAO_peak = 152.29 Mpc
BAO_reference_rd = 147.09 Mpc
fractional_error = 0.035353
```

---

## Verdict

```text
v0.70 = DUAL_PREDICTION_CERN_PASSLIKE_COSMOLOGY_CLOSE
```

This is the closest combined result so far, but it is still a compact prediction test rather than a full collider likelihood or full cosmology pipeline.
