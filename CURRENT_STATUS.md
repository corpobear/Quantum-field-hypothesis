# Current MCIFT Status: v0.29

**Status:** speculative theoretical framework / toy cosmology scaffold; not established physics.  
**Current milestone:** v0.29 collapse-containment overlay on the thermodynamic spin-growth scaffold.

---

## One-sentence status

```text
MCIFT now has an internally constrained thermodynamic spin-growth scaffold plus a collapse-containment rule: when coherence capacity cannot contain complexity, uncontained modes are drained into a collapsed-knot reservoir. In the first v0.29 overlay, the previous 617.87 Mpc global peak is reduced and the global peak returns to 152.29 Mpc, but this is still a toy/scaffold result and not a Lambda-CDM replacement.
```

---

## Wording correction

Earlier project files used **"no-fit"** too strongly.

Correct wording:

```text
no parameter sweep / internally constrained heuristic closure
```

Meaning:

```text
The run did not scan parameters to match the target, but the closure choices are still model assumptions. They are not observationally fitted constants and not first-principle proof.
```

---

## What changed through v0.29

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
v0.28  thermodynamic spin-growth; shape score improved to PASS-LIKE but global peak remained 617.87 Mpc
v0.29  collapse-containment overlay; uncontained 617.87 Mpc mode drains into collapsed-knot reservoir and global peak returns to 152.29 Mpc
```

---

## Current MCIFT mechanics under test

```text
R_A(a)        anchor/coherence RMS radius
k_cut(a)     2 pi / R_A(a)
A_lock(a)    anchor fraction of total positive channel density
N_internal   six dark sectors from eight-sector / one-point-anchor source math
N_eff(a)     effective sink count after spin blur
theta_G      mass/gravity time-response load
theta_T      rho_R / (rho_R + rho_G)
T_rel        theta_T^(1/4)
beta_T       sqrt(T_rel)
W_capture    4(1-exp[-beta_T^2]) exp[-beta_T^2]
c_s^2        beta_T^2 / 3
S_contain    coherence capacity minus contained complexity
B            collapsed-knot reservoir, not yet dynamically evolved
```

v0.29 containment rule:

```text
coherence_capacity = 3.5 n X_containment A_lock W_capture
contained_complexity_load = C_n (1 + theta_G + c_s^2)
collapse_excess = max(0, contained_complexity_load - coherence_capacity)
collapse_pressure = max(0, contained_complexity_load / coherence_capacity - 1)
```

First retest choices:

```text
n = 4
C_n = 16
X_containment = 1 + beta_spin
collapse activates only for modes with wavelength lambda > R_A
collapse_factor(lambda) = exp[-collapse_pressure * lambda / R_A]
```

---

## Latest v0.29 result

```text
v0.28 RMS before collapse = 0.302859
v0.29 RMS after collapse = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before collapse = 617.87 Mpc
v0.29 global peak after collapse = 152.29 Mpc
v0.29 BAO-window peak = 152.29 Mpc
```

Important interpretation:

```text
The scored RMS is unchanged because the collapsed 617.87 Mpc mode lies outside the v0.28 P(k) scoring window. The meaningful change is that the uncontained super-anchor mode no longer dominates the global peak.
```

---

## Current strengths

```text
1. MCIFT gives explicit channel language for visible-manifest and dark-manifest behavior.
2. Several control quantities are now derived internally or replaced by internally constrained closures.
3. Raw geometric MCIFT tests repeatedly produce a BAO-like scale near the sound-horizon comparison scale.
4. v0.28 improves native no-import shape scoring to PASS-LIKE without a parameter sweep.
5. v0.29 gives an MCIFT-native explanation for the previous 617.87 Mpc long-mode dominance: coherence capacity was not enough to contain the mode's complexity.
```

---

## Current weaknesses

```text
1. MCIFT remains speculative and unvalidated.
2. v0.29 is an overlay, not a dynamic A/V/D/R/B conserved-background solver.
3. The collapse rule is heuristic and internally constrained, not established black-hole/GR physics.
4. CMB temperature/polarization spectra are not implemented.
5. BBN light-element predictions are not implemented.
6. Lensing, halo, galaxy-rotation, and cluster tests are not implemented.
7. Dark energy / late-time acceleration is not derived.
8. A fair likelihood / parameter-count comparison against Lambda-CDM is not complete.
```

---

## MCIFT vs Lambda-CDM: safe wording

Safe:

```text
MCIFT provides a possible mechanism for dark/visible channel splitting, spin-blurred dark-sector projection, thermodynamic capture effects, and collapse-containment of uncontained coherent complexity.
```

Safe:

```text
MCIFT v0.29 moves the previous global peak failure from 617.87 Mpc to 152.29 Mpc in a collapse-containment overlay, while preserving the v0.28 PASS-LIKE scored shape window.
```

Not safe:

```text
MCIFT proves black holes.
MCIFT proves dark matter.
MCIFT proves dark energy.
MCIFT replaces Lambda-CDM.
```

---

## Next proof target

The next hard test is dynamic:

```text
Add B = collapsed-knot reservoir and evolve conserved A/V/D/R/B backgrounds, then rerun the thermodynamic perturbation solver without post-processing.
```

Required background form:

```text
d rho_A / d ln a = -Q_A_to_V - Q_A_to_D
d rho_V / d ln a =  Q_A_to_V - Q_V_to_D - Q_V_to_R - Q_V_to_B
d rho_D / d ln a =  Q_A_to_D + Q_V_to_D - Q_D_to_B
d rho_R / d ln a =  Q_V_to_R + collapse thermal feedback
d rho_B / d ln a =  Q_V_to_B + Q_D_to_B
```

Secondary targets:

```text
- determine whether dynamic B evolution preserves the 152.29 Mpc global peak
- dark-channel equation of state w_D approximately 0
- dark-channel dilution rho_D(a) approximately a^-3
- lensing and halo behavior
- CMB temperature/polarization spectra
- BBN light-element abundances
- dark-energy / late-time acceleration sector
- fair likelihood comparison against Lambda-CDM
```
