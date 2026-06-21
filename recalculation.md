# MCIFT Earth–Mars Travel-Time Recalculation

## Purpose

This note gives the reproducible travel-time calculation for the three Earth-to-Mars comparison paths:

1. Traditional orbital transfer
2. MCIFT dive below gravitational-wave path
3. MCIFT wave-rider path

The corrected setup is:

```text
Do not set the traditional arrival date to April 30.
Calculate the traditional orbital transfer time first.
Then calculate the MCIFT travel times as reductions of that orbital-transfer time.
```

---

## 1. Launch Time

Launch time:

```text
launch = 2027-02-01 00:00 UTC
```

This is the only date fixed at the start.

The arrival dates are calculated from the travel-time formulas.

---

## 2. Traditional Orbital Path Travel Time

Use the standard two-body Hohmann transfer approximation from Earth orbit to Mars orbit.

The Hohmann transfer time is half the orbital period of the transfer ellipse.

Formula:

```text
T_orbital = π × sqrt(a_transfer³ / μ_sun)
```

Using astronomical units and years, this becomes:

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

Calculate orbital transfer time in years:

```text
T_orbital_years = 0.5 × 1.2618395^(3/2)
```

```text
T_orbital_years = 0.708788...
```

Convert to days using one sidereal year:

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

Rounded mission-day value:

```text
T_orbital_rounded = 259 days
```

Traditional arrival from launch:

```text
traditional_arrival_exact = launch + 258.86537949951685 days
```

```text
traditional_arrival_exact = 2027-10-17 20:46:08 UTC
```

Rounded-day arrival:

```text
traditional_arrival_rounded = launch + 259 days
```

```text
traditional_arrival_rounded = 2027-10-18 00:00 UTC
```

---

## 3. MCIFT Version Used

Repo version used:

```text
MCIFT v0.97 Threefold Reducer
```

Relevant v0.97 loop-balance outputs:

```text
loop_sum = 0.341737250747
beta4_needed_for_balance = 0.170868625373
```

For this travel-time comparison:

```text
loop_sum = dive-path time-reduction factor
beta4_needed_for_balance = wave-rider time-reduction factor
```

---

## 4. Traditional Route Travel Time

Formula:

```text
T_traditional = T_orbital_days
```

Substitution:

```text
T_traditional = 258.86537949951685 days
```

Rounded:

```text
T_traditional_rounded = 259 days
```

Arrival:

```text
traditional_arrival = launch + T_traditional
```

Result:

```text
traditional_arrival_exact   = 2027-10-17 20:46:08 UTC
traditional_arrival_rounded = 2027-10-18 00:00 UTC
```

---

## 5. MCIFT Dive Travel Time

Formula:

```text
T_dive = T_orbital_days × (1 - loop_sum)
```

Substitution:

```text
T_dive = 258.86537949951685 × (1 - 0.341737250747)
```

Simplify:

```text
T_dive = 258.86537949951685 × 0.658262749253
```

Result:

```text
T_dive = 170.40143639577315 days
```

Rounded mission-day value:

```text
T_dive_rounded = 170 days
```

Arrival:

```text
dive_arrival_exact = launch + 170.40143639577315 days
```

```text
dive_arrival_exact = 2027-07-21 09:38:04 UTC
```

Rounded-day arrival:

```text
dive_arrival_rounded = launch + 170 days
```

```text
dive_arrival_rounded = 2027-07-21 00:00 UTC
```

---

## 6. MCIFT Wave-Rider Travel Time

Formula:

```text
T_wave_rider = T_orbital_days × (1 - beta4_needed_for_balance)
```

Substitution:

```text
T_wave_rider = 258.86537949951685 × (1 - 0.170868625373)
```

Simplify:

```text
T_wave_rider = 258.86537949951685 × 0.829131374627
```

Result:

```text
T_wave_rider = 214.63340794777443 days
```

Rounded mission-day value:

```text
T_wave_rider_rounded = 215 days
```

Arrival:

```text
wave_rider_arrival_exact = launch + 214.63340794777443 days
```

```text
wave_rider_arrival_exact = 2027-09-03 15:12:06 UTC
```

Rounded-day arrival:

```text
wave_rider_arrival_rounded = launch + 215 days
```

```text
wave_rider_arrival_rounded = 2027-09-04 00:00 UTC
```

---

## 7. Final Travel-Time Comparison

| Path | Formula | Exact Travel Time | Rounded Travel Time | Exact Arrival UTC | Rounded Arrival UTC |
|---|---:|---:|---:|---:|---:|
| Traditional orbital transfer | `0.5 × ((r_Earth + r_Mars)/2)^(3/2) × sidereal_year` | 258.86537949951685 days | 259 days | 2027-10-17 20:46:08 UTC | 2027-10-18 00:00 UTC |
| MCIFT dive below GW path | `T_orbital_days × (1 - loop_sum)` | 170.40143639577315 days | 170 days | 2027-07-21 09:38:04 UTC | 2027-07-21 00:00 UTC |
| MCIFT wave-rider | `T_orbital_days × (1 - beta4_needed_for_balance)` | 214.63340794777443 days | 215 days | 2027-09-03 15:12:06 UTC | 2027-09-04 00:00 UTC |

---

## 8. Minimal Reproducible Python

```python
from datetime import datetime, timezone, timedelta

# Fixed launch date
launch = datetime(2027, 2, 1, 0, 0, tzinfo=timezone.utc)

# Mean orbital radii in AU
r_earth = 1.000000
r_mars = 1.523679

# Sidereal year in days
sidereal_year_days = 365.256363004

# Hohmann transfer semi-major axis
a_transfer = (r_earth + r_mars) / 2

# Traditional orbital transfer time
T_orbital_days = 0.5 * (a_transfer ** 1.5) * sidereal_year_days

# MCIFT v0.97 values
loop_sum = 0.341737250747
beta4_needed_for_balance = 0.170868625373

# Travel times
T_traditional = T_orbital_days
T_dive = T_orbital_days * (1 - loop_sum)
T_wave_rider = T_orbital_days * (1 - beta4_needed_for_balance)

# Arrivals
traditional_arrival = launch + timedelta(days=T_traditional)
dive_arrival = launch + timedelta(days=T_dive)
wave_rider_arrival = launch + timedelta(days=T_wave_rider)

print("a_transfer:", a_transfer, "AU")
print("traditional:", T_traditional, "days →", traditional_arrival.isoformat())
print("dive:", T_dive, "days →", dive_arrival.isoformat())
print("wave rider:", T_wave_rider, "days →", wave_rider_arrival.isoformat())

print("rounded traditional:", round(T_traditional), "days →", launch + timedelta(days=round(T_traditional)))
print("rounded dive:", round(T_dive), "days →", launch + timedelta(days=round(T_dive)))
print("rounded wave rider:", round(T_wave_rider), "days →", launch + timedelta(days=round(T_wave_rider)))
```

Expected output:

```text
a_transfer: 1.2618395 AU
traditional: 258.86537949951685 days → 2027-10-17T20:46:08.788758+00:00
dive: 170.40143639577315 days → 2027-07-21T09:38:04.104595+00:00
wave rider: 214.63340794777443 days → 2027-09-03T15:12:06.446688+00:00
rounded traditional: 259 days → 2027-10-18 00:00:00+00:00
rounded dive: 170 days → 2027-07-21 00:00:00+00:00
rounded wave rider: 215 days → 2027-09-04 00:00:00+00:00
```

---

## 9. One-Line Summary

```text
Calculate the traditional Earth-to-Mars orbital path as a Hohmann transfer using Earth/Mars mean orbital radii, then reduce that computed orbital travel time with MCIFT v0.97 loop_sum for the dive path and beta4_needed_for_balance for the wave-rider path.
```
