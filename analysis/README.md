# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current level

```text
Current tested solver: v0.35 minimal spatial cubic lattice solver
Current previous solver: v0.34 first-principle cubic field toy solver
Current field formula: v0.33 cubic cell-complex field formula
Current mechanism layer: v0.32 cube-face Higgs vortex mass mechanism
Current geometry layer: v0.31 cube-center six-connector knot model
```

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The correct wording is "no parameter sweep / internally constrained heuristic closure", not strict no-fit proof.
```

---

## v0.35 spatial lattice solver

Run after generating full v0.28 residuals/tracks:

```bash
python analysis/mcift_spatial_cubic_lattice_v0.35.py
```

The solver instantiates:

```text
64^3 periodic cube-center nodes
six nearest-neighbor connector activations
Higgs face-plane vortex response
mass / complexity loading
local coherence capacity
local stability score
spatial reservoir field
shell-spectrum measurement
```

Key result:

```text
v0.34 mode-level RMS = 0.302859
v0.35 spatial-lattice mapped RMS = 0.303948
shape verdict = PASS-LIKE
spatial pre-collapse peak = 617.87 Mpc, harmonic n=1
spatial post-collapse peak = 154.47 Mpc, harmonic n=4
mapped v0.35 global peak = 152.29 Mpc
mapped v0.35 BAO-window peak = 152.29 Mpc
```

Outputs:

```text
analysis/results_v0.35/mcift_v0.35_spatial_lattice_report.md
analysis/results_v0.35/mcift_v0.35_spatial_lattice_metrics.csv
analysis/results_v0.35/mcift_v0.35_spatial_lattice_shell_power.csv
```

---

## Cosmology scaffold: v0.16-v0.35

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
| v0.30 | `mcift_big_bang_dynamic_ordered_collapse_v0.30.py` | `results_v0.30/` | response-epoch reservoir before final scoring | PASS-LIKE; global peak 152.29 Mpc |
| v0.34 | `mcift_big_bang_first_principle_cubic_field_v0.34.py` | `results_v0.34/` | first-principle cubic field mode-level solver | PASS-LIKE; global peak 152.29 Mpc |
| v0.35 | `mcift_spatial_cubic_lattice_v0.35.py` | `results_v0.35/` | explicit spatial cubic lattice solver | PASS-LIKE; spatial peak shifts n=1 to n=4 |

---

## Next analysis target

```text
v0.36 target:
Generate initial fields from internal connector/vortex noise and boundary conditions rather than explicitly seeding the super-anchor and n=4 stress-test modes.
```
