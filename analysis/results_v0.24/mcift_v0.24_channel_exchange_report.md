# MCIFT v0.24 Derived Channel-Exchange Retest Report

**Status:** derived channel-exchange perturbation scaffold; not established physics and not a CLASS/CAMB replacement.  
**Script:** `analysis/mcift_big_bang_channel_exchange_v0.24.py`  
**Main change from v0.23:** replaces one scalar native-growth closure with coupled A/V/D/R perturbations and exchange terms derived from MCIFT source-aperture math.

## Source-math quantities used

```text
A_tip = 0.01977858948
A_side = 0.10714285710
A_side / A_tip = 5.417113
F_visible = A_tip / (A_tip + A_side) = 0.155833
F_dark = A_side / (A_tip + A_side) = 0.844167
N_dark_sinks = 4
```

Derived closure coefficients:

```text
gamma_exchange = (A_side/A_tip) / N_dark_sinks = 1.354278
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
v0.24 channel-exchange RMS = 0.469
shape verdict = WEAK
RMS improvement = 3.679
```

## Scale diagnostics

```text
raw geometric global peak = 152.29 Mpc
native channel-exchange global peak = 617.87 Mpc
native channel-exchange BAO-window peak = 152.29 Mpc
nearest BAO bin = 152.29 Mpc
reference scoring peak = 350.21 Mpc
sound horizon r_s = 147.11 Mpc
```

## Slope diagnostics

```text
large-scale slope native = 0.418
large-scale slope reference = -0.729
small-scale slope native = -1.046
small-scale slope reference = -1.814
```

## Interpretation

```text
v0.24 improves the full P(k) shape substantially versus v0.23 without importing a standard transfer curve into the model.
The result is still not a full pass: it is WEAK, not PASS-LIKE.
The BAO/sound-horizon-adjacent structure survives, but the native growth peak shifts relative to the raw 152 Mpc geometric peak.
```

## Next retest target

The next equation target is to convert the derived exchange closure into a stricter conservation-law system for the background and perturbations:

```text
d rho_A / d ln a = -Q_A_to_V - Q_A_to_D
d rho_V / d ln a =  Q_A_to_V - Q_V_to_D - Q_V_to_R
d rho_D / d ln a =  Q_A_to_D + Q_V_to_D
d rho_R / d ln a =  Q_V_to_R
```

and then evolve the perturbations using those self-consistent background densities rather than interpolated milestone channel tracks.
