# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.28 no-fit thermodynamic spin-growth cosmology scaffold

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model (Lambda-CDM). This repository contains exploratory mechanics, toy calculations, and increasingly testable cosmology-style scaffolds.

---

## Current focus

MCIFT models physical reality as a multi-channel information field:

$$
\Psi(x,y,z,t,c)
$$

where `c` labels internal activation channels such as visibility/light activation, mass/Higgs activation, gravitational projection, knot coherence, exchange, amplitude, radiation-like response, and dark/visible manifestation.

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
-> no-fit thermodynamic spin-growth layer
-> BAO/sound-horizon and full P(k)-shape scoring
```

Earlier mechanics remain in the repository as historical stages: one-point shadow anchor, 7/8 spin-vortex fraction, Fibonacci/Higgs anchor-tip source, six-side dark-manifest sink geometry, collider event-shape scaffold, and matter-antimatter channel-reversed toy geometry.

---

## MCIFT vs standard models, in plain terms

There are two standard models that matter here:

1. **Standard Model of particle physics**: describes known particles and non-gravitational interactions, but does not explain gravity, dark matter, or dark energy.
2. **Lambda-CDM standard cosmology**: describes the observed universe using general relativity, expansion, ordinary matter, radiation, cold dark matter, and dark energy / cosmological constant.

MCIFT is different in goal. It tries to provide a possible internal mechanism for dark/visible structure, anchor-driven coherence, scale selection, and the way internal sector dynamics could project into observable growth channels.

| Question | Lambda-CDM / standard cosmology | MCIFT current scaffold |
|---|---|---|
| Status | Precision-tested standard cosmology | Speculative toy/scaffold |
| Dark matter | Required component, fitted by observation | Candidate dark-manifest channel/sink mechanism |
| Dark energy | Cosmological constant / dark-energy parameter | Not yet derived |
| BAO / sound horizon | Accurately modeled with established perturbation physics | Repeated BAO-window proxy near 152 Mpc |
| Full matter power spectrum | Modeled with Boltzmann/growth solvers | v0.28 no-fit thermodynamic native scaffold reaches PASS-LIKE shape score, but still has global long-mode failure |
| CMB peaks / polarization | Precision-matched | Not yet implemented |
| BBN light elements | Standard early-universe calculation | Not yet implemented |
| Lensing / halo behavior | Well tested in many regimes | Not yet tested |

Safe current statement:

```text
MCIFT now has a no-fit thermodynamic spin-growth scaffold that improves native P(k)-shape scoring and preserves a BAO-window scale, but it has not replaced Lambda-CDM because the global long-mode behavior, CMB, BBN, lensing, halos, and dark energy remain unsolved.
```

---

## Current strengths and weaknesses

### Current strengths

```text
1. MCIFT has moved beyond static visual metaphor into reproducible toy/scaffold calculations.
2. Several previously hand-set knobs are now derived internally or replaced by internal closures:
   - anchor radius R_A
   - cutoff k_cut = 2 pi / R_A
   - scale-lock amplitude A_lock
   - scale-lock envelope R_env = R_A
   - six internal dark sectors from the eight-sector / one-point-anchor rule
   - effective sink count N_eff from spin blur
   - mass/gravity time-response theta_G
   - thermal-radiation fraction theta_T
   - thermodynamic relative temperature T_rel
   - thermal speed beta_T
   - capture window W_capture
   - thermal sound-speed proxy c_s^2
3. The raw geometric MCIFT scale repeatedly lands near a BAO/sound-horizon-like scale.
4. v0.28 improves the native shape RMS to 0.303 without a parameter sweep or fitted thermodynamic constants.
5. The framework gives a concrete place to ask whether dark-manifest behavior can be derived instead of inserted as an unexplained dark-matter component.
```

### Current weaknesses

```text
1. MCIFT is still speculative and not experimentally confirmed.
2. v0.28 is a scaffold, not a CLASS/CAMB/Boltzmann replacement.
3. The native global peak still sits at 617.87 Mpc, so the long-mode / background-conservation problem remains.
4. The thermodynamic layer is no-fit, but still layered on milestone channel snapshots rather than fully evolved conservation equations.
5. CMB temperature/polarization spectra are not implemented.
6. BBN light-element predictions are not implemented.
7. Lensing, halo, galaxy-rotation, and cluster tests are not implemented.
8. Dark energy / late-time acceleration has not yet been derived.
9. A fair parameter-count / likelihood comparison against Lambda-CDM has not yet been performed.
```

---

## Cosmology scaffold status: v0.16 through v0.28

| Version | Purpose | Main outcome | Status |
|---|---|---|---|
| v0.16 | First Big Bang comparison proxies | Visible/dark ratio weak overall; BAO scale failed globally | exploratory |
| v0.17 | Expansion-coupled scale-lock | BAO-window peak near sound horizon; global long mode still failed | partial |
| v0.18 | Long-mode damping / primordial gate | Suppressed the 617 Mpc mode and moved global peak near 152 Mpc | pass-like proxy |
| v0.19 | Anchor-derived cutoff | Derived `k_cut` from anchor radius instead of fitting it | stronger proxy |
| v0.20 | Derived scale-lock amplitude/envelope | Derived remaining scale-lock knobs from channel geometry | strongest raw geometric proxy |
| v0.21 | Full P(k) shape test | Peak stayed pass-like but full shape failed | important failure |
| v0.22 | Growth-transfer compatibility scaffold | Full shape passed after importing standard transfer physics | compatibility pass, not independent derivation |
| v0.23 | Native scalar growth attempt | Removed imported transfer; full shape failed | useful failure |
| v0.24 | Coupled channel-exchange growth | Shape RMS improved to 0.469; BAO-window survived; global long mode failed | weak native pass |
| v0.25 | First-principle six-sink count | Six sectors more fundamental but weaker than four-sink projection | weak |
| v0.26 | Spin-blur projection | Six internal sectors blurred to about four effective sinks; recovered v0.24 behavior | weak |
| v0.27 | Mass-gravity-time spin blur | More conservative time-response model; N_eff ≈ 4.06; RMS 0.482 | weak |
| v0.28 | No-fit thermodynamic spin-growth | RMS 0.303; BAO-window peak preserved; global long mode still failed | PASS-LIKE shape, not full cosmology pass |

Current v0.28 result summary:

```text
thermo_spin_growth_shape_rms_log_residual = 0.302859
shape verdict = PASS-LIKE
native thermodynamic BAO-window peak = 152.29 Mpc
nearest BAO bin = 152.29 Mpc
native thermodynamic global peak = 617.87 Mpc
```

Important caveat:

```text
v0.28 improves native shape scoring without fitting the thermodynamic constants, but it does not solve the global long-mode failure. The next hard test is self-consistent background conservation and growth, not another sink-count adjustment.
```

---

## Key files

```text
analysis/mcift_big_bang_thermo_spin_growth_v0.28.py
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_report.md
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_metrics.csv
analysis/mcift_big_bang_mass_gravity_time_spin_v0.27.py
analysis/mcift_big_bang_spin_blur_v0.26.py
analysis/mcift_big_bang_first_principle_sinks_v0.25.py
analysis/mcift_big_bang_channel_exchange_v0.24.py
analysis/mcift_big_bang_native_growth_v0.23.py
analysis/mcift_big_bang_growth_transfer_v0.22.py
analysis/mcift_big_bang_pk_shape_v0.21.py
analysis/mcift_big_bang_derived_scalelock_v0.20.py
analysis/mcift_big_bang_anchor_cutoff_v0.19.py
analysis/mcift_big_bang_longmode_v0.18.py
analysis/mcift_big_bang_scale_lock_v0.17.py
analysis/mcift_big_bang_comparison_v0.16.py
paper/v0.28_thermodynamic_spin_growth_addendum.md
paper/v0.22_cosmology_comparison_addendum.md
paper/README.md
mechanics/mechanics_v0.13.md
models/six_side_sink_dark_manifest_v0.13.md
models/antimatter_channel_geometry_v0.15.md
```

---

## How to run the latest cosmology scaffold

```bash
python analysis/mcift_big_bang_thermo_spin_growth_v0.28.py
```

Expected outputs:

```text
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_report.md
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_metrics.csv
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_tracks.csv
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_residuals.csv
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_comparison.png
analysis/results_v0.28/mcift_v0.28_thermo_spin_growth_comparison.svg
```

---

## Research roadmap

Next required tests:

```text
1. Replace milestone channel snapshots with self-consistent background conservation:
   d rho_A / d ln a = -Q_A_to_V - Q_A_to_D
   d rho_V / d ln a =  Q_A_to_V - Q_V_to_D - Q_V_to_R
   d rho_D / d ln a =  Q_A_to_D + Q_V_to_D
   d rho_R / d ln a =  Q_V_to_R
2. Re-run thermodynamic growth with conserved channel densities instead of interpolated milestone tracks.
3. Determine whether the 617.87 Mpc global long mode is an artifact of the toy box/spectrum binning or a real MCIFT growth failure.
4. Test dark-manifest behavior against lensing / halo / rotation-curve proxies.
5. Add CMB temperature and polarization spectra.
6. Add BBN light-element predictions.
7. Derive or falsify a dark-energy / late-time acceleration sector.
8. Compare MCIFT and Lambda-CDM with fair parameter-count penalties.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
