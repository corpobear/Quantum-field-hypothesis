# MCIFT v0.54 Cosmology Coarse-Graining Layer

**Status:** speculative cosmology-scale scaffold; not established physics.

## Purpose

The collision mechanics are promoted into effective large-scale fields. Local branch fractions become coarse-grained densities. Local clock, rotation, and sound effects become lapse, vorticity, and acoustic-spread terms.

## Fields

```text
rho_v(x,t)    visible matter density
rho_h(x,t)    hidden/sink density
rho_rot(x,t)  rotation/vorticity density
rho_s(x,t)    acoustic/sound-shell density
rho_r(x,t)    radiation density
N(x,t)        lapse / clock field
Omega(x,t)    vorticity field
c_s(x,t)      effective sound speed
```

## Gravity source

```text
rho_grav = rho_v + C_h rho_h + C_rot rho_rot + C_s rho_s + rho_r
```

## Expansion scaffold

```text
H_core(a)^2 = sum_i Omega_i a^(-n_i)
N(a) = tau_rot / sqrt(1 + chi0 H_core(a)^2)
H_lab(a) = H_core(a) / N(a)
```

## Acoustic horizon

```text
r_s(a) = integral_0^a c_s(a') / (a'^2 H_lab(a')) da'
```

## Continuity equations

```text
dot(rho_i) + 3H(rho_i + p_i) = Q_i
sum_i Q_i = 0
```

## Perturbation scaffold

```text
delta_i'' + 2H delta_i' + (c_s,i^2 k^2/a^2) delta_i
= 4 pi G sum_j mu_ij(a,k) rho_j delta_j
```

## Meaning

The learned collision geometry becomes a cosmology language:

```text
hidden load      -> dark/sink gravitational density
sound spread     -> acoustic pressure and horizon
time dilation    -> lapse / clock mismatch
rotation         -> vorticity and shear support
branch transfer  -> source exchange terms
```

## Next target

v0.55 should implement the Q_i transfer network and test whether the hidden/sound/rotation sectors can evolve without hand-normalization.
