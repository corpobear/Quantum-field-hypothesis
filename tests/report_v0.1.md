# Test Report v0.1

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Author:** Adrian Newton / corpobear  
**Date:** 2026-06-17  
**Status:** first numerical stress test against real charged-lepton mass data

## 1. Purpose

This report tests the current MCIFT toy model against real particle mass data, focusing on the charged leptons:

```text
electron, muon, tau
```

The goal is not to prove the theory. The goal is to identify what currently works, what fails, and what must be improved before the framework can be called physically predictive.

## 2. Data used

The charged-lepton masses used in this report are:

| Particle | Symbol | Mass used |
|---|---:|---:|
| electron | e | 0.51099895000 MeV |
| muon | mu | 105.6583755 MeV |
| tau | tau | 1776.86 MeV |

Useful ratios:

| Ratio | Value |
|---|---:|
| muon / electron | 206.7682829877 |
| tau / muon | 16.8170293324 |
| tau / electron | 3477.2282800190 |

References:

- Particle Data Group: https://pdg.lbl.gov/
- Accessible overview of lepton generations: https://en.wikipedia.org/wiki/Lepton
- Koide formula overview: https://en.wikipedia.org/wiki/Koide_formula

## 3. Current MCIFT assumptions tested

The current toy model uses:

```math
\Psi(x,y,z,t,c)
```

where `c` is an internal channel coordinate.

Cluster complexity:

```math
C_n = 2^n
```

Coherence:

```math
Q_n = an
```

Stability:

```math
S_n = an - 2^n
```

Fractal catching surface:

```math
A_n = (C_n-1)^{D_f}
```

Finite Higgs response:

```math
H(C_n)=e^{-\frac{(C_n-C_\star)^2}{2\sigma_H^2}}
```

Mass rule:

```math
m_n = m_0 (C_n-1)^{D_f} H(C_n)\max(S_n,0)
```

Default locked values tested:

```text
a = 3.5
D_f = 3.5
C_star = 6
C_n = 2^n
```

## 4. Test 1: three stable modes and fourth-mode failure

Using:

```math
S_n = 3.5n - 2^n
```

we get:

| Mode | Complexity C_n | Coherence Q_n | Stability S_n | Outcome |
|---:|---:|---:|---:|---|
| 1 | 2 | 3.5 | +1.5 | survives |
| 2 | 4 | 7.0 | +3.0 | survives |
| 3 | 8 | 10.5 | +2.5 | survives |
| 4 | 16 | 14.0 | -2.0 | fails |
| 5 | 32 | 17.5 | -14.5 | fails hard |

### Result

This part works internally.

For the general condition:

```math
S_n = an - 2^n
```

exactly three modes survive and the fourth fails when:

```math
\frac{8}{3}<a<4
```

### Strength

The model naturally produces a three-generation-like cutoff from a simple conflict between linear coherence growth and binary complexity growth.

### Weakness

The parameter `a` is not yet derived from deeper physics. This is currently an internal structural result, not a verified physical mechanism.

## 5. Test 2: no-Higgs fractal surface only

This test removes the finite Higgs window and uses only:

```math
m_n = m_0(C_n-1)^{3.5}S_n
```

`m_0` is calibrated from the electron mass.

### Result

| Particle | Real mass | Predicted mass | Percent error |
|---|---:|---:|---:|
| electron | 0.510999 MeV | 0.510999 MeV | 0.000% |
| muon | 105.658376 MeV | 47.794112 MeV | -54.765% |
| tau | 1776.860000 MeV | 772.879694 MeV | -56.503% |

### Interpretation

The fractal catching surface alone is not enough.

### Strength

This failure is useful because it shows the finite Higgs-response window is not optional if the model wants to approach real charged-lepton masses.

### Weakness

Without the Higgs-response term, the model badly underpredicts both muon and tau masses.

## 6. Test 3: fixed MCIFT core with linear Gaussian Higgs response

This test keeps:

```text
a = 3.5
D_f = 3.5
C_star = 6
C_n = 2^n
```

and uses a linear Gaussian Higgs response:

```math
H(C_n)=e^{-\frac{(C_n-6)^2}{2\sigma_H^2}}
```

The electron and muon masses are used to calibrate `m_0` and `sigma_H`.

This gives:

```text
sigma_H = 2.7501384141
```

Then tau is predicted without using tau as input.

### Result

| Particle | Real mass | Predicted mass | Percent error |
|---|---:|---:|---:|
| electron | 0.510999 MeV | input | 0.000% |
| muon | 105.658376 MeV | input | 0.000% |
| tau | 1776.860000 MeV | 1708.604051 MeV | -3.841% |

### Interpretation

This is the first meaningful MCIFT numerical success.

A locked simple version of the model predicts tau within about 4 percent from electron and muon inputs.

### Strength

The model captures a large part of the charged-lepton hierarchy using a fixed complexity sequence and a finite Higgs-response window.

### Weakness

A 3.84 percent miss is much larger than experimental uncertainty. The model is interesting but not precision-level.

## 7. Test 4: fixed MCIFT core with log-fractal Gaussian Higgs response

This test keeps the same locked core:

```text
a = 3.5
D_f = 3.5
C_star = 6
C_n = 2^n
```

but uses a log-fractal Higgs response:

```math
H(C_n)=e^{-\frac{(\ln C_n-\ln 6)^2}{2w^2}}
```

The electron and muon masses are used to calibrate `m_0` and `w`.

This gives:

```text
w = 0.8106096177
```

Then tau is predicted without using tau as input.

### Result

| Particle | Real mass | Predicted mass | Percent error |
|---|---:|---:|---:|
| electron | 0.510999 MeV | input | 0.000% |
| muon | 105.658376 MeV | input | 0.000% |
| tau | 1776.860000 MeV | 1818.114580 MeV | +2.322% |

### Interpretation

The log-fractal Higgs response performs better than the linear Gaussian in this first test.

### Strength

Because MCIFT already assumes fractal complexity growth, a log-scale Higgs response may be more natural than a linear complexity Gaussian.

### Weakness

The prediction is still not precision-level. Also, the model has not yet derived why `w` should have this value.

## 8. Test 5: fitted MCIFT shape parameters

This test allows the model to fit all three charged-lepton masses by adjusting two shape parameters:

```text
D_f and sigma_H
```

with:

```text
a = 3.5
C_star = 6
C_n = 2^n
```

Using the linear Gaussian version, an exact fit gives approximately:

```text
D_f = 3.5462305773
sigma_H = 2.8426396770
```

### Result

The fitted value of `D_f` is close to the proposed structural value:

```math
D_f = 3.5
```

### Strength

The fitted fractal dimension landing near 3.5 is encouraging. It supports the idea that the proposed three-thread-plus-half-bond structure may be in the right numerical region.

### Weakness

This is not a prediction. It is a fit. A model that uses all three masses to fit parameters cannot claim to have predicted the tau mass.

## 9. Koide benchmark comparison

The charged leptons are known to approximately satisfy Koide's empirical relation:

```math
Q = \frac{m_e+m_\mu+m_\tau}{(\sqrt{m_e}+\sqrt{m_\mu}+\sqrt{m_\tau})^2}\approx \frac{2}{3}
```

Using the masses in this report:

```text
Q = 0.6666605115
```

Percent difference from `2/3`:

```text
-0.000923%
```

Solving Koide's formula using only electron and muon masses predicts:

```text
tau = 1776.969027 MeV
```

Real tau value used:

```text
tau = 1776.860000 MeV
```

Error:

```text
+0.109027 MeV
+0.006136%
```

### Interpretation

Koide currently beats MCIFT by a large margin as a charged-lepton mass relation.

### Strength for MCIFT

MCIFT is trying to explain why a square-root/fractal/coherence structure might exist underneath the charged-lepton hierarchy. Koide's success suggests that the charged-lepton masses do contain a deep geometric pattern.

### Weakness for MCIFT

MCIFT does not yet derive Koide's formula. Until it does, Koide remains a stronger empirical benchmark than the current MCIFT mass equation.

## 10. Black-hole channel claim

MCIFT proposes:

```math
T_{BH\rightarrow outside}\approx 0
```

meaning black holes are internal-channel confinement regions.

### Strength

The idea maps cleanly onto the standard qualitative fact that black-hole interiors are externally inaccessible beyond the event horizon.

### Weakness

No numerical black-hole test exists yet in MCIFT. The model currently does not predict a new black-hole observable, horizon radius, entropy relation, Hawking temperature, or gravitational-wave correction.

This part remains conceptual only.

## 11. Overall strengths

1. The model has a clean internal mechanism for three stable modes and fourth-mode failure.
2. A fixed-core version gets the tau mass within a few percent using electron and muon inputs.
3. The fitted fractal dimension lands close to the proposed value `D_f = 3.5`.
4. The finite Higgs-response window is mathematically useful and appears necessary.
5. The framework gives one language for particles, mass emergence, channel transfer, and black-hole confinement.

## 12. Overall weaknesses

1. The model is not yet derived from a Lagrangian or action.
2. The coherence parameter `a` is not derived.
3. The Higgs-response width is fitted, not predicted.
4. The current model does not beat the Koide relation.
5. The black-hole extension has no numerical test yet.
6. No Lorentz-invariant or gauge-invariant formulation exists yet.
7. The model has not been tested against quarks, neutrinos, bosons, decay rates, or scattering data.

## 13. Current verdict

MCIFT is promising as a speculative toy framework, but it is not yet a confirmed physical theory.

Best current description:

> MCIFT is an early-stage multi-channel information-field toy model that captures some charged-lepton mass hierarchy structure and naturally produces a three-mode stability cutoff, but it still requires a derived action, fewer fitted parameters, and sharper predictions.

## 14. Next tests

The next research steps should be:

1. Derive the channel-transfer rule from an energy functional.
2. Derive `a = 3.5` rather than choosing it.
3. Decide whether the Higgs response should be linear Gaussian or log-fractal Gaussian.
4. Attempt to derive Koide's formula from MCIFT geometry.
5. Use electron and muon only to predict tau with no adjustable post-hoc tuning.
6. Test whether cluster stability correlates with real lepton lifetimes.
7. Build a simulation that evolves clusters over channel space.

## 15. Bottom line

The real data does not validate MCIFT yet, but it also does not kill it.

The strongest positive result is:

```text
fixed-core MCIFT predicts tau within ~2.3% to ~3.8%, depending on Higgs-response form
```

The strongest negative result is:

```text
Koide predicts tau much more accurately, and MCIFT has not derived Koide yet
```

Therefore the next major goal is clear:

> Derive Koide-like square-root geometry from channel coherence and fractal cluster structure.
