# MCIFT v0.51 Time-Dilation / Kappa-Width Bridge Report

**Status:** internal-clock bridge calculation; speculative MCIFT scaffold, not established physics.

## Purpose

v0.51 tests the proposed missing bridge: the compact rotating core may run on a slower internal clock than the lab-frame clock used for collider-style data. This can produce a mismatch between an internal MCIFT proper-time run and measured lab-time rates.

## Time-dilation rule

```text
chi_time = 2 beta_G G_load / R_hidden
tau_G = sqrt(1 - chi_time)
v_core = omega_final R_dense
tau_rot = sqrt(1 - v_core^2)
tau_core_to_lab = tau_G tau_rot
```

## Result

```text
verdict = PASS_TIME_DILATION_BRIDGE_WITH_COMPENSATION
G_load = 0.874502
R_hidden = 10.582795
R_dense = 6.198812
omega_final = 0.072027
v_core = 0.446482
chi_time = 0.057844
tau_G = 0.970647
tau_rot = 0.894793
tau_core_to_lab = 0.868528
time_slowdown_pct = 13.147198
```

## Width effect

If the internal run is compared directly to lab time without correction:

```text
Gamma_SM_total = 4.070000 MeV
Gamma_lab_uncompensated = 3.534909 MeV
delta = -13.147198 %
```

Because the time factor is common to all visible partial widths, the branching ratios do not change. The total width changes.

To compare a proper-time MCIFT run to lab-frame reference widths, a universal proper-width compensation is:

```text
kappa_time = sqrt(1 / tau_core_to_lab) = 1.073021
proper_width_scale = 1 / tau_core_to_lab = 1.151373
```

Then the lab-frame total width returns to the SM-like reference:

```text
Gamma_lab_compensated = 4.070000 MeV
max_abs_BR_delta_pct = 0.000000
max_abs_signal_strength_delta_pct = 0.000000
```

## Interpretation

Time dilation can explain a global rate/width mismatch but cannot by itself fix channel ratios. If it is a common clock factor, it rescales all partial widths together, leaving branching ratios unchanged. Channel-specific corrections would require channel-specific formation times or geometry-dependent clock factors, which v0.51 does not claim.

## Limitation

This is an internal MCIFT clock bridge, not a full GR calculation and not empirical collider confirmation.
