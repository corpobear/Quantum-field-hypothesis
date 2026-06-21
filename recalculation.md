# MCIFT Earth–Mars Travel-Time Recalculation

## Purpose

This note gives the reproducible travel-time calculation for the three Earth-to-Mars comparison paths:

1. Traditional orbital route
2. MCIFT dive below gravitational-wave path
3. MCIFT wave-rider path

The corrected setup is:

```text
Set only the base launch time and the traditional comparison window.
Then calculate the MCIFT travel times from MCIFT v0.97 loop-balance outputs.
```

---

## 1. Base Time Window

Launch time:

```text
launch = 2027-02-01 00:00 UTC
```

Traditional comparison endpoint:

```text
traditional_target = 2027-04-30 00:00 UTC
```

Base travel window:

```text
T_base = traditional_target - launch
```

Substitution:

```text
T_base = 2027-04-30 00:00 UTC - 2027-02-01 00:00 UTC
```

Result:

```text
T_base = 88 days
```

---

## 2. MCIFT Version Used

Repo version used:

```text
MCIFT v0.97 Threefold Reducer
```

The relevant v0.97 loop-balance outputs are:

```text
loop_sum = 0.341737250747
beta4_needed_for_balance = 0.170868625373
```

Interpretation for this recalculation:

```text
loop_sum = dive-path reduction factor
beta4_needed_for_balance = wave-rider reduction factor
```

---

## 3. Traditional Route Travel Time

Formula:

```text
T_traditional = T_base
```

Substitution:

```text
T_traditional = 88
```

Result:

```text
T_traditional = 88 days
```

Arrival:

```text
traditional_arrival = launch + T_traditional
```

Substitution:

```text
traditional_arrival = 2027-02-01 00:00 UTC + 88 days
```

Result:

```text
traditional_arrival = 2027-04-30 00:00 UTC
```

---

## 4. MCIFT Dive Travel Time

Formula:

```text
T_dive = round(T_base × (1 - loop_sum))
```

Substitution:

```text
T_dive = round(88 × (1 - 0.341737250747))
```

Simplify:

```text
T_dive = round(88 × 0.658262749253)
```

Multiply:

```text
T_dive = round(57.927121934264)
```

Result:

```text
T_dive = 58 days
```

Arrival:

```text
dive_arrival = launch + T_dive
```

Substitution:

```text
dive_arrival = 2027-02-01 00:00 UTC + 58 days
```

Result:

```text
dive_arrival = 2027-03-31 00:00 UTC
```

---

## 5. MCIFT Wave-Rider Travel Time

Formula:

```text
T_wave_rider = round(T_base × (1 - beta4_needed_for_balance))
```

Substitution:

```text
T_wave_rider = round(88 × (1 - 0.170868625373))
```

Simplify:

```text
T_wave_rider = round(88 × 0.829131374627)
```

Multiply:

```text
T_wave_rider = round(72.963560967176)
```

Result:

```text
T_wave_rider = 73 days
```

Arrival:

```text
wave_rider_arrival = launch + T_wave_rider
```

Substitution:

```text
wave_rider_arrival = 2027-02-01 00:00 UTC + 73 days
```

Result:

```text
wave_rider_arrival = 2027-04-15 00:00 UTC
```

---

## 6. Final Travel-Time Comparison

| Path | Formula | Travel Time | Arrival UTC |
|---|---:|---:|---:|
| Traditional orbital route | `T_base` | 88 days | 2027-04-30 00:00 UTC |
| MCIFT dive below GW path | `round(T_base × (1 - loop_sum))` | 58 days | 2027-03-31 00:00 UTC |
| MCIFT wave-rider | `round(T_base × (1 - beta4_needed_for_balance))` | 73 days | 2027-04-15 00:00 UTC |

---

## 7. Minimal Reproducible Python

```python
from datetime import datetime, timezone, timedelta

launch = datetime(2027, 2, 1, 0, 0, tzinfo=timezone.utc)
traditional_target = datetime(2027, 4, 30, 0, 0, tzinfo=timezone.utc)

T_base = (traditional_target - launch).days

loop_sum = 0.341737250747
beta4_needed_for_balance = 0.170868625373

T_traditional = T_base
T_dive = round(T_base * (1 - loop_sum))
T_wave_rider = round(T_base * (1 - beta4_needed_for_balance))

traditional_arrival = launch + timedelta(days=T_traditional)
dive_arrival = launch + timedelta(days=T_dive)
wave_rider_arrival = launch + timedelta(days=T_wave_rider)

print("traditional:", T_traditional, "days →", traditional_arrival.isoformat())
print("dive:", T_dive, "days →", dive_arrival.isoformat())
print("wave rider:", T_wave_rider, "days →", wave_rider_arrival.isoformat())
```

Expected output:

```text
traditional: 88 days → 2027-04-30T00:00:00+00:00
dive: 58 days → 2027-03-31T00:00:00+00:00
wave rider: 73 days → 2027-04-15T00:00:00+00:00
```

---

## 8. One-Line Summary

```text
Use the 88-day traditional Earth-to-Mars window as T_base, then calculate MCIFT travel times by reducing T_base with v0.97 loop_sum for the dive path and v0.97 beta4_needed_for_balance for the wave-rider path.
```
