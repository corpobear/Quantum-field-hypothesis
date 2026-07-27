# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework and executable toy-model research scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v1.07 tetrahedral facet-core toy benchmark chain

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, geometric checks, toy simulations, mapping experiments, and testable scaffolds.

---

## Start here

```text
CURRENT_STATUS.md
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
```

The v1.02-v1.07 chain introduces executable tetrahedral toy experiments. It does not alter the stored v0.97-v0.99 collider or cosmology mappings.

---

## Main v1.03-v1.07 findings

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

Therefore the current diagnostic distinguishes the tetrahedron by 3D isotropy, not by the mere existence of a center.

### Four facet modes

For regular tetrahedral inward normals:

```text
J0 = mean(Jf)
S  = (3/4) sum_f Jf nf
Jf = J0 + nf . S
```

This is an exact decomposition of four facet inputs into:

```text
one symmetric scalar mass/breathing mode
three directional sink modes
```

The six edges remain structural relations, not six mass sinks.

### Toy dynamic behavior

Under the stated assumed dynamics:

```text
- disturbed tetrahedral states recovered under damped restoring forces
- symmetric loading generated mass gain and radial breathing with zero translation
- removing damping produced persistent centered radial vibration
- any nonzero single-facet asymmetry activated bounded translation
- no finite instability threshold appeared in the linear restoring model
```

### Nonlinear overload benchmark

An explicitly assumed nonlinear radius law produced a sampled transition between stable breathing and an inner-channel collapse branch:

```text
last sampled stable amplitude = 0.6666667
first sampled collapse amplitude = 0.7037037
```

This breakpoint is a property of the selected toy law, which includes an assumed quadratic turnover and an explicit collapse radius. It is not evidence for a physical black-hole or Big Bang threshold.

---

## Strict current status

```text
supported geometry:
    tetrahedron is the minimum nondegenerate 3D simplex

supported representation:
    four tetrahedral facet fluxes = one scalar mode + three directional modes

supported internal toy result:
    coherent tetrahedral face normals create isotropic central localization

not established:
    physical dimension emergence
    a tetrahedral Standard Model Higgs field
    physical mass generation by the toy scalar mode
    physical black-hole or Big Bang formation
    a parameter-free collapse threshold

unchanged:
    all v0.97-v0.99 outputs and their previous caveats
```

---

## Reproducing v1.07

The committed benchmark is:

```text
simulations/mcift_v1_07_mass_breakpoint_benchmark_gif.py
analysis/results_v1.07/mass_breakpoint_benchmark_metrics.json
```

It requires:

```text
numpy
matplotlib
Pillow
```

The script regenerates the GIF locally. Generated animations are visualization artifacts; the source and JSON metrics are the auditable outputs.

The measured v1.02-v1.06 precursor findings and their limitations are consolidated in `models/mcift_v1.07_tetrahedral_facet_core_toy_chain.md`. Their equations should be consolidated and reviewed before the precursor source files are promoted as canonical repository models.

---

## Next target

```text
Derive a nonlinear transfer and shell-coupling law from explicit MCIFT
assumptions, then test asymmetric shell rupture and parameter-free threshold
behavior before making any external physical mapping.
```

Only after the equations and parameters are frozen should any collider, cosmology, black-hole, or early-universe comparison be attempted.

---

## License

Unless otherwise noted, this repository is licensed under the **GNU Affero General Public License v3.0**. See [`LICENSE`](LICENSE).

Commercial use is allowed under the AGPL only when the user complies with the AGPL's reciprocal source-code obligations, including the network-use source availability requirement. Organizations that want proprietary, closed-source, paid-product, or other non-AGPL commercial terms should review [`COMMERCIAL-LICENSE.md`](COMMERCIAL-LICENSE.md) and contact Adrian Newton / corpobear for a separate written commercial license.

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
