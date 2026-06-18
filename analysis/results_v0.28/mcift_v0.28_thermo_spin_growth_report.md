# MCIFT v0.28 No-Fit Thermodynamic Spin-Growth Retest Report

**Status:** no-fit thermodynamic spin-growth perturbation scaffold; not established physics and not a CLASS/CAMB replacement.  
**Script:** `analysis/mcift_big_bang_thermo_spin_growth_v0.28.py`  
**Main change from v0.27:** adds a temperature / thermal-speed / capture-window / sound-speed layer using only existing channel loads and analytic normalizations. No parameter sweep or fitting was used.

## No-fit thermodynamic closure

```text
rho_G      ~ A + 0.6 V + 0.45 D + exchange
rho_T      = R
theta_T    = rho_R / (rho_R + rho_G)
T_rel      = theta_T^(1/4)
beta_T     = sqrt(T_rel)
W_capture  = 4(1-exp[-beta_T^2]) exp[-beta_T^2]
c_s^2      = beta_T^2 / 3
chi_thermo = chi_MGT * (1 + beta_T)
N_eff      = 4 + 2 exp[-chi_thermo^2]
```

The factor `4` in the capture window is the analytic normalization of `(1-e^-x)e^-x`, whose maximum is `1/4`; it is not fitted.

## Derived final values

```text
theta_G(5B) = 0.969081
theta_T(5B) = 0.030919
T_rel(5B) = 0.419329
beta_T(5B) = 0.647556
W_capture(5B) = 0.900790
c_s^2(5B) = 0.139776
chi_thermo(5B) = 3.097662
N_eff(5B) = 4.000136
mean N_eff = 4.000110
```

## Result

```text
v0.23 native-growth RMS = 4.148
v0.24 four-sink channel-exchange RMS = 0.469
v0.25 first-principle six-sink RMS = 0.807
v0.26 aperture spin-blur RMS = 0.469
v0.27 mass-gravity-time spin-blur RMS = 0.482
v0.28 no-fit thermodynamic spin-growth RMS = 0.303
shape verdict = PASS-LIKE
```

## Scale diagnostics

```text
raw geometric global peak = 152.29 Mpc
native thermodynamic global peak = 617.87 Mpc
native thermodynamic BAO-window peak = 152.29 Mpc
nearest BAO bin = 152.29 Mpc
reference scoring peak = 350.21 Mpc
sound horizon r_s = 147.11 Mpc
```

## Interpretation

```text
The no-fit thermodynamic layer improves the full-shape score versus v0.27 while preserving the six-to-four spin-blur behavior and the BAO-window peak.
However, it does not solve the global 617.87 Mpc long-mode failure.
This suggests thermodynamics is a useful missing layer, but it still needs to be coupled to a self-consistent background conservation/growth law rather than only layered onto milestone channel snapshots.
```
