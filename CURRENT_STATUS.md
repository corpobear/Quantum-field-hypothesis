# Current MCIFT Status: v1.09 Relational Formation and Orbit

**Status:** speculative two-cell tetrahedral geometry/dynamics scaffold; not established physics.  
**Current layer:** v1.09 second-cell relational mass formation and bound-orbit compatibility benchmark.  
**Previous layer:** v1.08 primordial tetrahedron intrinsic-stability benchmark.  
**Previous physical-mapping layer:** v0.99 CERN/collider mapping from the v0.97 shared threefold reducer.

## Verdict

```text
RELATIONAL_APEX_FORMATION_COMPATIBLE_WITH_BOUND_WEAK_FIELD_ORBITS_IN_TOY_MODEL
```

## Latest chain

```text
v0.92: bubble light-cone projection
v0.93: simplified first-principle bubble formula
v0.94: central failed-mode-4 seed
v0.95: central-seed reducer
v0.96: threefold bubble-knot formula
v0.97: shared threefold reducer
v0.98: cosmology mapping from shared reducer
v0.99: CERN/collider mapping from shared reducer
v1.01: dimensional simplex scope clarification
v1.02: explicit mobile-core tetrahedral precursor
v1.03: emergent face-reservoir overlap core
v1.04: damped tetrahedral recovery toy dynamics
v1.05: four facet inputs -> one scalar plus three directional modes
v1.06: undamped breathing and symmetry-breaking sweep
v1.07: nonlinear overload breakpoint benchmark
v1.08: primordial tetrahedron intrinsic-stability benchmark
v1.09: relational second-cell formation and bound-orbit benchmark
```

## v1.09 question

v1.08 supplied a stable first tetrahedral cell `T0` inside the selected intrinsic toy energy. v1.09 asks what happens to a later cell `T1` when `T0` already exists.

The test does not introduce a global up/down axis. The only relational inward direction for T1 is

```text
r_hat = (c0 - c1) / |c0 - c1|
```

where `c0` and `c1` are the cell centers.

## Static coupling-location control

Two finite-body 1/r control locations were first compared for an already-formed T1:

```text
face-vortex centroids -> face-inward energy minimum
vertices              -> apex-inward energy minimum
```

The distinction follows the regular-tetrahedron duality

```text
face centroid opposite vertex i = -vertex_i / 3
```

so apex-inward alignment cannot be claimed from tetrahedral attraction alone; the coupling location matters.

## Formation-time relational field

T0 supplies a normalized radial source field

```text
Phi0(x) = gamma M0 / |x|
```

T1 keeps the v1.08 face-vortex energy but its face drive is modified while mass is gained.

Direct face-centroid sampling:

```text
k_f = k_self + Phi0(g_f)
```

produced face-inward formation in all four tested random initial orientations.

Vertex-sampled face drive:

```text
k_f = k_self + (1/3) sum_{v in face f} Phi0(x_v)
```

produced apex-inward formation in all four tested random initial orientations.

Final apex scores:

```text
0.9999999983
0.9999999959
0.9999999972
0.9999999944
```

Representative face-drive split:

```text
0.2910805
0.2720902
0.2910798
0.2910803
```

Representative vortex amplitudes:

```text
0.4354578
0.4271218
0.4354559
0.4354570
```

The selected normalized T1 remained finite-volume with approximately 4.5% edge CV.

Strict interpretation:

```text
The three-strong / one-weak face pattern is a candidate derived mechanism for
relational apex selection because one nearer proto-vertex belongs to three
faces. This does not establish the physical coupling location or a physical
Higgs mechanism.
```

## Orbital-role separation

The formation-bias interaction was not promoted as the orbital binding law. In the tested effective reduction it produced radial behavior too steep to provide the desired stable circular branch.

The integrated benchmark therefore separates:

```text
T1 formation/orientation:
    vertex-sampled T0 radial field -> T1 face-vortex drive

T1 center motion:
    existing weak-field/Newtonian bridge
```

The weak-field bridge remains a control layer, not a derivation of gravity from the v1.08 vortex energy.

## Integrated formation during orbit

Reference source:

```text
M0 = 1.663148923591514
```

from the v1.08 `H=1.5` normalized positive localized mass proxy.

Formation ramp:

```text
k_self: -0.12 -> 0.08
ramp duration: 1 nominal circular period
run duration: 3 nominal circular periods
```

T1 internal state is solved by adiabatic local-equilibrium continuation. This removes an otherwise arbitrary vortex inertia/relaxation timescale from the benchmark.

### `0.9 v_c`

```text
radius min = 8.16811819
radius max = 11.99999719
orbital energy < 0 throughout
M1/M0 = 0.19400736
apex min after 10% retained mass = 0.99999639
max edge CV after 10% retained mass = 0.05719996
min volume after 10% retained mass = 1.31022229
```

Verdict:

```text
bound orbit = PASS
apex-inward formation orbit = PASS
```

### `1.0 v_c`

```text
radius min = 12.00000000
radius max = 12.00001480
orbital energy < 0 throughout
M1/M0 = 0.08430595
apex min after 10% retained mass = 0.99997382
max edge CV after 10% retained mass = 0.01859862
min volume after 10% retained mass = 0.80467988
```

Verdict:

```text
bound orbit = PASS
apex-inward formation orbit = PASS
```

### `1.1 v_c`

```text
radius min = 12.00000311
radius max = 18.37720223
orbital energy < 0 throughout
M1/M0 = 0.08430506
apex min after 10% retained mass = 0.99740706
max edge CV after 10% retained mass = 0.01679208
min volume after 10% retained mass = 0.82332104
```

Verdict:

```text
bound orbit = PASS
apex-inward formation orbit = PASS
```

### `1.45 v_c` super-escape control

```text
positive orbital energy ~= 0.007103
radius max = 79.46803300 before test exit
M1/M0 = 0.00975218
apex mean after 10% mass = 0.47555263
```

Verdict:

```text
bound orbit = FAIL
apex-inward formation orbit = FAIL
```

The benchmark therefore does not convert the super-escape trajectory into a captured orbit.

## Relationship to v1.08

v1.08 established the stable first-cell scaffold under the selected intrinsic face-vortex energy. v1.09 does not modify that result. It adds a second-cell relational experiment in which an already-existing source breaks T1's otherwise rotationally degenerate formation environment.

The first/second distinction is model ordering, not an established cosmological history.

## Strict status

```text
supported internal toy behavior:
    v1.08 finite stable regular tetrahedral branch
    v1.08 bounded undamped perturbations and planar buckling control
    face-centroid inter-cell sampling prefers face-inward orientation
    vertex-sampled face drive selects apex-inward T1 formation in tested cases
    bound weak-field orbit controls are compatible with apex-inward T1 formation
    super-escape control remains unbound

not established:
    physical Higgs tetrahedral microstructure
    physical mass generation/calibration
    gravity derived from the tetrahedral vortex energy
    physical dimensional emergence
    a primordial cosmic center
    true capture from an initially unbound trajectory
    spontaneous dissipative spin/orbit locking
    two-body backreaction
    N-body hierarchy formation
    channel inversion
    parameter-free black-hole formation
    Big Bang formation

unchanged:
    v0.97-v0.99 numerical mappings and caveats

not claimed:
    replacement of QFT, GR, the Standard Model, or Lambda-CDM
```

## Canonical files

```text
models/mcift_v1.09_relational_formation_and_orbit.md
simulations/mcift_v1_09_two_tetrahedron_orientation_benchmark.py
simulations/mcift_v1_09_second_tetrahedron_mass_gain_under_t0.py
simulations/mcift_v1_09_formation_during_orbit.py
analysis/results_v1.09/two_tetrahedron_orientation_metrics.json
analysis/results_v1.09/two_tetrahedron_orientation_sweep.csv
analysis/results_v1.09/second_tetrahedron_mass_gain_metrics.json
analysis/results_v1.09/formation_during_orbit_metrics.json
```

## Next

```text
1. Replace the adiabatic internal solver with an explicit conservative internal
   kinetic term whose inertia is derived rather than chosen arbitrarily.
2. Couple T1 orbital motion to shape/breathing/vortex modes and test true
   positive-energy -> negative-energy capture with total-energy conservation.
3. If capture survives, release the fixed-T0 approximation and test two-body
   backreaction before attempting successive/N-body tetrahedral hierarchy.
4. Keep channel inversion/black-hole work as a separate derived degree-of-
   freedom problem, not as an interpretation of the current orbit result.
```
