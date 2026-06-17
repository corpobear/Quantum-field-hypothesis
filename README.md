# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy field model  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** 0.15 matter-antimatter channel-geometry toy ratio

> This is not established physics and is not a replacement for quantum field theory. It is a speculative framework being developed into a more testable mathematical toy model.

---

## Current focus

MCIFT models physical reality as a multi-channel information field:

$$
\Psi(x,y,z,t,c)
$$

The current chain is:

```text
coherent information cluster
-> original/shadow knot structure
-> one-point anchor
-> 7/8 free spin-vortex fraction
-> Fibonacci-shaped anchor-tip source
-> Higgs-response resonance overlap
-> funnel-speed capture window
-> bounded fourth-mode reservoir availability
-> channel-specific activation
-> visible-manifest / dark-manifest split
-> collider event-shape comparison
-> antimatter channel-reversed geometry
-> matter-antimatter toy ratio
```

---

## GitHub Actions automation

This repo includes a workflow:

```text
.github/workflows/generate-mechanics-and-analysis.yml
```

It runs the Matplotlib mechanics generator and commits changed SVG figures back into:

```text
mechanics/figures/
```

It also uploads the generated figures as workflow artifacts.

The CERN event-shape analysis runs only when both repo-local input files exist:

```text
analysis/input/data.csv
analysis/input/sm_mc.csv
```

If those files exist, the workflow writes results to:

```text
analysis/results_v0.14/
```

and commits changed results back into the repo. Without those input CSVs, it skips the analysis step and does not invent collider results.

---

## Latest v0.15 matter-antimatter toy ratio

v0.15 defines antimatter as positive-mass channel-reversed geometry, not negative mass.

```text
matter visible drill      = center-tip collector
matter dark sink          = side-belt collector
antimatter dark sink      = Higgs-drop collector
antimatter light drill    = splash-ring collector with discarded middle
```

The reduced toy calculation gives:

$$
\frac{A_M}{A_{\bar M}}=1.28669912372469.
$$

The corresponding asymmetry parameter is:

$$
\epsilon_{MCIFT}=0.125376845930524.
$$

Short verdict:

```text
matter aperture > antimatter aperture in this toy geometry
```

This is an internal toy-model consistency result, not physical confirmation of baryon asymmetry.

Run:

```bash
python analysis/matter_antimatter_toy_v0.15.py
```

---

## v0.14 CERN-facing test

v0.14 maps the two-drill collision picture to collider observables.

```text
visible drill activity -> jets and visible transverse energy
dark side channel -> missing transverse momentum and event imbalance
```

Main proxy:

$$
R_{miss}=\frac{E_T^{miss}}{H_T}.
$$

The published-results comparison uses ATLAS/CMS missing-momentum searches. Existing broad published searches report agreement with Standard Model expectations, so the v0.14/v0.14b verdict is:

```text
not confirmed; constrained by existing missing-momentum searches
```

A local open-data scaffold is provided at:

```text
analysis/cern_two_drill_event_shape_test.py
```

---

## Mechanics reference

The current mechanics are consolidated in:

```text
mechanics/mechanics_v0.13.md
```

Visual diagrams are generated with Matplotlib by running:

```bash
python mechanics/plot_mechanics.py
```

---

## v0.13 dark-manifest finding

v0.13 tests a six-side sink geometry in the eight-sector knot/shadow model.

```text
visible-manifest sector: one axial tip intake
dark-manifest sector: six lateral side intakes
```

The reduced aperture ratio is:

$$
\frac{A_{side}}{A_{tip}}=5.417.
$$

The comparison target from Planck 2018 densities is approximately:

$$
\frac{0.120}{0.0224}=5.357.
$$

This is an internal toy-model consistency result, not an experimental confirmation.

---

## Activation terminology

Use:

```text
light activation = electromagnetic / visibility-channel activation
```

Do not use:

```text
light activation = existence itself
```

Current terms:

```text
unmanifest        no stable visible, mass, or gravitational projection
dark-manifest     mass-active and gravity-active, but light-inactive
visible-manifest  light-active, mass-active, gravity-active, and knot-coherent
```

---

## Key files

```text
.github/workflows/generate-mechanics-and-analysis.yml
analysis/README.md
analysis/matter_antimatter_toy_v0.15.py
analysis/results_v0.15/matter_antimatter_toy_ratio.csv
analysis/cern_two_drill_event_shape_test.py
models/antimatter_channel_geometry_v0.15.md
models/two_drill_collision_cern_v0.14.md
tests/report_v0.15_matter_antimatter_toy_ratio.md
tests/report_v0.14b_published_limits.md
tests/report_v0.14_cern_two_drill_event_shape.md
mechanics/README.md
mechanics/mechanics_v0.13.md
mechanics/plot_mechanics.py
paper/main.md
paper/v0.13_six_side_sink_dark_manifest_addendum.md
models/six_side_sink_dark_manifest_v0.13.md
notes/six_side_sink_dark_manifest.md
tests/report_v0.13.md
tests/README.md
paper/README.md
```

Older model files remain in `models/`, `notes`, `paper/`, and `tests/`.

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
