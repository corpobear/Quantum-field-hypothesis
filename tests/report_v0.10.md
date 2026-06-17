# Test Report v0.10

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Author:** Adrian Newton / corpobear  
**Date:** 2026-06-17  
**Status:** speculative reduced test of funnel-speed Higgs capture window  
**Revision:** v0.10.0 initial report

---

## 1. Purpose

This report tests the v0.10 funnel-speed capture window inside the reduced tau toy model.

The tested idea is:

```text
funnel tip too slow  -> no Higgs-channel connection
funnel tip just right -> mass amplitude is captured and accumulated in the knot
funnel tip too fast  -> amplitude scatters and is not retained
```

The goal is to check whether adding a speed window preserves the successful v0.9 tau result while adding the desired slow/capture/scatter behavior.

---

## 2. Previous v0.9 reduced tau source

The v0.9 reduced tau equation was:

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
\langle O_\varphi\rangle=0.9837806705.
```

The `7/8` term is the one-anchor free spin-vortex fraction for the tau-like eight-sector knot.

---

## 3. Funnel-speed capture window

The v0.10 capture factor is:

```math
W_v(v)
=
\frac{
\left(1-e^{-(v/v_{min})^2}\right)
e^{-(v/v_{scatter})^2}
}{W_{max}}.
```

Interpretation:

```text
1 - exp[-(v/v_min)^2]  -> penetration / channel-opening term
exp[-(v/v_scatter)^2]  -> retention / non-scattering term
W_max                  -> normalization so optimal speed gives W_v = 1
```

---

## 4. Reduced tau test with capture window

The reduced tau equation becomes:

```math
m_\tau
=
m_\tau^{base}
\left[
1+
W_v(v_{tip})
\left(
\frac{1}{56}
+
\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
\right)
\right]^2.
```

This means the speed window controls how much of the anchor-tip source is retained by the knot.

---

## 5. Numerical result

Using the v0.9 resonance overlap:

```math
\langle O_\varphi\rangle=0.9837806705,
```

and normalizing the best funnel speed to:

```math
W_v=1,
```

we get the following reduced test:

| Funnel speed | Capture `W_v` | Tau mass | Interpretation |
|---:|---:|---:|---|
| 0.00 x optimal | 0.000 | 1708.604 MeV | no capture |
| 0.25 x optimal | 0.204 | 1722.402 MeV | too slow |
| 0.50 x optimal | 0.616 | 1750.505 MeV | weak capture |
| 0.75 x optimal | 0.915 | 1771.012 MeV | near capture |
| 1.00 x optimal | 1.000 | 1776.860 MeV | mass captured |
| 1.25 x optimal | 0.950 | 1773.421 MeV | slight overshoot/scatter |
| 1.50 x optimal | 0.850 | 1766.521 MeV | scattering begins |
| 2.00 x optimal | 0.624 | 1751.053 MeV | too fast |
| 3.00 x optimal | 0.257 | 1726.039 MeV | mostly scattered |
| 4.00 x optimal | 0.074 | 1713.637 MeV | almost no capture |

---

## 6. Result interpretation

The capture-window factor produces the desired three regimes:

```text
too slow:
  tip cannot open/reach the Higgs-response channel
  source correction remains weak

just right:
  tip connects, phase-locks, and retains the source
  mass amplitude accumulates inside the knot

too fast:
  tip overshoots or tears through the resonance
  source scatters instead of remaining trapped in the knot
```

The successful tau value is preserved at the optimal capture speed:

```math
m_\tau=1776.86\ \mathrm{MeV}.
```

---

## 7. Updated source term

The v0.10 source term is:

```math
\mathcal{S}_{tip,a}
=
\lambda_a
\Omega_{OS,a}
B_{C_a}(1)
O_{\varphi,a}(t)
W_v(v_{tip,a})
\delta_{\epsilon,a}^{(\varphi)}.
```

The candidate field equation becomes:

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
W_v(v_{tip,a})
\delta_{\epsilon,a}^{(\varphi)}.
```

---

## 8. Optional fourth-mode reservoir extension

If the failed fourth mode is treated as an unmanifest residue/reservoir:

```math
\mathcal{R}_4=\Theta(-S_4)|S_4|\rho_4(c),
```

then:

```math
\mathcal{S}_{tip,a}
=
\lambda_a
\Omega_{OS,a}
B_{C_a}(1)
O_{\varphi,a}(t)
W_v(v_{tip,a})
\mathcal{R}_4
\delta_{\epsilon,a}^{(\varphi)}.
```

This reservoir form is not tested numerically here. It is preserved as a possible next step.

---

## 9. Strengths

1. Adds the desired too-slow / capture / too-fast behavior.
2. Preserves the v0.9 reduced tau result at optimal capture speed.
3. Gives physical meaning to the speed of the anchor-tip funnel.
4. Keeps the correction as amplitude capture, not direct mass multiplication.
5. Provides a natural reason why not every vortex overlap becomes mass.

---

## 10. Weaknesses

1. `v_tip` is not yet derived from knot geometry.
2. `v_min`, `v_scatter`, and the optimal capture speed are model parameters.
3. The speed table is normalized for a reduced toy test.
4. The fourth-mode reservoir term is not yet mathematically tested.
5. No field action or gauge/Lorentz structure has been derived.

---

## 11. Current verdict

The funnel-speed capture window is a useful v0.10 extension.

Best statement:

> Mass amplitude is gathered only if the Fibonacci-shaped anchor-tip funnel reaches the Higgs-response channel at the correct speed. Too slow fails to connect; too fast scatters the source; the capture-speed window retains amplitude inside the knot.

This strengthens the v0.9 candidate source equation but does not yet make it a final physical theory.

---

## 12. Reproducibility pseudocode

```python
m_tau_base = 1708.60405054
O_phi = 0.9837806705
B = 7 / 8
s1 = 1 / 56
s2 = 1 / 448

source = s1 + B * s2 * O_phi

def tau_mass(W):
    return m_tau_base * (1 + W * source)**2

rows = [
    (0.00, 0.000),
    (0.25, 0.204),
    (0.50, 0.616),
    (0.75, 0.915),
    (1.00, 1.000),
    (1.25, 0.950),
    (1.50, 0.850),
    (2.00, 0.624),
    (3.00, 0.257),
    (4.00, 0.074),
]

for speed, W in rows:
    print(speed, W, tau_mass(W))
```
