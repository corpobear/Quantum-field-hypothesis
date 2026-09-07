# Current MCIFT Status: v1.08 Primordial Tetrahedron Intrinsic Stability

**Status:** speculative intrinsic-geometry and vortex-energy toy scaffold; not established physics.  
**Current layer:** v1.08 free-vertex tetrahedral stability and planar-buckling benchmark.  
**Previous layer:** v1.07 nonlinear overload benchmark with an explicitly selected collapse branch.  
**Previous physical-mapping layer:** v0.99 CERN/collider mapping from the v0.97 shared threefold reducer.

## Verdict

```text
PRIMORDIAL_TETRAHEDRON_INTRINSIC_STABILITY_PASS_WITHIN_SELECTED_TOY_ENERGY
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
```

## v1.08 intrinsic construction

The v1.08 state uses:

```text
4 freely moving vertices
4 triangular faces
4 face-vortex amplitudes
```

For each face:

```text
A_f = triangular area
Q_f = sum over face vertices |x_i - face centroid|^2
c_tri = 27/2800
```

The selected intrinsic potential is

```text
F = sum_f A_f [
      0.5 (rho c_tri Q_f - k_f) Omega_f^2
      + beta/4 Omega_f^4
    ]

k_f = g H_f chi_f - alpha
```

The benchmark normalization is

```text
alpha = g = beta = rho = chi = 1
```

No target edge length, target volume, edge spring, target core radius, damping, collapse switch, or preferred Cartesian direction is used.

## Finite regular branch

Under equal face loading `k_f=k`, the regular tetrahedral stationary branch is

```text
L_eq^2 = k / (3 rho c_tri)
Omega_eq^2 = 2 k / (3 beta)
```

Thus finite size is not supplied as a target length inside this benchmark; it follows from the selected face-coupling/circulation energy competition.

## Full stability spectrum

The full state has 16 coordinates:

```text
12 vertex coordinates
4 vortex amplitudes
```

Across

```text
H = 1.01, 1.05, 1.10, 1.25, 1.50, 2.0, 3.0, 5.0, 10.0
```

every tested regular state had

```text
negative modes = 0
zero modes = 6
positive modes = 10
```

The six zero modes are consistent with the three translations and three rigid rotations expected for an intrinsic potential.

Reference `H=1.5`:

```text
L_eq = 4.1573970964
Omega_eq = 0.5773502692
mass proxy = 1.6631489236
softest positive eigenvalue = 0.06415002991
softest unit-inertia frequency = 0.2532785619
```

The mass proxy is a normalized positive localized vortex-energy bookkeeping quantity, not physical mass.

## Undamped nonlinear perturbations

At `H=1.5`, randomized free-vertex/vortex perturbations remained nondegenerate and bounded over the simulated interval.

```text
5% perturbation:
    max edge CV = 0.0182872
    min volume = 7.5776453

10% perturbation:
    max edge CV = 0.0350478
    min volume = 6.6141303

20% perturbation:
    max edge CV = 0.0803135
    min volume = 4.4994656
```

No damping was used.

## Planar control

The symmetric planar four-point square at `H=1.5` had

```text
negative modes = 1
zero modes = 6
positive modes = 9
unstable eigenvalue = -0.05555555556
```

The negative mode is alternating out-of-plane vertex motion. A tiny perturbation along that mode produced nonzero 3D volume in the undamped simulation:

```text
initial sampled volume = 0.0311148
maximum sampled volume = 9.7566331
minimum sampled edge CV = 0.00172718
```

Strict interpretation:

```text
This is a 3D-buckling instability of the planar control under the selected
toy energy. It is not evidence by itself that physical spacetime emerges
from a two-dimensional state.
```

## Relationship to v1.07

v1.07 inserted:

```text
nonlinear radius turnover
collapse radius
inner-channel target radius
```

and therefore demonstrated only the behavior of that selected collapse law.

v1.08 removes those elements. Over `H=1.01..10`, no regular-branch instability appeared; the tested branch instead became stiffer with loading.

However:

```text
channel inversion is not represented by the current v1.08 coordinates
```

so v1.08 establishes neither the existence nor impossibility of an inverted-channel branch.

## Earlier retained results

```text
v1.03:
    regular tetrahedral face channels give isotropic central localization

v1.05:
    J0 = mean(Jf)
    S = (3/4) sum_f Jf nf
    exact one-scalar plus three-directional facet decomposition

v1.06:
    ideal symmetric loading separates breathing from translation
    nonzero single-face asymmetry activates bounded directional motion
```

## Existing v0.97-v0.99 outputs

The older mapping values are unchanged and are not regenerated by v1.08.

```text
load_proxy = 0.009817928223
mean_shear_proxy = 0.063915576742
beta4_needed_for_balance = 0.170868625373
H_proxy_relative = 0.977215138494

Gamma_model = 4.109958967868 MeV
mu_inclusive_model = 1.000000000000
CMS HZZ residual = 0.526 sigma
D_proxy = -0.504201958707
ATLAS D residual = 1.717 sigma
CMS D residual = -0.880 sigma
```

## Strict status

```text
supported geometry:
    simplex nondegeneracy and tetrahedral volume checks

supported representation:
    exact one-scalar plus three-directional decomposition of four facet fluxes

supported internal toy behavior:
    isotropic face-channel center
    finite regular tetrahedral branch under the selected v1.08 intrinsic energy
    positive physical Hessian spectrum across the tested regular branch
    bounded undamped free-vertex perturbations at H=1.5
    planar four-point out-of-plane buckling instability

not established:
    physical Higgs tetrahedral microstructure
    physical mass generation
    physical dimensional emergence
    a primordial cosmic center
    channel inversion
    parameter-free black-hole formation
    Big Bang formation

unchanged:
    v0.97-v0.99 numerical mappings and caveats

not claimed:
    replacement of QFT, GR, the Standard Model, or Lambda-CDM
```

## Files

```text
models/mcift_v1.08_primordial_tetrahedron_intrinsic_stability.md
simulations/mcift_v1_08_primordial_tetrahedron_stability.py
analysis/results_v1.08/primordial_tetrahedron_stability_metrics.json
analysis/results_v1.08/primordial_tetrahedron_stability_sweep.csv
models/mcift_v1.07_tetrahedral_facet_core_toy_chain.md
models/mcift_v1.01_dimensional_simplex_scope.md
reports/mcift_v0.99_cern_mapping_report.md
reports/mcift_v0.98_cosmology_mapping_report.md
reports/mcift_v0.97_threefold_reducer_report.md
```

## Next

```text
1. Test unequal face loading with fully free vertices and compare the derived
   deformation direction with the exact v1.05 vector S.
2. Derive a channel orientation/inversion coordinate and add it to the same
   intrinsic energy without a hand-coded collapse trigger.
3. Search for competing nonplanar four-point minima and parameter-family
   failures of the regular branch.
4. Freeze equations and acceptance criteria before any new external mapping.
```

No new collider, cosmology, black-hole, or early-universe mapping should be promoted before those derivations and out-of-sample tests exist.
