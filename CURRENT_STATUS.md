# Current MCIFT Status: v0.22

**Status:** speculative theoretical framework / toy cosmology scaffold; not established physics.  
**Current milestone:** v0.22 growth-transfer compatibility scaffold.

---

## One-sentence status

```text
MCIFT now has internally derived anchor/cutoff/scale-lock mechanics that repeatedly produce a BAO-like geometric scale, and v0.22 shows compatibility with standard broadband growth-transfer physics, but MCIFT has not yet independently derived the full cosmological transfer function or replaced Lambda-CDM.
```

---

## What changed through v0.22

The latest chain of cosmology tests moved from visual/toy field outputs to increasingly stricter numerical scaffolds:

```text
v0.16  first Big Bang proxy comparison
v0.17  expansion-coupled scale-lock
v0.18  long-mode damping / primordial gate
v0.19  anchor-derived cutoff k_cut = 2 pi / R_A
v0.20  derived scale-lock amplitude and envelope
v0.21  full P(k) shape test; raw shape failed
v0.22  growth-transfer compatibility scaffold; full shape passed after imported transfer layer
```

---

## Current MCIFT mechanics under test

```text
R_A(a)      anchor/coherence RMS radius
k_cut(a)   2 pi / R_A(a)
A_lock(a)  anchor fraction of total positive channel density
R_env(a)   R_A(a)
p           number of dark-side sinks = 4
```

v0.22 uses:

```text
P(k,a) = A_s (k/k_pivot)^n_s T_growth^2(k) T_MCIFT^2(k,a)
```

with MCIFT modulation:

```text
T_MCIFT(k,a) = 1 + epsilon_lock sin(k r_s) exp[-(k/0.18)^1.4]
epsilon_lock = 0.12 * A_lock(a)
```

---

## Current strengths

```text
1. MCIFT gives explicit channel language for visible-manifest and dark-manifest behavior.
2. Several control quantities are now derived internally rather than hand-set.
3. Raw geometric MCIFT tests repeatedly produce a BAO-like scale near the sound horizon.
4. v0.22 shows MCIFT-derived modulation can coexist with standard growth-transfer physics.
5. The scaffold provides clear next failure/proof points instead of vague claims.
```

---

## Current weaknesses

```text
1. MCIFT remains speculative and unvalidated.
2. v0.22 imports T_growth(k) from existing cosmology rather than deriving it.
3. CMB temperature/polarization spectra are not implemented.
4. BBN light-element predictions are not implemented.
5. Lensing, halo, galaxy-rotation, and cluster tests are not implemented.
6. Dark energy / late-time acceleration is not derived.
7. A fair likelihood / parameter-count comparison against Lambda-CDM is not complete.
```

---

## MCIFT vs Lambda-CDM: safe wording

Safe:

```text
MCIFT provides a possible mechanism for dark/visible channel splitting and BAO-like scale selection.
```

Safe:

```text
MCIFT v0.22 is compatible with a standard growth-transfer layer while supplying a derived anchor/acoustic modulation.
```

Not safe:

```text
MCIFT proves dark matter.
```

Not safe:

```text
MCIFT proves dark energy.
```

Not safe:

```text
MCIFT replaces Lambda-CDM.
```

---

## Next proof target

The next hard test is:

```text
Derive T_growth(k) from MCIFT channel dynamics instead of importing BBKS/Sugiyama or another standard growth-transfer approximation.
```

Secondary targets:

```text
- dark-channel equation of state w_D approximately 0
- dark-channel dilution rho_D(a) approximately a^-3
- lensing and halo behavior
- CMB temperature/polarization spectra
- BBN light-element abundances
- dark-energy / late-time acceleration sector
- fair likelihood comparison against Lambda-CDM
```
