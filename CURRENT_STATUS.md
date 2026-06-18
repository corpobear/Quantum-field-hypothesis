# Current MCIFT Status: v0.30

**Status:** speculative theoretical framework / toy cosmology scaffold; not established physics.  
**Current milestone:** v0.30 dynamic ordered collapse-containment retest.

---

## One-sentence status

```text
MCIFT now tests collapse-containment in the correct chronological order: each response epoch checks whether coherence capacity can contain complexity, updates a collapsed-knot reservoir B, and only then scores the final spectrum. In this first v0.30 dynamic-ordered retest, the previous 617.87 Mpc global peak is suppressed before final scoring and the global peak returns to 152.29 Mpc, while the scored shape RMS remains PASS-LIKE.
```

---

## Wording correction

Use:

```text
no parameter sweep / internally constrained heuristic closure
```

Do not overstate the current result as strict no-fit proof. The retest did not scan parameters against the target, but the closure choices remain model assumptions.

---

## What changed through v0.30

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
v0.29  collapse-containment overlay; post-run correction moved global peak to 152.29 Mpc
v0.30  dynamic ordered collapse; response-epoch B reservoir suppresses 617.87 Mpc before final scoring
```

---

## Current mechanics under test

```text
R_A(a)        anchor/coherence RMS radius
A_lock(a)    anchor fraction of total positive channel density
theta_G      mass/gravity time-response load
theta_T      rho_R / (rho_R + rho_G)
W_capture    thermodynamic capture window
c_s^2        thermal sound-speed proxy
S_contain    coherence capacity minus contained complexity
B            collapsed-knot reservoir
```

Correct-order dynamic rule:

```text
coherence_capacity = 3.5 n X_containment A_lock W_capture
contained_complexity_load = C_n (1 + theta_G + c_s^2)
collapse_pressure = max(0, contained_complexity_load / coherence_capacity - 1)
collapse_factor(lambda) = exp[-collapse_pressure * max(0,lambda/R_A - 1) * lambda/R_A]
B_next = B + leaked V/D contained-complexity excess
```

---

## Latest v0.30 result

```text
v0.28 RMS = 0.302859
v0.29 overlay RMS = 0.302859
v0.30 dynamic-ordered RMS = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before dynamic order = 617.87 Mpc
v0.30 global peak after dynamic order = 152.29 Mpc
v0.30 BAO-window peak = 152.29 Mpc
```

Dynamic background at 5B:

```text
A_bg = 0.891174
V_bg = 0.048089
D_bg = 0.047217
R_bg = 0.010379
B_bg = 0.003141
```

Interpretation:

```text
Applying collapse-containment in chronological response-epoch order suppresses the uncontained 617.87 Mpc mode before final scoring and returns the global peak to the BAO-window scale. The scored RMS is unchanged because the affected super-anchor mode is outside the P(k) scoring window.
```

---

## Current strengths

```text
1. MCIFT has a reproducible chain of toy/scaffold tests through v0.30.
2. The BAO-window scale repeatedly survives near 152 Mpc.
3. Six internal dark sectors can project toward four effective transverse sinks through spin blur.
4. Temperature, mass/gravity time response, and collapse containment are now represented as internal closures.
5. v0.30 tests collapse in the correct chronological order rather than only as a final overlay.
```

---

## Current weaknesses

```text
1. MCIFT remains speculative and unvalidated.
2. v0.30 is an aggregate response-epoch scaffold, not a spatial B(k,a) mode solver.
3. The collapse rule is heuristic and internally constrained, not established black-hole/GR physics.
4. CMB, BBN, lensing, halo, galaxy-rotation, cluster, and dark-energy tests are not implemented.
5. No fair likelihood / parameter-count comparison against Lambda-CDM is complete.
```

---

## Safe wording

Safe:

```text
MCIFT v0.30 shows that chronological collapse-containment can suppress the previous 617.87 Mpc super-anchor mode and restore the global peak to the BAO-window scale inside the current scaffold.
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

```text
Replace aggregate response-epoch B with a mode-coupled B(k,a) reservoir inside the perturbation equations, then rerun the thermodynamic growth solver.
```

Required dynamic form:

```text
d rho_A / d ln a = -Q_A_to_V - Q_A_to_D
d rho_V / d ln a =  Q_A_to_V - Q_V_to_D - Q_V_to_R - Q_V_to_B
d rho_D / d ln a =  Q_A_to_D + Q_V_to_D - Q_D_to_B
d rho_R / d ln a =  Q_V_to_R + collapse thermal feedback
d rho_B / d ln a =  Q_V_to_B + Q_D_to_B
```
