# MCIFT v0.29 Collapse-Containment Retest Report

**Status:** collapse-containment overlay on the v0.28 thermodynamic spin-growth scaffold; speculative toy/scaffold result, not established physics.  
**Script:** `analysis/mcift_big_bang_collapse_containment_v0.29.py`  
**Main change from v0.28:** adds a collapsed-knot sink rule: when coherence capacity is not enough to contain complexity, uncontained modes are drained from the free growth spectrum.

## Wording correction

Earlier docs used **"no-fit"** too strongly. v0.29 uses the more accurate wording:

```text
no parameter sweep / internally constrained heuristic closure
```

The constants are not tuned by scanning against the target, but the closure choices are still model assumptions. They are not observationally fitted parameters and not first-principle proof.

## Containment rule

Existing MCIFT stability uses complexity and coherence capacity:

```text
C_n = 2^n
S_n = 3.5 n X_n - C_n
```

v0.29 applies the same idea to the thermodynamic cosmology scaffold:

```text
coherence_capacity = 3.5 n X_containment A_lock W_capture
contained_complexity_load = C_n (1 + theta_G + c_s^2)
collapse_excess = max(0, contained_complexity_load - coherence_capacity)
collapse_pressure = max(0, contained_complexity_load / coherence_capacity - 1)
```

For this first retest:

```text
n = 4
C_n = 16
X_containment = 1 + beta_spin
collapse activates only for modes with wavelength lambda > R_A
collapse_factor(lambda) = exp[-collapse_pressure * lambda / R_A]
```

This is a no-sweep rule: the fourth-mode containment test, the anchor radius, and the thermodynamic quantities come from prior MCIFT mechanics/results.

## Final containment values

```text
R_A(5B) = 505.829530 Mpc
coherence_capacity = 23.171783
contained_complexity_load = 33.741724
collapse_excess = 10.569941
collapse_pressure = 0.456156
uncontained modes with lambda > R_A = 1
collapse factor at 617.87 Mpc = 0.572816
```

## Result

```text
v0.28 RMS before collapse = 0.302859
v0.29 RMS after collapse = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before collapse = 617.87 Mpc
v0.29 global peak after collapse = 152.29 Mpc
v0.29 BAO-window peak = 152.29 Mpc
```

The scored RMS is unchanged because the collapsed 617.87 Mpc mode lies outside the v0.28 P(k) scoring window. The important change is that the uncontained super-anchor mode no longer dominates the global peak.

## Interpretation

```text
The 617.87 Mpc mode behaves like an uncontained coherence mode: its wavelength is larger than the anchor/coherence radius R_A.
When MCIFT applies the rule that coherence must exceed contained complexity, that mode is drained into a collapsed-knot reservoir.
This moves the global peak back to the BAO-window scale without changing the scored shape window.
```

## What remains unproven

```text
This is still a collapse-containment overlay, not a full black-hole/GR treatment.
The next step is to place the B collapsed-knot reservoir inside the conserved A/V/D/R/B background evolution equations and rerun the perturbation solver dynamically.
```
