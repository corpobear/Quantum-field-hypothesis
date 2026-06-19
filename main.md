# MCIFT Main Paper: Inverse Timeflow and Dark-Visible Width Envelope

**Status:** speculative research scaffold; not established physics.  
**Current version:** v0.70 dual first-principle prediction test.  
**Author:** Adrian Newton / corpobear.

---

## Abstract

This paper records the current MCIFT development path from raw 3D field readouts to inverse-timeflow and dark-visible gravitational envelope tests. The current result is not a proof of new physics. It is an internal consistency scaffold showing that a single first-principle-style structure can make compact predictions for both cosmology and CERN/Higgs-width behavior without using backpropagation for the final blind prediction tests.

---

## Core idea

MCIFT treats observed quantities as lab-frame readouts of a deeper field state. The field state contains:

```text
visible-sector formation
hidden/dark-sector loading
anchor or boundary structure
connector-supported coherence
contained complexity
```

The key internal stress variable is:

```text
S_i = Coh_i - q_i
```

When contained complexity exceeds coherence, inverse-timeflow load rises. When dark-sector loading overlaps visible-sector formation, the available visible decay-width envelope changes.

---

## Version history

```text
v0.59: real-data audit; raw CERN and raw cosmology failed.
v0.60: inverse-timeflow backpropagation improved the trained CERN bridge.
v0.61: first-principle inverse-timeflow improved raw cosmology H(z=0.75).
v0.62: blind CERN inverse-timeflow predicted pass-like branching ratios without backpropagation.
v0.63: dark-visible gravitational envelope fixed the total-width deficit while preserving branching ratios.
v0.64: consolidated the formula and defined the next cell-resolved first-principle version.
v0.70: runs two compact first-principle prediction tests: CERN/Higgs and cosmology.
```

---

## First-principle sector formula

Let:

```text
N_D = dark-sector sink count
N_V = visible-sector count
N_A = anchor count
A_lock = retained scale-lock amplitude
```

The inverse-timeflow load is:

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
```

The lab-time factor is:

```text
tau_ITF = exp[-C_ITF / (N_V + N_A)]
```

The dark-visible gravitational overlap is:

```text
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
```

The universal width envelope is:

```text
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

For the current sector values:

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

## v0.70 Test 1: CERN/Higgs prediction

The collider map is:

```text
tau_i = exp[-C_ITF * s_i / (N_V + N_A)]
Gamma_i_blind = tau_i * Gamma_i_core
Gamma_i_final = E_DV * Gamma_i_blind
```

The v0.70 compact prediction is:

```text
width_prediction = 4.107221 MeV
width_delta_vs_4.07 = +0.914526 percent
max_channel_delta = 8.247649 percent
BR_L1 = 0.052372
```

Status:

```text
CERN/Higgs compact prediction: pass-like
backpropagation used: False
target-loss fit used: False
```

---

## v0.70 Test 2: Cosmology prediction

The cosmology map applies the dark-visible envelope as a 3D expansion projection:

```text
H075_v070 = H075_v061 / E_DV^(1/3)
```

The compact prediction is:

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
cosmology H(z) compact prediction: close
full BAO ladder: not implemented
CMB spectra: not implemented
BBN network: not implemented
```

---

## Reworked next formula

The sector formula should be replaced by a cell-resolved rule:

```text
C_ITF(a) = sum_i W_i(a) max(0, -S_i(a))^2
           / sum_i W_i(a) [Coh_i(a)^2 + q_i(a)^2 + epsilon]
```

and:

```text
O_DV(a) = 2 sqrt(Rho_D(a) Rho_V(a))
          / [Rho_D(a) + Rho_V(a) + Rho_A(a) + epsilon]
```

Then:

```text
E_DV(a) = exp[C_ITF(a) * O_DV(a) / (N_V + N_A)]
```

Observable maps:

```text
H_lab(a) = tau_ITF(a) * H_core(a) / E_DV(a)^(1/3)
Gamma_i_lab = E_DV * tau_i * Gamma_i_core
```

---

## Safe interpretation

Safe:

```text
MCIFT v0.70 is a speculative compact prediction scaffold. It tests whether one first-principle-style formula can produce close CERN/Higgs and cosmology readouts without backpropagation or target-loss fitting.
```

Unsafe:

```text
MCIFT proves a new interaction.
MCIFT replaces the Standard Model or Lambda-CDM.
The v0.70 formula is experimentally confirmed.
```
