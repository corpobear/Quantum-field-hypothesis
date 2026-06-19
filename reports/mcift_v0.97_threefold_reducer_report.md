# MCIFT v0.97 Threefold Reducer Report

**Status:** reducer for the v0.96 threefold bubble-knot formula. This is not a cosmology or collider score.

## 1. Input formula

v0.97 uses the v0.96 rule:

```text
r_0(n,t) = c Delta t rho_0(r) A_3(n)
```

with:

```text
A_3(theta,phi) = 1 + epsilon_3 sin(theta)^2 cos(3 phi + psi_3)
```

## 2. Settings

```text
M0 = 2
alpha_M = 0.05
r_core = 1
epsilon_3 = 0.125
psi_3 = 0
shells = 1..10
```

`epsilon_3` is an assumed symbolic strength for the first reducer. It is not fitted to data.

## 3. What changed versus v0.95

v0.95 had an isotropic central seed.

v0.97 keeps the same average central load, but distributes it through a threefold surface pattern.

This creates a nonzero shear proxy while preserving the average load and H proxy.

## 4. Main outputs

```text
mean_A3 = 1.000000000000
A3_min = 0.875042834378
A3_max = 1.124957165622
A3_std = 0.064549317306
mean_D3 = 0.009817928223
mean_shear_proxy = 0.063915576742
mean_threefold_amp = 0.247460690278
mean_abs_lc_resid = 0.054439708131
mean_null_resid = 0.015243226439
H_proxy_relative = 0.977215138494
global_anisotropy = 0.351925814364
```

## 5. Loop balance

Using beta_3 = 1:

```text
loop_sum = 0.341737250747
```

The central hidden phase is tied to R4 = 2. Therefore the reducer exports:

```text
beta4_needed_for_balance = 0.170868625373
```

This means the three visible loops can be balanced against the hidden failed-mode-4 center by a definite central coupling.

## 6. Shared outputs for the next comparisons

The same reducer now exports quantities that can feed both future arms:

```text
H_proxy_relative
load_proxy / mean_D3
shear_proxy
threefold_amplitude
mean light-cone residual
mean null residual
loop balance factor
```

Cosmology will use the expansion, load, shear, and residual proxies.

Collider comparison will use the same load, surface activation, shear, and loop-balance proxies.

## 7. What is not done

No cosmology data are scored.

No collider data are scored.

No GR derivation is claimed.

## 8. Next

v0.98 should build the cosmology mapping layer from the v0.97 shared reduced outputs and compare only after every value is labeled derived, assumed, fitted, placeholder, or not tested.
