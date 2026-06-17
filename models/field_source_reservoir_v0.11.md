# Field-Source Reservoir Normalization v0.11

**Version:** v0.11 model supplement  
**Status:** speculative toy-model extension; not established physics  
**Purpose:** define a bounded reservoir-availability term for the integrated field-source equation.

---

## 1. Core idea

The fourth-mode sector may act like a very large supply of unmanifest amplitude. The mass equation should not use the raw size of that supply as a direct multiplier.

Instead, the fourth-mode sector is converted into a bounded availability factor.

```text
large fourth-mode supply -> availability
funnel aperture -> tiny captured fraction
Higgs resonance -> conversion condition
speed window -> capture or scatter
knot -> accumulated amplitude
mass -> squared amplitude
```

---

## 2. Bounded availability

Use:

$$
R_4^{gate}=\frac{R_4}{R_4+R_*}.
$$

This keeps:

$$
0\le R_4^{gate}\le1.
$$

If the fourth-mode supply is weak, `R_4^gate` is near zero.

If the fourth-mode supply is very large, `R_4^gate` approaches one.

So a large supply means full availability, not unbounded mass.

---

## 3. Tip aperture

The captured fraction is controlled by the finite anchor-tip aperture:

$$
A_{tip,C}=P_C+B_C(1)E_C\langle O_\varphi\rangle.
$$

For the tau-like eight-sector knot:

$$
P_8=\frac{1}{56},
$$

$$
E_8=\frac{1}{448},
$$

$$
B_8(1)=\frac{7}{8}.
$$

Therefore:

$$
A_{tip,8}=\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle.
$$

---

## 4. Source term

The v0.11 source term is:

$$
S_{tip,a}
=
\lambda_a
\Omega_{OS,a}
W_v(v_{tip,a})
\left[
P_{C_a}+B_{C_a}(1)E_{C_a}\langle O_{\varphi,a}\rangle
\right]
R_{4,a}^{gate}
\delta_{\epsilon,a}^{(\varphi)}.
$$

The candidate field equation is:

$$
\left(\partial_t^2-c_*^2\nabla^2-D_c\partial_c^2+V'(\psi)\right)\psi
=
\sum_a S_{tip,a}.
$$

---

## 5. Integrated source

Assume the finite Fibonacci-shaped core is normalized:

$$
\int \delta_{\epsilon,a}^{(\varphi)}\,du\,dv\,dc=1.
$$

Then:

$$
\Sigma_a
=
\lambda_a
\Omega_{OS,a}
W_v(v_{tip,a})
\left[
P_{C_a}+B_{C_a}(1)E_{C_a}\langle O_{\varphi,a}\rangle
\right]
R_{4,a}^{gate}.
$$

For the reduced tau test:

$$
\lambda_a\Omega_{OS,a}=1,
$$

so:

$$
\Sigma_\tau
=
W_v
\left[
\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
\right]
R_4^{gate}.
$$

The mass rule remains:

$$
m_\tau=m_\tau^{base}(1+\Sigma_\tau)^2.
$$

---

## 6. Interpretation

The reservoir is the supply.

The aperture, Higgs overlap, and speed window are the filters.

The knot receives only the filtered amplitude.

This makes the fourth-mode reservoir compatible with a finite mass result.

---

## 7. Open tasks

1. Derive `R_*` from field geometry.
2. Derive `R_4` from the failed fourth-mode sector.
3. Derive `lambda_a Omega_OS,a` instead of setting it to one in the reduced test.
4. Replace the normalized core assumption with an explicit finite Fibonacci-shaped profile.
5. Test the field-source equation beyond the tau-like reduced model.
