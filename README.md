# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.22 growth-transfer cosmology compatibility scaffold

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model (Lambda-CDM). The current repository contains exploratory mechanics, toy calculations, and increasingly testable cosmology-style scaffolds.

---

## Current focus

MCIFT models physical reality as a multi-channel information field:

$$
\Psi(x,y,z,t,c)
$$

where `c` labels internal activation channels such as visibility/light activation, mass/Higgs activation, gravitational projection, knot coherence, exchange, amplitude, and dark/visible manifestation.

The current cosmology chain is:

```text
multi-channel information field
-> coherent knot/anchor structure
-> visible-manifest and dark-manifest channel split
-> anchor/coherence radius R_A
-> anchor-derived cutoff k_cut = 2 pi / R_A
-> anchor-derived scale-lock amplitude A_lock
-> BAO/sound-horizon scale comparison
-> full P(k) shape test
-> v0.22 compatibility test with standard growth-transfer physics
```

Earlier mechanics remain in the repository as historical stages: one-point shadow anchor, 7/8 spin-vortex fraction, Fibonacci/Higgs anchor-tip source, six-side dark-manifest sink geometry, collider event-shape scaffold, and matter-antimatter channel-reversed toy geometry.

---

## MCIFT vs standard models, in plain terms

There are two standard models that matter here:

1. **Standard Model of particle physics**: describes known particles and non-gravitational interactions, but does not explain gravity, dark matter, or dark energy.
2. **Lambda-CDM standard cosmology**: describes the observed universe using general relativity, expansion, ordinary matter, radiation, cold dark matter, and dark energy / cosmological constant.

MCIFT is different in goal. It tries to provide a possible internal mechanism for dark/visible structure, anchor-driven coherence, and scale selection.

| Question | Lambda-CDM / standard cosmology | MCIFT current scaffold |
|---|---|---|
| Status | Precision-tested standard cosmology | Speculative toy/scaffold |
| Dark matter | Required component, fitted by observation | Candidate dark-manifest channel/sink mechanism |
| Dark energy | Cosmological constant / dark-energy parameter | Not yet derived |
| BAO / sound horizon | Accurately modeled with established perturbation physics | Pass-like proxy and compatibility tests so far |
| Full matter power spectrum | Modeled with Boltzmann/growth solvers | v0.21 failed raw shape; v0.22 passes only after importing standard growth-transfer physics |
| CMB peaks / polarization | Precision-matched | Not yet implemented |
| BBN light elements | Standard early-universe calculation | Not yet implemented |
| Lensing / halo behavior | Well tested in many regimes | Not yet tested |

Safe current statement:

```text
MCIFT may offer a possible mechanism for dark/visible structure and BAO-like scale behavior,
but it has not yet replaced or matched the full predictive scope of Lambda-CDM.
```

---

## Current strengths and weaknesses

### Current strengths

```text
1. MCIFT has moved beyond static visual metaphor into reproducible toy/scaffold calculations.
2. Several previously hand-set knobs are now derived internally:
   - anchor radius R_A
   - cutoff k_cut = 2 pi / R_A
   - scale-lock amplitude A_lock
   - scale-lock envelope R_env = R_A
   - damping exponent p from the four dark-side sinks
3. The raw geometric MCIFT scale repeatedly lands near a BAO/sound-horizon-like scale.
4. The v0.22 scaffold shows MCIFT anchor/acoustic modulation can sit on top of an existing growth-transfer layer without destroying the broadband shape.
5. The framework gives a concrete place to ask whether dark-manifest behavior can be derived instead of inserted as an unexplained dark-matter component.
```

### Current weaknesses

```text
1. MCIFT is still speculative and not experimentally confirmed.
2. The full broadband transfer function is not yet derived from MCIFT; v0.22 imports an existing Lambda-CDM-like growth-transfer layer.
3. The model has not yet produced CMB temperature/polarization spectra.
4. The model has not yet produced BBN light-element predictions.
5. The dark channel has not yet been shown to reproduce lensing, halos, galaxy rotation curves, or cluster-scale behavior.
6. Dark energy / late-time acceleration has not yet been derived.
7. A fair parameter-count / likelihood comparison against Lambda-CDM has not yet been performed.
```

---

## Cosmology scaffold status: v0.16 through v0.22

| Version | Purpose | Main outcome | Status |
|---|---|---|---|
| v0.16 | First Big Bang comparison proxies | Visible/dark ratio weak overall; BAO scale failed globally | exploratory |
| v0.17 | Expansion-coupled scale-lock | BAO-window peak near sound horizon; global long mode still failed | partial |
| v0.18 | Long-mode damping / primordial gate | Suppressed the 617 Mpc mode and moved global peak near 152 Mpc | pass-like proxy |
| v0.19 | Anchor-derived cutoff | Derived `k_cut` from anchor radius instead of fitting it | stronger proxy |
| v0.20 | Derived scale-lock amplitude/envelope | Derived remaining scale-lock knobs from channel geometry | strongest raw geometric proxy |
| v0.21 | Full P(k) shape test | Peak stayed pass-like but full shape failed | important failure |
| v0.22 | Growth-transfer compatibility scaffold | Full shape passed after importing standard transfer physics | compatibility pass, not independent derivation |

Current v0.22 result summary:

```text
raw MCIFT geometric global peak = 152.29 Mpc
raw MCIFT BAO-window peak = 152.29 Mpc
shape RMS log residual after growth-transfer scaffold = 0.004
shape verdict = PASS-LIKE
```

Important caveat:

```text
v0.22 passes the full-shape scaffold by importing an existing Lambda-CDM-like broadband transfer layer.
The next hard test is to derive T_growth(k) from MCIFT channel dynamics rather than importing it.
```

---

## Key files

```text
analysis/mcift_big_bang_growth_transfer_v0.22.py
analysis/results_v0.22/mcift_v0.22_growth_transfer_report.md
analysis/results_v0.22/mcift_v0.22_growth_transfer_metrics.csv
analysis/mcift_big_bang_pk_shape_v0.21.py
analysis/results_v0.21/mcift_v0.21_pk_shape_report.md
analysis/mcift_big_bang_derived_scalelock_v0.20.py
analysis/mcift_big_bang_anchor_cutoff_v0.19.py
analysis/mcift_big_bang_longmode_v0.18.py
analysis/mcift_big_bang_scale_lock_v0.17.py
analysis/mcift_big_bang_comparison_v0.16.py
paper/main.md
paper/v0.22_cosmology_comparison_addendum.md
paper/README.md
mechanics/mechanics_v0.13.md
models/six_side_sink_dark_manifest_v0.13.md
models/antimatter_channel_geometry_v0.15.md
```

---

## How to run the latest cosmology scaffold

```bash
python analysis/mcift_big_bang_growth_transfer_v0.22.py
```

Expected outputs:

```text
analysis/results_v0.22/mcift_v0.22_growth_transfer_metrics.csv
analysis/results_v0.22/mcift_v0.22_growth_transfer_residuals.csv
analysis/results_v0.22/mcift_v0.22_growth_transfer_comparison.png
analysis/results_v0.22/mcift_v0.22_growth_transfer_residuals.png
```

---

## Research roadmap

Next required tests:

```text
1. Derive T_growth(k) from MCIFT channel dynamics instead of importing BBKS/Sugiyama.
2. Add a perturbation-growth equation for delta_m(k,a).
3. Test dark-manifest behavior against lensing / halo / rotation-curve proxies.
4. Add CMB temperature and polarization spectra.
5. Add BBN light-element predictions.
6. Derive or falsify a dark-energy / late-time acceleration sector.
7. Compare MCIFT and Lambda-CDM with fair parameter-count penalties.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
