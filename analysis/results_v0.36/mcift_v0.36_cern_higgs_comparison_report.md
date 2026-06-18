# MCIFT v0.36 CERN/LHC Higgs-Sector Comparison Report

**Status:** first collider-facing comparison scaffold; speculative and not established physics.  
**Scope:** compare the v0.33-v0.35 cubic field/Higgs-vortex model against core CERN/LHC Higgs-sector results.

## Purpose

Cosmology-style toy testing has gone far enough for now. v0.36 asks whether the updated cubic MCIFT model can face collider constraints from CERN/LHC Higgs measurements.

The comparison is deliberately strict:

```text
structural compatibility is not counted as quantitative prediction
calibrated mass is not counted as independent mass prediction
unimplemented production/decay rates are marked NOT_IMPLEMENTED
```

## CERN/LHC target set used

```text
Higgs mass: 125.04 ± 0.12 GeV
Higgs width: 3.0 +2.0/-1.5 MeV, SM about 4.1 MeV
spin-parity: scalar 0+ favored/compatible
global signal strength: Run1 ATLAS+CMS mu = 1.09 ± 0.11
ATLAS Run2 global signal strength: mu = 1.11 +0.09/-0.08
observed/evidenced channels: ZZ, WW, gamma gamma, tau tau, bb, mu mu, gluon/photon/W/Z/top/bottom/tau interactions
```

## MCIFT v0.36 structural mapping

From v0.33/v0.34:

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

Collider-facing Higgs-vortex subset:

```text
chi_i,mu     = A_ij,mu P_phase P_timing P_match
Omega_i,mu   = H_i,mu sigma(chi_i,mu - chi_c)
m_i,mu       = m_scale Omega_i,mu a_i,mu
m_i          = sum_mu m_i,mu
```

## Mass-scale calibration check

For an ideal symmetric six-face Higgs-vortex excitation:

```text
a_i,mu = 1
H_i,mu = 1
chi_i,mu = 1
chi_c = 1/sqrt(2)
sigma = 0.5 [1 + tanh(6(chi-chi_c))]
ideal six-face vortex mass proxy = 5.826622
```

To match the CERN Higgs mass:

```text
m_scale = 125.04 GeV / 5.826622
m_scale = 21.460119 GeV
```

This is a calibration, not an independent prediction.

## Scorecard

```text
STRUCTURAL_PASS:
- scalar / 0+ style central balanced excitation
- neutral/colorless structural representation

CALIBRATION_REQUIRED:
- Higgs mass scale

WEAK_QUALITATIVE:
- coupling hierarchy / mass-response idea

NOT_IMPLEMENTED:
- total width in MeV
- production rates: ggF, VBF, VH, ttH
- branching fractions: ZZ, WW, gamma gamma, tau tau, bb, mu mu
- signal-strength likelihood
- detector-level event distributions

CONSTRAINED:
- MCIFT collider limit must reduce to SM-like Higgs behavior within current LHC uncertainties
```

## Overall verdict

```text
STRUCTURAL_ONLY_NOT_A_CERN_PASS
```

v0.36 does not fail because of a numerical contradiction; it fails to be complete enough for a full CERN/LHC quantitative claim.

## What would be required for a real CERN-facing test

```text
v0.37 target:
Build a collider-Higgs effective model from MCIFT variables:
1. derive coupling modifiers kappa_W, kappa_Z, kappa_t, kappa_b, kappa_tau, kappa_mu
2. derive loop modifiers kappa_g and kappa_gamma
3. compute partial widths and total width
4. compute production x branching signal strengths
5. compare to ATLAS/CMS likelihood-style targets
```

## Safe wording

```text
MCIFT v0.36 is structurally compatible with a scalar Higgs-like mass-coupling excitation, but it is not yet a quantitative CERN/LHC Higgs model.
```

Unsafe wording:

```text
MCIFT matches CERN.
MCIFT predicts the Higgs mass.
MCIFT replaces the Standard Model Higgs mechanism.
```
