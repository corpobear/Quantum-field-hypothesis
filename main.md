# MCIFT Main Paper: Inverse Timeflow and Dark-Visible Width Envelope

**Status:** speculative research scaffold; not established physics.  
**Current version:** v0.64 unified first-principle formula note.  
**Author:** Adrian Newton / corpobear.

---

## Abstract

This paper records the current MCIFT development path from raw 3D field readouts to inverse-timeflow and dark-visible gravitational envelope tests. The current result is not a proof of new physics. It is an internal consistency scaffold showing that a single first-principle-style structure can improve both cosmology and CERN/Higgs-width behavior without using backpropagation for the final blind predictions.

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
v0.64: consolidates the formula and defines the next cell-resolved first-principle version.
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
O_DV = 0.612372
E_DV = 1.234890
```

---

## Cosmology result

The v0.61 cosmology map is:

```text
H_lab(a) = tau_ITF(a) * H_core(a)
```

At z = 0.75:

```text
v0.59 raw H075 = 156.663819
v0.61 first-principle ITF H075 = 111.004443
LCDM compact reference H075 = 103.831075
raw-to-v0.61 error improvement = 7.364392x
```

This is an improvement over raw over-expansion, but not a full cosmology pass. BAO ladder, growth, CMB spectra, and BBN remain future work.

---

## CERN/Higgs result

The v0.62 blind channel map is:

```text
tau_i = exp[-C_ITF * s_i / (N_V + N_A)]
Gamma_i_blind = tau_i * Gamma_i_core
```

The v0.63 dark-visible envelope is:

```text
Gamma_i_final = E_DV * Gamma_i_blind
```

Because E_DV is universal, branching ratios are preserved:

```text
v0.62 max channel delta = 8.247649 percent
v0.63 max channel delta = 8.247649 percent
```

The total width improves:

```text
v0.62 total width = 3.325981 MeV
v0.62 width delta = -18.280555 percent
v0.63 total width = 4.107221 MeV
v0.63 width delta = +0.914526 percent
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
H_lab(a) = tau_ITF(a) * H_core(a)
Gamma_i_lab = E_DV * tau_i * Gamma_i_core
```

---

## Safe interpretation

Safe:

```text
MCIFT v0.64 is a speculative unified scaffold linking inverse timeflow and dark-visible gravitational overlap. It documents an internally consistent way to improve the current cosmology and CERN-width tests.
```

Unsafe:

```text
MCIFT proves a new interaction.
MCIFT replaces the Standard Model or Lambda-CDM.
The v0.64 formula is experimentally confirmed.
```
