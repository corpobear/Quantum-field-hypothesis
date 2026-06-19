# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.56 unified first-principle field formula

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has a consolidated formula layer:

```text
v0.33 base:
  cubic node/link/face/cell field formula

v0.49-v0.55 learned mechanics:
  visible/hidden split, rotation, clock/lapse, sound, kappa/readout, cosmology, Q_i transfer

v0.56 consolidation:
  all downstream calculations become projections/readouts of one extended field object
```

Current verdict:

```text
v0.56 unified first-principle formula = PASS_FIRST_PRINCIPLE_CLOSURE_SCAFFOLD
```

This is a formula-consolidation scaffold, not a complete predictive physics theory.

---

## v0.56 result

```text
criteria_pass_count = 14/14
Omega_m_like_from_visible_plus_hidden = 0.315000
component_sum_after_transfer = 1.000000
omega_lab_direct_from_tau = 0.062557986756
omega_lab_reference = 0.062557986756
c_sound_proxy = 0.582034
sound_horizon_proxy_at_a1 = 0.394142
mu_eff_k_0p1 = 1.214007
```

---

## Unified field object

```text
Psi_i^0.56 = (
  K_i, phi_i, T_i,
  {a_i,mu}, {chi_i,mu},
  {H_i,mu}, {Omega_i,mu}, {m_i,mu},
  E_i, R_lock_i, lambda_R_i, rho_ratio_i,
  L_i, omega_i, I_i,
  P_v,i, P_h,i,
  rho_v,i, rho_h,i, rho_rot,i, rho_s,i, rho_r,i,
  G_i, N_i,
  c_s,i, A_sound_i, Sigma_i,
  q_i, Coh_i, S_i, B_i,
  {Q_i->j}
)
```

---

## Direct readout map

```text
collision stability -> S_i = Coh_i - q_i
visible channels -> W_c(Psi)
hidden matter -> P_h(Psi)
rotation -> L_i from discarded vibration
time dilation -> N_i from load and rotation
sound spread -> c_s and A_sound from coherence/load
cosmology -> coarse-grained rho_alpha and Q_i
```

---

## Analysis result files

```text
CURRENT_STATUS.md
models/first_principle_unified_field_formula_v0.56.md
analysis/results_v0.56/mcift_v0.56_first_principle_closure_report.md
analysis/results_v0.56/mcift_v0.56_first_principle_closure_metrics.csv
analysis/results_v0.56/mcift_v0.56_direct_readouts.csv
analysis/results_v0.56/mcift_v0.56_criteria.csv
```

---

## Important limitation

```text
v0.56 defines one field object and projection chain. It does not yet derive all numerical coefficients from first principles.
```

---

## Research roadmap

Next required tests:

```text
1. Implement v0.56 as executable code.
2. Replace assigned channel/category coefficients with field-measured projections.
3. Derive Q_i transfer rates dynamically from Psi_i.
4. Recompute particle and cosmology outputs from the unified field only.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
