# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current cosmology scaffold: v0.16-v0.29

The current analysis focus is the MCIFT Big Bang / BAO / matter-power-spectrum scaffold.

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The phrase "no-fit" has been replaced by "no parameter sweep / internally constrained heuristic closure" because the closures are still model assumptions.
```

| Version | Script | Result folder | Purpose | Status |
|---|---|---|---|---|
| v0.16 | `mcift_big_bang_comparison_v0.16.py` | `results_v0.16/` | first visible/dark and BAO proxy comparison | exploratory |
| v0.17 | `mcift_big_bang_scale_lock_v0.17.py` | `results_v0.17/` | expansion-coupled scale-lock | partial |
| v0.18 | `mcift_big_bang_longmode_v0.18.py` | `results_v0.18/` | long-mode damping / primordial gate | pass-like peak proxy |
| v0.19 | `mcift_big_bang_anchor_cutoff_v0.19.py` | `results_v0.19/` | derives `k_cut = 2 pi / R_A` from anchor radius | stronger proxy |
| v0.20 | `mcift_big_bang_derived_scalelock_v0.20.py` | `results_v0.20/` | derives scale-lock amplitude and envelope | strongest raw geometric proxy |
| v0.21 | `mcift_big_bang_pk_shape_v0.21.py` | `results_v0.21/` | full P(k) shape test | raw shape FAIL |
| v0.22 | `mcift_big_bang_growth_transfer_v0.22.py` | `results_v0.22/` | growth-transfer compatibility scaffold | PASS-LIKE with imported transfer |
| v0.23 | `mcift_big_bang_native_growth_v0.23.py` | `results_v0.23/` | first no-import scalar native growth | FAIL |
| v0.24 | `mcift_big_bang_channel_exchange_v0.24.py` | `results_v0.24/` | coupled A/V/D/R channel exchange | WEAK |
| v0.25 | `mcift_big_bang_first_principle_sinks_v0.25.py` | `results_v0.25/` | first-principle six-sink count | WEAK |
| v0.26 | `mcift_big_bang_spin_blur_v0.26.py` | `results_v0.26/` | six-sector spin blur to four effective sinks | WEAK |
| v0.27 | `mcift_big_bang_mass_gravity_time_spin_v0.27.py` | `results_v0.27/` | mass/gravity time-response spin blur | WEAK |
| v0.28 | `mcift_big_bang_thermo_spin_growth_v0.28.py` | `results_v0.28/` | thermodynamic spin-growth layer | PASS-LIKE shape; global mode still 617.87 Mpc |
| v0.29 | `mcift_big_bang_collapse_containment_v0.29.py` | `results_v0.29/` | collapse-containment overlay when coherence cannot hold complexity | PASS-LIKE shape; global peak returns to 152.29 Mpc |

---

## Latest run: v0.29 collapse-containment overlay

Run after generating full v0.28 residuals/tracks:

```bash
python analysis/mcift_big_bang_collapse_containment_v0.29.py
```

Containment rule:

```text
coherence_capacity = 3.5 n X_containment A_lock W_capture
contained_complexity_load = C_n (1 + theta_G + c_s^2)
collapse_excess = max(0, contained_complexity_load - coherence_capacity)
collapse_pressure = max(0, contained_complexity_load / coherence_capacity - 1)
```

First retest:

```text
n = 4
C_n = 16
X_containment = 1 + beta_spin
collapse activates only for modes with wavelength lambda > R_A
collapse_factor(lambda) = exp[-collapse_pressure * lambda / R_A]
```

Key result:

```text
v0.28 RMS before collapse = 0.302859
v0.29 RMS after collapse = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before collapse = 617.87 Mpc
v0.29 global peak after collapse = 152.29 Mpc
v0.29 BAO-window peak = 152.29 Mpc
```

Interpretation:

```text
v0.29 treats the 617.87 Mpc mode as uncontained because its wavelength is larger than the anchor/coherence radius. The mode is drained into a collapsed-knot reservoir, so it no longer dominates the global spectrum.
```

Outputs:

```text
analysis/results_v0.29/mcift_v0.29_collapse_containment_report.md
analysis/results_v0.29/mcift_v0.29_collapse_containment_metrics.csv
analysis/results_v0.29/mcift_v0.29_collapse_containment_residuals.csv
analysis/results_v0.29/mcift_v0.29_collapse_containment_tracks.csv
analysis/results_v0.29/mcift_v0.29_collapse_containment_comparison.png
analysis/results_v0.29/mcift_v0.29_collapse_containment_comparison.svg
```

---

## Current strengths and weaknesses from analysis

### Strengths

```text
- Internal anchor radius, cutoff, scale-lock amplitude, and envelope are derived in the toy scaffold.
- Six internal dark sectors can project toward four effective 3D transverse sinks through spin blur.
- Mass/gravity time response and temperature affect the spin-growth closure.
- MCIFT repeatedly produces a BAO-window scale near the sound-horizon comparison scale.
- v0.29 gives a model-native explanation for the previous 617.87 Mpc global-mode failure: coherence capacity was insufficient to contain that mode's complexity.
```

### Weaknesses

```text
- v0.29 is still a toy/scaffold overlay, not a dynamic collapse solver.
- The collapse rule is heuristic and internally constrained, not established black-hole/GR physics.
- The B collapsed-knot reservoir is not yet part of conserved A/V/D/R/B background evolution.
- CMB, BBN, lensing, halos, and dark energy behavior are not yet calculated.
```

---

## Next analysis target

```text
v0.30 target:
Dynamic collapsed-knot reservoir B plus self-consistent conserved A/V/D/R/B background evolution and thermodynamic perturbation growth.
```

Required background equations:

```text
d rho_A / d ln a = -Q_A_to_V - Q_A_to_D
d rho_V / d ln a =  Q_A_to_V - Q_V_to_D - Q_V_to_R - Q_V_to_B
d rho_D / d ln a =  Q_A_to_D + Q_V_to_D - Q_D_to_B
d rho_R / d ln a =  Q_V_to_R + collapse thermal feedback
d rho_B / d ln a =  Q_V_to_B + Q_D_to_B
```

---

## Historical v0.15 matter-antimatter toy ratio

Script:

```text
analysis/matter_antimatter_toy_v0.15.py
```

Output:

```text
analysis/results_v0.15/matter_antimatter_toy_ratio.csv
```

This reduced calculation treats antimatter as positive-mass channel-reversed geometry, not negative mass.

The toy geometry uses:

```text
matter visible drill      = center-tip collector
matter dark sink          = side-belt collector
antimatter dark sink      = Higgs-drop collector
antimatter light drill    = splash-ring collector with discarded middle
```

The reduced toy result is:

$$
\frac{A_M}{A_{\bar M}}=1.28669912372469.
$$

This is an internal toy-model consistency result, not physical confirmation of baryon asymmetry.
