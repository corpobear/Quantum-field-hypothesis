# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework and executable toy-model research scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v1.08 primordial tetrahedron intrinsic-stability benchmark

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, geometric checks, toy simulations, mapping experiments, and testable scaffolds.

---

## Start here

```text
CURRENT_STATUS.md
models/mcift_v1.08_primordial_tetrahedron_intrinsic_stability.md
models/mcift_v1.07_tetrahedral_facet_core_toy_chain.md
models/mcift_v1.01_dimensional_simplex_scope.md
reports/mcift_v0.99_cern_mapping_report.md
reports/mcift_v0.98_cosmology_mapping_report.md
reports/mcift_v0.97_threefold_reducer_report.md
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
```

The v1.02-v1.08 chain is an executable tetrahedral toy-model development path. It does not alter the stored v0.97-v0.99 collider or cosmology mappings.

---

## Main v1.08 finding

v1.08 replaces the hand-selected v1.07 collapse-radius experiment with an intrinsic four-face vortex-energy test. Four freely moving vertices and four face-vortex amplitudes evolve under a potential that depends only on triangular face area, face-centered second moment, vortex amplitude, and normalized face coupling.

The benchmark uses no:

```text
target edge length
edge spring
target volume
target core radius
damping
collapse switch
preferred Cartesian direction
```

For equal face loading, the regular tetrahedral branch is

```text
L_eq^2 = k / (3 rho c_tri)
Omega_eq^2 = 2 k / (3 beta)
c_tri = 27/2800
```

with `k = g H chi - alpha`.

Across the tested normalized range `H=1.01..10`, the full 16-coordinate Hessian gave:

```text
negative modes = 0
zero symmetry modes = 6
positive physical modes = 10
```

The six zero modes are consistent with three translations and three rigid rotations. Undamped 5%, 10%, and 20% perturbation runs remained bounded and retained nonzero tetrahedral volume.

### Planar control

A symmetric planar four-point square under the same toy energy had:

```text
negative modes = 1
zero modes = 6
positive modes = 9
```

The negative mode is alternating out-of-plane vertex motion. A tiny out-of-plane perturbation therefore drives the planar control into nonzero 3D volume and it passes close to a regular tetrahedral edge pattern during the undamped run.

Strict interpretation:

```text
This is a stability/buckling result of the selected intrinsic toy energy.
It is not a derivation that physical spacetime emerges from a plane.
```

---

## Earlier tetrahedral findings retained

### Emergent geometric center

Four inward face-normal channels of a regular tetrahedron intersect at the tetrahedral center and produce isotropic localization:

```text
four-way overlap score = 4.0
localization condition number = 1.0
```

A four-channel planar square also produces a center, but with anisotropic localization:

```text
localization condition number = 2.0
```

Therefore center formation itself is not unique to the tetrahedron; the earlier diagnostic distinguished isotropic 3D localization.

### Four facet modes

For regular tetrahedral inward normals:

```text
J0 = mean(Jf)
S  = (3/4) sum_f Jf nf
Jf = J0 + nf . S
```

This is an exact decomposition of four facet inputs into one symmetric scalar mode plus three directional modes. The six edges remain structural relations rather than six independent sinks.

### v1.07 overload control

v1.07 demonstrated a finite collapse branch only after an explicit nonlinear radius turnover and collapse radius were selected. v1.08 does not reuse that switch.

---

## Strict current status

```text
supported geometry:
    tetrahedron is the minimum nondegenerate 3D simplex

supported representation:
    four tetrahedral facet fluxes = one scalar mode + three directional modes

supported internal toy results:
    coherent tetrahedral face normals create isotropic central localization
    the v1.08 selected intrinsic energy has a finite regular tetrahedral branch
    all tested v1.08 regular-branch physical modes are positive
    tested undamped perturbations remain bounded and nondegenerate
    the planar four-point control has an out-of-plane buckling instability

not established:
    physical dimension emergence
    a tetrahedral Standard Model Higgs field
    physical mass generation
    a primordial cosmic center
    a physical black-hole or Big Bang mechanism
    channel inversion or a parameter-free collapse threshold

unchanged:
    all v0.97-v0.99 outputs and their previous caveats
```

---

## Reproducing v1.08

Canonical files:

```text
models/mcift_v1.08_primordial_tetrahedron_intrinsic_stability.md
simulations/mcift_v1_08_primordial_tetrahedron_stability.py
analysis/results_v1.08/primordial_tetrahedron_stability_metrics.json
analysis/results_v1.08/primordial_tetrahedron_stability_sweep.csv
```

Python dependencies:

```text
numpy
pandas
torch
```

The simulation generates its detailed dynamics trace locally. The committed JSON metrics and loading sweep are the compact auditable outputs.

---

## Next target

```text
1. Test unequal face loading with free vertices and compare the derived
   deformation direction with the exact v1.05 facet-mode vector S.
2. Derive an inward/outward channel-orientation degree of freedom and its
   energy, then search for an inversion branch without a hand-coded trigger.
3. Add nonplanar competing four-point controls and parameter-family sweeps.
4. Freeze equations, parameters, and acceptance criteria before any new
   collider, cosmology, black-hole, or early-universe mapping.
```

---

## License

Unless otherwise noted, this repository is licensed under the **GNU Affero General Public License v3.0**. See [`LICENSE`](LICENSE).

Commercial use is allowed under the AGPL only when the user complies with the AGPL's reciprocal source-code obligations, including the network-use source availability requirement. Organizations that want proprietary, closed-source, paid-product, or other non-AGPL commercial terms should review [`COMMERCIAL-LICENSE.md`](COMMERCIAL-LICENSE.md) and contact Adrian Newton / corpobear for a separate written commercial license.

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
