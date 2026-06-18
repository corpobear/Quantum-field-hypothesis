# MCIFT v0.18 Long-Mode Damping / Primordial-Spectrum Rerun Report

**Status:** equation-input toy rerun, not a validated cosmology model.  
**Script:** `analysis/mcift_big_bang_longmode_v0.18.py`  
**Main change from v0.17:** adds a Fourier-space primordial gate that damps over-large coherent modes and applies a Planck-like scalar tilt.

## New equation implemented

```text
delta_v0.18(k) = delta_v0.17(k)
              * [1 - exp(-(k/k_cut)^p)]
              * (k/k_pivot)^((n_s - 1)/2)
```

Parameter choices in this toy rerun:

```text
n_s = 0.965
k_pivot = 0.050 1/Mpc
k_cut = 0.030 1/Mpc
p = 4.0
```

## External anchors used

```text
Planck baryon/CDM ratio = Omega_b h^2 / Omega_c h^2 = 0.186667
Calculated sound horizon r_s = 147.111 Mpc
DESI reference r_d context = 147.09 Mpc
```

## Visible/dark ratio check

This equation acts on the structure spectrum, not the channel-density totals. The visible/dark ratio therefore remains the same benchmark as v0.17.

| Milestone | Age [Gyr] | scale factor a | redshift z | MCIFT V/D weighted | Fractional error | Verdict |
|---:|---:|---:|---:|---:|---:|---|
| 1B | 1.0 | 0.150286 | 5.654 | 1.018471 | 4.456 | FAIL |
| 2B | 2.0 | 0.238990 | 3.184 | 0.195224 | 0.046 | PASS-LIKE |
| 3B | 3.0 | 0.314353 | 2.181 | 0.162572 | 0.129 | WEAK |
| 4B | 4.0 | 0.382917 | 1.612 | 0.155448 | 0.167 | WEAK |
| 5B | 5.0 | 0.447526 | 1.235 | 0.153635 | 0.177 | WEAK |

Best ratio point: **2B**, with `0.195224`, error `0.046`, verdict **PASS-LIKE**.  
Final 5B point: `0.153635`, verdict **WEAK**.

## Structure-scale test

Before v0.18 damping, the v0.17 scale-locked global peak stayed too large:

```text
v0.17 global peak = 617.87 Mpc
v0.17 BAO-window peak = 152.29 Mpc
```

After v0.18 long-mode damping:

```text
v0.18 global peak = 152.29 Mpc
v0.18 BAO-window peak = 152.29 Mpc
sound horizon r_s = 147.11 Mpc
global fractional error = 0.035
BAO-window fractional error = 0.035
global verdict = PASS-LIKE
BAO-window verdict = PASS-LIKE
```

## Interpretation

```text
Visible/dark ratio: still partial match, best near 2B.
BAO-window scale: remains PASS-LIKE.
Global power spectrum: improved from FAIL to PASS-LIKE.
CMB acoustic peaks: still undefined; no Boltzmann/radiation transfer solver.
BBN: still undefined; no nuclear reaction network.
```

## Theory implication

The long-mode damping equation fixes the specific v0.17 problem: the 617.87 Mpc coherent mode no longer dominates the power-spectrum diagnostic. This is still not a derived prediction, because `k_cut` and `p` are chosen toy parameters. The next improvement is to derive `k_cut` from MCIFT expansion/anchor dynamics instead of selecting it by hand.

Recommended v0.19 target:

```text
Derive k_cut from anchor horizon crossing:
k_cut(a) = beta * aH(a)/c or beta/r_anchor(a)
then fit beta against visible/dark + BAO + global P(k) together.
```
