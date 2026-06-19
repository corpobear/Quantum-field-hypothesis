# Current MCIFT Status: v0.47 Aero Drill-Sink Stabilization Test

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current strict shape-flow test:** v0.47 aero drill-sink stabilization test.  
**Previous rotation test:** v0.46 discarded-vibration rotation test.  
**Previous density test:** v0.45 dense entangled merge strict test.

---

## One-sentence status

```text
MCIFT v0.47 adds a shape-flow rule based on the rotating drill/sink geometry of the merged dense sphere. The rule converts part of the post-rotation core load into shell flow and adds a shape-supported coherence gain. The strict verdict is PASS_AERO_STABILIZED: 19/19 criteria passed. Core pressure drops below capacity and the channel hierarchy remains close to the rough reference.
```

---

## v0.47 strict result

```text
verdict = PASS_AERO_STABILIZED
criteria_pass_count = 19/19
drill_index = 0.676114
sink_intake_index = 0.928600
streamline_index = 0.655629
wake_index = 0.348632
total_aero_bleed = 0.093460
coherence_capacity_before_aero = 0.770210
coherence_capacity_aero = 0.854501
E_core_after_rotation = 0.639429
E_core_after_aero = 0.545969
density_pressure_after_rotation = 0.183042
density_pressure_after_aero = 0.162344
core_pressure_after_aero = 0.828920
final_energy_over_peak = 0.246000
```

Channel fractions:

```text
bb_like     = 0.580984
WZ_like     = 0.244118
gg_like     = 0.107516
tau_like    = 0.064210
gamma_like  = 0.001302
mumu_like   = 0.001870
```

---

## Analysis result files

```text
analysis/results_v0.47/mcift_v0.47_aerodynamic_drill_sink_stabilization_metrics.csv
analysis/results_v0.47/mcift_v0.47_channels_summary.csv
```

The full report, plots, history, and radial profile are in the local output bundle.

---

## Next proof target

```text
v0.48 target:
derive the shape-flow coefficients directly from the full 3D vector phase field and then compute kappa coupling modifiers / partial widths without channel tuning.
```

---

## Safe wording

```text
v0.47 is a scaffold pass: drill/sink shape-flow stabilizes the dense merge in this toy field calculation. It is not detector-level collider evidence.
```
