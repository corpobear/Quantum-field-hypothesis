# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.35 minimal spatial cubic lattice solver

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model (Lambda-CDM). This repository contains exploratory mechanics, toy calculations, and increasingly testable cosmology-style scaffolds.

---

## Current focus

MCIFT now tests the cubic field formula in an explicit periodic spatial lattice.

```text
64^3 cube-center nodes
six nearest-neighbor connector activations
Higgs face-plane vortex response
mass / complexity loading
local coherence capacity
local stability score
spatial reservoir field
shell-spectrum measurement
```

The current conceptual chain is:

```text
cube-center knot
-> six axial connector states
-> neighboring-cell connector compatibility
-> Higgs-coupled face-plane vortex formation
-> vortex mass gathering / retained Higgs response
-> contained complexity loading
-> connector-supported coherence capacity
-> local stability score
-> spatial reservoir field
-> shell spectrum and mapped P(k) scoring
```

---

## v0.35 spatial-lattice result

```text
v0.34 mode-level RMS = 0.302859
v0.35 spatial-lattice mapped RMS = 0.303948
shape verdict = PASS-LIKE
spatial pre-collapse peak = 617.87 Mpc, harmonic n=1
spatial post-collapse peak = 154.47 Mpc, harmonic n=4
mapped v0.35 global peak = 152.29 Mpc
mapped v0.35 BAO-window peak = 152.29 Mpc
```

Transfer diagnostics:

```text
mapped transfer at 617.87 Mpc = 0.005363
mapped transfer at nearest BAO bin = 0.940620
shell n=1 transfer = 0.005363
shell n=4 transfer = 0.940620
```

Important limitation:

```text
v0.35 is still a toy lattice stress test. The initial field includes a super-anchor domain mode and a cubic connector resonance to test whether the mechanism evolves them correctly. It is not yet a full cosmological initial-condition generator.
```

---

## Key files

```text
analysis/mcift_spatial_cubic_lattice_v0.35.py
analysis/results_v0.35/mcift_v0.35_spatial_lattice_report.md
analysis/results_v0.35/mcift_v0.35_spatial_lattice_metrics.csv
analysis/results_v0.35/mcift_v0.35_spatial_lattice_shell_power.csv
analysis/mcift_big_bang_first_principle_cubic_field_v0.34.py
models/first_principle_cubic_field_formula_v0.33.md
models/cube_face_higgs_vortex_mass_v0.32.md
models/cube_center_six_connector_knot_v0.31.md
paper/v0.35_spatial_cubic_lattice_solver_addendum.md
paper/v0.34_first_principle_cubic_field_toy_solver_addendum.md
```

---

## Wording correction

Earlier docs used **"no-fit"** too strongly. The current wording is:

```text
no parameter sweep / internally constrained heuristic closure
```

This means parameters were not swept to match the target, but the closure choices remain model assumptions.

---

## Research roadmap

Next required tests:

```text
1. Remove explicit stress-test harmonic seeding.
2. Initialize K_i, a_i,mu, and H_i,mu from internal noise and boundary constraints.
3. Let connector/vortex dynamics generate the dominant spectrum.
4. Check whether n=4 / BAO-window resonance emerges without being placed in the initial condition.
5. Then test lensing, halos, CMB, BBN, and fair comparison against Lambda-CDM.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
