# MCIFT Earth–Mars Travel-Time Methodology and Results

## 0. Purpose

This document records the methodology used to calculate the Earth-to-Mars baseline orbital travel time, then apply the MCIFT v0.97 reduction factors for two MCIFT approaches:

1. Traditional orbital transfer baseline
2. MCIFT wave dive
3. MCIFT wave ride

The launch date is fixed:

```text
launch = 2027-02-01 00:00 UTC
```

The arrival dates are **not** preset. They are calculated from the travel-time equations.

---

## 1. Traditional Orbital Transfer Baseline

The traditional orbital path is calculated first. This becomes the baseline timeframe for the MCIFT comparison.

Use a Hohmann-style Earth-to-Mars transfer approximation.

Formula:

```text
T_orbital = π × sqrt(a_transfer³ / μ_sun)
```

Using astronomical units and years, the same transfer time can be written as:

```text
T_orbital_years = 0.5 × a_transfer^(3/2)
```

where:

```text
a_transfer = (r_Earth + r_Mars) / 2
```

Use mean orbital radii:

```text
r_Earth = 1.000000 AU
r_Mars  = 1.523679 AU
```

Calculate transfer semi-major axis:

```text
a_transfer = (1.000000 + 1.523679) / 2
```

```text
a_transfer = 1.2618395 AU
```

Calculate transfer time in years:

```text
T_orbital_years = 0.5 × 1.2618395^(3/2)
```

```text
T_orbital_years = 0.708788...
```

Convert to days:

```text
sidereal_year = 365.256363004 days
```

```text
T_orbital_days = 0.708788... × 365.256363004
```

Result:

```text
T_orbital_days = 258.86537949951685 days
```

Rounded:

```text
T_orbital_rounded = 259 days
```

Traditional orbital arrival:

```text
traditional_arrival = launch + T_orbital_days
```

Result:

```text
traditional_arrival_exact = 2027-10-17 20:46:08 UTC
traditional_arrival_rounded = 2027-10-18 00:00 UTC
```

---

## 2. MCIFT Version Used

The MCIFT comparison uses:

```text
MCIFT v0.97 Threefold Reducer
```

Core v0.97 formula:

```text
r0(n,t) = c Δt ρ0(r) A3(n)
```

Threefold angular activation:

```text
A3(θ,φ) = 1 + ε3 sin²(θ) cos(3φ + ψ3)
```

Repo settings used:

```text
M0        = 2
alpha_M   = 0.05
r_core    = 1
epsilon_3 = 0.125
psi_3     = 0
shells    = 1..10
```

Therefore:

```text
A3(θ,φ) = 1 + 0.125 sin²(θ) cos(3φ)
```

---

## 3. MCIFT v0.97 Values Used

The field/fabric values used for the graph:

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

The travel-time reduction values used:

```text
loop_sum = 0.341737250747
beta4_needed_for_balance = 0.170868625373
```

For this calculation:

```text
loop_sum = wave-dive reduction factor
beta4_needed_for_balance = wave-ride reduction factor
```

---

## 4. MCIFT Wave Dive Calculation

The wave-dive method uses the orbital baseline and reduces it by the v0.97 loop-sum factor.

Formula:

```text
T_wave_dive = T_orbital_days × (1 - loop_sum)
```

Substitute:

```text
T_wave_dive = 258.86537949951685 × (1 - 0.341737250747)
```

Simplify:

```text
T_wave_dive = 258.86537949951685 × 0.658262749253
```

Result:

```text
T_wave_dive = 170.40143639577315 days
```

Rounded:

```text
T_wave_dive_rounded = 170 days
```

Arrival:

```text
wave_dive_arrival = launch + T_wave_dive
```

Result:

```text
wave_dive_arrival_exact = 2027-07-21 09:38:04 UTC
wave_dive_arrival_rounded = 2027-07-21 00:00 UTC
```

Time saved against traditional orbital baseline:

```text
T_saved_dive = T_orbital_days - T_wave_dive
```

```text
T_saved_dive = 258.86537949951685 - 170.40143639577315
```

```text
T_saved_dive = 88.46394310374370 days
```

---

## 5. MCIFT Wave Ride Calculation

The wave-ride method uses the orbital baseline and reduces it by the v0.97 beta4 balance factor.

Formula:

```text
T_wave_ride = T_orbital_days × (1 - beta4_needed_for_balance)
```

Substitute:

```text
T_wave_ride = 258.86537949951685 × (1 - 0.170868625373)
```

Simplify:

```text
T_wave_ride = 258.86537949951685 × 0.829131374627
```

Result:

```text
T_wave_ride = 214.63340794777443 days
```

Rounded:

```text
T_wave_ride_rounded = 215 days
```

Arrival:

```text
wave_ride_arrival = launch + T_wave_ride
```

Result:

```text
wave_ride_arrival_exact = 2027-09-03 15:12:06 UTC
wave_ride_arrival_rounded = 2027-09-04 00:00 UTC
```

Time saved against traditional orbital baseline:

```text
T_saved_ride = T_orbital_days - T_wave_ride
```

```text
T_saved_ride = 258.86537949951685 - 214.63340794777443
```

```text
T_saved_ride = 44.23197155174242 days
```

---

## 6. Final Results

| Path | Formula | Exact Travel Time | Rounded Travel Time | Exact Arrival UTC | Rounded Arrival UTC | Time Saved vs Orbital |
|---|---:|---:|---:|---:|---:|---:|
| Traditional orbital transfer | `0.5 × ((r_Earth + r_Mars)/2)^(3/2) × sidereal_year` | 258.86537949951685 days | 259 days | 2027-10-17 20:46:08 UTC | 2027-10-18 00:00 UTC | — |
| MCIFT wave ride | `T_orbital_days × (1 - beta4_needed_for_balance)` | 214.63340794777443 days | 215 days | 2027-09-03 15:12:06 UTC | 2027-09-04 00:00 UTC | 44.23197155174242 days |
| MCIFT wave dive | `T_orbital_days × (1 - loop_sum)` | 170.40143639577315 days | 170 days | 2027-07-21 09:38:04 UTC | 2027-07-21 00:00 UTC | 88.46394310374370 days |

Rounded summary:

```text
Traditional orbital transfer: 259 days
MCIFT wave ride:              215 days
MCIFT wave dive:              170 days
```

---

## 7. Minimal Reproducible Python

```python
from datetime import datetime, timezone, timedelta

# Fixed launch date
launch = datetime(2027, 2, 1, 0, 0, tzinfo=timezone.utc)

# Mean orbital radii in AU
r_earth = 1.000000
r_mars = 1.523679

# Sidereal year in days
sidereal_year_days = 365.256363004

# Traditional Earth-to-Mars Hohmann-style transfer baseline
a_transfer = (r_earth + r_mars) / 2
T_orbital_days = 0.5 * (a_transfer ** 1.5) * sidereal_year_days

# MCIFT v0.97 reduction values
loop_sum = 0.341737250747
beta4_needed_for_balance = 0.170868625373

# MCIFT approaches
T_wave_dive = T_orbital_days * (1 - loop_sum)
T_wave_ride = T_orbital_days * (1 - beta4_needed_for_balance)

# Arrivals
traditional_arrival = launch + timedelta(days=T_orbital_days)
wave_dive_arrival = launch + timedelta(days=T_wave_dive)
wave_ride_arrival = launch + timedelta(days=T_wave_ride)

# Savings
saved_dive = T_orbital_days - T_wave_dive
saved_ride = T_orbital_days - T_wave_ride

print("a_transfer:", a_transfer, "AU")
print("traditional orbital:", T_orbital_days, "days →", traditional_arrival.isoformat())
print("MCIFT wave dive:", T_wave_dive, "days →", wave_dive_arrival.isoformat(), "saved", saved_dive, "days")
print("MCIFT wave ride:", T_wave_ride, "days →", wave_ride_arrival.isoformat(), "saved", saved_ride, "days")

print("rounded traditional:", round(T_orbital_days), "days →", launch + timedelta(days=round(T_orbital_days)))
print("rounded wave dive:", round(T_wave_dive), "days →", launch + timedelta(days=round(T_wave_dive)))
print("rounded wave ride:", round(T_wave_ride), "days →", launch + timedelta(days=round(T_wave_ride)))
```

Expected output:

```text
a_transfer: 1.2618395 AU
traditional orbital: 258.86537949951685 days → 2027-10-17T20:46:08.788758+00:00
MCIFT wave dive: 170.40143639577315 days → 2027-07-21T09:38:04.104595+00:00 saved 88.4639431037437 days
MCIFT wave ride: 214.63340794777443 days → 2027-09-03T15:12:06.446688+00:00 saved 44.23197155174242 days
rounded traditional: 259 days → 2027-10-18 00:00:00+00:00
rounded wave dive: 170 days → 2027-07-21 00:00:00+00:00
rounded wave ride: 215 days → 2027-09-04 00:00:00+00:00
```

---

## 8. One-Line Methodology

```text
Calculate the traditional Earth-to-Mars orbital transfer time first, then apply MCIFT v0.97 loop_sum as the wave-dive reduction and beta4_needed_for_balance as the wave-ride reduction to produce the final MCIFT travel-time comparison.
```
