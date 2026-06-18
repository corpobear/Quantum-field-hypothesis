# MCIFT v0.45 Dense Entangled Merge Strict Test Report

**Status:** density-amplified entanglement merge test after v0.44; speculative scaffold, not established physics.

## Purpose

v0.45 tests the correction that entanglement does not simply add two masses. The two objects attempt to become one denser object. The merged radius is compressed below the volume-add radius, density amplifies the effective mass-energy, and the rhythm-lock split is applied after density amplification.

## Dense merge rule

```text
R_volume = (R_A^3 + R_B^3)^(1/3)
R_dense = lambda_R R_volume, with lambda_R < 1
rho_ratio = (R_volume / R_dense)^3 = 1 / lambda_R^3
D_rho = 1 + alpha_rho (rho_ratio - 1) + beta_rho (rho_ratio - 1)^2
M_dense = (m_A + m_B) D_rho
E_raw_dense = E_raw_v44 D_rho
E_core_seed = eta_core R_lock E_raw_dense
E_beat_seed = (1 - R_lock) E_raw_dense
explosion_pressure = (E_core_seed + density_pressure) / coherence_capacity
```

## Strict result

```text
verdict = FLOP_DENSITY_DETONATION
criteria_pass_count = 12/16
lambda_R = 0.820000
R_volume = 7.559526
R_dense = 6.198812
rho_ratio = 1.813671
density_gain_D_rho = 1.546828
M_sum = 2.000000
M_dense = 3.093656
coherence_capacity = 0.770210
E_raw_v44 = 1.140500
E_raw_dense = 1.764157
rhythm_lock = 0.892989
E_core_seed_after_density_lock = 1.496605
E_beat_seed = 0.188784
density_pressure = 0.300755
explosion_pressure_0 = 2.333597
max_explode_index = 2.753645
final_energy_over_peak = 0.231836
```

## Shape result

```text
weighted_shell_radius = 9.801101
weighted_shell_width = 3.410000
weighted_sphericity = 0.706000
weighted_anisotropy = 0.294000
core_fraction = 0.589456
inner_fraction = 0.151096
outer_fraction = 0.259448
```

## Channel fractions

```text
bb_like     = 0.348297  target ~ 0.582000
WZ_like     = 0.168978  target ~ 0.240000
gg_like     = 0.353948  target ~ 0.086000
tau_like    = 0.070954  target ~ 0.063000
gamma_like  = 0.050173  target ~ 0.002300
mumu_like   = 0.007651  target ~ 0.000220
```

## Criteria

```text
dense_radius_smaller_than_volume_radius = True
density_ratio_above_one = True
density_amplified_mass_above_sum = True
field_heartbeat_derived = True
rhythm_lock_computed_positive = True
entanglement_score_above_threshold = True
merged_single_dense_sphere_created = True
mass_energy_density_amplified = True
core_pressure_below_capacity = False
density_pressure_below_limit = False
shell_detaches_outside_dense_radius = True
final_energy_not_runaway = True
sphericity_remains_reasonable = True
bb_like_largest = False
WZ_gg_not_dominant_combined = True
gamma_mumu_suppressed = False
```

## Interpretation

```text
The dense-merge correction makes the test much harsher. The merged object becomes smaller and denser than the simple volume-add sphere, so the effective mass-energy is amplified. Under this rule the rhythm-lock split is not enough: the density-amplified core seed plus density pressure exceed coherence capacity, producing a strict density detonation. This supports the user's correction that entanglement/compression is more violent than simple mass addition, but it fails stabilization under the current containment rule.
```

## Limitation

```text
This is a toy density-amplified merge calculation, not a detector-level CERN simulation. A FLOP here means this dense merge rule requires an additional first-principle stabilizer before collider-style claims can be made.
```

## Next target

```text
v0.46 target:
derive a density-responsive coherence capacity or adaptive outward beat-bleed from geometry so compression can stabilize without directly tuning channels.
```
