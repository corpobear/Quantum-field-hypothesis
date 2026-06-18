# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.32 cube-face Higgs vortex mass mechanism + v0.30 numeric retest

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model (Lambda-CDM). This repository contains exploratory mechanics, toy calculations, and increasingly testable cosmology-style scaffolds.

---

## Current focus

MCIFT models physical reality as a multi-channel information field:

$$
\Psi(x,y,z,t,c)
$$

where `c` labels internal activation channels such as visibility/light activation, mass/Higgs activation, gravitational projection, knot coherence, exchange, amplitude, radiation-like response, collapsed-knot containment, and dark/visible manifestation.

The current conceptual chain is:

```text
multi-channel information field
-> cube-centered knot with six axial connector states
-> Higgs-coupled planes on cube faces
-> information compatibility between neighboring cube centers
-> face-plane vortex formation
-> vortex mass gathering / retained Higgs response
-> contained complexity loading
-> chronological collapse-containment when coherence cannot hold complexity
-> dynamic response-epoch B reservoir
-> BAO/sound-horizon and full P(k)-shape scoring
```

---

## Cube-center six-connector knot geometry

A knot is modeled as the center of a spacetime cube-cell with six axial connector states:

```text
+x, -x, +y, -y, +z, -z
```

Each connector links one cube-center knot to a neighboring cube-center knot and may be inactive, partially active, or fully active:

```text
0 <= a_mu <= 1
```

The six connector states supply local coherence capacity. Collapse-containment occurs when connector-supported coherence cannot contain the knot's internal complexity.

See:

```text
models/cube_center_six_connector_knot_v0.31.md
```

---

## Cube-face Higgs vortex mass mechanism

Each connector crosses a Higgs-coupled face plane:

```text
H_i,mu >= 0
```

A connector becomes mass-active only when the information exchanged between neighboring cube centers is compatible enough:

```text
chi_ij,mu = sqrt(a_i,mu a_j,-mu)
           * P_phase(i,j)
           * P_timing(i,j)
           * P_match(i,j)
```

A face-plane vortex forms when:

```text
chi_ij,mu >= chi_c
```

Vortex strength:

```text
Omega_i,mu = H_i,mu * sigma(chi_ij,mu - chi_c)
```

Mass gathered by the knot:

```text
m_i = m_scale * sum_mu Omega_i,mu * a_i,mu
```

See:

```text
models/cube_face_higgs_vortex_mass_v0.32.md
```

---

## Wording correction

Earlier docs used **"no-fit"** too strongly. The current wording is:

```text
no parameter sweep / internally constrained heuristic closure
```

This means parameters were not swept to match the target, but the closure choices remain model assumptions.

---

## Latest numeric result: v0.30

```text
v0.28 RMS = 0.302859
v0.29 overlay RMS = 0.302859
v0.30 dynamic-ordered RMS = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before dynamic order = 617.87 Mpc
v0.30 global peak after dynamic order = 152.29 Mpc
v0.30 BAO-window peak = 152.29 Mpc
```

---

## Key files

```text
models/cube_face_higgs_vortex_mass_v0.32.md
models/cube_center_six_connector_knot_v0.31.md
analysis/mcift_big_bang_dynamic_ordered_collapse_v0.30.py
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_report.md
analysis/results_v0.30/mcift_v0.30_dynamic_ordered_collapse_metrics.csv
paper/v0.32_cube_face_higgs_vortex_mass_addendum.md
paper/v0.31_cube_center_six_connector_addendum.md
paper/v0.30_dynamic_ordered_collapse_addendum.md
mechanics/mechanics_v0.13.md
models/six_side_sink_dark_manifest_v0.13.md
```

---

## Research roadmap

Next required tests:

```text
1. Use the cube-center six-connector geometry to define connector-level coherence and imbalance.
2. Use the cube-face Higgs vortex mechanism to define mass loading from compatible face-plane vortices.
3. Replace response-epoch B transfer with mode-coupled B(k,a) inside the perturbation equations.
4. Re-run thermodynamic growth with B and vortex mass loading coupled directly to each mode.
5. Test dark-manifest behavior against lensing / halo / rotation-curve proxies.
6. Add CMB temperature and polarization spectra.
7. Add BBN light-element predictions.
8. Compare MCIFT and Lambda-CDM with fair parameter-count penalties.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
