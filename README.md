# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.42 entangled merge-sphere strict test

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

MCIFT now tests a strict entanglement-first collision:

```text
two particles attempt to entangle
if entanglement score passes threshold, they become one temporary sphere
masses add into the merged object
vibration is intensified first
merged sphere either stabilizes or explodes
```

Verdict:

```text
v0.42 entangled merge-sphere strict test = FLOP_EXPLODES, 8/12 criteria
```

This is a useful failure, not a cosmetic pass. The merge forms, but the mass-energy vibration seed exceeds the merged coherence capacity.

---

## v0.42 result

```text
entanglement_score = 0.292811
entanglement_threshold = 0.280000
merged_mass = 2.000000
merged_radius = 7.559526
coherence_capacity = 0.526780
E_mass_added = 0.500000
E_vib_seed = 1.139518
explosion_pressure_0 = 2.163178
max_explode_index = 3.544722
```

Shape result:

```text
weighted_shell_radius = 7.985898
weighted_sphericity = 0.828023
weighted_anisotropy = 0.171977
weighted_core_fraction = 0.475223
weighted_inner_fraction = 0.412373
weighted_outer_fraction = 0.112404
```

Channel fractions:

```text
bb_like     = 0.205855  target ~ 0.582000
WZ_like     = 0.519062  target ~ 0.240000
gg_like     = 0.206559  target ~ 0.086000
tau_like    = 0.053204  target ~ 0.063000
gamma_like  = 0.014296  target ~ 0.002300
mumu_like   = 0.001023  target ~ 0.000220
```

---

## Key math

```text
entanglement_score = overlap_gate * phase_lock * spin_lock * mass_match * timing_match
merge allowed only if entanglement_score >= threshold
M_merge = m_A + m_B
R_merge = (R_A^3 + R_B^3)^(1/3)
I_merge = (2/5) M_merge R_merge^2
E_vib_seed = eta_m M_merge c^2 + eta_c E_dissipated + eta_s E_spin
explosion_pressure = E_vib_seed / coherence_capacity
```

---

## Analysis result files

```text
analysis/results_v0.42/mcift_v0.42_entangled_merge_sphere_report.md
analysis/results_v0.42/mcift_v0.42_entangled_merge_sphere_metrics_summary.csv
analysis/results_v0.42/mcift_v0.42_entangled_merge_sphere_channels.csv
```

---

## Important limitation

```text
v0.42 is a strict toy merge-sphere calculation, not a detector-level CERN simulation. A flop means this specific entanglement/merge rule is unstable, not that the full MCIFT program is falsified.
```

---

## Research roadmap

Next required tests:

```text
1. Search for a first-principle stabilizer term: merged-shell coherence, phase-lock damping, or outward vibration bleed.
2. Do not tune decay channels directly.
3. Retest stability before comparing channels.
4. Only after stability should the model derive coupling modifiers and collider observables.
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
