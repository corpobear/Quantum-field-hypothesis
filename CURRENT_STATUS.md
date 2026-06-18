# Current MCIFT Status: v0.42 Entangled Merge-Sphere Strict Test

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current strict PASS/FLOP test:** v0.42 entangled merge-sphere strict test.  
**Previous collision retest:** v0.41 spinning-sphere collision retest.  
**Previous explicit 3D retest:** v0.40 explicit 3D spherical leakage collision test.  
**Previous geometric leakage retest:** v0.39 spherical leakage geometry retest.  
**Current collider comparison layer:** v0.36 CERN/LHC Higgs-sector comparison.

---

## One-sentence status

```text
MCIFT v0.42 tests a strict entanglement-first collision: two particles attempt to become one temporary merged sphere, their masses add, vibration is intensified first, and the merged sphere must either stabilize or explode. The strict verdict is FLOP_EXPLODES: the merge forms, but the mass-energy vibration seed exceeds the merged coherence capacity and the object fails stabilization.
```

---

## v0.42 strict result

```text
verdict = FLOP_EXPLODES
criteria_pass_count = 8/12
entanglement_score = 0.292811
entanglement_threshold = 0.280000
merged_mass = 2.000000
merged_radius = 7.559526
binding_capacity = 0.464809
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

## Math under test

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

## Limitation

```text
v0.42 is a strict toy merge-sphere calculation, not a detector-level CERN simulation. A flop means this specific entanglement/merge rule is unstable, not that the full MCIFT program is falsified.
```

---

## Next proof target

```text
v0.43 target:
find the missing stabilizer term, if one exists, using only first-principle geometry: merged-shell coherence, phase-lock damping, or outward vibration bleed. Do not tune decay channels directly.
```

---

## Safe wording

```text
v0.42 is a useful failure: the entanglement merge forms, but the merged sphere explodes because vibration energy exceeds containment. The next step is to search for a first-principle stabilizer, not to tune the output channels.
```
