# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.34 first-principle cubic field toy solver

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model (Lambda-CDM). This repository contains exploratory mechanics, toy calculations, and increasingly testable cosmology-style scaffolds.

---

## Current focus

MCIFT now tests the v0.33 cubic cell-complex field formula in a minimal mode-level toy solver.

The field object is:

```text
Psi_MCIFT(i,t) = (
  K_i,
  phi_i,
  T_i,
  {a_i,mu},
  {chi_i,mu},
  {H_i,mu},
  {Omega_i,mu},
  {m_i,mu},
  m_i,
  q_i,
  Coh_i,
  S_i,
  B_i
)
```

The current conceptual chain is:

```text
cube-center knot
-> six axial connector states
-> connector information compatibility
-> Higgs-coupled face-plane vortex formation
-> vortex mass gathering / retained Higgs response
-> contained complexity loading
-> connector-supported coherence capacity
-> containment score
-> mode-coupled reservoir transfer
-> cosmology-scale growth and BAO/P(k) scoring scaffold
```

---

## v0.34 toy-solver result

```text
v0.30 dynamic-ordered RMS = 0.302859
v0.34 cubic-field RMS = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before cubic field = 617.87 Mpc
v0.34 global peak after cubic field = 152.29 Mpc
v0.34 BAO-window peak = 152.29 Mpc
```

Transfer diagnostics:

```text
v0.34 transfer at 617.87 Mpc = 0.449576
v0.30 transfer at 617.87 Mpc = 0.558702
v0.34 transfer at nearest BAO bin = 1.000000
```

Final 617.87 Mpc field state:

```text
chi_617 = 0.682207
Omega_617 = 0.379155
m_617 = 1.882739
q_617 = 36.197423
coherence_capacity_617 = 22.471565
S_617 = -13.725858
```

---

## Key files

```text
analysis/mcift_big_bang_first_principle_cubic_field_v0.34.py
analysis/results_v0.34/mcift_v0.34_first_principle_cubic_field_report.md
analysis/results_v0.34/mcift_v0.34_first_principle_cubic_field_metrics.csv
models/first_principle_cubic_field_formula_v0.33.md
models/cube_face_higgs_vortex_mass_v0.32.md
models/cube_center_six_connector_knot_v0.31.md
paper/v0.34_first_principle_cubic_field_toy_solver_addendum.md
paper/v0.33_first_principle_cubic_field_formula_addendum.md
paper/v0.32_cube_face_higgs_vortex_mass_addendum.md
paper/v0.31_cube_center_six_connector_addendum.md
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
1. Move from mode-level toy solver to a minimal spatial cubic lattice solver.
2. Instantiate explicit neighboring cube cells.
3. Evolve K_i, a_i,mu, H_i,mu, Omega_i,mu, q_i, S_i, and reservoir state directly.
4. Measure whether super-anchor collapse emerges without injecting P(k)-mode proxies.
5. Compare the resulting field spectrum back to the v0.30/v0.34 toy outputs.
6. Then test lensing, halos, CMB, BBN, and fair comparison against Lambda-CDM.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
