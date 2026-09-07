# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework and executable toy-model research scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v1.09 relational formation and orbit benchmark

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, geometric checks, toy simulations, mapping experiments, and testable scaffolds.

---

## Start here

```text
CURRENT_STATUS.md
models/mcift_v1.09_relational_formation_and_orbit.md
models/mcift_v1.08_primordial_tetrahedron_intrinsic_stability.md
models/mcift_v1.07_tetrahedral_facet_core_toy_chain.md
models/mcift_v1.01_dimensional_simplex_scope.md
reports/mcift_v0.99_cern_mapping_report.md
```

## Active version chain

```text
v0.92  bubble light-cone projection
v0.93  simplified first-principle bubble formula
v0.94  central failed-mode-4 seed
v0.95  central-seed reducer
v0.96  threefold bubble-knot formula
v0.97  shared threefold reducer
v0.98  cosmology mapping from shared reducer
v0.99  CERN/collider mapping from shared reducer
v1.01  dimensional simplex scope clarification
v1.02  explicit mobile-core tetrahedral precursor
v1.03  emergent four-face reservoir overlap core
v1.04  damped perturbation-recovery toy dynamics
v1.05  one scalar plus three directional facet-mode decomposition
v1.06  undamped breathing and symmetry-breaking sweep
v1.07  nonlinear central-overload breakpoint benchmark
v1.08  primordial tetrahedron intrinsic-stability benchmark
v1.09  relational second-cell formation and bound-orbit benchmark
```

The v1.02-v1.09 chain is an executable tetrahedral toy-model development path. It does not alter the stored v0.97-v0.99 collider or cosmology mappings.

---

## Main v1.09 finding

v1.09 asks what happens when a second tetrahedral cell forms after the stable v1.08 cell already exists.

The central relational rule tested is:

```text
Phi0(x) = gamma M0 / |x|

k_f(t) = k_self(t)
       + mean_{v in face f} Phi0(x_v)
```

T0's field is sampled at T1's four proto-vertices; each triangular face receives the mean of the three vertex samples on that face. No apex alignment term is used.

Across formation tests from four random initial orientations, vertex-sampled face drive produced:

```text
APEX_INWARD
APEX_INWARD
APEX_INWARD
APEX_INWARD
```

while direct face-centroid sampling produced the opposite dual orientation:

```text
FACE_INWARD
FACE_INWARD
FACE_INWARD
FACE_INWARD
```

The candidate mechanism is incidence-based: a proto-vertex closer to T0 contributes to three faces, creating a three-strong / one-weak face-drive pattern that selects that vertex as the inward apex.

### Integrated formation during orbit

The formation-bias term itself did not provide a satisfactory stable orbital potential, so v1.09 keeps two roles separate:

```text
relational orientation/mass formation:
    vertex-sampled T0 field -> T1 face-vortex drive

orbital binding control:
    existing weak-field/Newtonian bridge
```

With T0 fixed and using the v1.08 `H=1.5` normalized mass proxy as the source, T1 self-drive was ramped during the first orbital period.

Bound cases:

```text
0.9 v_c:
    radius = 8.1681 .. 12.0000
    M1/M0 = 0.1940
    minimum apex alignment after 10% mass = 0.9999964

1.0 v_c:
    radius = 12.0000 .. 12.000015
    M1/M0 = 0.08431
    minimum apex alignment after 10% mass = 0.9999738

1.1 v_c:
    radius = 12.0000 .. 18.3772
    M1/M0 = 0.08431
    minimum apex alignment after 10% mass = 0.9974071
```

All retained finite tetrahedral volume and modest edge deformation.

Super-escape control:

```text
1.45 v_c:
    positive orbital energy
    radius -> 79.47 before test exit
    M1/M0 = 0.00975
    no stable apex-inward formation orbit
```

Strict interpretation:

```text
v1.09 shows compatibility of relational apex selection during T1 mass gain
with separately modeled weak-field bound orbits. It does not derive physical
gravity from the tetrahedral vortex energy and does not demonstrate true
capture from an initially unbound trajectory.
```

---

## v1.08 retained result

The v1.08 intrinsic four-face vortex-energy benchmark uses no target edge length, edge spring, target volume, target core radius, damping, collapse switch, or preferred Cartesian direction.

Across `H=1.01..10`, the full regular-branch Hessian gave:

```text
negative modes = 0
zero symmetry modes = 6
positive physical modes = 10
```

Undamped 5%, 10%, and 20% perturbation runs remained bounded and nondegenerate. A symmetric planar four-point control had one alternating out-of-plane negative mode.

---

## Strict current status

```text
supported geometry:
    tetrahedron is the minimum nondegenerate 3D simplex

supported representation:
    four tetrahedral facet fluxes = one scalar mode + three directional modes

supported internal toy results:
    v1.08 selected intrinsic energy has a finite stable regular tetrahedral branch
    tested v1.08 undamped perturbations remain bounded and nondegenerate
    planar four-point control has an out-of-plane buckling instability
    direct face-centroid inter-cell sampling prefers face-inward orientation
    vertex-sampled face drive selects apex-inward T1 formation in tested cases
    apex-inward T1 formation is compatible with bound weak-field orbit controls
    super-escape control remains unbound

not established:
    physical dimension emergence
    a tetrahedral Standard Model Higgs field
    physical mass generation/calibration
    gravity derived from tetrahedral vortex energy
    a primordial cosmic center
    true capture from an initially unbound trajectory
    N-body hierarchy formation
    physical black-hole/channel inversion

unchanged:
    all v0.97-v0.99 outputs and their previous caveats
```

---

## Reproducing v1.09

Canonical files:

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

Python dependencies across the v1.09 scripts:

```text
numpy
pandas
scipy
torch
```

---

## Next target

```text
1. Add explicit conservative coupling between T1 orbital motion and its
   internal shape/breathing/vortex modes.
2. Launch T1 with positive orbital energy and test whether internal excitation
   can make the late orbital energy negative while total energy is conserved.
3. Only if true capture appears, release the fixed-T0 approximation and test
   two-body backreaction, then successive/N-body tetrahedral formation.
4. Keep black-hole/channel-inversion work separate until its own internal
   degree of freedom is derived without a hand-coded trigger.
```

---

## License

Unless otherwise noted, this repository is licensed under the **GNU Affero General Public License v3.0**. See [`LICENSE`](LICENSE).

Commercial use is allowed under the AGPL only when the user complies with the AGPL's reciprocal source-code obligations, including the network-use source availability requirement. Organizations that want proprietary, closed-source, paid-product, or other non-AGPL commercial terms should review [`COMMERCIAL-LICENSE.md`](COMMERCIAL-LICENSE.md) and contact Adrian Newton / corpobear for a separate written commercial license.

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
