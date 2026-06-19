# MCIFT v0.95 Central Seed Reducer Report

**Status:** dimensionless reducer for the v0.94 central failed-mode-4 seed. This is not a comparison with observational cosmology.

## 1. Input seed

The seed uses the failed fourth mode:

```text
C4 = 16
Q4 = 14
S4 = -2
R4 = 2
mu4 = 1
M0 = 2
```

## 2. Regulated center

The center is not treated as an infinite singularity.

Use:

```text
rho(r) = 1 - alpha_M M0 / (r^2 + r_core^2)
```

with:

```text
alpha_M = 0.05
r_core = 1
rho_floor = 0.1
```

## 3. Shell reducer

Ten dimensionless shells were evaluated:

```text
r = 1..10
```

For each shell:

```text
deformation = 1 - rho
lightcone residual norm = deformation
null residual norm = 1 - rho^2
```

## 4. Reduced proxies

The reducer exports:

```text
mean_rho = 0.990182071777
mean_deformation = 0.009817928223
max_deformation = 0.05
load_proxy = 0.009817928223
anisotropy_proxy = 0.051589369463
mean_null_residual = 0.019329303052
H_proxy_relative = 0.977215138494
curvature_proxy_isotropic = 0
```

## 5. Interpretation

The central seed produces a bounded inward deformation that fades outward.

Because the seed is isotropic, the surface-loop curvature proxy is zero in this first reducer.

The nonzero load proxy is the first reduced quantity available for a later cosmology retest.

## 6. Checks

```text
seed M0 = 2: pass
regulated center: pass
rho bounded: pass
deformation positive: pass
rho increases outward: pass
isotropic curvature zero: pass
cosmology scored: no
```

## 7. What this does not do

This does not score Planck, DESI, SH0ES, BAO, S8, BBN, or CMB data.

This does not validate cosmology.

It creates a reduced central-seed observable set that can be used in the next cosmology retest.

## 8. Next

v0.96 should convert these dimensionless proxies into a calibrated cosmology comparison layer with explicit labels: derived, fitted, assumed, placeholder, or not tested.
