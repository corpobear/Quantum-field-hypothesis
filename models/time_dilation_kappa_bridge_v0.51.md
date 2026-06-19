# MCIFT v0.51 Time-Dilation / Kappa Bridge

**Status:** internal-clock bridge layer; speculative MCIFT scaffold, not established physics.

## Purpose

v0.51 tests whether the compact rotating core should be compared to lab-frame data through a time-flow conversion. In this bridge, the internal MCIFT core clock can run slower than the lab clock because of compact core load and rotation.

This is not a full general-relativistic calculation.

## Clock rule

```text
chi_time = 2 beta_G G_load / R_hidden
tau_G = sqrt(1 - chi_time)
v_core = omega_final R_dense
tau_rot = sqrt(1 - v_core^2)
tau_core_to_lab = tau_G tau_rot
```

## Width rule

If all visible partial widths share the same clock factor:

```text
Gamma_i,lab = tau_core_to_lab Gamma_i,proper
Gamma_total,lab = tau_core_to_lab Gamma_total,proper
```

Branching ratios remain unchanged under a common time factor:

```text
BR_i = Gamma_i,lab / Gamma_total,lab = Gamma_i,proper / Gamma_total,proper
```

## v0.51 result

```text
tau_core_to_lab = 0.868528
uncompensated lab total width = 3.534909 MeV
SM-like reference width = 4.070000 MeV
proper kappa_time needed = sqrt(1/tau_core_to_lab) = 1.073021
```

## Meaning

Time dilation can explain a global width/rate-scale mismatch. It does not fix branching-ratio mismatches unless time flow becomes channel-specific.

## Next target

v0.52 should derive channel-specific formation-time factors from the full 3D phase field, rather than applying a single universal clock factor.
