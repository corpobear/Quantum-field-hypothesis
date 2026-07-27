# MCIFT Main Synopsis: v1.01 Dimensional Simplex Scope Clarification

**Status:** speculative research scaffold; not established physics.  
**Current version:** v1.01 dimensional simplex scope clarification built on the v0.97-v0.99 threefold reducer and mapping chain.  
**Author:** Adrian Newton / corpobear.

---

## Abstract

This synopsis records the MCIFT development path through v1.01. The active numerical structure remains the bubble light-cone and threefold reducer scaffold. It exports a small set of shared reduced quantities that were mapped to cosmology proxies in v0.98 and selected CERN/collider proxies in v0.99.

v1.01 adds no new numerical fit or physical validation. It corrects the dimensional scope of the stability language used around the threefold model.

The corrected distinction is:

```text
triadic closure = minimum simple relational cycle
triangle = minimum nondegenerate 2D simplex
tetrahedron = minimum nondegenerate 3D simplex
d-simplex = d + 1 affinely independent vertices
```

This is a logical and geometric clarification. It does not establish that physical dimensions emerge from MCIFT, that the historical mode 4 is depth, or that tetrahedral dynamics improve any existing result.

---

## Late-version chain

```text
v0.92  bubble light-cone projection
v0.93  simplified first-principle bubble formula
v0.94  central failed-mode-4 seed
v0.95  central-seed reducer
v0.96  threefold bubble-knot first-principle update
v0.97  shared threefold reducer
v0.98  cosmology mapping from shared reducer
v0.99  CERN/collider mapping from shared reducer
v1.01  dimensional simplex scope clarification
```

---

## Core object

The late scaffold begins from an event-bubble primitive:

```text
B_i = {C_i, S_i, r_i, W_i, Phi_i}
```

with:

```text
C_i       center event
S_i       2D causal bubble surface
r_i       center-to-surface radial distance
W_i       diagonal causal weights
Phi_i     phase/timing/knot state
```

The threefold update extends the primitive to:

```text
B_i^3 = {C_i, S_i, r_i, W_i, Phi_i, M_0, R_4, L_3}
```

where:

```text
M_0       central seed load from the historical mode-4 construction
R_4       model-specific central reservoir
L_3       three surface loops / channels
```

v1.01 keeps this object as the active numerical scaffold. It does not reinterpret `R_4` as physical depth or as a fourth tetrahedral vertex.

---

## Threefold reducer

The compact surface activation used by v0.97 is:

```text
A_3(theta, phi) = 1 + epsilon_3 sin(theta)^2 cos(3 phi + psi_3)
```

with surface mean:

```text
<A_3>_S2 = 1
```

The central regulated radial compression is:

```text
rho_0(r) = 1 - alpha_M M_0 / (r^2 + r_core^2)
```

The threefold radius scale is:

```text
r_0(n,t) = c Delta t rho_0(r) A_3(n)
```

The deformation proxy is:

```text
D_3(n,r) = 1 - rho_0(r) A_3(n)
```

v1.01 interprets this explicitly as a threefold pattern on the two-dimensional causal bubble surface. The formula is not a tetrahedral reducer.

---

## v1.01 dimensional clarification

### Relational closure

For graph relations:

```text
one node  -> no internal edge
two nodes -> one open relation
three nodes -> first simple closed cycle
```

The cycle:

```text
A -> B -> C -> A
```

is therefore the smallest simple relational loop.

### Affine geometric closure

Let:

```text
E_d = [x_1 - x_0, x_2 - x_0, ..., x_d - x_0]
```

The points form a nondegenerate `d`-simplex when:

```text
rank(E_d) = d
```

Equivalently, for:

```text
G_d = E_d^T E_d
```

nondegeneracy requires:

```text
det(G_d) > 0
```

with Euclidean simplex volume:

```text
V_d = sqrt(det(G_d)) / d!
```

Therefore:

```text
3 non-collinear points -> nondegenerate triangle in 2D
4 non-coplanar points  -> nondegenerate tetrahedron in 3D
d + 1 affinely independent points -> nondegenerate d-simplex
```

### Scope of the word stability

v1.01 distinguishes:

```text
relational closure:
    closed graph or information cycle

geometric nondegeneracy:
    points span the intended affine dimension

volumetric closure:
    nonzero simplex volume

dynamical stability:
    bounded behavior under an explicit evolution law and perturbations
```

The first three can be checked geometrically. Dynamical stability requires a separate executable model and test.

---

## Historical mode 4

The earlier chain described modes 1-3 as surviving and mode 4 as a failed central reservoir.

v1.01 does not promote the following interpretation to a result:

```text
mode 4 = depth-generating physical mode
```

The geometric fact that a tetrahedron needs four non-coplanar vertices is insufficient to identify the existing `R_4` variable with a fourth physical node.

The conservative status is:

```text
R_4 remains a model-specific central reservoir inherited from v0.94-v0.99.
A fourth non-coplanar node is a separate future construction to implement and compare.
```

---

## Shared v0.97 outputs

For:

```text
M0 = 2
alpha_M = 0.05
r_core = 1
epsilon_3 = 0.125
psi_3 = 0
shells = 1..10
```

the reducer exported:

```text
mean_A3 = 1.000000000000
load_proxy / mean_D3 = 0.009817928223
mean_shear_proxy = 0.063915576742
mean_threefold_amp = 0.247460690278
mean_abs_lc_resid = 0.054439708131
mean_null_resid = 0.015243226439
H_proxy_relative = 0.977215138494
beta4_needed_for_balance = 0.170868625373
```

These are unchanged historical outputs of the threefold surface reducer. They are not tetrahedral predictions.

---

## v0.98 cosmology mapping

v0.98 used the shared reducer to map:

```text
H0_early_model = fitted Planck-like anchor
H0_local_model = H0_early_model * (1 + mean_shear_proxy)
S8_late_model = S8_planck * (1 - mean_shear_proxy)
```

Current stored values:

```text
H0_local_model = 71.665353249341
H0_local_residual_sigma = -1.321775721787
S8_late_model = 0.778822240151
S8_late_residual_sigma = 0.166014126510
```

Strict interpretation:

```text
H0 early value is fitted, not an independent prediction.
S8 late value is pass-like against the selected DES Y3 anchor.
BAO, CMB acoustic scale, and BBN are not numerically scored in v0.98.
No value above has been regenerated from a tetrahedral model.
```

---

## v0.99 CERN mapping

v0.99 used:

```text
Gamma_model = Gamma_SM * (1 + load_proxy)
mu_inclusive_model = mean_A3
D_proxy = -(1/3 + beta4_needed_for_balance)
```

Current stored values:

```text
Gamma_model = 4.109958967868 MeV
mu_inclusive_model = 1.000000000000
CMS HZZ residual = 0.526 sigma
D_proxy = -0.504201958707
ATLAS D residual = 1.717 sigma
CMS D residual = -0.880 sigma
```

Strict interpretation:

```text
CMS HZZ signal-strength proxy is pass-like at this coarse level.
CMS top-entanglement D proxy is pass-like.
ATLAS top-entanglement D proxy is close but not pass-claimed.
Higgs width is reference-close against the SM value, not a direct experimental-width score.
Higgs branching ratios, channel signal strengths, and detector event shapes are not scored.
No value above validates tetrahedral dynamics.
```

---

## Minimal tetrahedral comparison target

A future model should define:

```text
T_4 = {x_0, x_1, x_2, x_3}
```

with:

```text
4 vertices
6 edges
4 triangular faces
1 tetrahedral volume
```

At minimum it should compute:

```text
rank(E_3)
det(G_3)
V_tet
four face-closure residuals
edge and phase consistency
response to small perturbations
```

It should then compare the tetrahedral construction against the existing threefold surface reducer under the same normalization and parameter accounting.

No cosmology or collider remapping should be promoted until this comparison exists.

---

## Safe interpretation

Safe:

```text
MCIFT v1.01 clarifies that triadic closure is the minimum simple relational cycle, while a tetrahedron is the minimum nondegenerate simplex spanning three Euclidean dimensions. The active numerical model remains the v0.97 threefold surface reducer, and all v0.98-v0.99 mappings retain their previous caveats.
```

Unsafe:

```text
MCIFT proves that dimensions emerge from information.
The historical mode 4 is proven to create physical depth.
The tetrahedron validates the current collider or cosmology mappings.
MCIFT replaces the Standard Model, QFT, GR, or Lambda-CDM.
The v0.99 mapping is a full CERN validation.
```

---

## Current verdict

```text
DIMENSIONAL_SCOPE_CLARIFIED_NO_NEW_PHYSICAL_RESULT
```

---

## Next target

```text
Implement and audit a minimal tetrahedral comparison layer before changing the numerical mapping chain.
```
