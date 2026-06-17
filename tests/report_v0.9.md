# Test Report v0.9

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Author:** Adrian Newton / corpobear  
**Date:** 2026-06-17  
**Status:** speculative reduced test of Fibonacci-Higgs anchor-tip source equation  
**Revision:** v0.9.0 initial report

---

## 1. Purpose

This report tests the v0.9 candidate field-source equation in a reduced charged-lepton toy model.

The tested idea is:

```text
original/shadow knot
-> one stable anchor point
-> anchor-tip vortex
-> Fibonacci-shaped oscillation
-> Higgs resonance overlap
-> accumulated mass amplitude
-> squared rest mass
```

This is not a proof of real particle physics. It is a consistency and sensitivity test inside the MCIFT toy model.

---

## 2. Candidate source equation

The proposed field equation is:

```math
\left(
\partial_t^2
-
c_*^2\nabla^2
-
D_c\partial_c^2
+
V'(\psi)
\right)\psi
=
\sum_a
\lambda_a
\Omega_{OS,a}
B_{C_a}(1)
O_{\varphi,a}(t)
\delta_{\epsilon,a}^{(\varphi)}.
```

where:

```math
B_{C_a}(1)=\frac{C_a-1}{C_a}
```

is the one-anchor free spin-vortex fraction.

For the tau-like third mode:

```math
C_3=8,
```

so:

```math
B_8(1)=\frac{7}{8}.
```

---

## 3. Higgs resonance overlap

The time-dependent resonance overlap is:

```math
O_{\varphi,a}(t)
=
\exp\left[-\frac{(\omega_{\varphi,a}(t)-\omega_H)^2}{2\sigma_\omega^2}\right]
\cos^2\left(\theta_{\varphi,a}(t)-\theta_H\right)
\exp\left[-\frac{d_{c,H,a}^{2}}{2\sigma_c^2}\right].
```

Minimal Fibonacci/golden wobble:

```math
\omega_\varphi(t)=\omega_H+\Delta\omega\sin(\varphi t),
```

with:

```math
\varphi=\frac{1+\sqrt{5}}{2}.
```

The Fibonacci/golden geometry is interpreted as shaping the resonance path, not multiplying mass directly.

---

## 4. Reduced tau test equation

The source contributes to mass amplitude.

Reduced amplitude equation:

```math
A_\tau
=
A_\tau^{base}
\left[
1+\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
\right].
```

Mass is amplitude squared:

```math
m_\tau
=
m_\tau^{base}
\left[
1+\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
\right]^2.
```

Inputs:

```math
m_\tau^{base}=1708.60405054\ \mathrm{MeV},
```

```math
m_\tau^{real}=1776.86\ \mathrm{MeV}.
```

---

## 5. Required average overlap

Solving for the average overlap needed to hit the real tau value gives:

```math
\langle O_\varphi\rangle=0.9837806705.
```

Interpretation:

```text
the Fibonacci anchor-tip resonance must remain close to the Higgs channel,
but it does not need perfect overlap.
```

---

## 6. Frequency-resonance sensitivity

Using:

```math
O_\varphi(t)=\exp\left[-\frac{(\Delta\omega\sin(\varphi t))^2}{2\sigma_\omega^2}\right],
```

we test different values of:

```math
r=\frac{\Delta\omega}{\sigma_\omega}.
```

| `r = Delta omega / sigma omega` | `<O_phi>` | Predicted tau | Error vs real tau |
|---:|---:|---:|---:|
| 0.0000 | 1.000000 | 1776.970394 MeV | +0.00621% |
| 0.1000 | 0.997505 | 1776.953410 MeV | +0.00526% |
| 0.2500 | 0.984557 | 1776.865281 MeV | +0.00030% |
| 0.2563 | 0.983781 | 1776.860000 MeV | ~0.00000% |
| 0.5000 | 0.940331 | 1776.564281 MeV | -0.01664% |
| 1.0000 | 0.791017 | 1775.548247 MeV | -0.07382% |
| 2.0000 | 0.465760 | 1773.335973 MeV | -0.19833% |

Best reduced-fit value:

```math
\frac{\Delta\omega}{\sigma_\omega}\approx0.2563.
```

---

## 7. Phase-lock sensitivity

The stricter overlap includes phase:

```math
O_\varphi(t)=O_{freq}(t)\cos^2(\theta_\varphi-\theta_H).
```

Using the best frequency setting, the phase-lock sensitivity is:

| Phase condition | Effective overlap | Tau result | Error |
|---|---:|---:|---:|
| phase locked | 0.98378 | 1776.860000 MeV | ~0.00000% |
| 95% phase coherence | 0.93459 | 1776.525223 MeV | -0.01884% |
| 90% phase coherence | 0.88540 | 1776.190478 MeV | -0.03768% |
| random phase | 0.49189 | 1773.513653 MeV | -0.18833% |

This shows that the candidate equation is not a loose fit. It requires strong phase locking between the Fibonacci anchor tip and the Higgs-response channel.

---

## 8. Result summary

The candidate equation passes the reduced tau toy test under near-resonant, phase-locked conditions.

Best summary:

```text
Delta omega / sigma omega approx 0.2563
phase must be mostly locked
average overlap approx 0.98378
```

This produces:

```math
m_\tau=1776.86\ \mathrm{MeV}
```

inside the reduced toy model.

---

## 9. Interpretation

The v0.9 equation gives a clearer mechanism than a direct correction factor:

```text
mass amplitude is gathered at anchor-tip vortex points
when the Fibonacci-shaped original/shadow drill overlaps the Higgs resonance
```

The `7/8` factor remains the one-anchor free circulation fraction for the tau-like eight-sector knot:

```math
B_8(1)=\frac{7}{8}.
```

The Fibonacci/golden shape controls the resonance path:

```text
Fibonacci shape -> oscillation around Higgs resonance -> overlap average -> mass amplitude gathered
```

---

## 10. Strengths

1. Turns the v0.8 correction into a field-source mechanism.
2. Keeps mass as an amplitude-first calculation.
3. Uses the existing one-anchor `7/8` result.
4. Uses frequency and phase matching, consistent with the earlier exchange-rate structure.
5. Shows a non-perfect but tight resonance condition can reproduce the tau value.

---

## 11. Weaknesses

1. `Delta omega / sigma omega approx 0.2563` is currently inferred, not derived.
2. The phase-lock condition is assumed, not yet explained from knot geometry.
3. The test is reduced to the tau-like mode only.
4. The field operator is candidate-level and not derived from an action.
5. No Lorentz-invariant or gauge-invariant formulation has been proven.
6. The finite Fibonacci-shaped core is not yet explicitly simulated.

---

## 12. Current verdict

The v0.9 candidate equation is worth preserving as the current best field-source proposal.

It should be treated as:

```text
candidate field equation / reduced toy-model success
```

not as:

```text
final physical field theory
```

The next real target is to derive the frequency ratio and phase-locking condition from the geometry of the original/shadow anchor-tip vortex.

---

## 13. Reproducibility pseudocode

```python
from math import sqrt, exp, sin

m_tau_base = 1708.60405054
m_tau_real = 1776.86

C3 = 8
k = 1
B = (C3 - k) / C3

s1 = 1 / 56
s2 = 1 / 448

def tau_mass(O_avg):
    Delta = 1 + s1 + B * s2 * O_avg
    return m_tau_base * Delta**2

# Solve target overlap directly
Delta_target = sqrt(m_tau_real / m_tau_base)
O_required = (Delta_target - 1 - s1) / (B * s2)
print(O_required)
print(tau_mass(O_required))

# Approximate average overlap over many samples
phi = (1 + sqrt(5)) / 2

def O_avg_for_ratio(r, N=200000):
    total = 0.0
    for i in range(N):
        t = 2 * 3.141592653589793 * i / N
        total += exp(-((r * sin(phi * t))**2) / 2)
    return total / N

for r in [0, 0.1, 0.25, 0.2563, 0.5, 1, 2]:
    O = O_avg_for_ratio(r)
    print(r, O, tau_mass(O))
```
