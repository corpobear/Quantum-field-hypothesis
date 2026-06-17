# Funnel-Speed Capture Window v0.10

**Version:** v0.10 model supplement  
**Status:** speculative toy-model extension; not established physics  
**Purpose:** add a capture-window condition to the Fibonacci-Higgs anchor-tip source equation: too slow fails to connect, resonant speed captures mass amplitude, too fast scatters the source.

---

## 1. Motivation

The v0.9 candidate source equation treats mass amplitude as gathered at original/shadow anchor-tip vortices when the Fibonacci-shaped tip overlaps the Higgs-response resonance.

v0.10 adds a speed condition:

```text
too slow  -> tip does not reach / open the Higgs-response channel
just right -> tip connects, phase-locks, and mass amplitude accumulates in the knot
too fast  -> source overshoots/scatters and is not retained by the knot
```

This introduces a Goldilocks-style capture window for the funnel tip.

---

## 2. Anchor-tip source from v0.9

The v0.9 source term was:

$$
\mathcal{S}_{tip,a}
=
\lambda_a
\Omega_{OS,a}
B_{C_a}(1)
O_{\varphi,a}(t)
\delta_{\epsilon,a}^{(\varphi)}.
$$

where:

- `lambda_a` is anchor coupling strength,
- `Omega_OS,a` is original/shadow vortex curl,
- `B_Ca(1)` is the one-anchor free circulation fraction,
- `O_phi,a(t)` is the Fibonacci-Higgs resonance overlap,
- `delta_epsilon,a^(phi)` is the finite Fibonacci-shaped source core.

---

## 3. Funnel-speed capture window

Let:

$$
v_{tip,a}
$$

be the effective speed of the anchor-tip funnel.

A simple normalized capture window is:

$$
W_v(v)
=
\frac{
\left(1-e^{-(v/v_{min})^2}\right)
e^{-(v/v_{scatter})^2}
}{W_{max}}.
$$

where:

- `v_min` controls the slow-speed penetration threshold,
- `v_scatter` controls high-speed scattering/overshoot,
- `W_max` normalizes the maximum of `W_v` to 1.

Interpretation:

```text
1 - exp[-(v/v_min)^2]     = penetration / channel-opening term
exp[-(v/v_scatter)^2]     = retention / non-scattering term
W_max                     = normalization so the best speed has W_v = 1
```

---

## 4. Three regimes

### Too slow

When:

$$
v_{tip}\ll v_{min},
$$

then:

$$
W_v(v_{tip})\approx0.
$$

The funnel does not reach or open the Higgs-response channel.

### Capture speed

At the optimal speed:

$$
v_{tip}\approx v_{cap},
$$

then:

$$
W_v(v_{tip})\approx1.
$$

The tip connects, resonance overlap is retained, and mass amplitude accumulates in the knot.

### Too fast

When:

$$
v_{tip}\gg v_{scatter},
$$

then:

$$
W_v(v_{tip})\rightarrow0.
$$

The funnel overshoots or tears through the resonance window, so amplitude scatters into the field rather than accumulating in the knot.

---

## 5. Updated source equation

The v0.10 source term is:

$$
\mathcal{S}_{tip,a}
=
\lambda_a
\Omega_{OS,a}
B_{C_a}(1)
O_{\varphi,a}(t)
W_v(v_{tip,a})
\delta_{\epsilon,a}^{(\varphi)}.
$$

The candidate field equation becomes:

$$
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
$$

---

## 6. Optional fourth-mode reservoir form

If the failed fourth mode is treated as an unmanifest residue/reservoir, define:

$$
\mathcal{R}_4=\Theta(-S_4)|S_4|\rho_4(c).
$$

Then the source becomes:

$$
\mathcal{S}_{tip,a}
=
\lambda_a
\Omega_{OS,a}
B_{C_a}(1)
O_{\varphi,a}(t)
W_v(v_{tip,a})
\mathcal{R}_4
\delta_{\epsilon,a}^{(\varphi)}.
$$

Interpretation:

```text
failed fourth-mode residue = unmanifest amplitude reservoir
Higgs response = conversion gate
funnel speed = capture/scatter condition
anchor-tip vortex = localized source inlet
```

This reservoir form is more speculative and should be tested separately.

---

## 7. Reduced tau toy form

In the reduced tau test, the capture window multiplies the full anchor-tip source correction:

$$
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
$$

This preserves the amplitude-first rule:

$$
m=A^2.
$$

---

## 8. Conceptual chain

```text
original/shadow spin
-> one-point anchor
-> Fibonacci-shaped funnel tip
-> tip speed increases
-> Higgs resonance capture window
-> too slow: no connection
-> just right: mass amplitude accumulates
-> too fast: amplitude scatters
-> squared mass
```

---

## 9. Caveats

This is a toy-model capture condition, not established physics.

Open tasks:

1. Derive `v_tip` from knot spin geometry.
2. Derive `v_min`, `v_scatter`, and `v_cap` from the Higgs/channel resonance structure.
3. Test whether different generations occupy different capture-window positions.
4. Determine whether the fourth-mode residue term is mathematically necessary or only interpretive.
5. Derive the full equation from a variational principle or field action.
