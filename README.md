# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.61 first-principle inverse-timeflow cosmology retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has a cosmology-specific inverse-timeflow retest layer:

```text
v0.60:
  inverse-timeflow backpropagation improved the particle/channel bridge
  cosmology still used transfer/smoothing scaffold

v0.61:
  inverse-timeflow acts inside the expansion rule
  tau_ITF is derived from six-sink / visible / anchor sector stress
  H_lab = tau_ITF * H_core
```

Current verdict:

```text
v0.61 = FIRST_PRINCIPLE_ITF_IMPROVES_RAW_HZ_NOT_FULL_COSMOLOGY_PASS
```

---

## v0.61 cosmology result

```text
C_ITF = 0.689064
tau_ITF = 0.708552

v0.59 raw H075_3d = 156.663819
v0.59 raw delta vs LCDM = +50.883364 percent

v0.60 transfer H075_3d = 103.897709
v0.60 transfer delta vs LCDM = +0.064175 percent

v0.61 first-principle ITF H075 = 111.004443
v0.61 first-principle ITF delta vs LCDM = +6.908691 percent
v0.61 residual vs compact CC point = +0.558221 sigma
```

Interpretation:

```text
v0.61 improves raw over-expansion by about 7.36x without using reference-derived smoothing.
It is not yet a full cosmology pass.
```

---

## Analysis result files

```text
simulations/mcift_v0_61_first_principle_cosmology_itf.py
analysis/results_v0.61/mcift_v0.61_first_principle_cosmology_metrics.csv
analysis/results_v0.61/mcift_v0.61_Hz_comparison.csv

simulations/mcift_v0_60_inverse_timeflow_backprop_retest.py
analysis/results_v0.60/mcift_v0.60_inverse_timeflow_metrics.csv
```

---

## Important limitation

```text
v0.61 improves the raw H(z=0.75) over-expansion, but does not implement the full BAO ladder, CMB spectra, growth data, or BBN.
```

---

## Research roadmap

Next required tests:

```text
1. Make C_ITF redshift-dependent from actual 3D field cells.
2. Use C_ITF(a) from cell containment stress S_i = Coh_i - q_i.
3. Add distance observables D_M(z), D_H(z), and BAO ladder scoring.
4. Add growth and CMB-spectrum comparisons.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
