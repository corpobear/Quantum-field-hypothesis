# v0.49 Model Note

Status: speculative scaffold note.

v0.49 changes v0.48 by feeding the hidden branch back into the rotating core as an extra bound load.

Rules used:

```text
G_visible = E_visible_pool
C_hidden = 1 + 0.45 density_shadow + 0.35 sink_gate + 0.20 hidden_core_retention
G_hidden = C_hidden E_hidden_sink
G_rotation = C_rot E_rotation_bound
G_total = G_visible + G_hidden + G_rotation
```

Core feedback:

```text
R_feedback = R_dense * (1 - radius_tightening_fraction)
I_feedback = (2/5) M_eff R_feedback^2
omega_feedback = L_discarded / I_feedback
Coh_feedback = Coh_aero + hidden_load_gain
pressure_feedback = (core_numerator + hidden_load_pressure) / Coh_feedback
```

Result:

```text
visible-only load = 0.605407
visible + hidden load = 0.776210
visible + hidden + rotation load = 0.884322
total gain over visible-only = 46.07%
pressure after feedback = 0.733320
```
