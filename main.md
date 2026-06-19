# MCIFT Main Synopsis: v0.99 Shared Threefold Reducer Mapping

**Status:** speculative research scaffold; not established physics.  
**Current version:** v0.99 CERN mapping from the v0.97 shared threefold reducer.
**Author:** Adrian Newton / corpobear.

---

## Abstract

This synopsis records the current MCIFT development path through v0.99. The active late-version structure is a bubble light-cone and threefold reducer scaffold. It exports a small set of shared reduced quantities that are mapped first to cosmology proxies in v0.98 and then to selected CERN/collider proxies in v0.99.

The result is not a proof of new physics. It is an internal consistency and mapping milestone: selected proxy checks land close to chosen anchors, while full cosmology and collider validation remain unimplemented.

---

## Late-version chain

```text
v0.92  bubble light-cone projection
v0.93  simplified first-principle bubble formula
v0.94  central failed-mode-4 seed
v0.95  central-seed reducer
v0.96  threefold bubble-knot first-principle update
v0.97  shared threefold reducer
v0.98  cosmology mapping from shared reducer
v0.99  CERN/collider mapping from shared reducer
```

---

## Core object

The late scaffold begins from an event-bubble primitive:

```text
B_i = {C_i, S_i, r_i, W_i, Phi_i}
```

with:

```text
C_i       center event
S_i       2D causal bubble surface
r_i       center-to-surface radial distance
W_i       diagonal causal weights
Phi_i     phase/timing/knot state
```

The threefold update extends the primitive to:

```text
B_i^3 = {C_i, S_i, r_i, W_i, Phi_i, M_0, R_4, L_3}
```

where:

```text
M_0       central seed load from failed mode 4
R_4       failed mode-4 reservoir
L_3       three stable surface loops
```

---

## Threefold reducer

The compact surface activation used by v0.97 is:

```text
A_3(theta, phi) = 1 + epsilon_3 sin(theta)^2 cos(3 phi + psi_3)
```

with surface mean:

```text
<A_3>_S2 = 1
```

The central regulated radial compression is:

```text
rho_0(r) = 1 - alpha_M M_0 / (r^2 + r_core^2)
```

The threefold radius scale is:

```text
r_0(n,t) = c Delta t rho_0(r) A_3(n)
```

The deformation proxy is:

```text
D_3(n,r) = 1 - rho_0(r) A_3(n)
```

---

## Shared v0.97 outputs

For:

```text
M0 = 2
alpha_M = 0.05
r_core = 1
epsilon_3 = 0.125
psi_3 = 0
shells = 1..10
```

the reducer exports:

```text
mean_A3 = 1.000000000000
load_proxy / mean_D3 = 0.009817928223
mean_shear_proxy = 0.063915576742
mean_threefold_amp = 0.247460690278
mean_abs_lc_resid = 0.054439708131
mean_null_resid = 0.015243226439
H_proxy_relative = 0.977215138494
beta4_needed_for_balance = 0.170868625373
```

---

## v0.98 cosmology mapping

v0.98 uses the shared reducer to map:

```text
H0_early_model = fitted Planck-like anchor
H0_local_model = H0_early_model * (1 + mean_shear_proxy)
S8_late_model = S8_planck * (1 - mean_shear_proxy)
```

Current values:

```text
H0_local_model = 71.665353249341
H0_local_residual_sigma = -1.321775721787
S8_late_model = 0.778822240151
S8_late_residual_sigma = 0.166014126510
```

Strict interpretation:

```text
H0 early value is fitted, not an independent prediction.
S8 late value is pass-like against the selected DES Y3 anchor.
BAO, CMB acoustic scale, and BBN are not numerically scored in v0.98.
```

---

## v0.99 CERN mapping

v0.99 uses:

```text
Gamma_model = Gamma_SM * (1 + load_proxy)
mu_inclusive_model = mean_A3
D_proxy = -(1/3 + beta4_needed_for_balance)
```

Current values:

```text
Gamma_model = 4.109958967868 MeV
mu_inclusive_model = 1.000000000000
CMS HZZ residual = 0.526 sigma
D_proxy = -0.504201958707
ATLAS D residual = 1.717 sigma
CMS D residual = -0.880 sigma
```

Strict interpretation:

```text
CMS HZZ signal-strength proxy is pass-like at this coarse level.
CMS top-entanglement D proxy is pass-like.
ATLAS top-entanglement D proxy is close but not pass-claimed.
Higgs width is reference-close against the SM value, not a direct experimental-width score.
Higgs branching ratios, channel signal strengths, and detector event shapes are not scored.
```

---

## Safe interpretation

Safe:

```text
MCIFT v0.99 is a speculative mapping milestone. It shows that the shared v0.97 threefold reducer can feed both a cosmology proxy layer and selected collider proxy checks while preserving explicit labels for fitted, derived, assumed, and untested quantities.
```

Unsafe:

```text
MCIFT proves a new interaction.
MCIFT replaces the Standard Model, QFT, GR, or Lambda-CDM.
The v0.99 mapping is a full CERN validation.
The v0.98 mapping is a full cosmology validation.
```

---

## Next target

```text
v1.00 should build a joint v0.98/v0.99 scorecard with every value labeled as derived, fitted anchor, assumed, placeholder, not tested, pass-like, close-not-pass, or fail.
```
