# MCIFT v0.49 Dark-Gravity Feedback Model

**Status:** speculative MCIFT scaffold rule; not established physics.

## Purpose

v0.48 separated visible matter from hidden/dark sink matter during entanglement. v0.49 adds the missing gravitational feedback: the hidden sink branch is non-visible but still contributes to the rotating core's gravitational load.

## Rule

Visible matter and hidden sink matter are still computed separately:

```text
visible matter = face/vortex-coupled capture
hidden sink matter = density shadow + sink intake + hidden core retention + rotation capture
```

The new gravitational core load is:

```text
C_sink = 1 + 0.35 sink_gate + 0.25 density_shadow
C_rot = 1 + 0.15 rotation_capture

G_visible = E_visible
G_dark = C_sink E_dark_sink
G_rotation = C_rot E_rotation_bound
G_total = G_visible + G_dark + G_rotation
```

The compact gravitational load then feeds back into the rotating core:

```text
gravity_pressure_add = 0.16 * (G_dark + 0.55 G_rotation)
Coh_grav = Coh_aero + rotational_gravity_support + sink_lensing_support
core_pressure_grav = (E_core + density_pressure + gravity_pressure_add) / Coh_grav
```

## Meaning

Dark/sink matter is not treated as a visible decay-like channel. It becomes a compact non-visible gravity source that changes core pressure, shell binding, and rotational precession.
