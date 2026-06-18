# MCIFT v0.25 First-Principle Six-Sink Retest Report

**Status:** first-principle sink-count channel-exchange perturbation scaffold; not established physics and not a CLASS/CAMB replacement.  
**Script:** `analysis/mcift_big_bang_first_principle_sinks_v0.25.py`  
**Main change from v0.24:** derives the dark-sink count from the eight-sector / one-point-anchor MCIFT principle instead of inheriting the four-sink 3D Cartesian toy geometry.

## First-principle sink-count derivation

```text
C_3 = 8 sectors
visible axial sector = 1
anchor/opposite axial sector = 1
N_dark_sinks = C_3 - 1 - 1 = 6
damping_power p = N_dark_sinks = 6
```

This is the most basic MCIFT-internal sector-count rule currently available. It differs from the earlier 3D Cartesian side-sink toy, where the dark sinks were placed at `+x, -x, +y, -y`, giving four side sinks.

## Source-math quantities used

```text
A_tip = 0.01977858948
A_side = 0.10714285714
A_side / A_tip = 5.417113
F_visible = A_tip / (A_tip + A_side) = 0.155833
F_dark = A_side / (A_tip + A_side) = 0.844167
N_dark_sinks = 6
```

Derived closure coefficients:

```text
gamma_exchange = (A_side/A_tip) / N_dark_sinks = 0.902852
radiation_drag_strength = 1 / F_visible = 6.417113
radiation_pressure_strength = 2 * (A_side/A_tip) = 10.834226
dark_sink_resistance = A_side/A_tip = 5.417113
```

## Coupled perturbations evolved

```text
delta_A(k,a), delta_V(k,a), delta_D(k,a), delta_R(k,a)
```

with derived exchange channels:

```text
Q_A_to_V ∝ gamma_exchange * F_visible * A_lock * T_anchor * T_lock
Q_A_to_D ∝ gamma_exchange * F_dark * A_lock * T_anchor * T_sink
Q_V_to_D ∝ gamma_exchange * F_dark * T_sink * horizon_inside / (1 + N_dark_sinks)
Q_V_to_R ∝ radiation_drag_strength * F_visible * Omega_R(a) * horizon_inside
```

The model evolution does not import BBKS/Sugiyama or CLASS/CAMB transfer functions. The reference curve is used only for external scoring.

## Result

```text
v0.23 native-growth RMS = 4.148
v0.24 four-sink channel-exchange RMS = 0.469
v0.25 first-principle six-sink RMS = 0.807
shape verdict = WEAK
RMS improvement versus v0.23 = 3.341
```

## Scale diagnostics

```text
raw geometric global peak = 152.29 Mpc
native first-principle six-sink global peak = 617.87 Mpc
native first-principle six-sink BAO-window peak = 128.15 Mpc
nearest BAO bin = 152.29 Mpc
reference scoring peak = 350.21 Mpc
sound horizon r_s = 147.11 Mpc
```

## Slope diagnostics

```text
large-scale slope native = 0.601
large-scale slope reference = -0.729
small-scale slope native = -0.610
small-scale slope reference = -1.814
```

## Interpretation

```text
v0.25 uses the deeper eight-sector MCIFT sink-count principle, so it is more theoretically grounded than the four-sink Cartesian toy assumption.
It still improves strongly over v0.23, but it is weaker than the v0.24 four-sink channel-exchange scaffold.
This means the first-principle six-sink geometry is not enough by itself; the next issue is likely the background channel-conservation law and how six dark sectors project into the 3D cosmology field.
```

## What this tells us

```text
Four was numerically cleaner in the current 3D toy scaffold.
Six is more consistent with the older eight-sector / one-point-anchor source math.
The model must now explain how the six-sector knot geometry projects into 3D cosmological growth.
```

## Next retest target

The next target is a projection/conservation version:

```text
v0.26 = six-sector first-principle background conservation + 3D projection
```

It should evolve:

```text
d rho_A / d ln a = -Q_A_to_V - Q_A_to_D
d rho_V / d ln a =  Q_A_to_V - Q_V_to_D - Q_V_to_R
d rho_D / d ln a =  Q_A_to_D + Q_V_to_D
d rho_R / d ln a =  Q_V_to_R
```

and then test whether six internal dark sectors project into four effective transverse 3D growth channels or remain six independent cosmological sink channels.
