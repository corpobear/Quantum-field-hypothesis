# Test Report v0.13

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Author:** Adrian Newton / corpobear  
**Date:** 2026-06-17  
**Status:** speculative reduced dark-manifest side-sink test  
**Revision:** v0.13.0 initial report

---

## 1. Purpose

This report tests whether the eight-sector knot/shadow geometry can produce a dark-manifest side-sink sector with a dark-to-visible matter ratio close to the observed cosmological dark-to-baryonic matter ratio.

The tested idea is:

```text
visible matter = axial drill/tip intake
dark-manifest matter = radial side/sink intake
```

---

## 2. Real-world comparison target

Using Planck 2018 cosmological values:

```math
\Omega_c h^2\approx0.120,
```

```math
\Omega_b h^2\approx0.0224,
```

so:

```math
\frac{\Omega_c}{\Omega_b}\approx\frac{0.120}{0.0224}=5.357142857.
```

This is the approximate target ratio for dark-manifest to visible-manifest matter in the toy model.

---

## 3. Eight-sector knot/shadow split

Use:

```math
C=8.
```

Split the eight sectors as:

```text
1 sector  = visible drill anchor / axial tip
1 sector  = opposite anti-tip / sink throat axis
6 sectors = lateral side-intake belt
```

Therefore:

```math
N_{side}=6.
```

---

## 4. Visible drill aperture

The visible/tip source aperture is:

```math
A_{tip}
=
\frac{1}{56}
+
\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle.
```

With:

```math
\langle O_\varphi\rangle=0.9837806705,
```

we get:

```math
A_{tip}=0.01977858948.
```

---

## 5. Dark side-sink aperture

The side-sink aperture uses six lateral sectors:

```math
A_{side}=6\left(\frac{1}{56}\right)=0.1071428571.
```

---

## 6. Reduced ratio result

Assuming equal coupling and optimal capture:

```math
\lambda_-\approx\lambda_+,
```

```math
W_{side}\approx W_{tip}\approx1,
```

```math
\kappa_{sink}\approx\Omega_z,
```

```math
R_4^{gate}\approx1,
```

then:

```math
\frac{\rho_{dark}}{\rho_{visible}}
\approx
\frac{A_{side}}{A_{tip}}.
```

So:

```math
\frac{\rho_{dark}}{\rho_{visible}}
=
\frac{0.1071428571}{0.01977858948}
=5.417.
```

---

## 7. Error versus target

Target:

```math
5.357142857.
```

Toy result:

```math
5.417.
```

Relative difference:

```math
\frac{5.417-5.357142857}{5.357142857}\approx0.0112.
```

or about:

```math
1.1\%.
```

The sink-efficiency correction needed to match the central target is:

```math
\epsilon_{sink}=\frac{5.357142857}{5.417}\approx0.989.
```

---

## 8. Field-source interpretation

Visible drill source:

```math
S_{visible}
=
\lambda_+
\Omega_z
W_{tip}
A_{tip}
R_4^{gate}
\delta_{tip}^{(\varphi)}.
```

Dark side-sink source:

```math
S_{dark}
=
-
\lambda_-
\kappa_{sink}
W_{side}
A_{side}
R_4^{gate}
\delta_{side}^{(\varphi)}.
```

where:

```math
\kappa_{sink}=-\nabla_\perp\cdot J_\perp.
```

The negative sign marks inverse field orientation, not negative mass.

Mass densities use magnitude:

```math
\rho_{visible}\propto |S_{visible}|,
```

```math
\rho_{dark}\propto |S_{dark}|.
```

Visibility differs by channel:

```math
L_{visible}\approx1,
```

```math
L_{dark}\approx0.
```

---

## 9. Verdict

The eight-sector knot/shadow geometry gives a strong first toy result.

Best statement:

> In the eight-sector knot/shadow model, visible matter uses one axial drill-tip intake, while dark-manifest matter uses six lateral side-intake sectors. The resulting side/tip aperture ratio is about 5.417, within about 1.1 percent of the Planck 2018 dark-to-baryonic matter density ratio.

This is not a proof of dark matter. It is a promising internal consistency test and should be preserved as a v0.13 candidate mechanism.

---

## 10. Reproducibility pseudocode

```python
O_phi = 0.9837806705
A_tip = 1/56 + (7/8) * (1/448) * O_phi
A_side = 6/56
ratio = A_side / A_tip
ratio_target = 0.120 / 0.0224
epsilon_sink = ratio_target / ratio
relative_error = (ratio - ratio_target) / ratio_target

print(A_tip)
print(A_side)
print(ratio)
print(ratio_target)
print(epsilon_sink)
print(relative_error)
```
