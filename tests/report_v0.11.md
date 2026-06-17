# Test Report v0.11

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Author:** Adrian Newton / corpobear  
**Date:** 2026-06-17  
**Status:** speculative reduced field-source integration test  
**Revision:** v0.11.0 initial report

---

## 1. Purpose

This report tests a bounded fourth-mode availability factor in the reduced field-source equation.

The goal is to keep the fourth-mode supply large while allowing only a tiny captured fraction through the Fibonacci-Higgs funnel.

---

## 2. Bounded availability factor

Use:

$$
R_4^{gate}=\frac{R_4}{R_4+R_*}.
$$

This term is always between 0 and 1.

If `R_4` is small, the field source has little reservoir access.

If `R_4` is very large, the factor approaches 1. This means the reservoir is available, but it does not directly multiply the mass result without bound.

---

## 3. Integrated source equation

The reduced source contribution is:

$$
\Sigma_\tau
=
W_v
\left[
\frac{1}{56}
+
\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
\right]
R_4^{gate}.
$$

The mass rule is:

$$
m_\tau=m_\tau^{base}(1+\Sigma_\tau)^2.
$$

Inputs:

$$
m_\tau^{base}=1708.60405054\ \mathrm{MeV},
$$

$$
\langle O_\varphi\rangle=0.9837806705.
$$

The aperture term is:

$$
A_{tip,8}
=
\frac{1}{56}
+
\frac{7}{8}\frac{1}{448}(0.9837806705)
=
0.01977858948.
$$

---

## 4. Reservoir availability scan

Set optimal funnel capture:

$$
W_v=1.
$$

| `R_4^gate` | Tau mass | Interpretation |
|---:|---:|---|
| 0.00 | 1708.604 MeV | no reservoir access |
| 0.25 | 1725.543 MeV | weak access |
| 0.50 | 1742.565 MeV | partial access |
| 0.75 | 1759.671 MeV | strong access |
| 1.00 | 1776.860 MeV | saturated availability |

---

## 5. Speed-window scan with saturated reservoir

Set:

$$
R_4^{gate}=1.
$$

| `W_v` | Tau mass | Interpretation |
|---:|---:|---|
| 0.000 | 1708.604 MeV | no capture |
| 0.204 | 1722.420 MeV | too slow |
| 0.616 | 1750.492 MeV | weak capture |
| 0.915 | 1771.006 MeV | near capture |
| 1.000 | 1776.860 MeV | optimal capture |
| 0.950 | 1773.415 MeV | slight overshoot |
| 0.850 | 1766.536 MeV | scattering begins |
| 0.624 | 1751.039 MeV | too fast |
| 0.257 | 1726.018 MeV | mostly scattered |
| 0.074 | 1713.609 MeV | almost no capture |

---

## 6. Raw reservoir warning

If the raw fourth-mode stability magnitude were used directly as a multiplier, for example `R_4 = 2`, then:

$$
m_\tau\approx1846.453\ \mathrm{MeV}.
$$

This overshoots the tau-like target.

Therefore, the reservoir should be treated as bounded availability, not a raw mass multiplier.

---

## 7. Verdict

The bounded availability factor passes the reduced field-source test.

Best statement:

> The fourth-mode sector supplies available unmanifest amplitude, but the captured mass amplitude is controlled by the funnel aperture, Higgs resonance overlap, speed window, and bounded reservoir availability.

This keeps the field-source equation finite while preserving the successful tau-like result.

---

## 8. Reproducibility pseudocode

```python
m_tau_base = 1708.60405054
O_phi = 0.9837806705
B = 7 / 8
s1 = 1 / 56
s2 = 1 / 448

aperture = s1 + B * s2 * O_phi

def tau_mass(W=1.0, Rgate=1.0):
    Sigma = W * aperture * Rgate
    return m_tau_base * (1 + Sigma)**2

for Rgate in [0, 0.25, 0.5, 0.75, 1]:
    print(Rgate, tau_mass(W=1, Rgate=Rgate))

for W in [0, 0.204, 0.616, 0.915, 1, 0.95, 0.85, 0.624, 0.257, 0.074]:
    print(W, tau_mass(W=W, Rgate=1))
```
