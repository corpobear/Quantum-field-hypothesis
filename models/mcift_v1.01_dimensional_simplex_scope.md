# MCIFT v1.01 Dimensional Simplex Scope Clarification

**Status:** logical and geometric scope correction inside a speculative research scaffold.  
**Empirical status:** no new fit, simulation, experimental score, or physical validation is introduced in v1.01.

## 1. Purpose

The v0.96 threefold update used three closed surface channels on a two-dimensional causal bubble surface and described triadic closure as the smallest closed relational circuit.

That statement remains valid at the relational and surface level. It must not, however, be generalized into the claim that three points are the universal minimum for stable spatial structure in every dimension.

v1.01 separates two different ideas:

```text
triadic relational closure
```

and:

```text
minimal nondegenerate spatial simplex in dimension d
```

This is a scope clarification, not a claim that MCIFT derives physical space.

## 2. Geometric statements used by v1.01

Let points be:

```text
x_0, x_1, ..., x_d
```

and define the edge matrix:

```text
E_d = [x_1 - x_0, x_2 - x_0, ..., x_d - x_0]
```

The points form a nondegenerate `d`-simplex when:

```text
rank(E_d) = d
```

Equivalently, with the Gram matrix:

```text
G_d = E_d^T E_d
```

nondegeneracy requires:

```text
det(G_d) > 0
```

The corresponding Euclidean simplex volume is:

```text
V_d = sqrt(det(G_d)) / d!
```

Therefore:

```text
2D: 3 non-collinear points define a nondegenerate triangle.
3D: 4 non-coplanar points define a nondegenerate tetrahedron.
dD: d + 1 affinely independent points define a nondegenerate d-simplex.
```

These are standard geometric facts. They do not by themselves establish a physical law, a dynamical stability result, or dimensional emergence.

## 3. What remains valid from v0.96

The v0.96 minimal triadic activation principle stated that:

```text
one node  -> no internal relation
two nodes -> one open relation / polarity
three nodes -> first closed relational circuit
```

with the cycle:

```text
A -> B -> C -> A
```

This remains a valid graph-level statement: a simple closed cycle requires at least three distinct vertices.

Inside the current MCIFT scaffold, the threefold surface pattern:

```text
L_3 = {ell_1, ell_2, ell_3}
```

and:

```text
A_3(theta, phi) = 1 + epsilon_3 sin(theta)^2 cos(3 phi + psi_3)
```

remain a model of threefold organization on the two-dimensional bubble surface `S^2`.

v1.01 does not invalidate the existing surface reducer.

## 4. Corrected scope of the stability language

The word `stable` was previously used across relational, geometric, and dynamical contexts. These are not equivalent.

v1.01 uses the following distinctions:

```text
relational closure:
    a closed graph or information cycle

geometric nondegeneracy:
    points span the intended affine dimension

volumetric closure:
    a nonzero d-dimensional simplex volume

dynamical stability:
    bounded response under an explicit evolution law and perturbations
```

Only the first two are addressed directly in this clarification.

The corrected internal rule is:

```text
Triadic closure is the minimum simple relational cycle.
A nondegenerate spatial cell in dimension d requires d + 1 affinely independent vertices.
Dynamical stability requires a separate model and test.
```

## 5. Treatment of the historical failed mode 4

The existing late-version chain describes:

```text
modes 1, 2, 3 survive
mode 4 fails and is stored at the center
```

and uses `R_4` as a central failed-mode-4 reservoir.

The existence of a tetrahedron does not logically prove that `R_4` is depth, a fourth vertex, or the mechanism by which physical space emerges.

Therefore v1.01 keeps the following conservative interpretation:

```text
R_4 remains a model-specific central reservoir inherited from v0.94-v0.99.
Its physical meaning is not established.
```

A future model may test whether a fourth non-coplanar node provides a better geometric construction than the central-reservoir interpretation. Until such a model is implemented and compared, the identification:

```text
R_4 = depth-generating mode
```

is explicitly not claimed.

## 6. Compatibility with current numerical results

v1.01 introduces no numerical changes to:

```text
load_proxy
mean_shear_proxy
beta4_needed_for_balance
H_proxy_relative
Gamma_model
D_proxy
cosmology residuals
collider residuals
```

The v0.97-v0.99 values remain historical outputs of the threefold surface reducer and its mapping layers.

They must not be presented as validation of tetrahedral dynamics because no tetrahedral reducer has yet generated them.

## 7. Minimal future tetrahedral test

A future executable extension should define four node states:

```text
T_4 = {x_0, x_1, x_2, x_3}
```

with:

```text
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
edge-length and phase consistency
response to small perturbations
```

The tetrahedral configuration should be compared against the current threefold surface reducer under the same normalization and parameter accounting.

Suggested comparison outputs are:

```text
mean load
shear / anisotropy
closure residual
light-cone residual
null residual
perturbation boundedness
parameter count
```

No cosmology or collider remapping should be claimed until those outputs have been generated and audited.

## 8. Claim table

```text
SUPPORTED GEOMETRY:
- Three non-collinear points form a nondegenerate triangle in 2D.
- Four non-coplanar points form a nondegenerate tetrahedron in 3D.
- A nondegenerate d-simplex has d + 1 affinely independent vertices.
- A simple closed graph cycle requires at least three vertices.

SUPPORTED INSIDE THE CURRENT MCIFT MODEL:
- The active reducer is a threefold pattern on a two-dimensional bubble surface.
- Existing v0.97-v0.99 outputs were produced from that threefold reducer.

NOT ESTABLISHED:
- Physical space emerges from simplex construction.
- The historical mode 4 is physical depth.
- A tetrahedral reducer improves the existing numerical mappings.
- MCIFT derives 3D space, spacetime, gravity, QFT, or Standard Model dynamics.
```

## 9. v1.01 verdict

```text
DIMENSIONAL_SCOPE_CLARIFIED_NO_NEW_PHYSICAL_RESULT
```

v1.01 keeps triadic closure as the minimum relational cycle, limits the current threefold reducer to its surface-level scope, and records the tetrahedron as the minimal nondegenerate three-dimensional simplex.

The next meaningful step is implementation and comparison, not stronger interpretation.
