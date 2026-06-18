# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current level

```text
Current first-principle formulation: v0.33 cubic cell-complex field formula
Current mechanism layer: v0.32 cube-face Higgs vortex mass mechanism
Current geometry layer: v0.31 cube-center six-connector knot model
Current numeric cosmology retest: v0.30 dynamic ordered collapse-containment
```

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The correct wording is "no parameter sweep / internally constrained heuristic closure", not strict no-fit proof.
```

---

## v0.33 solver target

The v0.33 field formula defines the local field as:

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

with:

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

This provides the next analysis target:

```text
first-principle cubic field variables -> minimal solver -> retest v0.30 collapse behavior
```

Read:

```text
models/first_principle_cubic_field_formula_v0.33.md
```

---

## Cosmology scaffold: v0.16-v0.30

| Version | Script | Result folder | Purpose | Status |
|---|---|---|---|---|
| v0.16 | `mcift_big_bang_comparison_v0.16.py` | `results_v0.16/` | first visible/dark and BAO proxy comparison | exploratory |
| v0.17 | `mcift_big_bang_scale_lock_v0.17.py` | `results_v0.17/` | expansion-coupled scale-lock | partial |
| v0.18 | `mcift_big_bang_longmode_v0.18.py` | `results_v0.18/` | long-mode damping / primordial gate | pass-like peak proxy |
| v0.19 | `mcift_big_bang_anchor_cutoff_v0.19.py` | `results_v0.19/` | derives `k_cut = 2 pi / R_A` | stronger proxy |
| v0.20 | `mcift_big_bang_derived_scalelock_v0.20.py` | `results_v0.20/` | derives scale-lock amplitude/envelope | raw geometric proxy |
| v0.21 | `mcift_big_bang_pk_shape_v0.21.py` | `results_v0.21/` | full P(k) shape test | raw shape FAIL |
| v0.22 | `mcift_big_bang_growth_transfer_v0.22.py` | `results_v0.22/` | imported growth-transfer compatibility | PASS-LIKE with imported transfer |
| v0.23 | `mcift_big_bang_native_growth_v0.23.py` | `results_v0.23/` | first native no-import growth | FAIL |
| v0.24 | `mcift_big_bang_channel_exchange_v0.24.py` | `results_v0.24/` | coupled A/V/D/R channel exchange | WEAK |
| v0.25 | `mcift_big_bang_first_principle_sinks_v0.25.py` | `results_v0.25/` | first-principle six-sink count | WEAK |
| v0.26 | `mcift_big_bang_spin_blur_v0.26.py` | `results_v0.26/` | six-sector spin blur | WEAK |
| v0.27 | `mcift_big_bang_mass_gravity_time_spin_v0.27.py` | `results_v0.27/` | mass/gravity time-response spin blur | WEAK |
| v0.28 | `mcift_big_bang_thermo_spin_growth_v0.28.py` | `results_v0.28/` | thermodynamic spin-growth | PASS-LIKE shape; global 617.87 Mpc |
| v0.29 | `mcift_big_bang_collapse_containment_v0.29.py` | `results_v0.29/` | post-run collapse-containment overlay | global peak 152.29 Mpc |
| v0.30 | `mcift_big_bang_dynamic_ordered_collapse_v0.30.py` | `results_v0.30/` | response-epoch B reservoir before final scoring | PASS-LIKE; global peak 152.29 Mpc |

---

## Latest numeric run: v0.30 dynamic ordered collapse-containment

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

## Next analysis target

```text
v0.34 target:
Implement a minimal numerical solver using the v0.33 field variables, then retest whether the v0.30 collapse behavior survives with connector/vortex variables active.
```
