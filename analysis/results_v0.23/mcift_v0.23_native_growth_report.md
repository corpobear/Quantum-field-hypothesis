# MCIFT v0.23 Native Growth Attempt Report

**Status:** first MCIFT-native growth attempt; not established physics; not a CLASS/CAMB replacement.  
**Script:** `analysis/mcift_big_bang_native_growth_v0.23.py`  
**Main change from v0.22:** removes the imported BBKS/Sugiyama transfer layer from the model evolution and tries to grow `T_growth(k)` from MCIFT channel mechanics.

## Model equation used

The native growth transfer is defined by evolving:

```text
T_growth_MCIFT(k,a_final) = exp[ integral f_MCIFT(k,a) d ln a ]
```

with the first closure:

```text
f_MCIFT(k,a) = Omega_m(a)^0.55
              * T_anchor(k,a)
              * T_lock(k,a)
              / [ radiation_drag(k,a) * dark_sink_resistance(k,a) ]
```

where:

```text
T_anchor(k,a) = 1 - exp[-(k/k_cut(a))^p]
k_cut(a) = 2 pi / R_A(a)
T_lock(k,a) = 1 + A_lock(a) exp[-0.5 ((k-k_s)/sigma_lock)^2]
k_s = 2 pi / r_s
sigma_lock = k_s * r_s / R_A(a)
p = 4 dark-side sinks
```

This model uses expansion and horizon timing from the background, but it does **not** import the BBKS/Sugiyama transfer curve into the native growth evolution. A Lambda-CDM-like curve is used only as the external shape-scoring reference.

## Derived MCIFT values retained at 5B

```text
R_A(5B) = 505.830 Mpc
k_cut(5B) = 0.012422 1/Mpc
A_lock(5B) = 0.918752
sound horizon r_s = 147.111 Mpc
```

## Result

```text
native shape RMS log residual = 4.148
native shape verdict = FAIL
raw geometric global peak = 152.29 Mpc
native growth global peak = 152.29 Mpc
native growth BAO-window peak = 152.29 Mpc
reference scoring peak = 350.21 Mpc
```

## Slope diagnostics

```text
large-scale slope native = 9.704
large-scale slope reference = -0.729
small-scale slope native = -3.791
small-scale slope reference = -1.814
```

## Interpretation

```text
v0.23 is the first no-import native-growth attempt.
It does not yet reproduce the full broadband transfer shape.
This means the missing ingredient is a stronger MCIFT perturbation system, not only a scalar growth-rate closure.
```

## Next equation target

The next version should evolve coupled perturbations directly:

```text
delta_A(k,a), delta_V(k,a), delta_D(k,a), delta_R(k,a)
```

with explicit channel exchange terms:

```text
Q_A_to_V(k,a), Q_A_to_D(k,a), Q_V_to_D(k,a), Q_V_to_R(k,a)
```

The desired non-imported definition remains:

```text
T_growth_MCIFT(k,a) = delta_m(k,a) / delta_m(k,a_initial)
```
