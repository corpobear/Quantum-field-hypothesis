# MCIFT v0.89 Diagonal Causal Net Geometry

**Status:** speculative geometry layer for the cubic MCIFT model; not established physics and not a proof of spacetime.

## 1. Purpose

The cubic MCIFT model already treats each cube as a cell-complex field with node, link, face, and cell variables. v0.89 adds a diagonal internal geometry:

```text
corner -> center -> opposite corner
```

These body-diagonal axes form a repeated net through the cubic lattice. The proposed name is:

```text
MCIFT Diagonal Causal Net
```

The purpose is to formalize how this diagonal net could act as a discrete spacetime scaffold.

## 2. Base cubic cell

Let cube centers be indexed by:

```text
i in Z^3
x_i = ell * (n_x, n_y, n_z)
```

Each cell has the existing MCIFT variables:

```text
K_i(t)      knot information state
phi_i(t)    local information phase
T_i(t)      local timing coordinate
q_i(t)      contained complexity
B_i(t)      collapsed reservoir
m_i(t)      gathered mass
Coh_i(t)    coherence capacity
S_i(t)      containment stability
```

v0.89 keeps the existing six face connectors but adds four body-diagonal axes.

## 3. Diagonal axes

Use the four tetrahedral body-diagonal directions:

```text
d_1 = ( 1,  1,  1) / sqrt(3)
d_2 = ( 1, -1, -1) / sqrt(3)
d_3 = (-1,  1, -1) / sqrt(3)
d_4 = (-1, -1,  1) / sqrt(3)
```

The opposite sign of each direction is the same axis reversed.

The frame identity is:

```text
(3/4) * sum_a d_a d_a^T = I
```

So equal diagonal participation reconstructs an isotropic spatial frame.

## 4. Diagonal state variables

For each cell `i` and diagonal axis `a`, define:

```text
A_Delta[i,a]      diagonal activation, 0 <= A_Delta <= 1
chi_Delta[i,a]    diagonal compatibility / causal readiness
w_Delta[i,a]      diagonal causal weight
U_Delta[i,a]      phase transport along the diagonal
```

Use:

```text
w_Delta[i,a] = chi_Delta[i,a]
U_Delta[i,a] = exp(i * theta_Delta[i,a])
```

The weight `w_Delta` is the local strength of causal/information transfer along that diagonal axis.

## 5. Diagonal compatibility mechanics

A diagonal channel becomes active only if phase, timing, and state agree across the diagonal neighbor.

Let the diagonal neighbor be:

```text
j = i + d_a
```

where `d_a` is interpreted as the corresponding integer corner offset before normalization.

Define:

```text
chi_Delta[i,a]
  = A_Delta[i,a]
  * P_phase_Delta[i,a]
  * P_timing_Delta[i,a]
  * P_match_Delta[i,a]
```

with:

```text
P_phase_Delta[i,a]  = cos^2(phi_i - phi_j)
P_timing_Delta[i,a] = exp[-(T_i - T_j)^2 / tau_Delta^2]
P_match_Delta[i,a]  = exp[-|K_i - K_j|^2 / sigma_Delta^2]
```

Interpretation:

```text
high chi_Delta  -> diagonal causal channel open
low chi_Delta   -> diagonal causal channel suppressed
chi_Delta ~ 0   -> local causal break / diagonal bottleneck
```

## 6. Local metric scaffold

Use the diagonal weights to build a local inverse spatial metric:

```text
q_inv[i] = (3/4) * sum_a w_Delta[i,a] * d_a d_a^T
```

If all diagonal weights are equal to one:

```text
w_Delta[i,1] = w_Delta[i,2] = w_Delta[i,3] = w_Delta[i,4] = 1
q_inv[i] = I
```

This is the local flat-cell limit.

If the weights differ, the cell has local geometric strain:

```text
equal weights       -> flat isotropic cell
average compression -> scalar gravity-like potential candidate
uneven weights      -> tensor strain / shear candidate
near-zero weight    -> causal bottleneck or boundary candidate
```

## 7. Discrete spacetime line element

Combine the local timing coordinate with the diagonal spatial metric:

```text
ds_i^2 = -N_i^2 c^2 dt^2 + dx^T q_i dx
```

where:

```text
N_i   = local lapse / clock factor
q_i   = inverse of q_inv[i], when invertible
```

Interpretation:

```text
T_i supplies local clock response
q_i supplies spatial geometry from diagonal weights
N_i links clock-rate distortion to local cell state
```

This is a discrete spacetime metric scaffold, not a proof of general relativity.

## 8. Diagonal causal transfer speed

The center-to-corner-to-opposite-corner diagonal length across a cube is:

```text
L_Delta = sqrt(3) * ell
```

Define a causal tick for diagonal axis `a`:

```text
Delta_T[i,a] = L_Delta / (c * sqrt(w_Delta[i,a]))
```

Constraint:

```text
0 <= w_Delta[i,a] <= 1
```

so the effective diagonal transfer speed does not exceed `c` unless a later renormalized rule explicitly permits it.

## 9. Diagonal propagation operator

For an MCIFT field component `Psi_i(t)`, define the diagonal Laplacian:

```text
nabla_Delta^2 Psi_i
  = (1 / (4 ell^2)) * sum_a w_Delta[i,a]
    * (Psi_{i+d_a} + Psi_{i-d_a} - 2 Psi_i)
```

Define the diagonal wave operator:

```text
Box_Delta Psi_i
  = -(1/c^2) * Delta_t^2 Psi_i + nabla_Delta^2 Psi_i
```

A basic field equation is:

```text
Box_Delta Psi_i + M_i^2 Psi_i = J_i
```

where:

```text
M_i = mass/loading term from MCIFT cell state
J_i = source or sink term
```

Mechanic:

```text
field movement follows diagonal causal weights
mass/loading resists propagation
sources/sinks inject or absorb information
```

## 10. Curvature and closure defects

Let diagonal phase transport be:

```text
U_Delta[i,a] = exp(i * theta_Delta[i,a])
```

For a closed loop `gamma` through diagonal and/or face links:

```text
H_gamma = product over loop of U_Delta
R_gamma = arg(H_gamma)
```

Interpretation:

```text
R_gamma = 0      -> diagonal phase closes cleanly
R_gamma != 0     -> curvature-like phase defect
```

Additional defect channels:

```text
timing closure failure      -> torsion-like timing defect
activation closure failure  -> causal tear / boundary defect
mass-loaded closure failure -> gravity-like trapped distortion
```

## 11. Scalar and tensor split

Let:

```text
w_Delta[i,a] = 1 + epsilon[i,a]
epsilon_bar[i] = (1/4) * sum_a epsilon[i,a]
```

Scalar strain candidate:

```text
psi_i ~= -0.5 * epsilon_bar[i]
```

Tensor strain candidate:

```text
h_Delta[i] = (3/4) * sum_a (epsilon[i,a] - epsilon_bar[i]) * d_a d_a^T
```

Interpretation:

```text
average diagonal compression -> gravity-like scalar potential
uneven diagonal compression  -> tensor strain / wave-like geometry
rotating diagonal imbalance  -> frame-dragging-like candidate
```

## 12. Mechanics update loop

At each simulation step:

```text
1. Read node state: K_i, phi_i, T_i, q_i, B_i, m_i, Coh_i, S_i
2. Compute diagonal neighbor states along all four axes
3. Compute P_phase_Delta, P_timing_Delta, P_match_Delta
4. Compute chi_Delta and w_Delta
5. Build q_inv[i] from weighted diagonal projectors
6. Compute causal ticks Delta_T[i,a]
7. Propagate Psi_i with Box_Delta
8. Compute loop holonomies H_gamma and closure defects R_gamma
9. Update strain, mass loading, coherence, and stability
10. Enforce constraints: 0 <= w_Delta <= 1 and q_inv invertibility where needed
```

## 13. Minimal action scaffold

A compact discrete action can be written:

```text
S_Delta = sum_i [
  0.5 * (Delta_t Psi_i)^2
  - (c^2 / (8 ell^2)) * sum_a w_Delta[i,a] * (Psi_{i+d_a} - Psi_i)^2
  - V(Psi_i)
] + S_closure
```

with closure penalty:

```text
S_closure = kappa_R * sum_gamma R_gamma^2
```

This penalizes non-closing diagonal phase loops unless the model treats them as physical curvature.

## 14. What can be tested next

Immediate tests:

```text
flat limit: all w_Delta = 1 should recover isotropic propagation
single-axis defect: one diagonal suppressed should create anisotropic propagation
loop closure: nonzero R_gamma should identify curvature-like defect
wave packet: diagonal operator should propagate a packet with no superluminal channel
weak-field bridge: small epsilon should reproduce v0.80/v0.81 weak-field behavior at leading order
```

## 15. Strict limits

This layer does not prove spacetime.

It does not derive full nonlinear Einstein field equations.

It does not replace general relativity or quantum field theory.

It defines a candidate discrete substrate from which spacetime-like metric behavior could emerge.
