# MCIFT v0.17 Expansion-Coupled Scale-Lock Rerun Report

**Status:** equation-input toy rerun, not a validated cosmology model.  
**Script:** `analysis/mcift_big_bang_scale_lock_v0.17.py`  
**Main change from v0.16:** adds a Planck-like FRW expansion background, a radiation placeholder channel, sound-horizon calculation, and an explicit MCIFT scale-lock modulation tied to the calculated sound horizon.

## Equations implemented

Expansion background:

```text
H(a)^2 = H0^2 [Omega_r a^-4 + Omega_m a^-3 + Omega_Lambda]
a = 1 / (1 + z)
```

Channel interpretation:

```text
rho_A = anchor/coherence positive density
rho_V = visible positive density
rho_D = dark positive density
rho_R = radiation placeholder density
rho_total = rho_A + 0.6 rho_V + 0.45 rho_D + rho_R + exchange
```

Sound horizon:

```text
r_s = integral c_s(a) / [a^2 H(a)] da
c_s = c / sqrt(3(1 + R_b))
R_b = 3 rho_b / (4 rho_gamma)
```

Scale-lock modulation:

```text
M_lock(r) = 1 + A cos(2 pi r / r_s) exp[-(r / R_env)^2]
rho_locked = rho_total * M_lock(r)
```

## External anchors used

```text
Planck baryon/CDM ratio = Omega_b h^2 / Omega_c h^2 = 0.186667
Calculated sound horizon r_s = 147.111 Mpc
DESI reference r_d context = 147.09 Mpc
```

## Visible/dark ratio rerun

| Milestone | Age [Gyr] | scale factor a | redshift z | MCIFT V/D weighted | Fractional error | Verdict |
|---:|---:|---:|---:|---:|---:|---|
| 1B | 1.0 | 0.150286 | 5.654 | 1.018471 | 4.456 | FAIL |
| 2B | 2.0 | 0.238990 | 3.184 | 0.195224 | 0.046 | PASS-LIKE |
| 3B | 3.0 | 0.314353 | 2.181 | 0.162572 | 0.129 | WEAK |
| 4B | 4.0 | 0.382917 | 1.612 | 0.155448 | 0.167 | WEAK |
| 5B | 5.0 | 0.447526 | 1.235 | 0.153635 | 0.177 | WEAK |

Best ratio point: **2B**, with `0.195224`, error `0.046`, verdict **PASS-LIKE**.

Final 5B point: `0.153635`, verdict **WEAK**.

## Structure-scale rerun

Unlocked global peak wavelength:

```text
lambda_global_unlocked = 617.87 Mpc
```

Locked global peak wavelength:

```text
lambda_global_locked = 617.87 Mpc
verdict vs r_s = FAIL
```

The long coherent pocket still dominates the **global** power spectrum. That means v0.17 does **not** fully solve the long-mode/coarse-structure problem.

However, in the BAO analysis window `80-250 Mpc`, the scale-lock sector produces:

```text
lambda_BAO_window_peak = 152.29 Mpc
sound horizon r_s      = 147.11 Mpc
fractional error       = 0.035
verdict                = PASS-LIKE
```

## Interpretation

```text
Visible/dark ratio: still partial match, best near 2B.
BAO-window scale: improved to PASS-LIKE after adding scale-lock.
Global power spectrum: still fails because the long coherent mode remains too strong.
CMB acoustic peaks: still undefined; no Boltzmann/radiation transfer solver.
BBN: still undefined; no nuclear reaction network.
```

## What this says about the theory

The new scale-lock equation can place a BAO-like ripple in the correct window, but this is an input hypothesis, not yet a derived prediction. The remaining missing theory is a **long-mode damping / primordial-spectrum sector** that prevents the huge coherent pocket from dominating the total power spectrum.

Recommended v0.18 target:

```text
Add primordial spectrum + long-mode damping:
P_initial(k) proportional to k^n_s with suppress_long_modes(k)
then rerun visible/dark + BAO + global P(k) together.
```
