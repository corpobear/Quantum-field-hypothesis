# MCIFT v0.30 Dynamic Ordered Collapse-Containment Retest Report

**Status:** dynamic response-epoch B-reservoir first pass; speculative toy/scaffold result, not established physics.  
**Script:** `analysis/mcift_big_bang_dynamic_ordered_collapse_v0.30.py`  
**Main change from v0.29:** collapse is applied in the correct order through the growth history. Each MCIFT response epoch updates the collapsed-knot reservoir B and applies containment to uncontained modes before final scoring.

## Wording

Use:

```text
no parameter sweep / internally constrained heuristic closure
```

Do not describe this as strict no-fit proof. No parameter sweep was performed, but the closure remains a model assumption.

## Correct-order dynamic rule

For each MCIFT response epoch:

```text
coherence_capacity = 3.5 n X_containment A_lock W_capture
contained_complexity_load = C_n (1 + theta_G + c_s^2)
collapse_pressure = max(0, contained_complexity_load / coherence_capacity - 1)
collapse_factor(lambda) = exp[-collapse_pressure * max(0,lambda/R_A - 1) * lambda/R_A]
B_next = B + leaked V/D contained-complexity excess
```

This is different from v0.29 because the spectrum is not corrected once at the end. The super-anchor mode is tested against containment at every response epoch before final scoring.

## Dynamic background at 5B

```text
A_bg(5B) = 0.891174
V_bg(5B) = 0.048089
D_bg(5B) = 0.047217
R_bg(5B) = 0.010379
B_bg(5B) = 0.003141
```

## Result

```text
v0.28 RMS = 0.302859
v0.29 overlay RMS = 0.302859
v0.30 dynamic-ordered RMS = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before dynamic order = 617.87 Mpc
v0.30 global peak after dynamic order = 152.29 Mpc
v0.30 BAO-window peak = 152.29 Mpc
```

## Transfer diagnostics

```text
cumulative transfer at 617.87 Mpc = 0.558702
transfer at nearest BAO bin = 1.000000
collapse pressure final = 0.456156
coherence capacity final = 23.171783
contained complexity load final = 33.741724
```

## Interpretation

```text
Applying collapse-containment in chronological response-epoch order suppresses the uncontained 617.87 Mpc mode before final scoring and returns the global peak to the BAO-window scale. The scored shape RMS remains unchanged because the affected super-anchor mode is outside the P(k) scoring window.
```

## Remaining limitation

```text
This is still an aggregate dynamic-background scaffold. The next step is to couple B directly into the mode equations as B(k,a), not only as response-epoch transfer and background leakage.
```
