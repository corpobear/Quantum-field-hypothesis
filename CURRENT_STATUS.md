# Current MCIFT Status: v0.28

**Status:** speculative theoretical framework / toy cosmology scaffold; not established physics.  
**Current milestone:** v0.28 no-fit thermodynamic spin-growth scaffold.

---

## One-sentence status

```text
MCIFT now has a no-fit thermodynamic spin-growth scaffold that improves native P(k)-shape scoring to PASS-LIKE while preserving a BAO-window scale, but it still fails the global long-mode test and has not replaced Lambda-CDM.
```

---

## What changed through v0.28

The latest chain of cosmology tests moved from visual/toy field outputs to increasingly stricter numerical scaffolds:

```text
v0.16  first Big Bang proxy comparison
v0.17  expansion-coupled scale-lock
v0.18  long-mode damping / primordial gate
v0.19  anchor-derived cutoff k_cut = 2 pi / R_A
v0.20  derived scale-lock amplitude and envelope
v0.21  full P(k) shape test; raw shape failed
v0.22  growth-transfer compatibility scaffold; full shape passed after imported transfer layer
v0.23  first no-import native scalar growth attempt; full shape failed
v0.24  coupled channel-exchange solver; shape improved to WEAK
v0.25  first-principle six-sink retest; weaker than four effective sinks
v0.26  spin-blur projection; six internal sectors blurred toward four effective sinks
v0.27  mass-gravity-time spin blur; conservative time-response version
v0.28  no-fit thermodynamic spin-growth; native shape score improved to PASS-LIKE
```

---

## Current MCIFT mechanics under test

```text
R_A(a)        anchor/coherence RMS radius
k_cut(a)     2 pi / R_A(a)
A_lock(a)    anchor fraction of total positive channel density
N_internal   six dark sectors from eight-sector / one-point-anchor source math
N_eff(a)     effective sink count after spin blur
rho_G        A + 0.6 V + 0.45 D + exchange
theta_G      mass/gravity time-response load
theta_T      rho_R / (rho_R + rho_G)
T_rel        theta_T^(1/4)
beta_T       sqrt(T_rel)
W_capture    4(1-exp[-beta_T^2]) exp[-beta_T^2]
c_s^2        beta_T^2 / 3
chi_thermo   chi_MGT * (1 + beta_T)
```

v0.28 uses a no-fit thermodynamic closure:

```text
rho_T      = R
theta_T    = rho_R / (rho_R + rho_G)
T_rel      = theta_T^(1/4)
beta_T     = sqrt(T_rel)
W_capture  = 4(1-exp[-beta_T^2]) exp[-beta_T^2]
c_s^2      = beta_T^2 / 3
chi_thermo = chi_MGT * (1 + beta_T)
N_eff      = 4 + 2 exp[-chi_thermo^2]
```

---

## Latest v0.28 result

```text
thermo_spin_growth_shape_rms_log_residual = 0.302859
shape verdict = PASS-LIKE
native thermodynamic BAO-window peak = 152.29 Mpc
nearest BAO bin = 152.29 Mpc
native thermodynamic global peak = 617.87 Mpc
```

Interpretation:

```text
Thermodynamics is a useful missing layer: it improves the native shape score and keeps the six-to-four spin-blur behavior. It does not solve the global long-mode failure.
```

---

## Current strengths

```text
1. MCIFT gives explicit channel language for visible-manifest and dark-manifest behavior.
2. Several control quantities are now derived internally or replaced by no-fit internal closures.
3. Raw geometric MCIFT tests repeatedly produce a BAO-like scale near the sound-horizon comparison scale.
4. v0.28 improves native no-import shape scoring to PASS-LIKE without a thermodynamic parameter sweep.
5. The scaffold provides clear next failure/proof points instead of vague claims.
```

---

## Current weaknesses

```text
1. MCIFT remains speculative and unvalidated.
2. v0.28 is a toy/scaffold calculation, not a precision Boltzmann solver.
3. The global 617.87 Mpc long mode still fails.
4. The thermodynamic layer is still applied to milestone channel snapshots rather than a fully conserved background evolution.
5. CMB temperature/polarization spectra are not implemented.
6. BBN light-element predictions are not implemented.
7. Lensing, halo, galaxy-rotation, and cluster tests are not implemented.
8. Dark energy / late-time acceleration is not derived.
9. A fair likelihood / parameter-count comparison against Lambda-CDM is not complete.
```

---

## MCIFT vs Lambda-CDM: safe wording

Safe:

```text
MCIFT provides a possible mechanism for dark/visible channel splitting, spin-blurred dark-sector projection, thermodynamic capture effects, and BAO-window scale behavior.
```

Safe:

```text
MCIFT v0.28 reaches PASS-LIKE native P(k)-shape scoring in a no-fit thermodynamic scaffold, while still failing the global long-mode test.
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
Evolve the A/V/D/R background channels self-consistently under conservation and exchange equations, then rerun the no-fit thermodynamic growth test without relying on milestone channel snapshots.
```

Required equations:

```text
d rho_A / d ln a = -Q_A_to_V - Q_A_to_D
d rho_V / d ln a =  Q_A_to_V - Q_V_to_D - Q_V_to_R
d rho_D / d ln a =  Q_A_to_D + Q_V_to_D
d rho_R / d ln a =  Q_V_to_R
```

Secondary targets:

```text
- determine whether the 617.87 Mpc global mode is a toy-box artifact or true failure
- dark-channel equation of state w_D approximately 0
- dark-channel dilution rho_D(a) approximately a^-3
- lensing and halo behavior
- CMB temperature/polarization spectra
- BBN light-element abundances
- dark-energy / late-time acceleration sector
- fair likelihood comparison against Lambda-CDM
```
