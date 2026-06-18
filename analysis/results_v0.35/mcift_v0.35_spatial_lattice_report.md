# MCIFT v0.35 Minimal Spatial Cubic Lattice Solver Report

**Status:** first spatial lattice toy solver for the v0.33/v0.34 cubic field formulation; speculative scaffold, not established physics.

## Purpose

v0.35 moves beyond the mode-level v0.34 toy solver by instantiating an explicit periodic 3D cubic grid. Each cube-center node evolves with six nearest-neighbor connector activations, Higgs face-plane vortex response, mass/complexity loading, local coherence capacity, stability score, and a spatial reservoir field.

## Spatial setup

```text
lattice size N = 64^3
box scale L = 617.866339 Mpc
six neighbor connectors = +x, -x, +y, -y, +z, -z
```

The initial stress-test field contains a super-anchor domain mode plus the first cubic connector resonance. The solver evolves the field spatially through the MCIFT response epochs before measuring the spectrum.

## Result

```text
v0.34 mode-level RMS = 0.302859
v0.35 spatial-lattice mapped RMS = 0.303948
shape verdict = PASS-LIKE
spatial pre-collapse peak = 617.87 Mpc, harmonic n=1
spatial post-collapse peak = 154.47 Mpc, harmonic n=4
mapped v0.35 global peak = 152.29 Mpc
mapped v0.35 BAO-window peak = 152.29 Mpc
```

## Transfer diagnostics

```text
mapped transfer at 617.87 Mpc = 0.005363
mapped transfer at nearest BAO bin = 0.940620
shell n=1 transfer = 0.005363
shell n=4 transfer = 0.940620
```

## Final lattice diagnostics

```text
B_mean = 0.543947
B_max = 0.571221
negative_S_fraction_final = 1.000000
mean_connector_activation_final = 0.659376
mean_chi_final = 0.649286
mean_omega_final = 0.297983
```

## Interpretation

```text
The spatial lattice solver suppresses the super-anchor n=1 mode and leaves the cubic connector resonance near n=4 as the dominant spatial peak. When this spatial transfer is mapped back onto the existing toy P(k) comparison bins, the global peak remains at the BAO-window scale and the scored shape window remains PASS-LIKE.
```

## Limitation

```text
This is still a toy lattice stress test. The initial field includes a super-anchor domain mode and a cubic connector resonance to test whether the v0.33/v0.34 mechanism can evolve them correctly. It is not yet a full cosmological initial-condition generator or observational likelihood test.
```
