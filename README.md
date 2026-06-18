# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.30 dynamic ordered collapse-containment cosmology scaffold

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model (Lambda-CDM). This repository contains exploratory mechanics, toy calculations, and increasingly testable cosmology-style scaffolds.

---

## Current focus

MCIFT models physical reality as a multi-channel information field:

$$
\Psi(x,y,z,t,c)
$$

where `c` labels internal activation channels such as visibility/light activation, mass/Higgs activation, gravitational projection, knot coherence, exchange, amplitude, radiation-like response, collapsed-knot containment, and dark/visible manifestation.

The current cosmology chain is:

```text
multi-channel information field
-> coherent knot/anchor structure
-> visible-manifest and dark-manifest channel split
-> anchor/coherence radius R_A
-> anchor-derived cutoff k_cut = 2 pi / R_A
-> anchor-derived scale-lock amplitude A_lock
-> native channel-exchange perturbation growth
-> six internal dark sectors
-> spin-blur projection toward four effective 3D transverse sinks
-> mass/gravity time-response correction
-> thermodynamic spin-growth layer
-> chronological collapse-containment when coherence cannot hold complexity
-> dynamic response-epoch B reservoir
-> BAO/sound-horizon and full P(k)-shape scoring
```

---

## Wording correction

Earlier docs used **"no-fit"** too strongly. The current wording is:

```text
no parameter sweep / internally constrained heuristic closure
```

This means parameters were not swept to match the target, but the closure choices remain model assumptions. They are not observationally fitted constants and not first-principle proof.

---

## MCIFT vs standard models, in plain terms

There are two standard models that matter here:

1. **Standard Model of particle physics**: describes known particles and non-gravitational interactions, but does not explain gravity, dark matter, or dark energy.
2. **Lambda-CDM standard cosmology**: describes the observed universe using general relativity, expansion, ordinary matter, radiation, cold dark matter, and dark energy / cosmological constant.

MCIFT is different in goal. It tries to provide a possible internal mechanism for dark/visible structure, anchor-driven coherence, scale selection, thermodynamic capture, and collapse-containment of uncontained complexity.

Safe current statement:

```text
MCIFT v0.30 applies collapse-containment in chronological response-epoch order. The prior 617.87 Mpc global peak is suppressed before final scoring and the global peak returns to 152.29 Mpc, while the scored shape RMS remains PASS-LIKE. This is still a speculative scaffold and not a Lambda-CDM replacement.
```

---

## Latest v0.30 result

```text
v0.28 RMS = 0.302859
v0.29 overlay RMS = 0.302859
v0.30 dynamic-ordered RMS = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before dynamic order = 617.87 Mpc
v0.30 global peak after dynamic order = 152.29 Mpc
v0.30 BAO-window peak = 152.29 Mpc
```

Dynamic background at 5B:

```text
A_bg = 0.891174
V_bg = 0.048089
D_bg = 0.047217
R_bg = 0.010379
B_bg = 0.003141
```

---

## Cosmology scaffold status: v0.16 through v0.30

| Version | Purpose | Main outcome | Status |
|---|---|---|---|
| v0.16 | First Big Bang comparison proxies | Visible/dark ratio weak overall; BAO scale failed globally | exploratory |
| v0.17 | Expansion-coupled scale-lock | BAO-window peak near sound horizon; global long mode still failed | partial |
| v0.18 | Long-mode damping / primordial gate | Suppressed the 617 Mpc mode and moved global peak near 152 Mpc | pass-like proxy |
| v0.19 | Anchor-derived cutoff | Derived `k_cut` from anchor radius instead of fitting it | stronger proxy |
| v0.20 | Derived scale-lock amplitude/envelope | Derived remaining scale-lock knobs from channel geometry | raw geometric proxy |
| v0.21 | Full P(k) shape test | Peak stayed pass-like but full shape failed | important failure |
| v0.22 | Growth-transfer compatibility scaffold | Full shape passed after importing standard transfer physics | compatibility pass, not independent derivation |
| v0.23 | Native scalar growth attempt | Removed imported transfer; full shape failed | useful failure |
| v0.24 | Coupled channel-exchange growth | Shape RMS improved to 0.469; BAO-window survived; global long mode failed | weak native pass |
| v0.25 | First-principle six-sink count | Six sectors more fundamental but weaker than four-sink projection | weak |
| v0.26 | Spin-blur projection | Six internal sectors blurred to about four effective sinks | weak |
| v0.27 | Mass-gravity-time spin blur | Conservative time-response model; RMS 0.482 | weak |
| v0.28 | Thermodynamic spin-growth | RMS 0.303; BAO-window peak preserved; global mode remained 617.87 Mpc | PASS-LIKE shape, global failure |
| v0.29 | Collapse-containment overlay | Post-run overlay moved global peak from 617.87 Mpc to 152.29 Mpc | PASS-LIKE overlay |
| v0.30 | Dynamic ordered collapse | Response-epoch B reservoir suppresses 617.87 Mpc before final scoring | PASS-LIKE scaffold |

---

## Key files

```text
analysis/mcift_big_bang_dynamic_ordered_collapse_v0.30.py
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_report.md
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_metrics.csv
analysis/mcift_big_bang_collapse_containment_v0.29.py
analysis/mcift_big_bang_thermo_spin_growth_v0.28.py
paper/v0.30_dynamic_ordered_collapse_addendum.md
paper/v0.29_collapse_containment_addendum.md
paper/v0.28_thermodynamic_spin_growth_addendum.md
mechanics/mechanics_v0.13.md
models/six_side_sink_dark_manifest_v0.13.md
```

---

## How to run the latest cosmology scaffold

After generating the full v0.28 residuals/tracks:

```bash
python analysis/mcift_big_bang_dynamic_ordered_collapse_v0.30.py
```

Expected outputs:

```text
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_report.md
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_metrics.csv
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_background.csv
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_residuals.csv
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_comparison.png
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_comparison.svg
```

---

## Research roadmap

Next required tests:

```text
1. Replace response-epoch B transfer with mode-coupled B(k,a) inside the perturbation equations.
2. Re-run thermodynamic growth with B coupled directly to each mode.
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
