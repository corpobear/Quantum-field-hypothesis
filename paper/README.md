# Paper Folder Index

This folder contains the main MCIFT draft and paper-style addenda.

**Status:** speculative theoretical framework / toy field model; not established physics.

---

## Files

```text
main.md                                      Full theory draft with v0.22 status note
v0.22_cosmology_comparison_addendum.md       MCIFT vs Lambda-CDM / standard-model comparison and current strengths/weaknesses
v0.13_six_side_sink_dark_manifest_addendum.md Six-side sink dark-manifest geometry addendum
v0.12_activation_terminology_addendum.md     Activation terminology and dark-manifest matter addendum
v0.11_field_source_reservoir_addendum.md     Bounded fourth-mode reservoir and integrated field-source addendum
v0.7_shadow_anchor_derivation.md             One-point shadow-anchor paper addendum
```

---

## Latest addendum: v0.22 cosmology comparison

The v0.22 addendum summarizes the current cosmology scaffold and compares MCIFT with both:

```text
1. Standard Model of particle physics
2. Lambda-CDM standard cosmology
```

The addendum distinguishes what MCIFT can safely claim from what remains unproved.

Safe current statement:

```text
MCIFT v0.22 is compatible with a standard growth-transfer layer while supplying
a derived anchor/acoustic modulation that preserves a BAO-like scale.
```

Critical caveat:

```text
v0.22 imports the broadband growth-transfer layer from existing cosmology.
MCIFT has not yet independently derived T_growth(k).
```

Key v0.22 result summary:

```text
raw MCIFT geometric global peak = 152.29 Mpc
raw MCIFT BAO-window peak = 152.29 Mpc
shape RMS log residual after growth-transfer scaffold = 0.004
shape verdict = PASS-LIKE
```

Read:

```text
paper/v0.22_cosmology_comparison_addendum.md
```

---

## Current strengths and weaknesses

### Strengths

```text
- MCIFT has explicit visible-manifest and dark-manifest channel mechanics.
- The anchor radius, cutoff, lock amplitude, and envelope are now derived in the toy scaffold.
- The model repeatedly produces a BAO-like scale in proxy tests.
- v0.22 shows compatibility with standard broadband growth-transfer physics.
```

### Weaknesses

```text
- MCIFT remains speculative and unvalidated.
- T_growth(k) is imported in v0.22, not derived from MCIFT.
- CMB spectra, BBN, lensing, halos, and dark-energy behavior are not yet solved.
- No fair likelihood or parameter-count comparison against Lambda-CDM has been completed.
```

---

## Previous addendum: v0.13

The v0.13 addendum tests a six-side sink geometry for dark-manifest matter.

Visible-manifest matter is modeled as a one-sector axial tip intake:

$$
A_{tip}=\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle.
$$

Dark-manifest matter is modeled as six lateral side intakes:

$$
A_{side}=6\left(\frac{1}{56}\right).
$$

Using:

$$
\langle O_\varphi\rangle=0.9837806705,
$$

the reduced ratio is:

$$
\frac{A_{side}}{A_{tip}}=5.417.
$$

The Planck 2018 comparison target is approximately:

$$
\frac{\Omega_c}{\Omega_b}\approx\frac{0.120}{0.0224}=5.357.
$$

A small efficiency factor:

$$
\epsilon_{sink}\approx0.989
$$

matches the central target.

---

## Previous addendum: v0.12

The v0.12 addendum clarifies activation terminology.

Use:

```text
light activation = electromagnetic / visibility-channel activation
```

Do not use:

```text
light activation = existence itself
```

The addendum separates channel factors:

$$
L_i=\text{light / electromagnetic visibility activation}
$$

$$
H_i=\text{Higgs / mass-capture activation}
$$

$$
G_i=\text{gravitational projection}
$$

$$
K_i=\text{knot coherence}
$$

with:

$$
\mathrm{Visibility}_i=L_iK_i
$$

$$
\mathrm{Mass}_i=H_iK_i
$$

$$
\mathrm{Gravity}_i=G_iH_iK_i.
$$

This introduces the term `dark-manifest` for mass-bearing, gravity-projecting, knot-coherent structures with suppressed light/electromagnetic activation:

$$
L_i\approx0,\quad H_i>0,\quad G_i>0,\quad K_i>0.
$$

---

## Previous addendum: v0.11

The v0.11 addendum introduces a bounded fourth-mode reservoir availability factor:

$$
R_4^{gate}=\frac{R_4}{R_4+R_*}.
$$

The purpose is to let the fourth-mode sector act as a large available supply without letting raw reservoir size directly multiply the mass result.

The reduced integrated field-source test uses:

$$
\Sigma_\tau
=
W_v
\left[
\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
\right]
R_4^{gate}
$$

and:

$$
m_\tau=m_\tau^{base}(1+\Sigma_\tau)^2.
$$

At saturated availability and optimal funnel capture, the reduced tau-like test gives:

$$
m_\tau=1776.86\ \mathrm{MeV}.
$$
