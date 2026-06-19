# MCIFT Main Paper: Inverse Timeflow and Dark-Visible Width Envelope

**Status:** speculative research scaffold; not established physics.  
**Current version:** v0.72 spatial scale-lapse retest.  
**Author:** Adrian Newton / corpobear.

---

## Abstract

This paper records the current MCIFT development path from raw 3D field readouts to inverse-timeflow, dark-visible gravitational envelope tests, and spatial scale-lapse retests. The current result is not a proof of new physics. It is an internal consistency scaffold showing that a single first-principle-style structure can make compact predictions for CERN/Higgs-width behavior and partially close several cosmology benchmarks, while failing others.

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

When contained complexity exceeds coherence, inverse-timeflow load rises. When dark-sector loading overlaps visible-sector formation, the available visible decay-width envelope changes. v0.72 adds that the effective ruler can change too: gravity may alter the spatial measurement scale, not only the clock.

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
v0.71: expanded cosmology to Planck-like H0, SH0ES H0, DESI LyA BAO, BBN baryon density, and S8-style checks.
v0.72: makes the spatial scale-lapse explicit and retests H(z), distance-style anchors, and raw BAO peak behavior.
```

---

## First-principle sector formula

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
tau_ITF = exp[-C_ITF / (N_V + N_A)]
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

Spatial scale-lapse:

```text
sigma_X = E_DV^(1/3)
        = exp[C_ITF * O_DV / (3 (N_V + N_A))]
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
sigma_X = 1.072549870
spatial_lapse = +7.254987 percent
```

---

## Observable maps

```text
H_lab = H_core / sigma_X
D_lab = sigma_X * D_core
k_lab = k_core / sigma_X
Gamma_lab = sigma_X^3 * tau_i * Gamma_core
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

## v0.72 spatial scale-lapse cosmology retest

```text
H075 before spatial lapse = 111.004443
H075 after spatial lapse = 103.465987
H075 delta vs compact LCDM = -0.351618 percent

Planck-like H0 residual = -0.364797 sigma
SH0ES H0 residual = -5.650952 sigma

DESI LyA D_H/r_d residual = +0.146909 sigma
DESI LyA D_M/r_d residual = +0.602802 sigma
```

Raw BAO peak check:

```text
raw BAO peak = 152.29 Mpc
reference r_d = 147.09 Mpc
raw fractional error = +0.035353

if divided by sigma_X: 141.987812 Mpc, fractional error = -0.034690
if multiplied by sigma_X: 163.340999 Mpc, fractional error = +0.110481
```

Strict interpretation:

```text
works well: H(z=0.75), Planck-like H0, DESI LyA distance ratios
still fails: local SH0ES H0
not solved: raw BAO peak scale
not implemented: full BAO ladder covariance, SN distance moduli, full CMB Cl
```

---

## Cell-resolved next formula

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
H_lab(a) = H_core(a) / sigma_X(a)
D_lab(a) = sigma_X(a) * D_core(a)
Gamma_i_lab = sigma_X(a)^3 * tau_i * Gamma_i_core
```

---

## Safe interpretation

Safe:

```text
MCIFT v0.72 is a speculative spatial-lapse benchmark. It tests whether one first-principle-style formula can improve distance and expansion readouts while exposing where the formula fails or remains unimplemented.
```

Unsafe:

```text
MCIFT proves a new interaction.
MCIFT replaces the Standard Model or Lambda-CDM.
The v0.72 formula is experimentally confirmed.
```
