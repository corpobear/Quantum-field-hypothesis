# MCIFT v0.92 Bubble Light-Cone Test Report

**Status:** model-level light-cone construction and retest for the diagonal causal net.

## 1. Question tested

Can the diagonal causal net be interpreted through a bubble geometry where a center event, a 2D surface coordinate, and the radial distance between them construct a light cone?

## 2. Mechanics update

A center event is:

```text
C_i = (x_i, t_i)
```

A bubble surface point is:

```text
X_i(theta, phi, t) = x_i + r_i(theta, phi, t) n(theta, phi)
```

For flat light motion:

```text
r_i = c Delta t
```

Thus:

```text
||X_i - x_i|| - c Delta t = 0
```

This is the model light-cone condition.

## 3. Bubble surface and loops

At fixed time, the light boundary is a closed 2D surface.

Closed paths on that surface allow loop holonomy tests.

The surface-loop phase is assigned from radial strain:

```text
theta_bubble(n) = beta [1 - rho(n)]
```

and:

```text
R_gamma = theta_1 + theta_2 - theta_3 - theta_4
```

## 4. Diagonal projection

The v0.89 diagonal net supplies sampling directions. The bubble radius in direction `n` is controlled by:

```text
rho(n)^2 = n^T q_inv n
r(n,t) = c Delta t rho(n)
```

Flat case:

```text
rho = 1
```

Single-defect case:

```text
w = [0.5,1,1,1]
rho_min = sqrt(0.625) = 0.790569415042
```

## 5. Retest results

Flat bubble:

```text
rho_min = 1
rho_max = 1
light-cone residual = 0
null residual = 0
loop R = 0
```

Single-defect bubble:

```text
rho_min = 0.790569415042
rho_max = 1
bubble anisotropy = 0.264911064067
normalized light-cone residual = 0.209430584958
normalized null residual = 0.375
loop R = 0.209430584958 rad
```

## 6. Interpretation

The flat test confirms that the bubble construction produces the model light-cone condition exactly.

The defect test confirms that suppressing one diagonal pulls the bubble surface inward in that direction and produces a nonzero surface-loop phase.

This connects the loop mechanism to a closed 2D bubble surface rather than to an arbitrary lattice square.

## 7. What is proven inside the model

```text
center + 2D surface + radial distance gives the cone condition
flat bubble satisfies r = c Delta t
surface loops can carry closure defects
single diagonal defect deforms the bubble and produces nonzero loop phase
```

## 8. What is not claimed

```text
not an empirical proof that physical spacetime is a bubble
not a derivation of full general relativity
not a replacement for QFT or GR
```

## 9. Next

v0.93 should test localized bubble defects across multiple neighboring cells and compare the small-strain limit with the v0.80/v0.81 weak-field bridge.
