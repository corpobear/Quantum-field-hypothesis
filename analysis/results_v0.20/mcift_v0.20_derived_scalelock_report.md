# MCIFT v0.20 Derived Scale-Lock Rerun Report

**Status:** equation-derived toy rerun, not a validated cosmology model.  
**Script:** `analysis/mcift_big_bang_derived_scalelock_v0.20.py`  
**Main change from v0.19:** removes the remaining toy scale-lock amplitude and envelope settings.

## Derived equations used

```text
R_A(a) = sqrt[ integral r^2 rho_A(r,a) d^3x / integral rho_A(r,a) d^3x ]
k_cut(a) = 2 pi / R_A(a)
A_lock(a) = integral rho_A d^3x / integral rho_total_positive d^3x
R_env(a) = R_A(a)
p = N_dark_sinks = 4
```

The scale-lock modulation becomes:

```text
M_lock(r,a) = 1 + A_lock(a) cos(2 pi r / r_s) exp[-(r/R_A(a))^2]
```

No fitted `k_cut`, no fixed `SCALE_LOCK_AMPLITUDE`, and no fixed `R_env = 0.45 * BOX_SIZE_MPC` are used in this rerun.

## Final 5B derived values

```text
R_A(5B) = 505.830 Mpc
k_cut(5B) = 0.012422 1/Mpc
A_lock(5B) = 0.918752
R_env(5B) = 505.830 Mpc
sound horizon r_s = 147.111 Mpc
```

## Milestone table

| Milestone | Age [Gyr] | a | z | V/D weighted | Ratio error | Ratio verdict | R_A [Mpc] | k_cut [1/Mpc] | A_lock | R_env [Mpc] |
|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| 1B | 1.0 | 0.150286 | 5.654 | 1.018471 | 4.456 | FAIL | 500.69 | 0.01255 | 0.8916 | 500.69 |
| 2B | 2.0 | 0.238990 | 3.184 | 0.195224 | 0.046 | PASS-LIKE | 503.88 | 0.01247 | 0.9005 | 503.88 |
| 3B | 3.0 | 0.314353 | 2.181 | 0.162572 | 0.129 | WEAK | 504.96 | 0.01244 | 0.9080 | 504.96 |
| 4B | 4.0 | 0.382917 | 1.612 | 0.155448 | 0.167 | WEAK | 505.50 | 0.01243 | 0.9141 | 505.50 |
| 5B | 5.0 | 0.447526 | 1.235 | 0.153635 | 0.177 | WEAK | 505.83 | 0.01242 | 0.9188 | 505.83 |

Best ratio point: **2B**, with `0.195224`, error `0.046`, verdict **PASS-LIKE**.  
Final 5B point: `0.153635`, verdict **WEAK**.

## Structure-scale test

```text
unlocked global peak = 617.87 Mpc
scale-lock global peak = 617.87 Mpc
v0.20 final global peak = 152.29 Mpc
v0.20 BAO-window peak = 152.29 Mpc
global fractional error = 0.035
BAO-window fractional error = 0.035
global verdict = PASS-LIKE
BAO-window verdict = PASS-LIKE
```

## Interpretation

```text
Visible/dark ratio: still partial match, best near 2B.
Scale-lock amplitude: now derived from anchor/channel density fraction.
Scale-lock envelope: now derived from anchor RMS radius.
Anchor cutoff: still derived from anchor RMS radius.
Global structure scale: PASS-LIKE.
CMB acoustic peaks: still undefined; no Boltzmann/radiation transfer solver.
BBN: still undefined; no nuclear reaction network.
```

## Theory implication

This is the strongest toy pass so far because the remaining scale-lock knobs are now derived from MCIFT channel geometry rather than fixed by hand. The next test should move from peak-only scoring to full power-spectrum shape scoring.
