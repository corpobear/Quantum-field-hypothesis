# Fourth-Mode Reservoir Normalization Note

**Status:** speculative note; not established physics  
**Version:** v0.11

---

## Core idea

The fourth-mode reservoir is treated as a very large supply of unmanifest amplitude.

The model should not use the raw size of that reservoir as a mass multiplier. Instead, it should use a bounded availability factor:

```math
R_4^{gate}=\frac{R_4}{R_4+R_*}.
```

This gives:

```math
0\le R_4^{gate}\le1.
```

So if the reservoir is very large, the equation reads it as full availability:

```math
R_4^{gate}\approx1.
```

not infinite mass.

---

## Interpretation

```text
reservoir = supply
funnel tip = aperture
Higgs overlap = conversion condition
speed window = capture/scatter filter
knot = storage structure
mass = squared accumulated amplitude
```

The reservoir provides what could be gathered. The funnel decides what actually enters the knot.

---

## Source contribution

The reduced source contribution is:

```math
\Sigma
=
W_v
\left[P_C+B_C(1)E_C\langle O_\varphi\rangle\right]
R_4^{gate}.
```

For the tau-like eight-sector knot:

```math
\Sigma_\tau
=
W_v
\left[
\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle\right]
R_4^{gate}.
```

Then:

```math
m_\tau=m_\tau^{base}(1+\Sigma_\tau)^2.
```

---

## Why this matters

If the raw fourth-mode reservoir were used directly, the toy model would overshoot the tau-like mass. The bounded gate avoids that by separating supply from captured fraction.

The fourth-mode sector becomes an available background, not the measured mass itself.

---

## Current toy result

At:

```math
W_v=1,
```

```math
R_4^{gate}=1,
```

```math
\langle O_\varphi\rangle=0.9837806705,
```

the reduced tau-like field-source test gives:

```math
m_\tau=1776.86\ \mathrm{MeV}.
```

---

## Next derivation targets

1. Derive the saturation scale `R_*`.
2. Derive reservoir strength `R_4` from failed fourth-mode geometry.
3. Derive the funnel aperture terms `P_C` and `E_C`.
4. Replace the normalized source core with an explicit finite Fibonacci profile.
5. Connect the reservoir flow to a possible local time-vector only after the source equation is better constrained.
