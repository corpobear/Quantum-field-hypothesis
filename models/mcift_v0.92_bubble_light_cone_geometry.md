# MCIFT v0.92 Bubble Light-Cone Projection

**Status:** speculative mechanics update for the v0.89 diagonal causal net; this is a model construction, not an empirical proof of spacetime or general relativity.

## 1. Purpose

v0.91 tested loop closure and wave-packet anisotropy in the diagonal net. v0.92 adds the missing geometric interpretation:

```text
A light cone is the time-history of a 2D causal bubble surface expanding from a center event.
```

The bubble is defined by:

```text
center coordinate
2D surface coordinate
radial distance between center and surface
```

If light is projected from the center to the expanding bubble surface, the surface history forms a cone.

## 2. Center event

For cell `i`, define the center event:

```text
C_i = (x_i, t_i)
```

where:

```text
x_i = cube-center position
t_i = local event time
```

The existing MCIFT timing variable `T_i` remains the local clock/response coordinate.

## 3. Bubble surface coordinate

A point on the causal bubble surface is:

```text
X_i(theta, phi, t) = x_i + r_i(theta, phi, t) * n(theta, phi)
```

where:

```text
theta, phi = 2D surface coordinates
n(theta, phi) = unit surface direction
r_i = center-to-surface radial distance
```

For a flat light bubble:

```text
r_i(theta, phi, t) = c * (t - t_i)
```

Therefore:

```text
||X_i - x_i|| = c * (t - t_i)
```

This is the bubble form of the light-cone condition.

## 4. Bubble line element

Use the spherical light-cone metric form:

```text
ds^2 = -c^2 dt^2 + dr^2 + r^2 dOmega^2
```

with:

```text
dOmega^2 = dtheta^2 + sin^2(theta) dphi^2
```

For radial light motion, `dOmega = 0`, so:

```text
ds^2 = -c^2 dt^2 + dr^2
```

The light condition is:

```text
ds^2 = 0  ->  dr = c dt  ->  r = c Delta t
```

Thus the cone is the sequence of bubble surfaces whose radius grows at speed `c`.

## 5. Projection of the diagonal causal net onto the bubble

The diagonal net gives local sampling directions:

```text
d_a, a = 1..4
```

with antipodal partners `-d_a`.

At time `t`, each diagonal ray intersects the bubble at:

```text
X_{i,a,+}(t) = x_i + r_i(d_a,t) * d_a
X_{i,a,-}(t) = x_i - r_i(d_a,t) * d_a
```

The diagonal net is therefore the internal skeleton; the bubble surface is the causal boundary.

## 6. Bubble radius from diagonal weights

Let the diagonal metric scaffold from v0.89 be:

```text
q_inv[i] = (3/4) * sum_a w_Delta[i,a] * d_a d_a^T
```

For a surface direction `n`, define effective channel strength:

```text
rho_i(n)^2 = n^T q_inv[i] n
```

The effective bubble radius in that direction is:

```text
r_i(n,t) = c * Delta t * rho_i(n)
```

Flat case:

```text
rho_i(n) = 1
r_i = c Delta t
```

Defected case:

```text
rho_i(n) < 1 in a weakened direction
```

This locally pulls the bubble surface inward and creates a light-cone deformation in the model.

## 7. Bubble light-cone residual

Define:

```text
E_LC(n,t) = ||X_i(n,t) - x_i|| - c Delta t
```

For a flat light bubble:

```text
E_LC = 0
```

For a diagonal defect:

```text
E_LC != 0 in affected directions
```

Also define the null-interval residual:

```text
E_null(n,t) = r_i(n,t)^2 - c^2 Delta t^2
```

Flat light bubble:

```text
E_null = 0
```

Defected bubble:

```text
E_null < 0 for inward compression
```

## 8. Why loops exist

At fixed time, the causal boundary is a 2D closed surface.

Surface coordinates can form closed paths:

```text
(theta, phi) -> closed loop -> (theta, phi)
```

Therefore the loop closure test is not arbitrary: it is a path around the 2D causal bubble surface.

A loop phase can be assigned from radial strain:

```text
theta_bubble(n) = beta * [1 - rho_i(n)]
```

Then a closed four-edge surface loop has:

```text
R_gamma = theta_1 + theta_2 - theta_3 - theta_4
```

Flat bubble:

```text
rho = 1, theta_bubble = 0, R_gamma = 0
```

Defected bubble:

```text
rho differs by direction, R_gamma != 0
```

## 9. Mechanics update loop

At each simulation step:

```text
1. Read center event C_i = (x_i, t_i).
2. Read local MCIFT state K_i, phi_i, T_i, q_i, m_i, Coh_i, S_i.
3. Build diagonal weights w_Delta[i,a].
4. Build q_inv[i] from the diagonal weights.
5. Sample bubble directions n(theta, phi), including the diagonal rays.
6. Compute rho_i(n)^2 = n^T q_inv[i] n.
7. Compute r_i(n,t) = c Delta t rho_i(n).
8. Compute light-cone residual E_LC and null residual E_null.
9. Project diagonal rays to surface points X_i(n,t).
10. Build closed surface loops.
11. Compute bubble phase theta_bubble(n) and loop holonomy R_gamma.
12. Record bubble anisotropy: max(r)/min(r) - 1.
13. If defects are present, identify inward deformation and loop phase mismatch.
14. Enforce no overclaim: model light-cone construction is not empirical GR proof.
```

## 10. v0.92 retest plan

Flat bubble:

```text
w = [1,1,1,1]
rho = 1 in every sampled direction
E_LC = 0
E_null = 0
R_gamma = 0
```

Single diagonal defect:

```text
w = [0.5,1,1,1]
rho(d_1) = sqrt(0.625)
normalized inward residual = 1 - sqrt(0.625)
R_gamma = 1 - sqrt(0.625) for beta = 1
```

## 11. Strict limits

This update gives a model-level light-cone construction from a bubble surface.

It does not prove that physical spacetime is a bubble.

It does not derive full nonlinear general relativity.

It gives MCIFT a testable geometry rule: center event plus expanding 2D surface plus radial light distance.
