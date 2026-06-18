# MCIFT v0.22 Growth-Transfer Rerun Report

**Status:** stricter toy/scaffold comparison, not a survey likelihood and not a CLASS/CAMB replacement.  
**Script:** `analysis/mcift_big_bang_growth_transfer_v0.22.py`  
**Main change from v0.21:** adds the existing matter-radiation growth/transfer ingredient for broadband P(k) shape.

## Ingredient added

v0.21 showed that MCIFT's geometric peak can pass while the full P(k) shape fails. v0.22 therefore uses the existing cosmology form:

```text
P(k,a) = A_s (k/k_pivot)^n_s T_growth^2(k) T_MCIFT^2(k,a)
```

with an analytic BBKS/Sugiyama matter-radiation transfer as `T_growth(k)`. MCIFT supplies the derived acoustic/anchor modulation:

```text
T_MCIFT(k,a) = 1 + epsilon_lock sin(k r_s) exp[-(k/0.18)^1.4]
epsilon_lock = 0.12 * A_lock(a)
```

This is a compatibility scaffold: it imports the established broadband transfer shape and checks whether the MCIFT-derived lock can sit on top of it.

## Derived values retained

```text
R_A(5B) = 505.830 Mpc
k_cut(5B) = 0.012422 1/Mpc
A_lock(5B) = 0.918752
epsilon_lock = 0.110250
sound horizon r_s = 147.111 Mpc
```

## Shape result

```text
shape RMS log residual = 0.004
mean absolute log residual = 0.004
max absolute log residual = 0.009
shape verdict = PASS-LIKE
```

## Peak diagnostics

```text
raw MCIFT geometric global peak = 152.29 Mpc
raw MCIFT BAO-window peak = 152.29 Mpc
growth-transfer broadband peak = 350.21 Mpc
reference broadband peak = 350.21 Mpc
nearest BAO-bin wavelength = 152.29 Mpc
```

## Interpretation

```text
Raw geometric scale test: still PASS-LIKE near the BAO/sound-horizon scale.
Full-shape test after adding existing growth transfer: PASS-LIKE.
```

The important distinction: v0.22 fixes the broadband shape by importing an existing ΛCDM-like transfer layer. That means MCIFT is compatible with the shape when placed on top of standard growth physics, but this does not yet prove MCIFT independently derives the full transfer function. The next hard test is to derive `T_growth(k)` from MCIFT channel dynamics rather than importing BBKS/Sugiyama.
