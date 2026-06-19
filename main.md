# MCIFT Main Paper: Inverse Timeflow and Dark-Visible Width Envelope

**Status:** speculative research scaffold; not established physics.  
**Current version:** v0.71 expanded cosmology benchmark.  
**Author:** Adrian Newton / corpobear.

---

## Abstract

This paper records the current MCIFT development path from raw 3D field readouts to inverse-timeflow and dark-visible gravitational envelope tests. The current result is not a proof of new physics. It is an internal consistency scaffold showing that a single first-principle-style structure can make compact predictions for CERN/Higgs-width behavior and partially close several cosmology benchmarks, while failing others.

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
v0.70: ran two compact first-principle prediction tests: CERN/Higgs and cosmology.
v0.71: expands cosmology to Planck-like H0, SH0ES H0, DESI LyA BAO, BBN baryon density, and S8-style checks.
```

---

## First-principle sector formula

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
tau_ITF = exp[-C_ITF / (N_V + N_A)]
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
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

## v0.70 CERN/Higgs prediction

```text
width_prediction = 4.107221 MeV
width_delta_vs_4.07 = +0.914526 percent
max_channel_delta = 8.247649 percent
BR_L1 = 0.052372
backpropagation used = False
target-loss fit used = False
```

---

## v0.71 expanded cosmology benchmark

```text
H0_prediction = 67.163010
Planck_H0 residual = -0.364797 sigma
SH0ES_H0 residual = -5.650952 sigma

H075_prediction = 103.465987
H075_delta_vs_compact_LCDM = -0.351618 percent
H075_residual_vs_CC = -0.142614 sigma

DESI_LyA_DH/rd prediction = 8.646895
DESI_LyA_DH/rd residual = +0.146909 sigma
DESI_LyA_DM/rd prediction = 39.311695
DESI_LyA_DM/rd residual = +0.602802 sigma

omega_b h2 prediction = 0.02237
BBN2024 residual = +0.345455 sigma

S8_prediction = 0.775722
DESY3_S8 residual = +0.206750 sigma
Planck_S8 residual = -4.329115 sigma
```

Strict interpretation:

```text
close/pass-like: Planck-like H0, H(z=0.75), DESI LyA BAO, BBN baryon density, DES Y3-style S8
fail/tension: SH0ES local H0, Planck S8 if the growth proxy is taken literally
not implemented: full CMB Cl, full SN distance moduli, full BAO covariance, BBN reaction network
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

Observable maps:

```text
H_lab(a) = tau_ITF(a) * H_core(a) / E_DV(a)^(1/3)
Gamma_i_lab = E_DV * tau_i * Gamma_i_core
```

---

## Safe interpretation

Safe:

```text
MCIFT v0.71 is a speculative expanded benchmark. It tests whether one first-principle-style formula can remain close to several real cosmology anchors while exposing where the formula fails or remains unimplemented.
```

Unsafe:

```text
MCIFT proves a new interaction.
MCIFT replaces the Standard Model or Lambda-CDM.
The v0.71 formula is experimentally confirmed.
```
