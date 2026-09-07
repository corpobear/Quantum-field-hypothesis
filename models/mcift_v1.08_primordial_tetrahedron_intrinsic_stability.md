# MCIFT v1.08 Primordial Tetrahedron Intrinsic Stability Benchmark

**Status:** executable intrinsic-geometry and vortex-energy toy benchmark; not established physics.  
**Physical status:** no physical Higgs, mass, black-hole, or spacetime-emergence claim is established.  
**Previous layer:** v1.07 nonlinear overload benchmark with an explicitly selected collapse branch.

## Purpose

v1.08 replaces the prescribed v1.07 radius-turnover/collapse law with a narrower question:

```text
Can four triangle-constrained face vortices define a finite, stable,
nondegenerate tetrahedral state without inserting a target side length,
edge spring, target volume, damping, or collapse switch?
```

The observer may represent the tetrahedron in Cartesian coordinates, but the potential depends only on intrinsic face geometry and vortex amplitudes. Translation and rigid rotation are therefore gauge/symmetry motions of the representation rather than physical deformation modes of the toy cell.

## Primitive tetrahedral object

The local object contains:

```text
4 freely moving vertices x_i in R^3
4 triangular faces f
4 face-vortex amplitudes Omega_f
```

For each face:

```text
A_f = triangle area
g_f = face centroid
Q_f = sum_{vertices on f} |x_i - g_f|^2
```

No preferred `+x/-x/+y/-y/+z/-z` directions enter the potential.

## Triangle-constrained vortex geometry

The face vortex uses the barycentric window

```text
W = 27 lambda_1 lambda_2 lambda_3
```

and schematic face-plane velocity field

```text
v_f(u) = Omega_f W(u) [n_f x (u - g_f)]
```

so the vortex vanishes on all three edges of the triangular face.

For this field the exact geometric integral is

```text
I_f = integral_face W^2 |u-g_f|^2 dA
    = (27/2800) A_f Q_f
```

Define

```text
c_tri = 27/2800
```

This is the geometric coefficient used by the benchmark.

## Intrinsic toy energy

The v1.08 benchmark uses

```text
F = sum_f A_f [
      0.5 (rho c_tri Q_f - k_f) Omega_f^2
      + beta/4 Omega_f^4
    ]
```

with

```text
k_f = g H_f chi_f - alpha
```

Interpretation inside the toy model:

```text
rho c_tri Q_f Omega_f^2  = finite-face circulation cost
-k_f Omega_f^2           = external face-coupling gain
beta Omega_f^4            = nonlinear vortex self-stabilization
```

The committed benchmark uses normalized values

```text
alpha = 1
g = 1
beta = 1
rho = 1
chi = 1
```

These values define a dimensionless structural test. `H=1` is therefore only the normalized onset point `k=0`; it is not a measured or predicted Higgs threshold.

## Regular tetrahedral branch

For a regular tetrahedron of edge length `L` under equal face loading `k_f=k`, symmetry gives

```text
Q_f = L^2
A_f = (sqrt(3)/4) L^2
```

Stationarity of the intrinsic energy gives the nonzero branch

```text
L_eq^2 = k / (3 rho c_tri)
Omega_eq^2 = 2 k / (3 beta)
```

or

```text
L_eq = sqrt[k / (3 rho c_tri)]
Omega_eq = sqrt[2 k / (3 beta)]
```

for `k > 0`.

The finite side length is therefore not supplied as a target length in this benchmark. It follows from competition between face-coupling gain and finite-triangle circulation cost under the selected energy law.

## Local stability spectrum

The full benchmark state has

```text
12 vertex-coordinate degrees of freedom
4 vortex-amplitude degrees of freedom
16 total coordinates
```

The complete Hessian of the potential was evaluated on the regular branch.

Across the tested loading range

```text
H = 1.01, 1.05, 1.10, 1.25, 1.50, 2.0, 3.0, 5.0, 10.0
```

every tested regular state had

```text
negative modes = 0
zero modes = 6
positive modes = 10
```

The six zero modes are consistent with

```text
3 translations
3 rigid rotations
```

leaving ten positive physical deformation/vortex modes in this coordinate representation.

Reference point `H=1.5`:

```text
k = 0.5
L_eq = 4.1573970964
Omega_eq = 0.5773502692
mass proxy = 1.6631489236
softest positive eigenvalue = 0.06415002991
softest unit-inertia frequency = 0.2532785619
largest positive eigenvalue = 5.0561351392
```

The mass proxy is the positive localized circulation plus quartic vortex self-energy used for bookkeeping in the normalized toy system. It is not a calibrated physical mass.

## Undamped nonlinear perturbation test

The free vertices and four vortex amplitudes were then integrated with velocity-Verlet dynamics and no damping.

At `H=1.5`, randomized perturbations of the regular state gave:

### 5% perturbation

```text
mean edge range = 4.0069241 .. 4.3044367
maximum edge coefficient of variation = 0.0182872
minimum tetrahedral volume = 7.5776453
relative energy drift = 6.89e-7
```

### 10% perturbation

```text
mean edge range = 3.8317966 .. 4.4661053
maximum edge coefficient of variation = 0.0350478
minimum tetrahedral volume = 6.6141303
relative energy drift = 3.40e-6
```

### 20% perturbation

```text
mean edge range = 3.3936620 .. 4.8273016
maximum edge coefficient of variation = 0.0803135
minimum tetrahedral volume = 4.4994656
relative energy drift = 2.36e-5
```

All tested perturbed regular states remained nonzero-volume tetrahedra and bounded over the simulated interval. Because the runs are undamped, the result is bounded oscillation around the stable branch rather than dissipative convergence to a resting state.

## Planar four-point control

A symmetric four-point square embedded in a plane was evaluated using the same intrinsic energy.

At `H=1.5` its Hessian had

```text
negative modes = 1
zero modes = 6
positive modes = 9
unstable eigenvalue = -0.05555555556
```

The unstable vertex component is, to numerical precision, an alternating out-of-plane mode:

```text
vertex 1: +z
vertex 2: -z
vertex 3: +z
vertex 4: -z
```

Thus the planar configuration is a saddle of this toy energy against 3D buckling.

An undamped dynamics run initialized with only a tiny alternating out-of-plane perturbation gave

```text
initial sampled volume = 0.0311148
maximum sampled volume = 9.7566331
minimum sampled edge coefficient of variation = 0.00172718
relative energy drift = 2.54e-7
```

The planar control therefore leaves the plane and passes close to a regular tetrahedral edge pattern under the selected energy law.

Strict interpretation:

```text
This demonstrates a 3D-buckling instability of the planar control in the
implemented toy potential. It is not by itself a derivation that physical
three-dimensional spacetime emerges from a two-dimensional state.
```

## Relationship to v1.05 facet modes

The v1.05 exact regular-tetrahedron decomposition remains available:

```text
J0 = mean(J_f)
S  = (3/4) sum_f J_f n_f
J_f = J0 + n_f . S
```

For four equal face-vortex energies, the directional contribution cancels because the regular tetrahedral inward normals sum to zero. Unequal face loading can therefore be tested as the next branch without introducing a preferred external axis.

## Relationship to v1.07 collapse benchmark

v1.07 demonstrated that an explicitly chosen nonlinear radius law plus an explicit collapse radius can produce a finite breakpoint.

v1.08 does not reuse that collapse switch.

Within the current v1.08 degrees of freedom:

```text
no regular-branch instability was observed over H=1.01..10
regular-branch stiffness increased with loading in the tested normalization
no channel inversion variable exists in the model
```

Therefore the benchmark does **not** establish either:

```text
channel inversion occurs
channel inversion is impossible
```

A genuine inversion test requires adding an inward/outward channel degree of freedom and deriving its energy before testing whether a second branch becomes favorable or the outer branch loses stability.

## Supported internal statements

```text
supported within the selected toy energy:
    a finite regular tetrahedral branch exists without a target edge length
    the regular branch has six symmetry zero modes and ten positive physical modes
    tested free-vertex perturbations remain bounded and nondegenerate without damping
    the symmetric planar four-point control has an out-of-plane negative mode
    the planar control dynamically buckles into nonzero 3D volume

not established:
    the Standard Model Higgs field has triangular face-vortex microstructure
    the normalized vortex-energy proxy is physical mass
    physical spacetime originates from one primordial tetrahedron
    a preferred cosmic center exists
    the planar buckling result is physical dimensional emergence
    a black hole is an inverted MCIFT channel
    channel inversion exists or has a threshold
```

## Reproducible files

```text
simulations/mcift_v1_08_primordial_tetrahedron_stability.py
analysis/results_v1.08/primordial_tetrahedron_stability_metrics.json
analysis/results_v1.08/primordial_tetrahedron_stability_sweep.csv
```

The simulation also generates a detailed dynamics trace locally. The committed JSON and loading sweep are the compact auditable outputs.

## Next falsifiable work

```text
1. Add unequal face loading and verify that derived free-vertex deformation
   transforms covariantly with the tetrahedral facet-mode vector S.
2. Introduce an explicit channel orientation/inversion coordinate from MCIFT
   assumptions, derive its contribution to the same energy, and search for a
   second stable or unstable branch without a hand-coded collapse trigger.
3. Compare the regular tetrahedron against additional nonplanar four-point
   controls, not only the planar square.
4. Repeat the Hessian and nonlinear tests across normalized parameter families
   rather than only alpha=g=beta=rho=chi=1.
5. Freeze equations, parameters, and acceptance criteria before any external
   collider, cosmology, black-hole, or early-universe mapping.
```
