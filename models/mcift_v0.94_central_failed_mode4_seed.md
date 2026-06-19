# MCIFT v0.94 Central Failed-Mode-4 Seed

**Status:** simplified cosmology initial-condition layer; speculative model construction, not established cosmology.

## 1. Motivation

The reduced v0.93 bubble formula needs one clean initial condition before cosmology is retested.

The earlier toy model already identifies a fourth mode that fails stability:

```text
Mode 4 complexity = 16
Mode 4 coherence = 14
Mode 4 stability = -2
Outcome = fails
```

That failed fourth mode is treated as reservoir availability rather than a fourth stable particle.

v0.94 promotes that failed mode into the central seed reservoir of the bubble cosmology scaffold.

## 2. Central seed event

Define the universe-seed cell:

```text
i = 0
C_0 = (x_0,t_0)
x_0 = 0
t_0 = 0
```

The central seed object is:

```text
B_0 = {C_0, S_0, r_0, W_0, Phi_0, M_0, R_4}
```

where:

```text
M_0 = central seed mass/load
R_4 = failed mode-4 reservoir
```

## 3. Failed mode-4 reservoir

Use the toy mode law:

```text
C_n = 2^n
Q_n = a n
S_n = Q_n - C_n
```

For the central toy value:

```text
a = 3.5
```

Mode 4 gives:

```text
C_4 = 16
Q_4 = 14
S_4 = -2
```

Define reservoir magnitude:

```text
R_4 = max(0, -S_4) = 2
```

The failed mode is not a stable particle. It is stored as central reservoir/load.

## 4. Central mass/load rule

Define central seed load:

```text
M_0 = mu_4 * R_4
```

where:

```text
mu_4 = conversion factor from failed-knot reservoir to bubble deformation load
```

For dimensionless toy tests, set:

```text
mu_4 = 1
M_0 = 2
```

## 5. Bubble deformation from central mass

The central mass/load creates isotropic inward deformation of the initial bubble:

```text
rho_0(n,r) = 1 - alpha_M * M_0 / (r^2 + r_core^2)
```

with bounds:

```text
rho_floor <= rho_0(n,r) <= 1
```

where:

```text
r_core prevents singular behavior at the exact center
rho_floor prevents complete collapse of the causal surface
```

The initial radius remains:

```text
r(n,t) = c Delta t rho_0(n,r)
```

## 6. Why this simplifies cosmology

Instead of inventing matter/loading later, the model begins with one central failed-knot reservoir.

Then cosmology observables can be reduced from:

```text
central seed load -> bubble deformation -> average expansion/lensing/curvature proxies
```

The first reducer should compute:

```text
M_0
R_4
mean rho
mean deformation = <1-rho>
H_proxy = <partial_t r / r>
load_proxy = <1-rho>
curvature_proxy = surface loop phase
anisotropy_proxy = max(rho)/min(rho)-1
```

## 7. Interpretation

The central failed mode acts like the stored instability at the origin of the model universe.

It is a candidate starting reservoir, not a confirmed Big Bang singularity.

The model should avoid a literal infinite point mass. The center is regulated by `r_core`.

## 8. Next test

v0.95 should run the central-seed reducer and export dimensionless cosmology proxies before comparing to observational data.

## 9. Strict limits

This does not prove the universe began as a mode-4 knot.

This does not derive standard Big Bang cosmology.

It provides a simplified initial condition for the MCIFT bubble cosmology retest.
