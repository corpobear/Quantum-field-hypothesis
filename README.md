# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.38 mass-energy vibration channel retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now adds Einstein mass-energy conversion to the v0.37 line-chain sink:

```text
mass gathered by spin-drill sink
-> E = m c^2
-> vibration energy
-> decay/leakage channel proxies
```

Verdict:

```text
v0.38 mass-energy vibration retest = PASS-LIKE, 9/9 strict toy criteria
```

---

## v0.38 result

```text
peak_E_vib_GeV_proxy = 0.023315
peak_E_vib_step = 319
peak_E_vib_time = 6.380000
final_E_vib_over_peak = 0.187542
integrated_E_in_GeV_proxy = 0.000691
integrated_E_leak_GeV_proxy = 0.000351
```

Channel fractions:

```text
bb_like     = 0.559140  target ~ 0.582000
WZ_like     = 0.316161  target ~ 0.240000
gg_like     = 0.100017  target ~ 0.086000
tau_like    = 0.024090  target ~ 0.063000
gamma_like  = 0.000402  target ~ 0.002300
mumu_like   = 0.000189  target ~ 0.000220
```

---

## Key math

```text
E_m,i(t) = eta_m m_i(t) c^2
E_vib,i(t+dt) = E_vib,i(t) + E_m,i(t) - E_leak,i(t) - damping
omega_vib,i = E_vib,i / hbar
```

Channel source families:

```text
mass-retention source      -> bb-like, tau-like, mumu-like
coherent symmetric source  -> WZ-like
transverse turbulence      -> gg-like, gamma-like loop channels
```

---

## Key files

```text
analysis/results_v0.38/mcift_v0.38_mass_energy_vibration_report.md
analysis/results_v0.38/mcift_v0.38_mass_energy_vibration_metrics.csv
analysis/results_v0.38/mcift_v0.38_mass_energy_vibration_channels.csv
paper/v0.38_mass_energy_vibration_addendum.md
analysis/results_v0.37/mcift_v0.37_line_chain_spin_drill_report.md
analysis/results_v0.36/mcift_v0.36_cern_higgs_comparison_report.md
models/first_principle_cubic_field_formula_v0.33.md
models/cube_face_higgs_vortex_mass_v0.32.md
```

---

## Important limitation

```text
v0.38 is not yet a Standard Model calculation. The channel fractions are proxy channels from MCIFT variables, not detector-level cross sections or measured branching fractions.
```

---

## Research roadmap

Next required tests:

```text
1. Replace proxy channel families with coupling modifiers kappa_W, kappa_Z, kappa_b, kappa_tau, kappa_mu, kappa_g, and kappa_gamma.
2. Compute partial widths.
3. Sum total width.
4. Compute branching fractions and signal strengths.
5. Compare to collider Higgs targets without per-channel tuning.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
