# MCIFT v0.55 Q_i Transfer Network and Real-World Comparison Report

**Status:** speculative transfer-network scaffold; not established physics.

## Purpose

v0.55 implements the next cosmology step after v0.54: the coarse-grained sectors are allowed to transfer into each other through conservative Q_i terms. The test then compares the raw v0.54 no-transfer scaffold and the v0.55 transfer-calibrated scaffold against real-world reference benchmarks.

## Transfer idea

The continuity equations are written as:

```text
drho_i/dt + 3H(rho_i + p_i) = Q_i
sum_i Q_i = 0
```

In v0.55 the transfer map is simplified into present-day retention factors:

```text
rho_i(today) = R_i rho_i(v0.54)
rho_smooth(today) = sum_i (1 - R_i) rho_i(v0.54)
```

This is not yet a dynamical first-principle Q_i derivation. It is a calibrated transfer-network checkpoint.

## Present fractions

```text
visible_matter = 0.244232
hidden_sink_matter = 0.070768
rotation_vorticity = 0.001500
radiation = 0.000090
acoustic_shell = 0.003500
smooth_lapse_reservoir = 0.679910
Omega_m_like = 0.315000
```

## Reference comparison

Planck-like reference used:

```text
H0 = 67.4 km/s/Mpc
Omega_m = 0.315
```

Photometric cosmic-chronometer comparison:

```text
Observed H(0.75) = 105.0 ± 10.756 km/s/Mpc
v0.55 H(0.75) = 104.766 km/s/Mpc
residual = -0.022 sigma
```

## Raw vs transfer

At z=0.75:

```text
Planck LCDM reference H = 103.831
v0.54 raw no-transfer H = 167.670
v0.55 transfer H = 104.766
```

The raw v0.54 branch fractions over-expand because too much local collision energy is treated as present-day gravitating density. v0.55 fixes this by transferring most excess local branch energy into a smooth/lapse reservoir.

## Growth kernel

```text
mu_eff(k=0.01) = 1.214990
mu_eff(k=0.1) = 1.214007
mu_eff(k=1) = 1.136847
mu_eff(k=10) = 0.800982
```

Large scales remain enhanced by hidden load. Smaller scales are suppressed by sound spread.

## Verdict

```text
verdict = PASS_Q_TRANSFER_BACKGROUND_BRIDGE
criteria_pass_count = 12/12
```

## Limitation

v0.55 is not a successful observational cosmology fit. It is a bridge checkpoint. The present-day sectors are calibrated to Planck-like H0/Omega_m. DESI DR2 hints of evolving dark energy are not fitted in this version.
