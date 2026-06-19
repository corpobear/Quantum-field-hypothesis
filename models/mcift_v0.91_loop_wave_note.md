# MCIFT v0.91 Loop Closure and Wave Packet Tests

**Status:** toy dynamics tests for the v0.89 diagonal causal net.

## Purpose

v0.91 tests two dynamics claims:

```text
loop closure detects phase defects
wave packet covariance detects diagonal anisotropy
```

## Loop closure test

The loop rule is:

```text
R_gamma = theta_1 + theta_2 - theta_3 - theta_4
```

Flat loop:

```text
phases = [0, 0, 0, 0]
R_gamma = 0
closure clean = true
```

Phase-defect loop:

```text
phases = [0.12, 0, 0, 0]
R_gamma = 0.12 rad
defect detected = true
```

## Wave packet test

A Gaussian packet was evolved on a 31^3 lattice using the diagonal stencil.

Flat weights:

```text
w = [1, 1, 1, 1]
covariance eigenvalues are equal
anisotropy = 0
```

Single diagonal defect:

```text
w = [0.5, 1, 1, 1]
covariance eigenvalues = [7.388589, 13.559273, 13.559273]
anisotropy = 0.835164
```

## Meaning

The loop test shows that phase closure can detect a curvature-like defect.

The wave test shows that a suppressed diagonal channel creates anisotropic packet spread.

## Strict limits

This is a toy dynamics check.

It does not prove spacetime.

It does not derive general relativity.

The wave test uses a numerical stability guard only; it does not claim a physical light-cone proof.

## Next

v0.92 should test localized defects, multiple loops, and recovery of weak-field-like behavior under small diagonal strain.
