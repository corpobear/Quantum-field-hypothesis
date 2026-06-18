# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## Current cosmology scaffold: v0.16-v0.22

The current analysis focus is the MCIFT Big Bang / BAO / matter-power-spectrum scaffold.

Important caveat:

```text
These scripts produce toy/scaffold metrics, not observational confirmation.
The v0.22 full-shape pass imports a standard Lambda-CDM-like growth-transfer layer;
it does not yet prove MCIFT independently derives T_growth(k).
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

---

## Latest run: v0.22 growth-transfer scaffold

Run:

```bash
python analysis/mcift_big_bang_growth_transfer_v0.22.py
```

Main equation:

```text
P(k,a) = A_s (k/k_pivot)^n_s T_growth^2(k) T_MCIFT^2(k,a)
```

with:

```text
T_MCIFT(k,a) = 1 + epsilon_lock sin(k r_s) exp[-(k/0.18)^1.4]
epsilon_lock = 0.12 * A_lock(a)
```

Key result:

```text
shape RMS log residual = 0.004
shape verdict = PASS-LIKE
raw MCIFT geometric global peak = 152.29 Mpc
raw MCIFT BAO-window peak = 152.29 Mpc
```

Interpretation:

```text
MCIFT is compatible with a standard growth-transfer layer,
but MCIFT has not yet independently derived that transfer layer.
```

Outputs:

```text
analysis/results_v0.22/mcift_v0.22_growth_transfer_report.md
analysis/results_v0.22/mcift_v0.22_growth_transfer_metrics.csv
analysis/results_v0.22/mcift_v0.22_growth_transfer_residuals.csv
analysis/results_v0.22/mcift_v0.22_growth_transfer_comparison.png
analysis/results_v0.22/mcift_v0.22_growth_transfer_residuals.png
```

---

## Current strengths and weaknesses from analysis

### Strengths

```text
- Internal anchor radius, cutoff, scale-lock amplitude, and envelope are now derived in the toy scaffold.
- MCIFT repeatedly produces a BAO-like geometric scale near the sound-horizon comparison scale.
- The v0.22 scaffold shows MCIFT-derived modulation can sit on top of standard growth-transfer physics cleanly.
```

### Weaknesses

```text
- Raw MCIFT field power failed full P(k) shape scoring in v0.21.
- v0.22 fixes broadband shape by importing an existing transfer layer.
- CMB, BBN, lensing, halos, and dark energy behavior are not yet calculated.
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

Jet lists should be semicolon-separated, for example:

```text
320;91;45
```

---

## Run v0.14 CERN test locally

```bash
python analysis/cern_two_drill_event_shape_test.py \
  --data analysis/input/data.csv \
  --mc analysis/input/sm_mc.csv \
  --out analysis/results_v0.14
```

Outputs:

```text
analysis/results_v0.14/data_vs_mc_summary.csv
analysis/results_v0.14/hist_met_over_ht.png
analysis/results_v0.14/hist_delta_phi_min.png
analysis/results_v0.14/hist_njets.png
```

---

## GitHub Actions behavior

The workflow:

```text
.github/workflows/generate-mechanics-and-analysis.yml
```

always runs the mechanics visual generator.

It runs the CERN event-shape analysis only if both files exist:

```text
analysis/input/data.csv
analysis/input/sm_mc.csv
```

Generated mechanics SVGs are committed back to the repository when they change.

Generated analysis results are also committed back only when input CSVs are present and results change.

Artifacts are uploaded for every workflow run.
