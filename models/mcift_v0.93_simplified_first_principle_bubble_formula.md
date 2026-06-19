# MCIFT v0.93 Simplified First-Principle Bubble Formula

**Status:** first-principle formula reset using the bubble light-cone projection; speculative model layer, not established physics.

## 1. Why this rework is needed

The earlier cubic first-principle formula used many separate structures:

```text
cube centers
six face connectors
face vortices
mass loading
containment
collapse state
```

The diagonal causal net and bubble light-cone construction simplify the foundation.

Instead of starting with many independent mechanisms, v0.93 starts from one primitive object:

```text
center event + expanding 2D bubble surface + radial light distance
```

The diagonal causal net becomes the internal sampling skeleton of the bubble.

Cosmology should not be retested until this simplified formula is the working first-principle layer.

## 2. Primitive object

For each cubic cell `i`, define the event-bubble object:

```text
B_i = {C_i, S_i, r_i, W_i, Phi_i}
```

where:

```text
C_i = (x_i, t_i)                    center event
S_i(theta,phi,t)                    2D causal surface
r_i(theta,phi,t)                    center-to-surface distance
W_i = {w_Delta[i,a]}                diagonal causal weights
Phi_i = {phi_i, T_i, K_i, q_i}       phase, timing, knot, contained complexity
```

## 3. Light-cone constraint

The flat bubble condition is:

```text
||X_i(theta,phi,t) - x_i|| = c * (t - t_i)
```

or:

```text
E_LC = ||X_i - x_i|| - c Delta t = 0
```

This is the simplified geometric core.

## 4. Diagonal sampling of the bubble

The four body-diagonal axes sample the bubble:

```text
d_1 = ( 1,  1,  1) / sqrt(3)
d_2 = ( 1, -1, -1) / sqrt(3)
d_3 = (-1,  1, -1) / sqrt(3)
d_4 = (-1, -1,  1) / sqrt(3)
```

Their weighted metric scaffold is:

```text
q_inv[i] = (3/4) * sum_a w_Delta[i,a] * d_a d_a^T
```

For any bubble direction `n`:

```text
rho_i(n)^2 = n^T q_inv[i] n
r_i(n,t) = c Delta t rho_i(n)
```

Flat case:

```text
w_Delta = [1,1,1,1]
rho_i(n) = 1
```

Defected case:

```text
w_Delta not equal across axes
rho_i(n) differs by direction
```

## 5. Unified field density

The local MCIFT field density is reduced to:

```text
F_i(n,t) = A_i(n,t) * rho_i(n)^2 * C_i_state(t)
```

where:

```text
A_i(n,t) = angular/surface activation
rho_i(n)^2 = diagonal causal metric strength
C_i_state = contained information state from K_i, q_i, phi_i, T_i
```

A compact version is:

```text
F_i(n,t) = A_i(n,t) * [n^T q_inv[i] n] * C_i_state(t)
```

This replaces several separate ad hoc weights with one bubble-projected causal density.

## 6. Mass and curvature as bubble deformation

Mass/loading is no longer a separate first primitive. It appears as persistent inward bubble deformation:

```text
m_i candidate ~ integral over surface of [1 - rho_i(n)] dOmega
```

Curvature-like closure appears as nonzero loop phase on the bubble surface:

```text
theta_bubble(n) = beta * [1 - rho_i(n)]
R_gamma = theta_1 + theta_2 - theta_3 - theta_4
```

Thus:

```text
flat bubble -> no mass-like deformation, no curvature-like loop phase
compressed bubble -> mass-like deformation, loop closure defect
```

## 7. Simplified action scaffold

The formula can now use one compact action:

```text
S = sum_i integral dt integral_S2 dOmega [
  0.5 * (partial_t r_i)^2
  - 0.5 * c^2 * rho_i(n)^2
  - V(C_i_state)
  - lambda_LC * E_LC(n,t)^2
  - lambda_R * R_gamma^2
]
```

Interpretation:

```text
partial_t r_i term      bubble expansion dynamics
rho_i term              diagonal causal geometry
V(C_i_state)            internal information state potential
E_LC penalty            keeps light-bubble relation stable
R_gamma penalty         controls loop closure defects
```

## 8. Mechanics update loop

At each step:

```text
1. Read center event C_i = (x_i,t_i).
2. Read local information state K_i, q_i, phi_i, T_i.
3. Compute diagonal weights w_Delta from phase/timing/state compatibility.
4. Build q_inv[i].
5. Sample surface directions n(theta,phi).
6. Compute rho_i(n)^2 = n^T q_inv[i] n.
7. Compute bubble radius r_i(n,t) = c Delta t rho_i(n).
8. Compute E_LC = r_i - c Delta t.
9. Compute surface density F_i(n,t).
10. Integrate deformation over S2 for mass/loading candidate.
11. Compute loop phases and R_gamma defects.
12. Update C_i_state from surface-integrated feedback.
13. Export reduced observables for downstream tests.
```

## 9. Why this simplifies cosmology

Cosmology can now be retested from fewer primitives:

```text
average bubble expansion -> Hubble-like expansion
surface deformation integral -> matter/loading density candidate
diagonal anisotropy -> lensing/shear candidate
loop closure defects -> curvature-like candidate
bubble residual E_LC -> speed-of-light/causal consistency check
```

The cosmology retest should use these reduced quantities rather than the older multi-bridge stack.

## 10. Downstream cosmology retest target

After this formula is adopted, retest:

```text
H0 / H(z)
BAO scale
S8 / lensing-like strain
BBN consistency placeholder
CMB acoustic-scale placeholder
```

with explicit labels for what is derived, fitted, assumed, or still placeholder.

## 11. Strict limits

This is a simplified first-principle scaffold.

It does not prove that spacetime is a bubble.

It does not derive full nonlinear general relativity.

It does not validate cosmology yet.

Cosmological data must be retested only after this formula is implemented numerically.
