# Toy Model Equations

This file collects the current toy-model math for the Multi-Channel Information Field Theory framework.

**Version:** v0.2 vibration, information-exchange, and shadow-amplitude update.

## 1. Field variable

The field is written as:

```math
\Psi(x,y,z,t,c)
```

where:

- `x,y,z` are spatial coordinates,
- `t` is time,
- `c` is an internal channel coordinate.

Possible channels include identity, light, Higgs response, phase, charge, knot structure, exchange-rate structure, shadow/complementary amplitude, and black-hole confinement.

## 2. Cluster complexity

The simplest complexity growth law is binary:

```math
C_n = 2^n
```

This gives:

| Mode | Complexity |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

Interpretation: each higher mode doubles the information burden.

## 3. Coherence and stability

A simple coherence law:

```math
Q_n = an
```

Original stability:

```math
S_n = Q_n - C_n = an - 2^n
```

Survival condition:

```math
S_n > 0
```

Failure condition:

```math
S_n < 0
```

Exactly three stable modes and fourth failure require:

```math
\frac{8}{3}<a<4
```

Example with `a = 3.5`:

| Mode | Complexity | Coherence | Stability | Outcome |
|---:|---:|---:|---:|---|
| 1 | 2 | 3.5 | +1.5 | survives |
| 2 | 4 | 7.0 | +3.0 | survives |
| 3 | 8 | 10.5 | +2.5 | survives |
| 4 | 16 | 14.0 | -2.0 | fails |

## 4. Fractal catching surface

Cluster catching surface:

```math
A_n = (C_n-1)^{D_f}
```

Proposed fractal dimension:

```math
D_f = 3.5 + \epsilon
```

where `3.5` is interpreted as a three-thread core plus half-dimensional bond:

```math
D_f = 3 + \frac{1}{2}
```

## 5. Finite Higgs response

Linear complexity Gaussian:

```math
H(C_n)=e^{-\frac{(C_n-C_\star)^2}{2\sigma_H^2}}
```

Log-fractal Gaussian:

```math
H(C_n)=e^{-\frac{(\ln C_n-\ln C_\star)^2}{2w^2}}
```

Interpretation: Higgs response is finite and windowed. It does not give infinite mass as complexity grows.

## 6. Original mass formula

Original toy formula:

```math
m_n = m_0 A_n H(C_n)\max(S_n,0)
```

Expanded:

```math
m_n = m_0 (C_n-1)^{D_f}
H(C_n)
\max(an-2^n,0)
```

with:

```math
C_n=2^n
```

## 7. Law of vibration and information exchange

The v0.2 model treats knots as internally moving structures.

Internal movement creates vibration. Similar information-points vibrating at compatible frequencies open stronger internal communication channels.

Pairwise exchange rate:

```math
\Gamma_{ij}
=
g
\exp\left[-\frac{(I_i-I_j)^2}{2\sigma_I^2}\right]
\exp\left[-\frac{(\omega_i-\omega_j)^2}{2\sigma_\omega^2}\right]
\cos^2(\phi_i-\phi_j)
```

where:

- `I_i-I_j` measures information mismatch,
- `omega_i-omega_j` measures vibration-frequency mismatch,
- `phi_i-phi_j` measures phase mismatch,
- `g` is base exchange strength.

Knot-level exchange rate:

```math
\Gamma_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}
```

Exchange/densification factor:

```math
X_n=e^{\eta\Gamma_n}
```

Weak-exchange approximation:

```math
X_n\approx1+\eta\Gamma_n
```

## 8. Exchange-updated stability

The original stability was:

```math
S_n=3.5n-2^n
```

The exchange-updated stability is:

```math
S_n=3.5nX_n-2^n
```

Interpretation:

```text
resonant exchange strengthens coherence, but complexity still fights back
```

Mode 4 still fails if:

```math
S_4=14X_4-16<0
```

Therefore:

```math
X_4<1.1428571429
```

or:

```math
\eta\Gamma_4<0.1335313926
```

## 9. Exchange-updated mass formula

The v0.2 exchange-rate mass formula is:

```math
m_n=m_0(C_n-1)^{D_f}X_nH(C_n)\max(S_n,0)
```

with:

```math
S_n=3.5nX_n-C_n
```

and:

```math
C_n=2^n
```

The key difference from v0.1 is that `X_n` affects both:

```text
densification
and
stability/coherence
```

## 10. Shadow/complementary amplitude extension

The v0.2 shadow-amplitude extension introduces a complementary inverted information pattern for each visible information cluster.

Visible cluster:

```math
I_n
```

Complementary pattern:

```math
I_n^s
```

Full knot state:

```math
K_n=(I_n,I_n^s)
```

Mass amplitude:

```math
A_n=I_n-I_n^s
```

Mass:

```math
m_n=A_n^2
```

This suggests that the deepest toy model should calculate amplitude first:

```math
A_n=\sqrt{m_n}
```

and then square into mass.

## 11. Amplitude correction form

Let the base MCIFT model produce:

```math
m_n^{base}
```

Base amplitude:

```math
A_n^{base}=\sqrt{m_n^{base}}
```

Introduce a visible/complementary amplitude correction:

```math
\Delta_n
```

Then:

```math
A_n=A_n^{base}\Delta_n
```

and:

```math
m_n=m_n^{base}\Delta_n^2
```

This matters because small amplitude corrections become larger mass corrections after squaring.

## 12. Relation to Koide-style amplitude geometry

Koide's charged-lepton relation is naturally written in amplitude space:

```math
\frac{A_1^2+A_2^2+A_3^2}{(A_1+A_2+A_3)^2}=\frac{2}{3}
```

where:

```math
A_i=\sqrt{m_i}
```

The v0.2 shadow-amplitude extension suggests that MCIFT should try to derive this square-root mass geometry from knot structure rather than fitting final masses directly.

## 13. Channel transfer law

For an incoming cluster `i` and receiving surface `s`:

```math
T_{i\rightarrow s}
=
Q_iQ_s
 e^{-\frac{(C_i-C_s)^2}{2\sigma_C^2}}
 e^{-\frac{(m_i-m_s)^2}{2\sigma_m^2}}
```

Transfer is strongest when:

- both systems are coherent,
- complexity mismatch is small,
- mass/ripple-weight mismatch is small.

The exchange-rate extension suggests an additional dependency:

```math
T_{i\rightarrow s}\propto X_iX_s
```

when internal vibration and phase coherence support transfer.

## 14. Core model chain

v0.1 chain:

```text
information cell
-> coherent cluster
-> light activation
-> Higgs response
-> mass
```

v0.2 chain:

```text
information cell
-> coherent knot cluster
-> internal vibration
-> information exchange rate
-> resonant densification
-> visible/complementary amplitude imbalance
-> Higgs response
-> squared mass
```

Failure path:

```text
over-complex cluster
-> exchange overload or coherence failure
-> delocalized/background-forming mode
```

Black-hole path:

```text
extreme coherent complexity
-> internal channel formation
-> external channel transfer suppressed
```

## 15. Status

The toy model currently explains structural patterns but does not yet provide a full quantum field Lagrangian or precision mass prediction.

The v0.2 additions improve the mechanism by introducing:

- vibration-driven information exchange,
- exchange-driven densification,
- exchange-updated stability,
- shadow/complementary amplitude correction,
- a possible bridge to Koide's square-root mass geometry.

The next mathematical task is to derive `Gamma_n` and `Delta_n` from a concrete knot geometry rather than fitting them after seeing the charged-lepton masses.
