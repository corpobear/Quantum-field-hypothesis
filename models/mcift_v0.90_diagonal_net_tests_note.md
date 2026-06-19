# MCIFT v0.90 Diagonal Causal Net Tests

**Status:** first numerical checks for v0.89 diagonal causal net geometry.

## Purpose

v0.90 tests two immediate predictions from the diagonal net geometry:

```text
flat limit: all four diagonal weights equal one
single-axis defect: one diagonal weight suppressed to 0.5
```

## Flat limit

Weights:

```text
w = [1, 1, 1, 1]
```

Result:

```text
q_inv = I
all eigenvalues = 1
anisotropy = 0
max causal tick ratio = 1
```

Meaning:

The four diagonal axes reconstruct an isotropic local spatial frame when all diagonal channels participate equally.

## Single-axis defect

Weights:

```text
w = [0.5, 1, 1, 1]
```

Result:

```text
eigenvalues = [0.625, 1, 1]
anisotropy = 0.6
frob_delta_I = 0.375
max causal tick ratio = sqrt(2)
```

Meaning:

Suppressing one diagonal creates a directional geometric strain. The affected diagonal channel has a slower transfer tick, while the other channels remain normal.

## Interpretation

The flat test confirms the frame identity used in v0.89.

The defect test confirms that nonuniform diagonal weights create a measurable anisotropic metric scaffold.

## Strict limits

This does not derive full general relativity.

This does not prove spacetime.

It verifies that the diagonal net math behaves consistently in the two simplest cases.

## Next

v0.91 should test loop closure and wave-packet propagation through the diagonal operator.
