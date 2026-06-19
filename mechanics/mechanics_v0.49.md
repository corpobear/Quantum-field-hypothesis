# MCIFT Mechanics v0.49: Dense Entanglement, Shape Flow, and Hidden Core Load

**Status:** speculative toy mechanics; not established physics.

## 1. Dense entanglement compression

Two entangling objects are not simply added. In this scaffold they compress into a denser merged object:

```text
R_volume = (R_A^3 + R_B^3)^(1/3)
R_dense = lambda_R * R_volume
rho_ratio = (R_volume / R_dense)^3
M_dense = (m_A + m_B) * D_rho
```

## 2. Rhythm lock

The two pre-merge rhythms combine into a single heartbeat:

```text
Z = A_A exp(i phi_A) + A_B exp(i phi_B)
A_merge = |Z|
phi_merge = arg(Z)
omega_merge = weighted average of source rhythms
R_lock = phase_lock * frequency_lock * amplitude_match
```

The lock separates core-retained vibration from discarded vibration:

```text
E_core = eta_core * R_lock * E_raw
E_discarded = (1 - R_lock) * E_raw
```

## 3. Discarded vibration becomes rotation

The discarded vibration carries angular mismatch and becomes angular impulse:

```text
I_dense = (2/5) * M_dense * R_dense^2
L_discarded = sqrt(2 * I_dense * E_rotation)
omega_final = L_discarded / I_dense
```

## 4. Drill/sink shape-flow stabilization

The rotating dense shape has a drill/sink flow:

```text
drill_index = omega_final * R_shell
sink_intake_index = core_fraction * rho_ratio
streamline_index = sphericity / (1 + anisotropy)
wake_index = anisotropy * (1 + drill_index)
```

Shape-flow bleeds part of the core load into shell flow and raises coherence support:

```text
E_core_after_shape = E_core_after_rotation - E_shape_bleed
Coh_shape = Coh_base + coherence_lift_gain
P_core_shape = (E_core_after_shape + density_pressure_after_shape) / Coh_shape
```

## 5. Visible / hidden split

The visible branch is computed from face/vortex capture:

```text
visible_capture_gate = face_visibility * vortex_capture_visibility
```

The hidden branch is computed separately:

```text
sink_gate = sigmoid((sink_intake_index - streamline_index) / width)
hidden_capture_gate = sink_gate * (density_shadow + hidden_core_retention + rotation_capture)
```

The hidden branch is not added to visible channels.

## 6. Hidden core-load feedback

The hidden branch still contributes local rotating-core load:

```text
G_visible = E_visible_pool
G_hidden = C_sink * E_hidden_sink
G_rot = xi_rot * E_rotation_bound
G_load = G_visible + G_hidden + G_rot
```

The feedback changes both capacity and pressure:

```text
capacity_after_feedback = capacity_before_feedback + confinement_gain
core_load_after_feedback = core_load_before_feedback + pressure_penalty
core_pressure_after_feedback = core_load_after_feedback / capacity_after_feedback
```

## 7. v0.49 checkpoint

```text
PASS_CORE_LOAD_FEEDBACK = 18/18 criteria
load_strength_vs_visible = 1.444487
core_pressure_after_feedback = 0.717440
```

## 8. Figures

See:

```text
mechanics/figures/dense_entanglement_compression.svg
mechanics/figures/discarded_vibration_rotation.svg
mechanics/figures/aero_drill_sink_shape_flow.svg
mechanics/figures/visible_hidden_split_geometry.svg
mechanics/figures/hidden_core_load_feedback.svg
```
