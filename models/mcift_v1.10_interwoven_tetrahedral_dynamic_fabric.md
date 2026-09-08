# MCIFT v1.10 — Interwoven Tetrahedral Dynamic Fabric

**Status:** speculative intrinsic-geometry and normalized-dynamics toy scaffold; not established physics.  
**Previous layer:** v1.09 relational second-cell formation and weak-field orbit compatibility.  
**Purpose:** insert the missing fabric layer before any renewed orbit/gravity claim.

## 1. Motivation

v1.09 showed that a later tetrahedral cell can acquire an apex-inward orientation while gaining vortex mass, and that this orientation is compatible with separately imposed weak-field bound orbits. That experiment assumed a background space for the orbital sector.

v1.10 steps back and asks whether the tetrahedral construction itself can provide an intrinsic spatial fabric and a conservative time-update layer.

The working hierarchy is:

```text
edge relation
-> triangular three-point closure
-> four interwoven triangular closures
-> tetrahedral 3-cell
-> shared tetrahedral complex
-> collective edge/dihedral response
-> normalized undamped dynamics
-> outward wave-like response from an oscillating source cell
```

No physical spacetime, gravity, gravitational-wave, or signal-speed claim is made.

## 2. Four triadic layers form one closed 3-cell

For an oriented tetrahedron `[0123]`:

```text
partial[0123] = [123] - [023] + [013] - [012]
partial^2[0123] = 0
```

The benchmark verifies exact cancellation of all six edge-boundary contributions.

Two tetrahedra sharing one triangular layer also cancel that face from their combined external boundary. The two-cell complex has:

```text
vertices = 5
edges = 9
faces = 7
tetrahedra = 2
Euler characteristic = 1
```

Thus the natural MCIFT fabric candidate is not a stack of independent three-point sheets but an interwoven simplicial complex whose triangular closures are reused by neighboring 3-cells.

## 3. Local weave tensor

For each face with inward unit normal `n_f`, define its tangent projector

```text
P_f = I - n_f n_f^T
```

and the local weave tensor

```text
W = sum_f w_f P_f.
```

For a regular tetrahedron with four equal layer weights:

```text
W = (8/3) I
```

Numerical eigenvalues:

```text
2.6666666667
2.6666666667
2.6666666667
```

with rank 3 and zero measured isotropy error.

Using the representative v1.09 vortex amplitudes and `w_f proportional to Omega_f^2` gives:

```text
weave eigenvalues:
2.62873665
2.62874333
2.66665542

principal-axis alignment with weak-face normal:
0.9999999981
```

Thus the v1.09 three-strong / one-weak state produces one intrinsic local weave axis without a global Cartesian down direction.

## 4. Intrinsic angular-deficit observable

For edge `e`:

```text
delta_e = 2 pi - sum_{T containing e} theta_{T,e}
```

A regular tetrahedron has internal dihedral angle:

```text
theta = arccos(1/3) = 70.5287793655 deg
```

Therefore:

```text
5 regular tetrahedra around one edge:
    delta = +7.3561031725 deg

6 regular tetrahedra around one edge:
    delta = -63.1726761931 deg
```

Regular tetrahedra therefore do not exactly tile a flat Euclidean edge-star. The deficit is used only as an intrinsic geometric diagnostic.

## 5. Vortex loading changes tetrahedral deficit

The v1.08 free-vertex face energy is reused. Three face drives remain at `k=0.5`; one is weakened. Vertex positions and vortex amplitudes are optimized without prescribing edge lengths or dihedral angles.

At representative ratio:

```text
k_weak / k_strong = 0.93475
volume = 8.2722566049
edge CV = 0.00637280
Omega_weak = 0.55259053
Omega_strong mean = 0.57895813
```

Inserted as one deformed member of a five-tetra edge-star control:

```text
weak-face-edge deficit mean = 7.01652691 deg
opposite-apex-edge deficit mean = 7.69353433 deg
deficit split = 0.67700742 deg
```

Toy chain:

```text
unequal face-vortex drive
-> free tetrahedral deformation
-> dihedral-angle change
-> angular-deficit change
```

This is not a calibrated physical mass-curvature law.

## 6. Fully coupled five-tetra fabric

Five tetrahedra share one common edge. Shared edges and triangular layers are represented once, with no global Euclidean embedding imposed by the optimizer.

Equal loading re-equilibrates to the regular branch:

```text
edge length = 4.1573970964
edge CV ~= 2e-15
common-edge deficit = 7.3561031725 deg
```

The selected intrinsic energy therefore does not self-flatten the regular five-cell edge-star.

Localized loading of cell 0 changes the entire shared geometry. Common-edge deficit sweep:

```text
0%  -> 7.3561 deg
2%  -> 7.4359 deg
5%  -> 7.5761 deg
10% -> 7.8510 deg
20% -> 8.4865 deg
```

At +10% loading, mean absolute edge response by topological ring distance is:

```text
distance 0: 3.278%
distance 1: 1.545%
distance 2: 0.435%
```

The common-edge dihedral response alternates in sign across the ring, so the network redistributes geometric strain rather than transmitting a single scalar deformation.

## 7. Explicit normalized time dynamics

Replace adiabatic global re-optimization with shared-edge coordinates

```text
q_e = ln L_e
```

and normalized unit-inertia evolution

```text
d^2 q_e / dt^2 = - partial F / partial q_e.
```

No damping is used.

The five-edge-star equilibrium Hessian has:

```text
positive modes = 16
negative modes = 0
zero intrinsic modes = 0
```

A localized initial velocity impulse applied only to non-common edges of cell 0 produces delayed dominant response across topology. At 1% impulse and a 0.05% cell-strain threshold:

```text
distance 0: t = 0.15
distance 1: t = 0.30
distance 2: t = 25.375
```

Energy conservation at 1% impulse:

```text
relative energy band = 6.10e-10
```

Nonlinear stress extension remained bounded through normalized impulse 0.40:

```text
max |Delta ln L| = 0.17506
minimum tetrahedral volume = 6.70396
relative energy band ~= 9.91e-7
```

Tiny analytic tails in a finite oscillator network prevent this threshold test from proving a strict causal front or fundamental propagation speed.

## 8. Central-cell vibration and rotating-anisotropy emission

A second five-cell topology is used:

```text
1 central tetrahedron
4 outer tetrahedra
1 attached to each central face
```

The central tetrahedron retains the v1.09 preferred face/axis. Its four shared triangular layers couple directly to the outer cells, while each outer cell has three outer-apex edges that are not directly driven.

Rigid-body rotation cannot couple to an intrinsic edge-length fabric, because edge lengths are rotation invariant. The rotation test therefore uses a smoothly rotating internal face-vortex anisotropy around the preferred axis.

Three controls are run:

```text
breathing only
rotating anisotropy only
combined breathing + rotating anisotropy
```

### Breathing emission

Signed outer-apex edge strain fits the central breathing frequency with approximately equal amplitudes on all four outer tetrahedra:

```text
outer amplitudes ~= 0.01691 .. 0.01696
source drive amplitude = 0.018
outer/source gain ~= 0.940 .. 0.942
fit R^2 ~= 0.903
phase lag ~= -0.97 rad
```

This is an approximately isotropic outward oscillatory response.

### Rotating anisotropy emission

The rotating source produces weaker, direction-dependent outer response. Three driven faces show:

```text
outer amplitudes ~= 0.00199 .. 0.00208
gain ~= 0.084 .. 0.088
fit R^2 ~= 0.64 .. 0.67
phase lag relative to local face drive ~= pi
```

The preferred-axis face has zero transverse rotating drive by construction and correspondingly negligible fitted response at that drive frequency.

Thus the rotating internal anisotropy emits a directional phase-structured disturbance rather than an isotropic pulse.

### Post-drive ringing

After forcing is smoothly switched off, the undamped five-cell complexes continue to ring while conserving mechanical energy:

```text
breathing post-drive relative energy band ~= 5.89e-8
rotating post-drive relative energy band ~= 1.72e-9
combined post-drive relative energy band ~= 5.87e-8
```

Strict interpretation:

```text
The selected toy fabric supports outward oscillatory transmission from a
vibrating/rotating-anisotropy source cell. This is not a physical gravitational-
wave prediction and does not yet define physical time or c.
```

## 9. Current v1.10 verdict

```text
INTERWOVEN_TETRAHEDRAL_DYNAMIC_FABRIC_PASS_WITH_NORMALIZED_OUTWARD_WAVE_RESPONSE
```

Supported inside the toy scaffold:

```text
- four triadic layers close into one tetrahedral 3-cell
- equal regular face layers reconstruct an isotropic rank-3 weave
- v1.09 unequal face loading produces one intrinsic weave axis
- shared tetrahedral complexes carry angular-deficit geometry
- vortex loading changes shape and angular deficits without prescribed deformation
- localized loading deforms neighboring cells through shared structure
- undamped shared-edge dynamics are bounded across tested impulses
- a vibrating central tetrahedron produces near-isotropic outward oscillatory response
- rotating internal anisotropy produces weaker directional/phase-structured response
```

Not established:

```text
- physical spacetime emergence
- physical time calibration
- a fundamental causal speed or c
- physical gravity derived from the face-vortex energy
- physical gravitational waves
- physical mass-curvature calibration
- physical rigid-body rotation coupling
- continuum or large-N limit
```

## 10. Next required tests

```text
1. Build a substantially larger tetrahedral complex and derive its normal-mode
   spectrum / dispersion relation omega(k).
2. Test whether a long-wavelength propagation branch and characteristic group
   velocity emerge without assigning a target signal speed.
3. Couple source vortex amplitudes dynamically rather than adiabatically
   eliminating them, with their inertia derived from the same energy scaffold.
4. Only after a dynamical fabric and propagation law are established should the
   v1.09 orbit/capture question be revisited without the weak-field bridge.
```
