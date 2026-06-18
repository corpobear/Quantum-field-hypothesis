# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current cosmology scaffold: v0.16-v0.30

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The correct wording is "no parameter sweep / internally constrained heuristic closure", not strict no-fit proof.
```

| Version | Script | Result folder | Purpose | Status |
|---|---|---|---|---|
| v0.16 | `mcift_big_bang_comparison_v0.16.py` | `results_v0.16/` | first visible/dark and BAO proxy comparison | exploratory |
| v0.17 | `mcift_big_bang_scale_lock_v0.17.py` | `results_v0.17/` | expansion-coupled scale-lock | partial |
| v0.18 | `mcift_big_bang_longmode_v0.18.py` | `results_v0.18/` | long-mode damping / primordial gate | pass-like peak proxy |
| v0.19 | `mcift_big_bang_anchor_cutoff_v0.19.py` | `results_v0.19/` | derives `k_cut = 2 pi / R_A` | stronger proxy |
| v0.20 | `mcift_big_bang_derived_scalelock_v0.20.py` | `results_v0.20/` | derives scale-lock amplitude/envelope | raw geometric proxy |
| v0.21 | `mcift_big_bang_pk_shape_v0.21.py` | `results_v0.21/` | full P(k) shape test | raw shape FAIL |
| v0.22 | `mcift_big_bang_growth_transfer_v0.22.py` | `results_v0.22/` | imported growth-transfer compatibility | PASS-LIKE with imported transfer |
| v0.23 | `mcift_big_bang_native_growth_v0.23.py` | `results_v0.23/` | first native no-import growth | FAIL |
| v0.24 | `mcift_big_bang_channel_exchange_v0.24.py` | `results_v0.24/` | coupled A/V/D/R channel exchange | WEAK |
| v0.25 | `mcift_big_bang_first_principle_sinks_v0.25.py` | `results_v0.25/` | first-principle six-sink count | WEAK |
| v0.26 | `mcift_big_bang_spin_blur_v0.26.py` | `results_v0.26/` | six-sector spin blur | WEAK |
| v0.27 | `mcift_big_bang_mass_gravity_time_spin_v0.27.py` | `results_v0.27/` | mass/gravity time-response spin blur | WEAK |
| v0.28 | `mcift_big_bang_thermo_spin_growth_v0.28.py` | `results_v0.28/` | thermodynamic spin-growth | PASS-LIKE shape; global 617.87 Mpc |
| v0.29 | `mcift_big_bang_collapse_containment_v0.29.py` | `results_v0.29/` | post-run collapse-containment overlay | global peak 152.29 Mpc |
| v0.30 | `mcift_big_bang_dynamic_ordered_collapse_v0.30.py` | `results_v0.30/` | response-epoch B reservoir before final scoring | PASS-LIKE; global peak 152.29 Mpc |

---

## Latest run: v0.30 dynamic ordered collapse-containment

Run after generating full v0.28 residuals/tracks:

```bash
python analysis/mcift_big_bang_dynamic_ordered_collapse_v0.30.py
```

Correct-order dynamic rule:

```text
coherence_capacity = 3.5 n X_containment A_lock W_capture
contained_complexity_load = C_n (1 + theta_G + c_s^2)
collapse_pressure = max(0, contained_complexity_load / coherence_capacity - 1)
collapse_factor(lambda) = exp[-collapse_pressure * max(0,lambda/R_A - 1) * lambda/R_A]
B_next = B + leaked V/D contained-complexity excess
```

Key result:

```text
v0.28 RMS = 0.302859
v0.29 overlay RMS = 0.302859
v0.30 dynamic-ordered RMS = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before dynamic order = 617.87 Mpc
v0.30 global peak after dynamic order = 152.29 Mpc
v0.30 BAO-window peak = 152.29 Mpc
```

Outputs:

```text
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_report.md
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_metrics.csv
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_background.csv
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_residuals.csv
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_comparison.png
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_comparison.svg
```

---

## Current strengths and weaknesses from analysis

### Strengths

```text
- BAO-window scale repeatedly survives near 152 Mpc.
- Six internal dark sectors can project toward four effective 3D transverse sinks through spin blur.
- Temperature, mass/gravity time response, and collapse-containment are represented as internal closures.
- v0.30 applies collapse-containment in chronological response-epoch order rather than only after the run.
```

### Weaknesses

```text
- v0.30 is still a toy/scaffold calculation.
- B is aggregate background/response-epoch feedback, not full B(k,a) mode-coupled dynamics.
- The collapse rule is not established GR/black-hole physics.
- CMB, BBN, lensing, halos, and dark energy behavior are not yet calculated.
```

---

## Next analysis target

```text
v0.31 target:
Couple B(k,a) directly into the perturbation equations instead of using response-epoch transfer history.
```
