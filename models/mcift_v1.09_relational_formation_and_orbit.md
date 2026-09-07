# MCIFT v1.09 — Relational Formation and Orbit Benchmark

**Status:** speculative two-cell geometry/dynamics scaffold; not established physics.

## Purpose

v1.09 asks what changes once the v1.08 primordial tetrahedron already exists and a second tetrahedral cell forms inside its field.

The research question is deliberately relational:

```text
T0 forms first and is older/heavier.
T0 has no external "down" direction.
T1 forms later inside T0's radial influence.
Can T1 acquire a preferred apex during mass gain and remain in a bound orbit?
```

The benchmark does not introduce a global up/down axis. For T1, the only local inward direction is the vector from the T1 center toward the T0 center.

## Starting point from v1.08

v1.08 established, within the selected intrinsic toy energy, a finite stable regular tetrahedral branch with four face-vortex amplitudes. It also produced an exact regular-tetrahedron decomposition of four face inputs into one scalar plus three directional components in the earlier v1.05 chain.

v1.09 keeps the v1.08 internal energy form:

```text
F = sum_f A_f [
      0.5 (c_tri Q_f - k_f) Omega_f^2
      + 0.25 Omega_f^4
    ]

c_tri = 27/2800
```

where `A_f` is triangular face area, `Q_f` is the centroidal second moment of the face vertices, and `Omega_f` is the face-vortex amplitude.

## 1. Static orientation control

Before modeling formation, two finite-body 1/r coupling locations were compared for an already-formed T1:

```text
A) face-vortex centroids
B) vertices
```

No apex-alignment term was used.

Across tested separations `R/L = 1.5, 2, 3, 5, 10`:

```text
face-centroid coupling -> face-inward minimum
vertex coupling        -> apex-inward minimum
```

This is not numerical coincidence. For a centered regular tetrahedron, the centroid of the face opposite vertex `i` is

```text
g_fi = -v_i / 3
```

so the four face centroids form the dual tetrahedron and point oppositely to the vertices.

Strict interpretation:

```text
The desired inverted-pyramid orientation is not a generic property of
attraction plus tetrahedral geometry. It depends on where the external
interaction is sampled/carried.
```

## 2. Bound-orbit control

The two coupling locations were then run under identical rigid-body orbital conditions.

Both could remain bound under the same conservative finite-body 1/r control.

The discriminator was orientation:

```text
face-centroid coupling:
    bound orbit = yes
    face-inward = yes
    apex-inward = no

vertex coupling:
    bound orbit = yes
    apex-inward = yes
    face-inward = no
```

At the nominal vertex-coupled eight-orbit run:

```text
radius min = 2.87277395
radius max = 2.99999997
apex mean = 0.99813144
apex min = 0.99388439
apex p05 = 0.99539625
```

A zero-spin control remained bound but did not self-lock into synchronous apex orientation. Therefore a pre-existing rigid tetrahedron still needs an energy-transfer mechanism for spontaneous spin/orientation capture.

## 3. Formation under the older T0 field

The key v1.09 step is to stop rotating an already-made T1 and instead let the preferred direction appear while T1 gains vortex mass.

T0 is fixed at the origin. T1's center is held at finite separation for this formation-only benchmark. T0 supplies a normalized relational radial field

```text
Phi0(x) = gamma M0 / |x|
```

Two ways of feeding this field into T1's four face drives were tested:

### Face-centroid sampling

```text
k_f = k_self + Phi0(g_f)
```

Result across four random initial orientations:

```text
FACE_INWARD
FACE_INWARD
FACE_INWARD
FACE_INWARD
```

### Vertex-sampled face drive

The field is sampled at the four vertices and each face receives the mean value at its three bounding vertices:

```text
k_f = k_self + (1/3) sum_{v in f} Phi0(x_v)
```

Result across four random initial orientations:

```text
APEX_INWARD
APEX_INWARD
APEX_INWARD
APEX_INWARD
```

Final apex alignment was effectively unity in all four runs:

```text
0.9999999983
0.9999999959
0.9999999972
0.9999999944
```

The mechanism is incidence-based rather than an explicit apex torque. If one proto-vertex is closer to T0, the three faces incident on that vertex receive the stronger field contribution while the opposite face does not. This produces a three-strong / one-weak face pattern and selects that vertex as the inward apex.

Representative final face drives:

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

The resulting tetrahedron remained rank-3 and finite-volume, with approximately 4.5% edge coefficient of variation in the tested normalized case.

Strict interpretation:

```text
This is a candidate derived mechanism for relational apex selection inside
this toy energy. It does not establish that physical MCIFT coupling is
vertex-sampled or that the Standard Model Higgs behaves this way.
```

## 4. Integrated formation during orbit

The integrated benchmark separates two roles that failed when forced into one interaction term:

```text
formation direction:
    T0 field sampled at T1 vertices -> face-drive anisotropy

orbital binding:
    existing weak-field/Newtonian bridge -> T1 center acceleration
```

An attempted use of the formation-bias energy itself as the orbital potential produced an effective radial dependence steeper than the stable inverse-radius orbital case and did not support the desired stable orbit branch. It was therefore not promoted as the binding law.

For the integrated test, T0 uses the v1.08 reference normalized mass proxy

```text
M0 = 1.663148923591514
```

and T1's center follows

```text
a = -G M0 r / |r|^3
```

while T1's internal face drives remain

```text
k_f(t) = k_self(t) + (1/3) sum_{v in f} gamma M0 / |x_v|.
```

T1 self-drive is ramped from

```text
k_self = -0.12 -> 0.08
```

over one nominal orbital period. Its four vertices and four vortex amplitudes are solved by adiabatic local-equilibrium continuation. No target apex, target side length, target volume, internal damping, or target orbital radius force is used.

### Circular case: `v = 1.0 v_c`

```text
radius min = 12.00000000
radius max = 12.00001480
retained T1 mass proxy = 0.14021335
M1/M0 = 0.08430595
apex mean after 10% mass = 0.99999975
apex min after 10% mass = 0.99997382
max edge CV after 10% mass = 0.01859862
min volume after 10% mass = 0.80467988
```

Verdict:

```text
bound orbit = pass
apex-inward formation during orbit = pass
```

### Mildly slower case: `v = 0.9 v_c`

```text
radius min = 8.16811819
radius max = 11.99999719
retained T1 mass proxy = 0.32266314
M1/M0 = 0.19400736
apex min after 10% mass = 0.99999639
```

Verdict:

```text
bound orbit = pass
apex-inward formation during orbit = pass
```

### Mildly faster case: `v = 1.1 v_c`

```text
radius min = 12.00000311
radius max = 18.37720223
retained T1 mass proxy = 0.14021187
M1/M0 = 0.08430506
apex min after 10% mass = 0.99740706
```

Verdict:

```text
bound orbit = pass
apex-inward formation during orbit = pass
```

### Super-escape control: `v = 1.45 v_c`

The escape control remained positive-energy and left the test region:

```text
radius max = 79.46803300
orbital energy ~= +0.007103
retained T1 mass proxy = 0.01621932
M1/M0 = 0.00975218
apex mean after 10% mass = 0.47555263
```

Verdict:

```text
bound orbit = fail
apex-inward formation orbit = fail
```

This is an important control: the benchmark does not capture a super-escape trajectory merely because the internal formation solver is present.

## 5. Current v1.09 interpretation

Within the selected toy assumptions, the chain is now:

```text
T0 forms first with no external preferred direction
        ↓
T0 possesses a finite normalized mass/vortex-energy proxy
        ↓
T0 creates a relational radial field for later cells
        ↓
T1 samples that field at its proto-vertices during mass gain
        ↓
three faces incident on the nearer vertex receive stronger drive
        ↓
T1 develops an inward apex while retaining finite 3D volume
        ↓
under the separate weak-field orbital bridge, bound circular and mildly
 eccentric trajectories are compatible with that apex-inward formation
```

This is a compatibility result, not a full derivation of gravity or cosmology.

## 6. What v1.09 does not establish

```text
physical Higgs microstructure
physical mass calibration
a primordial cosmic center
physical gravity from the v1.08 vortex energy
true capture from an initially unbound trajectory
spontaneous dissipative spin locking
N-body hierarchy formation
black-hole/channel inversion
replacement of QFT, GR, the Standard Model, or Lambda-CDM
```

The integrated benchmark is in the test-particle approximation with T0 fixed. Backreaction of T1 on T0 is not included.

## 7. Next target

The next meaningful test is not another pre-bound orbit. It is explicit conservative energy exchange between orbital motion and T1 internal modes:

```text
E_orbit -> E_shape + E_breathing + E_vortex
```

The target question is whether an initially positive-energy T1 trajectory can become negative-energy and bound while total energy is conserved and without inserting friction or damping.

Only after that should an N-body hierarchy of successive tetrahedral cells be explored.

## Canonical v1.09 files

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
