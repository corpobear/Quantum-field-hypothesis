# MCIFT v0.50 Kappa / Partial-Width Bridge Report

**Status:** calibrated κ-framework bridge; speculative MCIFT scaffold, not established physics.

## Purpose

v0.50 moves the collider-style comparison from rough visible-channel proxies to a standard Higgs κ-framework calculation. It computes:

```text
partial widths Γ_i = κ_i^2 Γ_i^SM
branching ratios BR_i = Γ_i / Γ_total
representative signal strengths μ(prod,decay) = κ_prod^2 κ_decay^2 / κ_H^2
```

This is a bridge/calibration layer, not yet a first-principle MCIFT derivation of Standard Model couplings. The fit uses the SM-like κ benchmark as the reference point because current Higgs measurements are consistent with the Standard Model within uncertainties.

## Reference data

```text
m_H ≈ 125.09 GeV
Γ_H^SM = 4.070000 MeV
```

Compact normalized branching fraction table for mH≈125 GeV:

```text
bb=0.582384, WW=0.213694, gg=0.081798, tau=0.062698, cc=0.028999, ZZ=0.026399, gamma=0.002270, Zgamma=0.001540, mumu=0.000217
```

## κ fit used

```text
κ_b = 1.000000
κ_W = 1.000000
κ_Z = 1.000000
κ_g = 1.000000
κ_tau = 1.000000
κ_c = 1.000000
κ_gamma = 1.000000
κ_mu = 1.000000
BR_BSM = 0.000000
```

## Fit quality

```text
verdict = PASS_KAPPA_BRIDGE_CALIBRATED
Γ_total_fit = 4.070000 MeV
κ_H^2 = 1.000000
max_abs_BR_delta_pct = 0.000000
max_abs_signal_strength_delta_pct = 0.000000
```

Because this benchmark uses κ≈1 and BR_BSM=0, it reproduces the SM reference table. That is expected and should not be mistaken for a new prediction.

## Geometry-prior warning

The raw v0.49 visible proxy fractions are close in some channels but not all. When mapped naively onto κ values:

```text
κ_g_prior ≈ 1.132196
κ_gamma_prior ≈ 0.737311
κ_mu_prior ≈ 2.974587
```

These priors do not yet form a valid LHC κ fit. Therefore v0.50 separates:

```text
geometry prior = MCIFT internal shape/channel tendency
κ fit = external collider-compatible coupling bridge
```

## Next target

v0.51 must derive κ values from the 3D vector phase field and hidden/core-load geometry without fitting directly to the SM branching ratios.
