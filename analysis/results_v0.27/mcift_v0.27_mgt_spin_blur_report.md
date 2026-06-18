# MCIFT v0.27 Mass-Gravity-Time Spin-Blur Retest Report

**Status:** mass-gravity-time spin-blur perturbation scaffold; not established physics and not a CLASS/CAMB replacement.  
**Script:** `analysis/mcift_big_bang_mass_gravity_time_spin_v0.27.py`  
**Main change from v0.26:** replaces the aperture-only spin-blur proxy with a time-response term derived from MCIFT mass/gravity channel load.

## Mass-gravity-time derivation

```text
Mass_i    = H_i K_i
Gravity_i = G_i H_i K_i
rho_G     ~ A + 0.6 V + 0.45 D + exchange
theta_G   = sum(rho_G) / sum(rho_G + R)
Gamma_rot = A_lock * (A_side/A_tip)
beta_spin = tanh(Gamma_rot)
chi_MGT   = (N_internal / 2pi) * beta_spin * (1 + theta_G)
N_eff     = 4 + 2 exp[-chi_MGT^2]
```

The closure keeps six first-principle internal dark sectors, but lets mass/gravity stretch the response time that determines how strongly knot spin blurs those sectors.

## Derived final values

```text
A_side/A_tip = 5.417113
A_lock(5B) = 0.918752
theta_G(5B) = 0.969081
Gamma_rot(5B) = 4.976985
beta_spin(5B) = 0.999905
chi_MGT(5B) = 1.880156
N_eff(5B) = 4.058318
mean N_eff over milestones = 4.063009
```

## Result

```text
v0.23 native-growth RMS = 4.148
v0.24 four-sink channel-exchange RMS = 0.469
v0.25 first-principle six-sink RMS = 0.807
v0.26 aperture spin-blur RMS = 0.469
v0.27 mass-gravity-time spin-blur RMS = 0.482
shape verdict = WEAK
```

## Scale diagnostics

```text
raw geometric global peak = 152.29 Mpc
native MGT spin-blur global peak = 617.87 Mpc
native MGT spin-blur BAO-window peak = 152.29 Mpc
nearest BAO bin = 152.29 Mpc
reference scoring peak = 350.21 Mpc
sound horizon r_s = 147.11 Mpc
```

## Slope diagnostics

```text
large-scale slope native = 0.431
large-scale slope reference = -0.729
small-scale slope native = -1.038
small-scale slope reference = -1.814
```

## Interpretation

```text
The mass-gravity-time derivation still blurs six internal sectors close to four effective transverse sinks.
It is slightly weaker than v0.26 because beta_spin is bounded by tanh() and the time factor is limited to 1 + theta_G.
This is more physically conservative than the aperture-only closure, but it keeps the same qualitative result: mass/gravity time response helps six internal sinks blur toward about four observed growth channels.
```

## What remains unproven

```text
The response-time law tau_response = tau0(1 + theta_G) is still a bounded scaffold.
A stricter next step is to evolve theta_G self-consistently from background conservation rather than milestone channel snapshots.
The global 617.87 Mpc long mode still remains and requires a conservation/growth correction, not just a sink-count correction.
```
