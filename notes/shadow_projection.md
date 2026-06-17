# Shadow Projection Geometry

**Status:** speculative toy-model extension, v0.4.

This note records the shadow-projection update to the MCIFT toy model.

## Core idea

The earlier shadow-amplitude model introduced a complementary pattern:

$$
I_n^s
$$

and modeled mass as amplitude squared:

$$
m_n=A_n^2
$$

with:

$$
A_n=I_n-I_n^s
$$

The v0.4 update asks whether the fractional shadow correction should be treated as a projection geometry rather than a literal count of shadow objects.

## Koide angle clue

Koide's charged-lepton relation can be written as:

$$
\frac{A_1^2+A_2^2+A_3^2}{(A_1+A_2+A_3)^2}=\frac{2}{3}
$$

where:

$$
A_i=\sqrt{m_i}
$$

This is equivalent to saying that the charged-lepton amplitude vector:

$$
(\sqrt{m_e},\sqrt{m_\mu},\sqrt{m_\tau})
$$

lies at a 45-degree angle from the equal-amplitude direction:

$$
(1,1,1)
$$

Thus the number `2/3` may be a projection ratio produced by angle geometry, not a literal fraction of a shadow object.

## Tau shadow structure

For the tau-like third mode:

$$
C_3=2^3=8
$$

The primary shadow term is modeled as:

$$
s_1=\frac{1}{C_3(C_3-1)}=\frac{1}{8\cdot7}=\frac{1}{56}
$$

The first echo-shadow term is:

$$
s_2=\frac{s_1}{C_3}=\frac{1}{448}
$$

Then the amplitude correction is:

$$
\Delta(f)=1+s_1+fs_2
$$

where `f` is the echo-shadow projection fraction.

## Two-thirds projection test

A natural Koide-inspired first test is:

$$
f=\frac{2}{3}
$$

Then:

$$
\Delta_{2/3}=1+\frac{1}{56}+\frac{2}{3}\frac{1}{448}=1.0193452381
$$

Using the baseline MCIFT tau value:

$$
m_\tau^{base}=1708.60405054\ \text{MeV}
$$

and mass-as-amplitude-squared:

$$
m_\tau(f)=m_\tau^{base}\Delta(f)^2
$$

we get:

$$
m_\tau^{2/3}=1775.35017984\ \text{MeV}
$$

This is close to the observed tau input but slightly low.

## Exact fraction tests

The exact echo-shadow projection fraction needed to reach the observed tau input is:

$$
f_{obs}=0.8608080867
$$

The exact echo-shadow projection fraction needed to reach the Koide high-root tau value is:

$$
f_{Koide}=0.8748242267
$$

This is very close to:

$$
\frac{7}{8}=0.875
$$

Since the tau mode has:

$$
C_3=8
$$

this suggests a possible structural rule:

$$
f_3=1-\frac{1}{C_3}=\frac{7}{8}
$$

## Seven-eighths projection test

Input:

$$
f=\frac{7}{8}
$$

Then:

$$
\Delta_{7/8}=1+\frac{1}{56}+\frac{7}{8}\frac{1}{448}=1.0198102679
$$

and:

$$
m_\tau^{7/8}=1776.97039439\ \text{MeV}
$$

This is nearly identical to the Koide high-root tau value:

$$
m_\tau^{Koide}=1776.96902708\ \text{MeV}
$$

## Interpretation

The `2/3` fraction is important because it is the Koide projection ratio and corresponds to 45-degree amplitude geometry.

However, when inserted into the current tau shadow-echo formula, the stronger numerical match is not `2/3` but `7/8`.

This may mean:

```text
2/3 = global amplitude-angle projection
7/8 = local tau echo-shadow completion fraction
```

## Best summary

**The two-thirds shadow idea points toward Koide's 45-degree amplitude geometry. But the tau-specific echo-shadow correction is better matched by seven-eighths, which naturally equals one minus one over the tau knot complexity.**

## Caveat

This is a speculative toy-model result. The next step is to derive the echo-shadow fraction from knot geometry rather than selecting it to match Koide.
