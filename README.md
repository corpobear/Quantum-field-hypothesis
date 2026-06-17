# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy field model  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** 0.14 CERN two-drill event-shape comparison

> This is not established physics and is not a replacement for quantum field theory. It is a speculative framework being developed into a more testable mathematical toy model.

---

## Current focus

MCIFT models physical reality as a multi-channel information field:

```math
\Psi(x,y,z,t,c)
```

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
```

---

## Latest v0.14 CERN-facing test

v0.14 maps the two-drill collision picture to collider observables.

```text
visible drill activity -> jets and visible transverse energy
dark side channel -> missing transverse momentum and event imbalance
```

Main proxy:

```math
R_{miss}=\frac{E_T^{miss}}{H_T}.
```

The first published-results comparison uses ATLAS monojet and multijet missing-momentum searches. Existing broad published searches report agreement with Standard Model expectations, so the v0.14 verdict is:

```text
not confirmed, not ruled out by this reduced comparison, now constrained
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

```math
\frac{A_{side}}{A_{tip}}=5.417.
```

The comparison target from Planck 2018 densities is approximately:

```math
\frac{0.120}{0.0224}=5.357.
```

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
analysis/cern_two_drill_event_shape_test.py
models/two_drill_collision_cern_v0.14.md
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

Older model files remain in `models/`, `notes/`, `paper/`, and `tests/`.

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
