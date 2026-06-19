# Current MCIFT Status: v0.51 Time-Dilation Bridge

**Status:** speculative theoretical framework / toy collider scaffold; not established physics.  
**Current bridge test:** v0.51 time-dilation / kappa-width bridge.  
**Previous bridge test:** v0.50 kappa / width bridge.

---

## One-sentence status

```text
MCIFT v0.51 adds a core-clock-to-lab-clock conversion. Compact rotating-core load and rotation slow the internal clock by a common factor. This can create a total-width/rate-scale mismatch if the internal run is compared directly to lab-frame reference values. Because the factor is common to all visible partial widths, branching ratios remain unchanged.
```

---

## v0.51 result

```text
verdict = PASS_TIME_DILATION_BRIDGE_WITH_COMPENSATION
G_load = 0.874502
R_hidden = 10.582795
R_dense = 6.198812
omega_final = 0.072027
v_core = 0.446482
chi_time = 0.057844
tau_G = 0.970647
tau_rot = 0.894793
tau_core_to_lab = 0.868528
time_slowdown_pct = 13.147198
```

Width bridge:

```text
Gamma_SM_total_MeV = 4.070000
Gamma_lab_uncompensated_MeV = 3.534909
Gamma_lab_uncompensated_delta_pct = -13.147198
universal_kappa_proper_needed = 1.073021
proper_width_scale_needed = 1.151373
Gamma_lab_compensated_MeV = 4.070000
max_abs_BR_delta_pct_compensated = 0.000000
```

---

## Analysis result files

```text
models/time_dilation_kappa_bridge_v0.51.md
analysis/results_v0.51/mcift_v0.51_time_dilation_report.md
analysis/results_v0.51/mcift_v0.51_time_dilation_metrics.csv
analysis/results_v0.51/mcift_v0.51_time_dilation_widths.csv
analysis/results_v0.51/mcift_v0.51_time_dilation_signal_summary.csv
```

The plots are in the local output bundle.

---

## Safe wording

```text
v0.51 is an internal-clock bridge. It is not a full general-relativistic calculation. A common time factor changes total width/rate scale, not branching ratios. Channel-specific time factors would be a separate v0.52 test.
```
