# MCIFT v0.42 Entangled Merge-Sphere Strict Test Report

**Status:** strict PASS/FLOP entanglement-merge test after v0.41; speculative scaffold, not established physics.

## Purpose

v0.42 tests the stricter idea that two particles do not first bounce like pool balls. Instead, they first attempt to entangle, become one merged sphere, add their masses, intensify vibration, and then either stabilize or explode.

## Merge rule

```text
entanglement_score = overlap_gate * phase_lock * spin_lock * mass_match * timing_match
merge allowed only if entanglement_score >= threshold
M_merge = m_A + m_B
R_merge = (R_A^3 + R_B^3)^(1/3)
I_merge = (2/5) M_merge R_merge^2
E_vib_seed = eta_m M_merge c^2 + eta_c E_dissipated + eta_s E_spin
```

## Strict result

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

## Shape result

```text
weighted_shell_radius = 7.985898
weighted_sphericity = 0.828023
weighted_anisotropy = 0.171977
weighted_core_fraction = 0.475223
weighted_inner_fraction = 0.412373
weighted_outer_fraction = 0.112404
```

## Channel fractions

```text
bb_like     = 0.205855  target ~ 0.582000
WZ_like     = 0.519062  target ~ 0.240000
gg_like     = 0.206559  target ~ 0.086000
tau_like    = 0.053204  target ~ 0.063000
gamma_like  = 0.014296  target ~ 0.002300
mumu_like   = 0.001023  target ~ 0.000220
```

## Criteria

```text
entanglement_score_above_threshold = True
merged_single_sphere_created = True
mass_added_correctly = True
vibration_intensified_first = True
center_stable = True
shell_forms_after_merge = True
sphericity_remains_reasonable = True
explosion_pressure_below_limit = False
final_energy_not_runaway = False
core_retention_not_erased = True
bb_like_largest = False
WZ_like_visible_not_dominant = False
```

## Interpretation

```text
The two particles pass the entanglement threshold and become one temporary merged sphere. The masses add and the vibration is intensified first. But the merged object does not stabilize under the strict containment rule. The mass-energy vibration seed exceeds the merged coherence capacity, the explosion index crosses the allowed limit, and the channel hierarchy is not collider-like. This is a strict FLOP: the entanglement merge forms, then explodes.
```

## Limitation

```text
This is a strict toy merge-sphere calculation, not a detector-level CERN simulation. A flop means this particular entanglement/merge rule is unstable, not that the entire MCIFT program is falsified.
```

## Next target

```text
v0.43 target:
find the missing stabilizer term, if one exists, using only first-principle geometry: merged-shell coherence, phase-lock damping, or outward vibration bleed. Do not tune decay channels directly.
```
