# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework and executable toy-model research scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v1.10 interwoven tetrahedral dynamic-fabric benchmark

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model, or standard cosmology. This repository contains exploratory mechanics, geometric checks, toy simulations, mapping experiments, and testable scaffolds.

---

## Start here

```text
CURRENT_STATUS.md
models/mcift_v1.10_interwoven_tetrahedral_dynamic_fabric.md
models/mcift_v1.09_relational_formation_and_orbit.md
models/mcift_v1.08_primordial_tetrahedron_intrinsic_stability.md
models/mcift_v1.01_dimensional_simplex_scope.md
```

## Active version chain

```text
v0.92  bubble light-cone projection
v0.93  simplified first-principle bubble formula
v0.94  central failed-mode-4 seed
v0.95  central-seed reducer
v0.96  threefold bubble-knot formula
v0.97  shared threefold reducer
v0.98  cosmology mapping
v0.99  CERN/collider mapping
v1.01  dimensional simplex scope clarification
v1.02  mobile-core tetrahedral precursor
v1.03  four-face reservoir overlap core
v1.04  damped tetrahedral recovery dynamics
v1.05  scalar + three directional facet modes
v1.06  undamped breathing and symmetry-breaking sweep
v1.07  nonlinear overload benchmark
v1.08  primordial tetrahedron intrinsic-stability benchmark
v1.09  relational second-cell formation and background-orbit compatibility
v1.10  interwoven tetrahedral dynamic fabric and outward-wave benchmark
```

The v1.02-v1.10 chain is an executable tetrahedral toy-model development path. Stored v0.97-v0.99 mapping outputs remain historical and unchanged.

---

## Main v1.10 finding

v1.10 inserts the missing fabric layer before renewed orbit/gravity claims.

Four oriented triangular closures form the boundary of one tetrahedral 3-cell and satisfy

```text
partial^2 = 0
```

so the fabric candidate is an interwoven simplicial complex rather than stacked independent triadic sheets.

For a regular tetrahedron, four equal face tangent projectors reconstruct

```text
W = (8/3) I
```

with three equal eigenvalues and exact numerical isotropy. The representative v1.09 three-strong/one-weak state instead produces one principal weave axis aligned with the weak-face normal / opposite-apex axis at `0.999999998`.

A shared tetrahedral complex carries an intrinsic angular-deficit diagnostic. Five regular tetrahedra around one edge retain

```text
delta = 7.356103 deg
```

even after fully coupled equal-loading re-equilibration.

Localized vortex loading changes the shared geometry. At +10% loading of one cell, the common-edge deficit becomes `7.850996 deg`, while mean edge response decays across the five-cell ring:

```text
distance 0: 3.278%
distance 1: 1.545%
distance 2: 0.435%
```

### Normalized time layer

Shared edge coordinates evolve under

```text
q_e = ln L_e
d2 q_e / dt2 = - partial F / partial q_e
```

with unit edge inertia and no damping.

The tested five-cell equilibrium has 16 positive edge modes and no negative modes. Localized impulses remain bounded through normalized amplitude `0.40`, with all tetrahedral volumes positive and post-step energy conserved to numerical precision.

### Central-source wave test

A five-cell source topology uses one central tetrahedron and four outer tetrahedra, one attached to each central face.

A breathing central face-vortex drive produces a near-isotropic outward response on outer-apex edges that are not directly forced:

```text
outer/source gain ~= 0.94
signed-frequency fit R^2 ~= 0.903
phase lag ~= -0.97 rad
```

A smoothly rotating internal face anisotropy around the preferred axis produces a weaker directional/phase-structured outer response:

```text
gain ~= 0.084 .. 0.088 on the three transverse driven faces
```

After forcing is removed, the undamped fabric continues ringing with conserved mechanical energy.

Strict interpretation:

```text
v1.10 demonstrates a normalized dynamic tetrahedral fabric with outward
oscillatory transmission inside the selected toy energy. It does not establish
physical spacetime, gravity, gravitational waves, a physical clock, or c.
```

---

## Relationship to v1.09

The v1.09 weak-field/Newtonian orbit runs remain historical compatibility controls. v1.10 makes clear that orbit/capture should not be promoted as internally derived until motion is formulated on the tetrahedral fabric itself.

---

## Reproducing v1.10

Canonical model:

```text
models/mcift_v1.10_interwoven_tetrahedral_dynamic_fabric.md
```

Core simulations:

```text
simulations/mcift_v1_10_interwoven_tetrahedral_fabric_benchmark.py
simulations/mcift_v1_10_vortex_loading_to_curvature_benchmark.py
simulations/mcift_v1_10_five_tetra_coupled_fabric_benchmark.py
simulations/mcift_v1_10_five_tetra_time_stress_test.py
simulations/mcift_v1_10_five_tetra_time_stress_extension.py
simulations/mcift_v1_10_central_tetra_wave_emission_phase_test.py
```

Compact audit outputs are under:

```text
analysis/results_v1.10/
```

Large time traces are generated locally by the scripts and are not required as committed audit artifacts.

Dependencies across the v1.10 scripts:

```text
numpy
pandas
scipy
torch
```

---

## Next target

```text
1. Build a 50-200 cell tetrahedral complex and derive the normal-mode dispersion
   relation omega(k).
2. Test whether a long-wavelength branch and characteristic group velocity
   emerge without assigning a target c.
3. Add explicitly dynamical vortex amplitudes with a derived inertia rather than
   adiabatically eliminating them.
4. Revisit orbit/capture only after propagation and motion are defined on the
   fabric itself.
```

---

## License

Unless otherwise noted, this repository is licensed under the **GNU Affero General Public License v3.0**. See [`LICENSE`](LICENSE).

Commercial use is allowed under the AGPL only when the user complies with its reciprocal source-code obligations. Organizations wanting proprietary or non-AGPL commercial terms should review [`COMMERCIAL-LICENSE.md`](COMMERCIAL-LICENSE.md) and contact Adrian Newton / corpobear.

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository. See [`NOTICE.md`](NOTICE.md).
