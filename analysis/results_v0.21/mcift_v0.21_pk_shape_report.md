# MCIFT v0.21 Full P(k) Shape Test Report

**Status:** stricter toy-shape comparison, not a survey likelihood and not a CLASS/CAMB replacement.  
**Script:** `analysis/mcift_big_bang_pk_shape_v0.21.py`  
**Main change from v0.20:** tests the whole matter-power-spectrum shape instead of only peak location.

## Ingredient added

```text
P_ref(k) = (k/k_pivot)^n_s T_BBKS^2(k) [1 + 0.12 sin(k r_s) exp(-(k/0.18)^1.4)]

shape score = RMS[ log P_MCIFT(k) - log A P_ref(k) ]
score window = 0.015 <= k <= 0.220 1/Mpc
```

A single best-fit amplitude `A` is allowed so the test compares **shape**, not absolute normalization.

## Result

```text
shape RMS log residual = 3.747
mean absolute log residual = 2.997
max absolute log residual = 8.111
shape verdict = FAIL
```

## Peak diagnostics preserved

```text
MCIFT global peak = 152.29 Mpc
MCIFT BAO-window peak = 152.29 Mpc
sound horizon r_s = 147.11 Mpc
```

## Derived MCIFT values retained

```text
R_A(5B) = 505.830 Mpc
k_cut(5B) = 0.012422 1/Mpc
A_lock(5B) = 0.918752
```

## Slope diagnostics

```text
large-scale slope MCIFT = 3.391
large-scale slope reference = -0.729
small-scale slope MCIFT = -7.244
small-scale slope reference = -1.814
```

## Interpretation

```text
Peak-scale test: still PASS-LIKE.
Full-shape test: FAIL.
```

If this is WEAK or FAIL, the missing ingredient is no longer the geometric scale-lock; it is a true perturbation-growth/transfer equation that controls the broadband shape of P(k), not just the dominant scale.
