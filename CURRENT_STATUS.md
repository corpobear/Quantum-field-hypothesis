# Current MCIFT Status: v0.63 Dark-Visible Gravitational Width Envelope

**Status:** speculative blind-prediction scaffold; not established physics.  
**Current layer:** v0.63 dark-visible gravitational width envelope.  
**Previous layer:** v0.62 blind CERN-channel inverse-timeflow test.

---

## One-sentence status

```text
MCIFT v0.63 adds a universal dark-visible gravitational envelope to the v0.62 blind CERN prediction. The branching-ratio pattern is preserved, while the total width rises from 3.325981 MeV to 4.107221 MeV without backpropagation or a target-loss fit.
```

---

## v0.63 verdict

```text
DV_ENVELOPE_FIXES_WIDTH_BR_RETAINED
```

---

## Method summary

```text
O_DV = 2 sqrt(N_dark N_visible) / (N_dark + N_visible + N_anchor)
E_DV = exp(C_ITF O_DV / (N_visible + N_anchor))
Gamma_i_final = E_DV Gamma_i_v0.62_blind
```

Numerical values:

```text
C_ITF = 0.689064
O_DV = 0.612372
E_DV = 1.234890
```

---

## CERN comparison

```text
v0.62 width = 3.325981 MeV
v0.62 width delta vs 4.07 MeV = -18.280555 percent

v0.63 width = 4.107221 MeV
v0.63 width delta vs 4.07 MeV = +0.914526 percent

v0.62 max channel delta = 8.247649 percent
v0.63 max channel delta = 8.247649 percent
```

Strict status:

```text
branching ratio prediction: RETAINED / PASS-LIKE
absolute width prediction: IMPROVED / PASS-LIKE
```

---

## Analysis result files

```text
simulations/mcift_v0_63_dark_visible_width_envelope.py
analysis/results_v0.63/mcift_v0.63_width_metrics.csv
analysis/results_v0.63/mcift_v0.63_width_channels.csv
```

---

## Next target

```text
v0.64 should test the same dark-visible envelope against cosmology, especially whether the sector-overlap rule also improves H(z), BAO scale behavior, or growth without target-derived smoothing.
```
