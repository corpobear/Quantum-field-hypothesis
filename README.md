# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.60 inverse-timeflow backpropagation retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has an implemented inverse-timeflow retest layer:

```text
v0.59 audit:
  before-implementation benchmark against cosmology and CERN/LHC anchors

v0.60 implementation:
  explicit gamma/Zgamma loop-surface readouts
  explicit cc projection
  inverse-timeflow backpropagation loss
  before/after retest against v0.59
```

Current verdict:

```text
v0.60 = IMPLEMENTED_BACKPROP_IMPROVES_CERN_BRIDGE_RAW_STILL_SCAFFOLD
```

This is an implementation and retest scaffold, not a completed particle or cosmology fit.

---

## v0.60 CERN/LHC result

```text
v0.59 raw BR_L1_vs_SM = 0.092428
v0.60 implemented BR_L1_vs_SM = 0.037697
v0.60 after backprop BR_L1_vs_SM = 0.000938

v0.59 raw max_abs_BR_delta_pct = 100.000000
v0.60 implemented max_abs_BR_delta_pct = 10.502733
v0.60 after backprop max_abs_BR_delta_pct = 0.294487

v0.59 failed_channels_10pct = gg,tau,cc,gamma,Zgamma,mumu
v0.60 implemented failed_channels_10pct = gg
v0.60 after backprop failed_channels_10pct = none
```

Interpretation:

```text
The implementation greatly improves the particle-channel comparison.
The post-backprop result is a trained bridge, not an independent raw prediction.
```

---

## v0.60 cosmology result

```text
v0.59 raw H075_3d = 156.663819
v0.59 transfer H075_3d = 103.897709
v0.60 after timeflow smoothing H075 = 103.897709
v0.60 H075 delta vs reference = 0.064175 percent
```

Interpretation:

```text
The cosmology side remains at transfer/smoothing scaffold level.
Raw 3D cosmology is still not a full pass.
```

---

## Inverse timeflow backpropagation status

```text
forward timeflow/clock formulas: PRESENT
inverse-timeflow backprop loss: IMPLEMENTED
```

The implemented loss is:

```text
observed lab residual -> inverse timeflow loss -> hidden/core correction parameters
```

---

## Analysis result files

```text
CURRENT_STATUS.md
simulations/mcift_v0_60_inverse_timeflow_backprop_retest.py
analysis/results_v0.60/mcift_v0.60_inverse_timeflow_retest_report.md
analysis/results_v0.60/mcift_v0.60_inverse_timeflow_metrics.csv
analysis/results_v0.60/mcift_v0.60_cern_channels_before_after.csv

analysis/results_v0.59/mcift_v0.59_cosmology_cern_retest_report.md
analysis/results_v0.59/mcift_v0.59_cosmology_cern_retest_metrics.csv
```

---

## Important limitation

```text
v0.60 implements and retests the missing inverse-timeflow/channel-readout layer.
The trained bridge result should not be described as a raw first-principle prediction.
Cosmology remains a transfer/smoothing scaffold, not a full raw cosmology pass.
```

---

## Research roadmap

Next required tests:

```text
1. Replace bridge-trained channel corrections with derived 3D dynamics.
2. Derive Q_i smoothing dynamically instead of retaining the v0.59 transfer scaffold.
3. Implement full cosmology observables: H(z), D_M(z), D_H(z), BAO ladder, C_l, and growth.
4. Rerun raw, implemented-readout, and trained-bridge modes separately.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
