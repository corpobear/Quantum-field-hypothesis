# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.63 dark-visible gravitational width envelope

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has a dark-visible gravitational width-envelope test:

```text
v0.62:
  blind ITF CERN channel prediction gave pass-like branching ratios
  absolute total width remained low

v0.63:
  adds a universal dark-visible gravitational envelope
  overlap is derived from dark / visible / anchor sector geometry
  branching ratios are preserved
  total width is lifted
```

Current verdict:

```text
v0.63 = DV_ENVELOPE_FIXES_WIDTH_BR_RETAINED
```

---

## v0.63 CERN result

Dark-visible overlap rule:

```text
O_DV = 2 sqrt(N_dark N_visible) / (N_dark + N_visible + N_anchor)
E_DV = exp(C_ITF O_DV / (N_visible + N_anchor))
```

Numerical result:

```text
C_ITF = 0.689064
O_DV = 0.612372
E_DV = 1.234890

v0.62 width = 3.325981 MeV
v0.62 width delta = -18.280555 percent

v0.63 width = 4.107221 MeV
v0.63 width delta = +0.914526 percent
```

Branching-ratio result:

```text
v0.62 max channel delta = 8.247649 percent
v0.63 max channel delta = 8.247649 percent
```

Interpretation:

```text
The dark-visible envelope solves the total-width deficit while preserving the blind branching-ratio prediction.
```

---

## Analysis result files

```text
simulations/mcift_v0_63_dark_visible_width_envelope.py
analysis/results_v0.63/mcift_v0.63_width_metrics.csv
analysis/results_v0.63/mcift_v0.63_width_channels.csv
```

---

## Important limitation

```text
v0.63 is still a speculative scaffold. The dark-visible envelope is a first-principle geometry rule, not a proof of new physics.
```

---

## Research roadmap

Next required tests:

```text
1. Apply the same dark-visible envelope to cosmology and check whether it changes H(z) consistently.
2. Test whether the width envelope can be derived from cell-level S_i = Coh_i - q_i instead of sector counts.
3. Retest CERN total width, branching ratios, and signal strengths separately.
4. Keep blind prediction, trained bridge, and calibrated scaffold labels separate.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
