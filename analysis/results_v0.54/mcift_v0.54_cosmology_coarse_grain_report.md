# MCIFT v0.54 Cosmology Coarse-Graining Test Report

**Status:** speculative cosmology-scale scaffold; not established physics.

## Purpose

v0.54 promotes the collision mechanics into a coarse-grained cosmology layer. The goal is not to fit observations yet. The goal is to test whether the local geometry can be converted into stable large-scale variables:

```text
visible density
hidden/sink density
rotation/vorticity density
radiation density
acoustic/sound-shell density
clock/lapse field
sound horizon proxy
growth kernel proxy
```

## Coarse-grained source

The local branch fractions are promoted to effective densities:

```text
rho_grav = rho_v + C_h rho_h + C_rot rho_rot + C_s rho_sound + rho_rad
```

v0.54 uses:

```text
C_h = 1.704656
C_rot = 0.710507
C_s = 1.333447
```

Normalized effective density fractions:

```text
visible_matter = 0.616356
hidden_sink_grav = 0.178592
rotation_load = 0.095371
radiation = 0.051573
acoustic_shell = 0.058107
```

## Expansion/lapse equations

```text
H_core(a)^2 = sum_i Omega_i a^(-n_i)
N(a) = tau_rot / sqrt(1 + chi0 H_core(a)^2)
H_lab(a) = H_core(a) / N(a)
```

At a=1:

```text
N(a=1) = 0.869985
H_lab/H_core = 1.149445
```

## Acoustic horizon proxy

From v0.53:

```text
c_sound = 0.582034
w_sound = c_sound^2 = 0.338764
radial_spread_factor = 1.094666
```

The coarse-grained acoustic horizon proxy is:

```text
r_s(a) = integral c_s / (a^2 H_lab) da
```

v0.54 result:

```text
r_s(a=1) = 0.394142
k_sound = 1/r_s = 2.537156
```

## Growth kernel proxy

A first structure-growth kernel is:

```text
mu_eff(k) =
1
+ hidden_gravity_enhancement(k)
+ rotation_support(k)
- sound_spread_suppression(k)
```

Selected values:

```text
mu_eff(k=0.01) = 1.147401
mu_eff(k=0.1)  = 1.147026
mu_eff(k=1)    = 1.118137
mu_eff(k=10)   = 0.983284
```

The kernel enhances large-scale growth from hidden load and suppresses small-scale growth from sound spread.

## Strict result

```text
verdict = PASS_COSMOLOGY_COARSE_GRAIN_SCAFFOLD
criteria_pass_count = 12/12
```

## Interpretation

The collision mechanics can be coherently lifted to a cosmology-scale scaffold:

```text
hidden branch -> gravitational density
sound spread -> pressure/acoustic horizon
time dilation -> lapse field
rotation -> vorticity/support term
channel exchange -> future Q_i transfer terms
```

## Limitation

This is not an observational cosmology fit. It is not a replacement for standard cosmology. It is a coarse-graining test that defines the next mathematical layer.
