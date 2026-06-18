# Current MCIFT Status: v0.38 Mass-Energy Vibration Retest

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current collider-style retest:** v0.38 mass-energy vibration channel retest.  
**Previous collider-style toy test:** v0.37 line-chain spin-drill Higgs test.  
**Current collider comparison layer:** v0.36 CERN/LHC Higgs-sector comparison.  
**Current spatial tested layer:** v0.35 minimal spatial cubic lattice solver.  
**Current field formula:** v0.33 cubic cell-complex field formula.  
**Current mechanism layer:** v0.32 cube-face Higgs vortex mass mechanism.

---

## One-sentence status

```text
MCIFT v0.38 adds Einstein mass-energy conversion to the v0.37 line-chain sink: gathered mass is converted into vibration energy, and that vibration leaks into channel proxies. The strict toy verdict is PASS-LIKE: 9/9 criteria passed, with a finite vibration lifetime and a Higgs-like channel hierarchy led by bb-like mass retention, WZ-like coherent symmetry, visible gg-like turbulence, visible tau-like retention, and suppressed gamma-like and mumu-like channels.
```

---

## v0.38 result

```text
verdict = PASS-LIKE
criteria_pass_count = 9/9
peak_E_vib_GeV_proxy = 0.023315
peak_E_vib_step = 319
peak_E_vib_time = 6.380000
final_E_vib_over_peak = 0.187542
integrated_E_in_GeV_proxy = 0.000691
integrated_E_leak_GeV_proxy = 0.000351
channel_l1_distance_to_rough_higgs_targets = 0.153878
channel_log10_rms_to_rough_higgs_targets = 0.358711
```

Channel fractions:

```text
bb_like     = 0.559140  target ~ 0.582000
WZ_like     = 0.316161  target ~ 0.240000
gg_like     = 0.100017  target ~ 0.086000
tau_like    = 0.024090  target ~ 0.063000
gamma_like  = 0.000402  target ~ 0.002300
mumu_like   = 0.000189  target ~ 0.000220
```

---

## Math under test

```text
E_m,i(t) = eta_m m_i(t) c^2
E_vib,i(t+dt) = E_vib,i(t) + E_m,i(t) - E_leak,i(t) - damping
omega_vib,i = E_vib,i / hbar
```

Channel source families:

```text
mass-retention source      -> bb-like, tau-like, mumu-like
coherent symmetric source  -> WZ-like
transverse turbulence      -> gg-like, gamma-like loop channels
```

---

## v0.36 CERN/LHC verdict remains

```text
STRUCTURAL_ONLY_NOT_A_CERN_PASS
```

v0.38 is still a toy decay-channel retest, not a detector-level CERN simulation.

---

## Next proof target

```text
v0.39 target:
replace proxy channel families with coupling modifiers kappa_W, kappa_Z, kappa_b, kappa_tau, kappa_mu, kappa_g, and kappa_gamma, then compute partial widths and signal strengths.
```

Required direction:

```text
- derive channel coupling modifiers from the same mass-energy vibration variables
- compute partial widths from those coupling modifiers
- sum total width
- compute branching fractions and signal strengths
- compare to collider Higgs targets without per-channel tuning
```

---

## Safe wording

```text
v0.38 shows that adding mass-energy conversion into vibration gives a PASS-LIKE toy channel hierarchy, but it is not yet a Standard Model or detector-level CERN calculation.
```
