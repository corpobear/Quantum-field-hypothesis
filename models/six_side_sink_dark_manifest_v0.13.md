# Six-Side Sink Dark-Manifest Model v0.13

**Version:** v0.13 model supplement  
**Status:** speculative toy-model extension; not established physics  
**Purpose:** test whether the eight-sector knot/shadow geometry can produce a dark-manifest side-sink sector with a dark-to-visible ratio close to the observed dark-to-baryonic matter ratio.

---

## 1. Motivation

v0.12 introduced channel-separated activation terminology:

```text
visible-manifest = light-active, mass-active, gravity-active, knot-coherent
dark-manifest    = light-inactive, mass-active, gravity-active, knot-coherent
unmanifest       = no stable visible, mass, or gravitational projection
```

v0.13 tests a possible dark-manifest mechanism.

Visible matter is modeled as an axial drill/tip intake:

```text
one anchor-tip collector
-> source enters through the drill-like tip
-> light/electromagnetic channel can remain active
```

Dark-manifest matter is modeled as the inverse side-fed sink:

```text
six lateral side sectors
-> source flows inward from the sides like water entering a sink
-> mass/gravity remain active
-> light/electromagnetic channel is suppressed
```

---

## 2. Eight-sector knot/shadow geometry

Use the tau-like eight-sector knot:

$$
C=8.
$$

The one-point original/shadow anchor pins one sector and leaves the familiar free circulation fraction:

$$
B_8(1)=\frac{7}{8}.
$$

For the side-sink test, split the eight sectors as:

```text
1 sector  = visible drill anchor / axial tip
1 sector  = opposite anti-tip / sink throat axis
6 sectors = lateral side-intake belt
```

Thus:

$$
N_{side}=8-2=6.
$$

---

## 3. Visible drill aperture

The visible drill/tip aperture is the v0.11 tau-like source aperture:

$$
A_{tip}
=
\frac{1}{56}
+
\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle.
$$

Using the v0.9/v0.11 resonance overlap:

$$
\langle O_\varphi\rangle=0.9837806705,
$$

this gives:

$$
A_{tip}=0.01977858948.
$$

---

## 4. Dark side-sink aperture

The dark-manifest sink is side-fed by the six lateral sectors.

Use the same primary sector unit:

$$
\frac{1}{56}.
$$

Then:

$$
A_{side}=6\left(\frac{1}{56}\right)=\frac{6}{56}=0.1071428571.
$$

The sink source has inverse orientation:

$$
S_{dark}<0
$$

as a field orientation, but mass density uses magnitude:

$$
\rho_{dark}\propto |S_{dark}|.
$$

So the model does not produce negative mass.

---

## 5. Field-source split

Visible drill source:

$$
S_{visible}
=
\lambda_+
\Omega_z
W_{tip}
A_{tip}
R_4^{gate}
\delta_{tip}^{(\varphi)}.
$$

Dark side-sink source:

$$
S_{dark}
=
-
\lambda_-
\kappa_{sink}
W_{side}
A_{side}
R_4^{gate}
\delta_{side}^{(\varphi)}.
$$

where:

$$
\kappa_{sink}=-\nabla_\perp\cdot J_\perp.
$$

A positive `kappa_sink` means inward radial convergence into the side-fed sink.

Mass densities:

$$
\rho_{visible}\propto |S_{visible}|,
$$

$$
\rho_{dark}\propto |S_{dark}|.
$$

Visibility factors:

$$
L_{visible}\approx1,
$$

$$
L_{dark}\approx0.
$$

---

## 6. Dark-to-visible ratio

Assume the first reduced test uses equal coupling, optimal capture, saturated reservoir availability, and comparable vortex/sink strengths:

$$
\lambda_-\approx\lambda_+,
$$

$$
W_{side}\approx W_{tip}\approx1,
$$

$$
R_4^{gate}\approx1,
$$

$$
\kappa_{sink}\approx\Omega_z.
$$

Then:

$$
\frac{\rho_{dark}}{\rho_{visible}}
\approx
\frac{A_{side}}{A_{tip}}.
$$

So:

$$
\frac{\rho_{dark}}{\rho_{visible}}
=
\frac{6/56}{1/56+(7/8)(1/448)\langle O_\varphi\rangle}.
$$

Using:

$$
\langle O_\varphi\rangle=0.9837806705,
$$

gives:

$$
\frac{\rho_{dark}}{\rho_{visible}}=5.417.
$$

---

## 7. Comparison to cosmological ratio

The Planck 2018 cosmological parameters give approximately:

$$
\Omega_c h^2\approx0.120,
$$

$$
\Omega_b h^2\approx0.0224.
$$

Thus:

$$
\frac{\Omega_c}{\Omega_b}\approx\frac{0.120}{0.0224}\approx5.36.
$$

The eight-sector side-sink geometry gives:

$$
5.417,
$$

which is within about:

$$
1.1\%
$$

of the target ratio.

A small sink-efficiency factor can match the central value:

$$
\epsilon_{sink}
=
\frac{5.36}{5.417}
\approx0.989.
$$

---

## 8. Interpretation

The result suggests a possible toy-model mechanism:

```text
visible matter:
  one axial anchor-tip drill collector
  narrow tip intake
  light/electromagnetic channel active

dark-manifest matter:
  six lateral side sectors in an eight-sector knot/shadow pair
  radial sink intake
  mass/gravity active
  light/electromagnetic channel suppressed
```

This is not a proof of dark matter. It is an internal toy-model consistency result: the eight-sector knot/shadow geometry naturally produces a side/tip aperture ratio close to the observed dark-to-baryonic matter ratio.

---

## 9. Open tasks

1. Derive the six-side split from explicit knot/shadow geometry.
2. Derive `kappa_sink` from the radial flow field.
3. Determine whether `epsilon_sink` has a geometric or dynamical origin.
4. Test whether the ratio survives for non-tau-like knots.
5. Test whether dark-manifest knots reproduce gravitational behavior without electromagnetic visibility.
6. Connect the side-sink mechanism to galaxy-scale dark matter distributions only after a field-density model is derived.
