# MCIFT v0.19 Anchor-Derived Cutoff Rerun Report

**Status:** equation-derived toy rerun, not a validated cosmology model.  
**Script:** `analysis/mcift_big_bang_anchor_cutoff_v0.19.py`  
**Main change from v0.18:** removes hand-picked `k_cut = 0.030 1/Mpc` and derives `k_cut` from the MCIFT anchor/coherence channel.

## MCIFT derivation used

The MCIFT anchor/coherence density defines its own RMS radius:

```text
R_A(a) = sqrt[ integral r^2 rho_A(r,a) d^3x / integral rho_A(r,a) d^3x ]
```

The long-mode cutoff is then the fundamental wavenumber of that anchor radius:

```text
k_cut(a) = 2 pi / R_A(a)
```

The damping exponent is derived from the existing four dark-side sinks in the 3D model:

```text
p = N_dark_sinks = 4
```

So the v0.19 gate is:

```text
delta_v0.19(k,a) = delta_v0.17(k,a)
                 * [1 - exp(-(k/k_cut(a))^p)]
                 * (k/k_pivot)^((n_s - 1)/2)
```

No fitted `k_cut` is used in this rerun.

## Derived cutoff at final 5B point

```text
R_A(5B) = 505.830 Mpc
k_cut(5B) = 2 pi / R_A = 0.012422 1/Mpc
```

## Visible/dark and anchor-derived cutoff table

| Milestone | Age [Gyr] | scale factor a | redshift z | MCIFT V/D weighted | Ratio error | Ratio verdict | R_A [Mpc] | k_cut [1/Mpc] |
|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 1B | 1.0 | 0.150286 | 5.654 | 1.018471 | 4.456 | FAIL | 500.69 | 0.01255 |
| 2B | 2.0 | 0.238990 | 3.184 | 0.195224 | 0.046 | PASS-LIKE | 503.88 | 0.01247 |
| 3B | 3.0 | 0.314353 | 2.181 | 0.162572 | 0.129 | WEAK | 504.96 | 0.01244 |
| 4B | 4.0 | 0.382917 | 1.612 | 0.155448 | 0.167 | WEAK | 505.50 | 0.01243 |
| 5B | 5.0 | 0.447526 | 1.235 | 0.153635 | 0.177 | WEAK | 505.83 | 0.01242 |

Best ratio point: **2B**, with `0.195224`, error `0.046`, verdict **PASS-LIKE**.  
Final 5B point: `0.153635`, verdict **WEAK**.

## Structure-scale test

Before anchor-derived damping, the scale-locked reference global peak stayed too large:

```text
reference global peak = 617.87 Mpc
reference BAO-window peak = 152.29 Mpc
```

After v0.19 anchor-derived damping:

```text
v0.19 global peak = 152.29 Mpc
v0.19 BAO-window peak = 152.29 Mpc
sound horizon r_s = 147.11 Mpc
global fractional error = 0.035
BAO-window fractional error = 0.035
global verdict = PASS-LIKE
BAO-window verdict = PASS-LIKE
```

## Interpretation

```text
Visible/dark ratio: still partial match, best near 2B.
Derived k_cut: now comes from MCIFT anchor geometry instead of fitting.
BAO-window scale: remains PASS-LIKE.
Global power spectrum: remains PASS-LIKE after anchor-derived damping.
CMB acoustic peaks: still undefined; no Boltzmann/radiation transfer solver.
BBN: still undefined; no nuclear reaction network.
```

## Theory implication

This is stronger than v0.18 because `k_cut` is no longer selected to make the answer work. It is computed from the RMS size of the anchor/coherence channel. The result shows that the MCIFT anchor-derived cutoff is sufficient to suppress the over-large coherent mode while preserving the BAO-like scale-lock peak.

The next non-fitted test is to derive the scale-lock amplitude and envelope from MCIFT channel dynamics rather than keeping `SCALE_LOCK_AMPLITUDE = 1.0` and `R_env = 0.45 * BOX_SIZE_MPC` as toy settings.
