# Analysis Folder

This folder contains analysis scaffolds for testing MCIFT toy-model predictions against external or derived datasets.

**Status:** speculative analysis tooling; not established physics.

---

## v0.15 matter-antimatter toy ratio

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

## v0.14 CERN two-drill event-shape test

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

## Required CSV columns

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
