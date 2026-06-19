# MCIFT v0.50 Kappa / Width Bridge

**Status:** calibrated bridge layer; speculative MCIFT scaffold, not established physics.

## Purpose

v0.50 moves the collider-style comparison from rough channel proxies to a standard Higgs kappa-framework calculation.

The bridge computes:

```text
partial widths:       Gamma_i = kappa_i^2 Gamma_i^SM
branching ratios:     BR_i = Gamma_i / Gamma_total
signal strengths:     mu(prod,decay) = kappa_prod^2 kappa_decay^2 / kappa_H^2
width scale:          kappa_H^2 = Gamma_total / Gamma_total^SM
```

## Important boundary

This is not yet a first-principle derivation of Standard Model couplings from MCIFT geometry.

```text
geometry prior = internal MCIFT shape/channel tendency
kappa fit      = collider-compatible coupling bridge
```

The v0.50 benchmark uses an SM-like calibrated kappa point:

```text
kappa_b = 1
kappa_W = 1
kappa_Z = 1
kappa_g = 1
kappa_tau = 1
kappa_c = 1
kappa_gamma = 1
kappa_mu = 1
BR_BSM = 0
```

This reproduces SM reference partial widths, branching ratios, and representative signal strengths by construction. It is a bridge/checkpoint, not a new prediction.

## Next target

v0.51 should derive kappa values from the 3D vector phase field, hidden/core-load geometry, and face/vortex capture without directly fitting to the SM branching ratios.
