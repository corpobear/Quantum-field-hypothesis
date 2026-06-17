# Test Report v0.8

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Author:** Adrian Newton / corpobear  
**Date:** 2026-06-17  
**Status:** speculative toy-model test of one-anchor spin-vortex correction  
**Revision:** v0.8.0 initial report

---

## 1. Purpose

This report tests whether the one-point shadow-anchor result can be reinterpreted as a spin-vortex correction for the tau-like charged-lepton mode.

The tested idea is:

```text
one stable origin-shadow anchor
-> one pinned sector
-> remaining sectors circulate
-> free spin-vortex fraction
-> amplitude correction
-> tau-like mass correction
```

This is not presented as established physics. It is a numerical stress test inside the MCIFT toy model.

---

## 2. Existing baseline

The current MCIFT charged-lepton toy model uses:

$$
C_n=2^n,
$$

$$
S_n=3.5n-C_n,
$$

$$
A_n=(C_n-1)^{D_f},
$$

with:

$$
D_f=3.5.
$$

The finite Higgs response may be linear Gaussian or log-fractal. The earlier linear-Gaussian baseline gave the out-of-sample tau prediction:

$$
m_\tau^{base}=1708.60405054\ \mathrm{MeV}.
$$

This baseline uses electron and muon as calibration anchors, so only tau is an out-of-sample prediction.

Real tau value used in the earlier report:

$$
m_\tau^{real}=1776.86\ \mathrm{MeV}.
$$

Baseline error:

$$
\frac{1708.60405054-1776.86}{1776.86}\times100=-3.840\ldots\%.
$$

---

## 3. One-point anchor result

The v0.7 shadow-anchor model defines the origin-shadow contact count:

$$
k=|K_C\cap S_C|.
$$

A true shadow must be connected:

$$
k\ge1.
$$

But multiple contacts create pairwise bridges:

$$
M(k)=\frac{k(k-1)}{2}.
$$

A stable shadow must avoid merger-motion, requiring:

$$
M(k)=0.
$$

The only connected, no-bridge solution is:

$$
k_*=1.
$$

---

## 4. Spin-vortex reinterpretation

For a `C`-sector knot, the one anchor point pins one sector. The remaining free spin-vortex fraction is:

$$
B_C(1)=\frac{C-1}{C}.
$$

For the tau-like third mode:

$$
C_3=2^3=8.
$$

Therefore:

$$
B_8(1)=\frac{8-1}{8}=\frac{7}{8}.
$$

This report interprets the same `7/8` factor as:

```text
one pinned anchor sector + seven circulating sectors
```

rather than only as an echo-shadow projection fraction.

---

## 5. Amplitude correction tested

The existing shadow amplitude correction form is:

$$
\Delta(f)=1+\frac{1}{56}+f\frac{1}{448}.
$$

The one-anchor spin-vortex hypothesis sets:

$$
f=B_8(1)=\frac{7}{8}.
$$

Therefore:

$$
\Delta_{anchor}
=
1+\frac{1}{56}+\frac{7}{8}\frac{1}{448}.
$$

Numerically:

$$
\Delta_{anchor}=1.0198102678571428.
$$

Because MCIFT treats this as an amplitude correction, mass is corrected by the square:

$$
m_\tau^{anchor}
=
m_\tau^{base}\Delta_{anchor}^2.
$$

---

## 6. Numerical result

Using:

$$
m_\tau^{base}=1708.60405054\ \mathrm{MeV},
$$

and:

$$
\Delta_{anchor}=1.0198102678571428,
$$

we get:

$$
m_\tau^{anchor}=1776.97039439\ \mathrm{MeV}.
$$

Comparison with real tau value:

$$
m_\tau^{real}=1776.86\ \mathrm{MeV}.
$$

Error:

$$
1776.97039439-1776.86=0.11039439\ \mathrm{MeV}.
$$

Percent error:

$$
\frac{0.11039439}{1776.86}\times100=0.00621\%.
$$

---

## 7. Comparison table

| Model | Tau mass | Error vs real tau |
|---|---:|---:|
| Linear MCIFT baseline | 1708.60405054 MeV | -3.84% |
| + one-anchor `7/8` spin-vortex correction | 1776.97039439 MeV | +0.00621% |

---

## 8. Koide comparison

The earlier report gives the Koide high-root tau value:

$$
m_\tau^{Koide}=1776.96902708\ \mathrm{MeV}.
$$

The one-anchor spin-vortex result is:

$$
m_\tau^{anchor}=1776.97039439\ \mathrm{MeV}.
$$

Difference:

$$
m_\tau^{anchor}-m_\tau^{Koide}=0.00136731\ \mathrm{MeV}.
$$

This is extremely close numerically, but the model must still derive why the correction belongs specifically to the tau-like eight-sector mode.

---

## 9. Interpretation

The test supports the following internal MCIFT chain:

```text
C_3 = 8 sectors
one stable anchor point
-> seven free circulating sectors
-> 7/8 spin-vortex fraction
-> amplitude correction
-> squared mass correction
-> tau-like mass moves near Koide high-root
```

This improves the toy model because the `7/8` factor is no longer only a selected projection value. It is tied to the one-point shadow-anchor derivation.

---

## 10. Strengths

1. The correction follows from the existing v0.7 one-point anchor rule.
2. The factor `7/8` arises naturally for an eight-sector tau-like knot.
3. The corrected tau value is close to both the real tau value and the Koide high-root value.
4. The mechanism connects shadow anchoring, spin circulation, amplitude correction, and mass.

---

## 11. Weaknesses

1. This is still a toy-model correction, not a derived physical law.
2. The model must explain why electron-like and muon-like modes do not receive the same kind of correction, or receive different corrections.
3. The base tau value comes from an earlier calibrated model using electron and muon anchors.
4. The correction is applied after the baseline calculation; a deeper model should derive the amplitude directly from the field.
5. No Lorentz-invariant or gauge-invariant field action has been derived yet.

---

## 12. Current verdict

The one-anchor spin-vortex correction is a promising internal extension of MCIFT.

Best current description:

> A stable one-point original-shadow anchor may pin one sector of an eight-sector tau-like knot, leaving a `7/8` free spin-vortex fraction. When interpreted as an amplitude correction, this moves the linear MCIFT tau prediction from a `-3.84%` miss to a `+0.00621%` result near the Koide high-root value.

This is mathematically interesting but not yet a confirmed physical prediction.

---

## 13. Next tests

1. Derive the spin-vortex correction from a concrete projected knot field.
2. Derive the anchor spin-transfer strength rather than choosing an amplitude correction form.
3. Test whether electron-like and muon-like modes have different anchor structures.
4. Rebuild the mass formula so it predicts amplitude directly, not by post-hoc correction.
5. Check whether the same anchor-spin mechanism predicts decay/instability patterns.
6. Add reproducible code for the v0.8 calculation.

---

## 14. Reproducibility pseudocode

```python
m_tau_base = 1708.60405054
m_tau_real = 1776.86
m_tau_koide = 1776.96902708

C3 = 8
k = 1
f_anchor = (C3 - k) / C3

Delta_anchor = 1 + 1/56 + f_anchor * (1/448)
m_tau_anchor = m_tau_base * Delta_anchor**2

error_mev = m_tau_anchor - m_tau_real
error_percent = 100 * error_mev / m_tau_real
koide_delta = m_tau_anchor - m_tau_koide

print(f_anchor)
print(Delta_anchor)
print(m_tau_anchor)
print(error_mev, error_percent)
print(koide_delta)
```
