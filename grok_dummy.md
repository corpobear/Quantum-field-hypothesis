# MCIFT Earth–Mars Feb/Mar/Apr 2027 Mission Comparison Methodology

## 0. Purpose

This document describes the step-by-step proxy process used to calculate and draw the Earth-to-Mars comparison graph with three routes:

1. Traditional orbital route
2. MCIFT dive below gravitational-wave path
3. MCIFT wave-rider path

Graph window:

```text
2027-02-01 00:00 UTC → 2027-04-30 00:00 UTC
```

Launch time for all three paths:

```text
launch_time = 2027-02-01 00:00 UTC
```

---

# 1. Base Planet Position Layer

## 1.1 Define time range

```text
t_start = 2027-02-01 00:00 UTC
t_end   = 2027-04-30 00:00 UTC
```

Total graph duration:

```text
T_total = 88 days
```

For each frame:

```text
t_i = t_start + i * Δt
```

where `i` is the frame index.

## 1.2 Calculate Earth and Mars positions

Use heliocentric 2D orbital positions:

```text
Earth(t) = [x_E(t), y_E(t)]
Mars(t)  = [x_M(t), y_M(t)]
```

These become the base map:

```text
Earth_trajectory = {Earth(t_i)}
Mars_trajectory  = {Mars(t_i)}
```

In the graph:

```text
Earth trajectory = blue
Mars trajectory  = orange/red
```

---

# 2. MCIFT Version Used

## 2.1 MCIFT version

```text
MCIFT version used = v0.97 Threefold Reducer
```

This version uses a threefold surface field modulation.

## 2.2 Main MCIFT v0.97 formula

The reducer formula is:

```text
r0(n,t) = c Δt ρ0(r) A3(n)
```

where:

```text
r0(n,t) = reduced field radius / activation at direction n and time t
c       = propagation constant
Δt      = timestep
ρ0(r)   = radial core density function
A3(n)   = threefold angular activation
```

## 2.3 Threefold angular activation

```text
A3(θ,φ) = 1 + ε3 sin²(θ) cos(3φ + ψ3)
```

where:

```text
θ  = polar angle
φ  = azimuth angle
ε3 = threefold modulation strength
ψ3 = phase offset
```

## 2.4 Repo settings used

```text
M0        = 2
alpha_M   = 0.05
r_core    = 1
epsilon_3 = 0.125
psi_3     = 0
shells    = 1..10
```

So the exact angular activation used is:

```text
A3(θ,φ) = 1 + 0.125 sin²(θ) cos(3φ)
```

---

# 3. MCIFT Reducer Outputs Used

From MCIFT v0.97, use the exported reducer values:

```text
mean_A3             = 1.000000000000
A3_min              = 0.875042834378
A3_max              = 1.124957165622
A3_std              = 0.064549317306
mean_D3             = 0.009817928223
mean_shear_proxy    = 0.063915576742
mean_threefold_amp  = 0.247460690278
mean_abs_lc_resid   = 0.054439708131
mean_null_resid     = 0.015243226439
H_proxy_relative    = 0.977215138494
global_anisotropy   = 0.351925814364
```

Loop-balance value:

```text
beta4_needed_for_balance = 0.170868625373
```

---

# 4. Build the MCIFT Field Fabric

## 4.1 Sun as central load

Set the Sun as the central source:

```text
Sun = central_load
```

The Sun generates the base radial field:

```text
ρ0(r) = exp(-r² / r_core²)
```

Using:

```text
r_core = 1
```

so:

```text
ρ0(r) = exp(-r²)
```

## 4.2 Build shell bands

For each shell:

```text
shell_index k = 1..10
```

create shell radius:

```text
R_shell(k) = k * shell_spacing
```

Each shell is modulated by the v0.97 threefold activation:

```text
Shell(k,θ,φ) = R_shell(k) * A3(θ,φ)
```

Expanded:

```text
Shell(k,θ,φ) = R_shell(k) * [1 + 0.125 sin²(θ) cos(3φ)]
```

## 4.3 Build fabric height / wave surface

The field fabric height is:

```text
F(r,θ,φ) = ρ0(r) * A3(θ,φ)
```

Expanded:

```text
F(r,θ,φ) = exp(-r²) * [1 + 0.125 sin²(θ) cos(3φ)]
```

Add shear response:

```text
F_shear(r,θ,φ) = F(r,θ,φ) + mean_shear_proxy * A3(θ,φ)
```

Using:

```text
mean_shear_proxy = 0.063915576742
```

therefore:

```text
F_shear(r,θ,φ)
=
exp(-r²) * [1 + 0.125 sin²(θ) cos(3φ)]
+
0.063915576742 * [1 + 0.125 sin²(θ) cos(3φ)]
```

---

# 5. Build the Gravitational-Wave Crest Path

## 5.1 Define crest path

The gravitational-wave crest path is the high-shear ridge of the MCIFT fabric.

```text
GW_crest(t) = BaseShell(t) + mean_shear_proxy * A3(θ,φ)
```

Expanded:

```text
GW_crest(t)
=
BaseShell(t)
+
0.063915576742 * [1 + 0.125 sin²(θ) cos(3φ)]
```

This becomes the dashed cyan wave-crest line in the graph.

---

# 6. Mission Path 1 — Traditional Orbital Route

## 6.1 Define arrival

```text
arrival_traditional = 2027-04-30 00:00 UTC
```

Travel time:

```text
T_traditional = arrival_traditional - launch_time
T_traditional = 88 days
```

## 6.2 Define normalized path parameter

```text
s = (t - launch_time) / T_traditional
```

So:

```text
s = 0 at launch
s = 1 at arrival
```

## 6.3 Calculate traditional transfer path

The traditional route is a smooth orbital arc from Earth at launch to Mars at arrival:

```text
P_traditional(s)
=
(1 - s) * Earth(launch_time)
+
s * Mars(arrival_traditional)
+
orbital_arc_lift(s)
```

The orbital arc lift is:

```text
orbital_arc_lift(s) = K_orbit * sin(πs)
```

So:

```text
P_traditional(s)
=
(1 - s) * Earth(launch_time)
+
s * Mars(arrival_traditional)
+
K_orbit * sin(πs)
```

In the graph:

```text
traditional route color = yellow/orange
traditional arrival     = 2027-04-30 00:00 UTC
traditional travel time = 88 days
```

---

# 7. Mission Path 2 — MCIFT Dive Below GW Path

## 7.1 Define arrival

```text
arrival_dive = 2027-03-31 00:00 UTC
```

Travel time:

```text
T_dive = arrival_dive - launch_time
T_dive = 58 days
```

## 7.2 Define normalized path parameter

```text
s = (t - launch_time) / T_dive
```

## 7.3 Calculate MCIFT dive factor

The dive factor uses the v0.97 threefold amplitude plus shear proxy:

```text
D_dive = mean_threefold_amp + mean_shear_proxy
```

Substitute values:

```text
D_dive = 0.247460690278 + 0.063915576742
```

Result:

```text
D_dive = 0.311376267020
```

## 7.4 Calculate dive path

The MCIFT dive path moves from Earth to Mars while subtracting the crest path, meaning it dives below the wave ridge:

```text
P_dive(s)
=
(1 - s) * Earth(launch_time)
+
s * Mars(arrival_dive)
-
D_dive * GW_crest(s)
```

Expanded:

```text
P_dive(s)
=
(1 - s) * Earth(launch_time)
+
s * Mars(2027-03-31 00:00 UTC)
-
0.311376267020 * GW_crest(s)
```

In the graph:

```text
MCIFT dive color       = cyan
MCIFT dive arrival     = 2027-03-31 00:00 UTC
MCIFT dive travel time = 58 days
```

---

# 8. Mission Path 3 — MCIFT Wave-Rider

## 8.1 Define arrival

```text
arrival_wave_rider = 2027-04-15 00:00 UTC
```

Travel time:

```text
T_wave_rider = arrival_wave_rider - launch_time
T_wave_rider = 73 days
```

## 8.2 Define normalized path parameter

```text
s = (t - launch_time) / T_wave_rider
```

## 8.3 Calculate wave-rider coupling factor

The wave-rider uses shear, anisotropy, and loop balance:

```text
R_ride = mean_shear_proxy * global_anisotropy * beta4_needed_for_balance
```

Substitute values:

```text
R_ride
=
0.063915576742
*
0.351925814364
*
0.170868625373
```

Result:

```text
R_ride ≈ 0.003844
```

## 8.4 Apply visual gain

Because the raw value is small on the graph scale, apply visual gain:

```text
R_ride_visual = R_ride * visual_gain
```

For visualization:

```text
visual_gain = chosen_display_scale
```

So:

```text
R_ride_visual = 0.003844 * visual_gain
```

## 8.5 Calculate wave-rider path

The MCIFT wave-rider does not dive below the crest. It rides the crest:

```text
P_wave_rider(s)
=
(1 - s) * Earth(launch_time)
+
s * Mars(arrival_wave_rider)
+
R_ride_visual * GW_crest(s)
```

Expanded:

```text
P_wave_rider(s)
=
(1 - s) * Earth(2027-02-01 00:00 UTC)
+
s * Mars(2027-04-15 00:00 UTC)
+
R_ride_visual * GW_crest(s)
```

In the graph:

```text
MCIFT wave-rider color       = neon green
MCIFT wave-rider arrival     = 2027-04-15 00:00 UTC
MCIFT wave-rider travel time = 73 days
```

---

# 9. Arrival Comparison

## 9.1 Traditional orbital route

```text
launch  = 2027-02-01 00:00 UTC
arrival = 2027-04-30 00:00 UTC
```

```text
travel_time = 88 days
```

## 9.2 MCIFT dive below GW path

```text
launch  = 2027-02-01 00:00 UTC
arrival = 2027-03-31 00:00 UTC
```

```text
travel_time = 58 days
```

## 9.3 MCIFT wave-rider

```text
launch  = 2027-02-01 00:00 UTC
arrival = 2027-04-15 00:00 UTC
```

```text
travel_time = 73 days
```

---

# 10. Final Comparison Table

| Path | Arrival UTC | Total Travel Time |
|---|---:|---:|
| Traditional orbital route | 2027-04-30 00:00 UTC | 88 days |
| MCIFT dive below GW path | 2027-03-31 00:00 UTC | 58 days |
| MCIFT wave-rider | 2027-04-15 00:00 UTC | 73 days |

---

# 11. Output Graph Elements

The final graph contains:

```text
Earth trajectory
Mars trajectory
traditional orbital route
MCIFT dive below GW path
MCIFT wave-rider path
gravitational-wave crest path
Earth shell
Mars shell
Sun load / wave source
output time box
arrival comparison table
bottom timeline bar
```

---

# 12. Minimal Reproduction Pseudocode

```python
# ------------------------------------------------------------
# MCIFT Earth–Mars Feb/Mar/Apr 2027 Proxy Comparison
# ------------------------------------------------------------

# 1. Time window
launch_time = "2027-02-01 00:00 UTC"
end_time    = "2027-04-30 00:00 UTC"

# 2. Arrivals
arrival_traditional = "2027-04-30 00:00 UTC"
arrival_dive        = "2027-03-31 00:00 UTC"
arrival_wave_rider  = "2027-04-15 00:00 UTC"

# 3. Travel times
T_traditional = 88
T_dive        = 58
T_wave_rider  = 73

# 4. MCIFT v0.97 parameters
epsilon_3 = 0.125
psi_3 = 0
r_core = 1

mean_shear_proxy = 0.063915576742
mean_threefold_amp = 0.247460690278
global_anisotropy = 0.351925814364
beta4_needed_for_balance = 0.170868625373

# 5. MCIFT A3 activation
def A3(theta, phi):
    return 1 + epsilon_3 * sin(theta)**2 * cos(3 * phi + psi_3)

# 6. Radial core density
def rho0(r):
    return exp(-r**2 / r_core**2)

# 7. MCIFT field fabric
def F_shear(r, theta, phi):
    return rho0(r) * A3(theta, phi) + mean_shear_proxy * A3(theta, phi)

# 8. GW crest path
def GW_crest(base_shell, theta, phi):
    return base_shell + mean_shear_proxy * A3(theta, phi)

# 9. Traditional path
def P_traditional(s):
    return (
        (1 - s) * Earth(launch_time)
        + s * Mars(arrival_traditional)
        + K_orbit * sin(pi * s)
    )

# 10. Dive factor
D_dive = mean_threefold_amp + mean_shear_proxy
# D_dive = 0.311376267020

# 11. MCIFT dive path
def P_dive(s):
    return (
        (1 - s) * Earth(launch_time)
        + s * Mars(arrival_dive)
        - D_dive * GW_crest_s(s)
    )

# 12. Wave-rider factor
R_ride = mean_shear_proxy * global_anisotropy * beta4_needed_for_balance
# R_ride ≈ 0.003844

R_ride_visual = R_ride * visual_gain

# 13. MCIFT wave-rider path
def P_wave_rider(s):
    return (
        (1 - s) * Earth(launch_time)
        + s * Mars(arrival_wave_rider)
        + R_ride_visual * GW_crest_s(s)
    )

# 14. Plot all paths
plot(Earth_trajectory)
plot(Mars_trajectory)
plot(P_traditional)
plot(P_dive)
plot(P_wave_rider)
plot(GW_crest_path)

# 15. Display table
print("Traditional:", arrival_traditional, T_traditional)
print("MCIFT dive:", arrival_dive, T_dive)
print("MCIFT wave-rider:", arrival_wave_rider, T_wave_rider)
```

---

# 13. One-Line Description

```text
Using MCIFT v0.97, calculate the threefold field fabric with r0(n,t)=cΔtρ0(r)A3(n), map Earth and Mars through the Feb–Apr 2027 window, define the gravitational-wave crest from the shear-modulated A3 shell, then compare three Earth→Mars paths: traditional orbital arc, MCIFT dive below the crest, and MCIFT wave-rider along the crest.
```
