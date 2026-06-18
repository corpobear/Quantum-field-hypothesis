# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.33 first-principle cubic field formula

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model (Lambda-CDM). This repository contains exploratory mechanics, toy calculations, and increasingly testable cosmology-style scaffolds.

---

## Current focus

MCIFT now defines the field as a cubic cell-complex object:

```text
node variables      at cube-center knots
link variables      on six center-to-center connectors
face variables      on Higgs-coupled vortex planes
cell variables      for mass, complexity, coherence, stability, and collapse reservoir
```

The v0.33 local field is:

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

---

## Current conceptual chain

```text
multi-channel information field
-> cube-centered knot with six axial connector states
-> connector information compatibility
-> Higgs-coupled face-plane vortex formation
-> vortex mass gathering / retained Higgs response
-> contained complexity loading
-> connector-supported coherence capacity
-> collapse-containment when coherence cannot hold complexity
-> collapsed-knot reservoir B
-> cosmology-scale growth and BAO/P(k) scoring scaffold
```

---

## Defining v0.33 equations

```text
A_ij,mu      = sqrt(a_i,mu a_j,-mu)
chi_i,mu     = A_ij,mu P_phase P_timing P_match
Omega_i,mu   = H_i,mu sigma(chi_i,mu - chi_c)
m_i,mu       = m_scale Omega_i,mu a_i,mu
m_i          = sum_mu m_i,mu
Coh_i        = 6 a_i,mean - lambda_Delta Delta_i
q_i          = q_i,base + alpha_m m_i + alpha_Omega sum_mu |grad_mu Omega_i,mu|
S_i          = Coh_i - q_i
dB_i/dt      = gamma_B max(0,-S_i) - decay_B B_i
```

---

## Wording correction

Earlier docs used **"no-fit"** too strongly. The current wording is:

```text
no parameter sweep / internally constrained heuristic closure
```

This means parameters were not swept to match the target, but the closure choices remain model assumptions.

---

## Latest numeric result: v0.30

```text
v0.28 RMS = 0.302859
v0.29 overlay RMS = 0.302859
v0.30 dynamic-ordered RMS = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before dynamic order = 617.87 Mpc
v0.30 global peak after dynamic order = 152.29 Mpc
v0.30 BAO-window peak = 152.29 Mpc
```

---

## Key files

```text
models/first_principle_cubic_field_formula_v0.33.md
models/cube_face_higgs_vortex_mass_v0.32.md
models/cube_center_six_connector_knot_v0.31.md
analysis/mcift_big_bang_dynamic_ordered_collapse_v0.30.py
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_report.md
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_metrics.csv
paper/v0.33_first_principle_cubic_field_formula_addendum.md
paper/v0.32_cube_face_higgs_vortex_mass_addendum.md
paper/v0.31_cube_center_six_connector_addendum.md
paper/v0.30_dynamic_ordered_collapse_addendum.md
mechanics/mechanics_v0.13.md
```

---

## Research roadmap

Next required tests:

```text
1. Implement a minimal numerical solver using v0.33 field variables.
2. Evolve a_i,mu connector activations.
3. Compute chi_i,mu information compatibility.
4. Generate Omega_i,mu Higgs face-plane vortex response.
5. Compute m_i mass loading and q_i contained complexity.
6. Update B_i collapse reservoir.
7. Test whether the v0.30 collapse result survives with connector/vortex variables active.
8. Then test lensing, halos, CMB, BBN, and fair comparison against Lambda-CDM.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
