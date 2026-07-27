# MCIFT v1.07 Tetrahedral Facet-Core Toy Benchmark Chain

**Status:** executable internal geometry and toy-dynamics research scaffold.  
**Physical status:** not established physics.  
**Numerical mapping status:** the v0.97-v0.99 collider/cosmology mapping chain is unchanged.

## Purpose

This milestone implements the minimal tetrahedral comparison requested by v1.01 and records a sequence of increasingly constrained toy tests:

```text
v1.02  tetrahedral shell with an explicitly mobile core
v1.03  four face-reservoir channels with an emergent overlap core
v1.04  damped perturbation recovery of a tetrahedral shell
v1.05  exact four-facet decomposition into one scalar and three directional modes
v1.06  undamped breathing and symmetry-breaking sweep
v1.07  nonlinear central-overload breakpoint benchmark
```

The sequence is useful for internal model development, but none of the stages establishes a physical Higgs microstructure, mass-generation law, black-hole mechanism, Big Bang mechanism, or replacement for established physics.

## Shared tetrahedral geometry

For four non-coplanar vertices:

```text
T4 = {x0, x1, x2, x3}
E3 = [x1 - x0, x2 - x0, x3 - x0]
rank(E3) = 3
det(E3^T E3) > 0
Vtet = sqrt(det(E3^T E3)) / 6
```

These are standard geometric checks, not a derivation of physical dimensions.

## v1.02: explicit mobile-core precursor

The first toy model coupled four outer nodes to an explicitly mobile, load-centered core.

```text
119 / 120 near-planar randomized starts reached nonzero tetrahedral volume
200 / 200 perturbed tetrahedral states recovered rank 3
best free-3D energy advantage over planar control = 2.2176%
```

This precursor demonstrated that a mobile central state can coexist with a stable tetrahedral shell under the chosen potential. It contained an explicit center-targeting term and therefore did not demonstrate an emergent center. It is retained as a historical control, not the preferred construction.

## v1.03: emergent face-reservoir overlap core

Each triangular face supplies a centroid `g_f`, an inward unit normal `n_f`, and a nonnegative reservoir amplitude `R_f`.

The core coordinate is not prescribed. It is inferred as the weighted least-squares intersection of the four face-normal channels:

```text
c* = argmin_x sum_f R_f ||(I - n_f n_f^T)(x - g_f)||^2
```

For a regular tetrahedron:

```text
inferred core-to-centroid distance = approximately 0
RMS channel mismatch = approximately 0
four-way overlap score = 4.0
localization condition number = 1.0
```

The condition number of 1 indicates equal localization strength in all three directions.

Important control:

```text
four planar square channels also produce an exact center and score 4.0
planar-square localization condition number = 2.0
```

Therefore, the existence of a center is not unique to tetrahedral organization. The distinguishing feature in this diagnostic is isotropic three-dimensional localization.

Random-orientation control:

```text
runs = 2000
median score = 0.046912
maximum score = 2.855506
random sets scoring at least 3.0 = 0 / 2000
```

## v1.04: damped dynamic recovery

A disturbed tetrahedral shell was evolved with assumed equal-edge restoring forces, face-reservoir pressure, reservoir relaxation, and damping. The core remained inferred from the four channels; no core-target force was applied.

```text
initial edge RMS error = 0.1083568971
final edge RMS error = 0.0000084750
initial channel mismatch = 0.0349572074
final channel mismatch = 2.9503e-10
initial localization condition = 1.4266946
final localization condition = 1.0000702
final kinetic energy = 3.3658e-11
```

Under this toy law, the disturbed cell returned to a regular tetrahedral resting state. The result depends on the assumed restoring and damping laws.

## v1.05: four facet modes, not six edge sinks

For regular tetrahedral inward normals:

```text
sum_f n_f = 0
J0 = mean(J_f)
S  = (3/4) sum_f J_f n_f
J_f = J0 + n_f . S
```

This is an exact decomposition into:

```text
J0          one symmetric scalar mass/breathing mode
Sx, Sy, Sz  three independent directional sink modes
```

Maximum numerical reconstruction error:

```text
1.1102e-16
```

The six tetrahedral edges remain structural and closure relations, not six independent mass sinks.

Symmetric pulse result:

```text
peak core mass = 3.27523
peak core radius = 0.241748
maximum directional sink = 6.7134e-6
maximum center displacement = 1.5241e-7
```

Asymmetric pulse result:

```text
peak directional sink = 0.539402
peak center displacement = 0.086536
```

This verifies the internal mode separation of the chosen representation: equal facet loading enters the scalar mode, while unequal loading enters the directional vector mode.

## v1.06: undamped breathing and symmetry breaking

Both radial and translational damping were removed.

Perfect symmetry:

```text
peak core mass = 3.01346
peak core radius = 0.232997
late radial oscillation amplitude = 0.005290
maximum directional sink = 0
maximum center displacement = 0
```

Thus the toy core can continue radial vibration while remaining exactly centered under ideal symmetric loading.

The single-facet asymmetry sweep used `epsilon = 0` through `1`.

```text
any epsilon > 0 activated bounded translational oscillation
no finite directional-activation threshold above zero was found
no unbounded instability occurred in the tested linear restoring model
late RMS displacement was approximately proportional to epsilon
```

This is expected for a linear oscillator with positive translational stiffness. A finite rupture threshold requires a nonlinear coupling rather than being inferred from this stage.

## v1.07: nonlinear overload breakpoint benchmark

A separate toy hypothesis was introduced for symmetric central overload:

```text
R_eq(M) = R0 [1 + a DeltaM - b (DeltaM)^2]
R0 = 0.16
a = 0.34
b = 0.18
collapse radius = 0.06
inner-channel radius = 0.036
```

This law makes the preferred radius expand at moderate mass and turn inward at high mass. Crossing the selected collapse radius switches the simulation to an inner-channel branch.

Benchmark:

```text
symmetric pulse amplitudes tested = 28 from 0 to 1
collapsed cases = 9
first sampled collapse amplitude = 0.7037037
```

Last sampled stable case:

```text
amplitude = 0.6666667
peak mass = 3.859280
minimum radius = 0.063616
```

First sampled collapse case:

```text
amplitude = 0.7037037
peak mass = 4.018129
minimum radius = 0.010318
collapse time = 5.824
```

Next supercritical case:

```text
amplitude = 0.7407407
peak mass = 4.176978
minimum radius = 0.003401
collapse time = 5.600
```

### Strict interpretation of the breakpoint

The finite breakpoint is valid behavior of the implemented nonlinear toy law. It is not an independent MCIFT prediction because:

```text
- the quadratic turnover in R_eq(M) was assumed
- the collapse radius was selected
- the inner-channel branch was explicitly implemented
```

It therefore demonstrates how a finite overload transition can be represented and benchmarked. It does not establish a black-hole threshold, Big Bang event, physical singularity, or Higgs collapse.

## Current supported statements

```text
supported geometry:
    four non-coplanar vertices form the minimum nondegenerate 3D simplex

supported representation:
    four tetrahedral facet fluxes decompose exactly into one scalar mode
    and three directional modes

supported internal toy result:
    coherent regular tetrahedral normals create isotropic central localization

supported under stated toy laws:
    disturbed states can recover
    symmetric loading can drive breathing without translation
    asymmetric loading can drive bounded translation
    an assumed nonlinear turnover can create a finite collapse branch
```

## Not established

```text
not established: the Standard Model Higgs field is a tetrahedral plane network
not established: failed Higgs reservoirs exist as defined here
not established: the scalar mode is physical mass
not established: the directional modes are physical spatial channels
not established: the v1.07 threshold is a black-hole or Big Bang threshold
not established: physical dimensional emergence
not changed: any v0.97-v0.99 collider or cosmology score
not claimed: replacement of QFT, GR, the Standard Model, or Lambda-CDM
```

## Next falsifiable work

```text
1. Derive a transfer or energy law from explicit MCIFT assumptions rather
   than selecting spring, damping, or radius-turnover terms.
2. Benchmark tetrahedral localization against other 3D orientation frames,
   not only planar and random controls.
3. Implement asymmetric shell deformation and rupture as a separate branch.
4. Determine whether a threshold follows from the derived equations without
   inserting a collapse radius by hand.
5. Freeze parameters and acceptance criteria before any external observable
   mapping or data comparison.
```

## Reproducible files in this milestone

```text
simulations/mcift_v1_07_mass_breakpoint_benchmark_gif.py
analysis/results_v1.07/mass_breakpoint_benchmark_metrics.json
```

The source and metrics for the latest breakpoint benchmark are committed directly. Earlier v1.02-v1.06 stages are recorded here with their measured results and remain precursor toy experiments; they should be promoted as separate source files only after their equations are consolidated and reviewed.
