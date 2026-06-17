# Mechanics Figure Index

**Status:** generated-figure index for MCIFT mechanics  
**Generator:** `mechanics/plot_mechanics.py`

Run:

```bash
python mechanics/plot_mechanics.py
```

The GitHub Actions workflow also runs this generator and commits changed SVGs to `mechanics/figures/`.

---

## One graph per mechanic

| Mechanic | Generated SVG |
|---|---|
| Mechanics overview | `figures/mechanics_overview.svg` |
| Channel-specific activation | `figures/activation_channels.svg` |
| Light-channel gate | `figures/light_activation_gate.svg` |
| Complexity growth | `figures/complexity_growth.svg` |
| Stability modes / failed fourth mode | `figures/stability_modes.svg` |
| Fractal catching surface | `figures/fractal_surface.svg` |
| Finite Higgs-response window | `figures/higgs_response_window.svg` |
| Exchange alignment | `figures/exchange_alignment.svg` |
| Exchange densification | `figures/exchange_densification.svg` |
| Amplitude-first mass | `figures/amplitude_mass.svg` |
| Shadow amplitude correction | `figures/shadow_correction.svg` |
| One-point anchor contact count | `figures/anchor_contacts.svg` |
| Spin-vortex free fraction | `figures/spin_vortex_fraction.svg` |
| Fibonacci-Higgs resonance | `figures/fibonacci_resonance.svg` |
| Funnel-speed capture window | `figures/capture_window.svg` |
| Bounded fourth-mode reservoir gate | `figures/reservoir_gate.svg` |
| Field-source pipeline | `figures/field_source_pipeline.svg` |
| Source-term aperture comparison | `figures/source_terms_bar.svg` |
| Motion by directional exchange | `figures/motion_exchange.svg` |
| Entanglement / shared-channel strength | `figures/entanglement_shared_channel.svg` |
| High-complexity confinement proxy | `figures/confinement_complexity.svg` |
| Eight-sector sink geometry | `figures/eight_sector_sink_geometry.svg` |
| Dark-visible ratio comparison | `figures/dark_visible_ratio.svg` |
| CERN two-drill event proxy | `figures/cern_event_proxy.svg` |

---

## Notes

The figures are schematic toy-model visualizations. They are meant to make the current mechanics easier to inspect and debug. They are not experimental evidence and should not be read as established physical results.

The workflow can commit the generated SVGs back into the repository. If a generated output push races with another update, the workflow now fetches and rebases before pushing.
