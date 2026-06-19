# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.62 blind inverse-timeflow CERN channel test

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now has a blind CERN-channel inverse-timeflow test:

```text
v0.60:
  inverse-timeflow backpropagation produced a trained particle/channel bridge

v0.61:
  first-principle inverse-timeflow improved raw cosmology H(z)

v0.62:
  applies the v0.61-style first-principle ITF rule to CERN channels
  no backpropagation
  no target loss
  no learned hidden channel correction
```

Current verdict:

```text
v0.62 = BLIND_ITF_BR_PASS_LIKE_TOTAL_WIDTH_LOW
```

---

## v0.62 CERN channel result

```text
C_ITF = 0.689064

v0.60 implemented-before-backprop max_abs_BR_delta_pct = 10.502733
v0.62 blind ITF max_abs_BR_delta_pct = 8.247649

v0.60 implemented-before-backprop failed channel = gg
v0.62 blind ITF failed channels = none
```

Width result:

```text
v0.62 blind total width = 3.325981 MeV
v0.62 blind total width delta vs 4.07 MeV = -18.280555 percent
```

Interpretation:

```text
Branching ratios improve without backpropagation.
Absolute total width is low without an additional first-principle envelope rule.
```

---

## Analysis result files

```text
simulations/mcift_v0_62_blind_cern_itf_prediction.py
analysis/results_v0.62/mcift_v0.62_blind_itf_metrics.csv
analysis/results_v0.62/mcift_v0.62_blind_itf_channels.csv
```

---

## Important limitation

```text
v0.62 is a blind branching-ratio prediction attempt, not a trained fit.
It passes the compact 10 percent branching-ratio criterion, but the absolute width envelope is still underdeveloped.
```

---

## Research roadmap

Next required tests:

```text
1. Add a first-principle width-envelope rule.
2. Test whether the same envelope also improves cosmology without target-derived smoothing.
3. Retest CERN branching ratios and total width separately.
4. Keep blind prediction, trained bridge, and calibrated scaffold labels separate.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
