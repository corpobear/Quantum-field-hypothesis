# Current MCIFT Status: v1.10 Interwoven Tetrahedral Dynamic Fabric

**Status:** speculative intrinsic tetrahedral geometry and normalized-dynamics scaffold; not established physics.  
**Current layer:** v1.10 interwoven spatial-fabric, shared-curvature, time-stress, and central-source outward-wave benchmark.  
**Previous layer:** v1.09 relational second-cell formation and background-orbit compatibility.  
**Previous physical-mapping layer:** v0.99 CERN/collider mapping from the v0.97 reducer.

## Verdict

```text
INTERWOVEN_TETRAHEDRAL_DYNAMIC_FABRIC_PASS_WITH_NORMALIZED_OUTWARD_WAVE_RESPONSE
```

## What changed in v1.10

v1.10 corrects a sequencing gap in v1.09: the orbit tests assumed a background weak-field space before the tetrahedral model had derived a fabric on which motion could occur.

The current order is:

```text
v1.08 stable tetrahedral cell
v1.09 relational second-cell orientation/mass formation
v1.10 interwoven shared spatial fabric + normalized dynamics
future: motion/orbit/capture on the derived fabric
```

## Interwoven geometry

One tetrahedron consists of four oriented triadic face closures:

```text
partial[0123] = [123] - [023] + [013] - [012]
partial^2[0123] = 0
```

Two tetrahedra sharing one triangular face cancel that face from the combined external boundary.

For face tangent projectors `P_f = I - n_f n_f^T`, define

```text
W = sum_f w_f P_f.
```

Equal regular face weights give

```text
W = (8/3) I
rank = 3
relative isotropy error = 0
```

The representative v1.09 three-strong/one-weak state produces one principal weave axis aligned with the weak-face normal / opposite-apex axis at `0.9999999981`.

## Angular-deficit geometry

Use the intrinsic control

```text
delta_e = 2 pi - sum theta_{T,e}.
```

Regular tetrahedron dihedral angle:

```text
70.5287793655 deg
```

Five regular tetrahedra around one edge:

```text
delta = +7.3561031725 deg
```

Fully coupled equal-loading optimization retains the same regular geometry and deficit rather than self-flattening.

## Loading -> deformation -> deficit

Using the v1.08 free-vertex energy, unequal face-vortex drive changes tetrahedral shape without prescribing deformation.

Representative weak/strong drive ratio `0.93475` gives a `0.677007 deg` split between weak-face-edge and opposite-apex-edge deficit controls.

In the fully coupled five-tetra ring, localized loading changes the common-edge deficit:

```text
0%  -> 7.3561 deg
2%  -> 7.4359 deg
5%  -> 7.5761 deg
10% -> 7.8510 deg
20% -> 8.4865 deg
```

At +10% loading, mean edge response decays with ring distance:

```text
0 -> 3.278%
1 -> 1.545%
2 -> 0.435%
```

## Normalized time stress

Shared edges evolve under

```text
q_e = ln L_e
d2 q_e / dt2 = - partial F / partial q_e
```

with unit edge inertia and no damping.

Five-ring edge-mode spectrum:

```text
positive modes = 16
negative modes = 0
zero intrinsic modes = 0
```

At 1% impulse and 0.05% strain threshold, dominant response appears in topological order:

```text
distance 0: t = 0.15
distance 1: t = 0.30
distance 2: t = 25.375
```

The nonlinear extension remains bounded through normalized impulse `0.40`:

```text
max |Delta ln L| = 0.17506
minimum tetra volume = 6.70396
relative energy band ~= 9.91e-7
```

Tiny analytic oscillator tails mean this does not prove a strict causal cone or physical signal speed.

## Central-source outward-wave test

A separate five-tetra topology consists of one central tetrahedron plus four outer tetrahedra attached to its four faces.

Rigid-body rotation is invisible to intrinsic edge lengths. Therefore the rotational source is represented as a smoothly rotating **internal face-vortex anisotropy** around the v1.09 preferred axis.

### Breathing source

The outer apex edges are not directly driven, yet signed response at the central breathing frequency is:

```text
outer amplitude ~= 0.01691 .. 0.01696
source amplitude = 0.018
gain ~= 0.940 .. 0.942
fit R^2 ~= 0.903
phase lag ~= -0.97 rad
```

The response is approximately isotropic over all four outer tetrahedra.

### Rotating internal anisotropy

Three transverse faces are driven by the rotating pattern while the preferred-axis face has zero transverse drive by construction.

For the driven faces:

```text
outer amplitude ~= 0.00199 .. 0.00208
gain ~= 0.084 .. 0.088
fit R^2 ~= 0.64 .. 0.67
phase relation ~= pi relative to local face drive
```

This is a weaker, directional, phase-structured outward response.

After drive shutoff, undamped post-drive energy bands remain approximately:

```text
breathing: 5.89e-8
rotating:  1.72e-9
combined:  5.87e-8
```

## Strict status

```text
supported internal toy behavior:
    four triadic faces close into one tetrahedral 3-cell
    equal regular layers reconstruct isotropic rank-3 weave
    v1.09 asymmetric face loading produces one intrinsic weave axis
    shared tetrahedral complexes carry angular-deficit geometry
    vortex loading changes shape and angular deficits
    localized loading deforms neighboring cells through shared structure
    undamped shared-edge dynamics are stable across tested impulses
    central breathing emits near-isotropic outward oscillatory response
    rotating internal anisotropy emits weaker directional/phase response

not established:
    physical spacetime emergence
    physical time calibration
    fundamental causal speed or c
    gravity derived from the tetrahedral vortex energy
    physical gravitational waves
    physical mass-curvature calibration
    continuum / large-N limit
    physical orbit/capture on the derived fabric
    physical Higgs tetrahedral microstructure
    black-hole/channel inversion

historical controls only:
    v1.09 weak-field/Newtonian orbit compatibility runs

unchanged:
    v0.97-v0.99 numerical mappings and caveats
```

## Canonical files

```text
models/mcift_v1.10_interwoven_tetrahedral_dynamic_fabric.md
simulations/mcift_v1_10_interwoven_tetrahedral_fabric_benchmark.py
simulations/mcift_v1_10_vortex_loading_to_curvature_benchmark.py
simulations/mcift_v1_10_five_tetra_coupled_fabric_benchmark.py
simulations/mcift_v1_10_five_tetra_time_stress_test.py
simulations/mcift_v1_10_five_tetra_time_stress_extension.py
simulations/mcift_v1_10_central_tetra_wave_emission_phase_test.py
analysis/results_v1.10/
```

## Next

```text
1. Scale to a much larger tetrahedral complex and derive omega(k).
2. Measure long-wavelength group velocity and dispersion without assigning c.
3. Make vortex amplitudes dynamically explicit with derived inertia.
4. Only then return to orbital/capture dynamics on the fabric itself.
```
