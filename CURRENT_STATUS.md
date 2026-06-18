# Current MCIFT Status: v0.31 Geometry Layer + v0.30 Numeric Retest

**Status:** speculative theoretical framework / toy cosmology scaffold; not established physics.  
**Current conceptual layer:** v0.31 cube-center six-connector knot geometry.  
**Current numeric retest:** v0.30 dynamic ordered collapse-containment.

---

## One-sentence status

```text
MCIFT now combines a cube-centered six-connector knot geometry with the v0.30 dynamic ordered collapse-containment retest: each knot sits at a cube-cell center with six axial connector states, and collapse-containment occurs when connector-supported coherence capacity cannot hold contained complexity. Numerically, the v0.30 scaffold suppresses the previous 617.87 Mpc super-anchor mode before final scoring and returns the global peak to 152.29 Mpc while keeping the scored shape RMS PASS-LIKE.
```

---

## Wording correction

Use:

```text
no parameter sweep / internally constrained heuristic closure
```

Do not overstate the current result as strict no-fit proof. The retests did not scan parameters against the target, but the closure choices remain model assumptions.

---

## Current geometry: cube-center six-connector knot

A knot is represented as the center of a spacetime cube-cell:

```text
knot position = center of cube-cell
```

It has six axial connector states through the cube faces:

```text
+x, -x, +y, -y, +z, -z
```

Each connector can be inactive, partially active, or fully active:

```text
0 <= a_mu <= 1
```

The six connector states supply local coherence capacity. Directional imbalance penalizes coherence:

```text
Delta_i = sqrt[(a_+x-a_-x)^2 + (a_+y-a_-y)^2 + (a_+z-a_-z)^2]
Coh_i = 6 a_i,mean - lambda_Delta Delta_i
```

Containment condition:

```text
S_i = Coh_i - Q_i
S_i >= 0   stable/open knot
S_i < 0    containment failure / collapsed-knot condition
```

---

## What changed through v0.31

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
v0.31  cube-center six-connector geometry; connector-level coherence and imbalance formalized
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
a_mu         six cube-face connector activations
Delta_i      directional imbalance of opposite connectors
Coh_i        local connector coherence capacity
S_contain    coherence capacity minus contained complexity
B            collapsed-knot reservoir
```

Correct-order dynamic collapse rule from v0.30:

```text
coherence_capacity = 3.5 n X_containment A_lock W_capture
contained_complexity_load = C_n (1 + theta_G + c_s^2)
collapse_pressure = max(0, contained_complexity_load / coherence_capacity - 1)
collapse_factor(lambda) = exp[-collapse_pressure * max(0,lambda/R_A - 1) * lambda/R_A]
B_next = B + leaked V/D contained-complexity excess
```

---

## Latest numeric result: v0.30

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

---

## Current strengths

```text
1. MCIFT has a reproducible chain of toy/scaffold tests through v0.30.
2. v0.31 supplies a local six-connector geometry for knots and containment.
3. The BAO-window scale repeatedly survives near 152 Mpc.
4. Six internal connector sectors can project toward four effective transverse channels through spin blur.
5. Temperature, mass/gravity time response, connector coherence, and collapse containment are now represented as internal closures.
```

---

## Current weaknesses

```text
1. MCIFT remains speculative and unvalidated.
2. v0.31 is a geometry note, not a tested connector-level solver yet.
3. v0.30 is an aggregate response-epoch scaffold, not a spatial B(k,a) mode solver.
4. The collapse rule is heuristic and internally constrained, not established black-hole/GR physics.
5. CMB, BBN, lensing, halo, galaxy-rotation, cluster, and dark-energy tests are not implemented.
6. No fair likelihood / parameter-count comparison against Lambda-CDM is complete.
```

---

## Safe wording

Safe:

```text
MCIFT can be visualized as a cube-centered six-connector information geometry, where each knot sits at a cube-cell center and coherence is supplied by six axial connector states to neighboring cube centers.
```

Safe:

```text
MCIFT v0.30 shows that chronological collapse-containment can suppress the previous 617.87 Mpc super-anchor mode and restore the global peak to the BAO-window scale inside the current scaffold.
```

Not safe:

```text
MCIFT proves spacetime is literally a cubic lattice.
MCIFT proves black holes.
MCIFT proves dark matter.
MCIFT proves dark energy.
MCIFT replaces Lambda-CDM.
```

---

## Next proof target

```text
Use the v0.31 six connector variables directly in a mode-coupled B(k,a) perturbation solver, replacing aggregate response-epoch B transfer.
```

Required direction:

```text
- evolve a_i,mu connector activations
- compute Delta_i and Coh_i dynamically
- couple collapse-containment into B(k,a)
- rerun thermodynamic growth with B coupled directly to each mode
```
