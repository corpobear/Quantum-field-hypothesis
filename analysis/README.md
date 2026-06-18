# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current cosmology scaffold: v0.16-v0.28

The current analysis focus is the MCIFT Big Bang / BAO / matter-power-spectrum scaffold.

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
v0.28 improves native no-fit shape scoring, but the global 617.87 Mpc long mode still fails.
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
| v0.28 | `mcift_big_bang_thermo_spin_growth_v0.28.py` | `results_v0.28/` | no-fit thermodynamic spin-growth layer | PASS-LIKE shape; global mode FAIL |

---

## Latest run: v0.28 no-fit thermodynamic spin-growth

Run:

```bash
python analysis/mcift_big_bang_thermo_spin_growth_v0.28.py
```

No-fit closure:

```text
rho_G      ~ A + 0.6 V + 0.45 D + exchange
rho_T      = R
theta_T    = rho_R / (rho_R + rho_G)
T_rel      = theta_T^(1/4)
beta_T     = sqrt(T_rel)
W_capture  = 4(1-exp[-beta_T^2]) exp[-beta_T^2]
c_s^2      = beta_T^2 / 3
chi_thermo = chi_MGT * (1 + beta_T)
N_eff      = 4 + 2 exp[-chi_thermo^2]
```

Key result:

```text
shape RMS log residual = 0.302859
shape verdict = PASS-LIKE
native thermodynamic BAO-window peak = 152.29 Mpc
nearest BAO bin = 152.29 Mpc
native thermodynamic global peak = 617.87 Mpc
```

Interpretation:

```text
v0.28 adds a useful no-fit thermodynamic layer and improves native shape scoring.
It does not yet solve the global long-mode failure.
```

Outputs:

```text
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_report.md
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_metrics.csv
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_tracks.csv
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_residuals.csv
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_comparison.png
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_comparison.svg
```

---

## Current strengths and weaknesses from analysis

### Strengths

```text
- Internal anchor radius, cutoff, scale-lock amplitude, and envelope are derived in the toy scaffold.
- Six internal dark sectors can project toward four effective 3D transverse sinks through spin blur.
- Mass/gravity time response and temperature now affect the spin-growth closure.
- MCIFT repeatedly produces a BAO-window scale near the sound-horizon comparison scale.
- v0.28 no-fit thermodynamics improves native shape RMS to 0.303.
```

### Weaknesses

```text
- v0.28 is still a toy/scaffold calculation.
- The 617.87 Mpc global long mode remains a failure.
- The thermodynamic layer is layered onto milestone tracks instead of fully conserved A/V/D/R background dynamics.
- CMB, BBN, lensing, halos, and dark energy behavior are not yet calculated.
```

---

## Next analysis target

```text
v0.29 target:
Self-consistent conserved A/V/D/R background evolution plus no-fit thermodynamic perturbation growth.
```

Required background equations:

```text
d rho_A / d ln a = -Q_A_to_V - Q_A_to_D
d rho_V / d ln a =  Q_A_to_V - Q_V_to_D - Q_V_to_R
d rho_D / d ln a =  Q_A_to_D + Q_V_to_D
d rho_R / d ln a =  Q_V_to_R
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

Run locally:

```bash
python analysis/matter_antimatter_toy_v0.15.py
```

---

## Historical v0.14 CERN two-drill event-shape test

Script:

```text
analysis/cern_two_drill_event_shape_test.py
```

Expected local input files:

```text
analysis/input/data.csv
analysis/input/sm_mc.csv
```

These files are not included by default. They should be generated from ATLAS/CMS open data or local derived ntuples.

---

## Required CSV columns for v0.14 CERN scaffold

Minimum useful columns:

```text
event_id
met
met_phi
jet_pt
jet_phi
```

Optional columns:

```text
weight
n_lep
n_photon
sample
```
