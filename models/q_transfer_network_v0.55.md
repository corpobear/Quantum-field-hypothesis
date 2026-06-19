# MCIFT v0.55 Q_i Transfer Network

**Status:** calibrated transfer-network scaffold; not established physics.

## Purpose

v0.55 implements the next cosmology step after v0.54. Coarse-grained sectors are allowed to transfer through conservative Q_i terms, then the resulting background is compared to real-world reference benchmarks.

## Continuity form

```text
dot(rho_i) + 3H(rho_i + p_i) = Q_i
sum_i Q_i = 0
```

## Simplified v0.55 transfer map

The full time-dependent Q_i network is approximated by present-day retention factors:

```text
rho_i(today) = R_i rho_i(v0.54)
rho_smooth(today) = sum_i (1 - R_i) rho_i(v0.54)
```

This converts excess local collision-branch energy into a smooth/lapse reservoir.

## Present-day sectors

```text
visible_matter = 0.244232
hidden_sink_matter = 0.070768
rotation_vorticity = 0.001500
radiation = 0.000090
acoustic_shell = 0.003500
smooth_lapse_reservoir = 0.679910
Omega_m_like = 0.315000
```

## Real-world comparison layer

The benchmark is calibrated to a Planck-like reference:

```text
H0 = 67.4 km/s/Mpc
Omega_m = 0.315
```

A photometric cosmic-chronometer check at z=0.75 gives:

```text
H_obs(0.75) = 105.0 ± 10.756 km/s/Mpc
H_v055(0.75) = 104.766 km/s/Mpc
residual = -0.022 sigma
```

## Limitation

This is not a predictive observational cosmology fit. It is a calibrated bridge checkpoint. The next step is to derive the Q_i rates dynamically from the 3D phase field instead of imposing present-day retention factors.
