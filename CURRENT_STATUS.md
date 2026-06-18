# Current MCIFT Status: v0.36 CERN/LHC Higgs-Sector Comparison

**Status:** speculative theoretical framework / toy collider and cosmology scaffold; not established physics.  
**Current collider-facing layer:** v0.36 CERN/LHC Higgs-sector comparison.  
**Current spatial tested layer:** v0.35 minimal spatial cubic lattice solver.  
**Current field formula:** v0.33 cubic cell-complex field formula.  
**Current mechanism layer:** v0.32 cube-face Higgs vortex mass mechanism.  
**Current geometry layer:** v0.31 cube-center six-connector knot geometry.

---

## One-sentence status

```text
MCIFT v0.36 compares the cubic Higgs-vortex mass mechanism to CERN/LHC Higgs-sector constraints. The result is structural-only compatibility, not a CERN pass: the model can represent a scalar neutral Higgs-like mass-coupling excitation, but it does not yet predict the Higgs mass independently, total width, production rates, branching fractions, signal strengths, or detector-level distributions.
```

---

## v0.36 verdict

```text
STRUCTURAL_ONLY_NOT_A_CERN_PASS
```

Scorecard:

```text
STRUCTURAL_PASS:
- scalar 0plus style central balanced excitation
- neutral/colorless structural representation

CALIBRATION_REQUIRED:
- Higgs mass scale

WEAK_QUALITATIVE:
- coupling hierarchy / mass-response idea

NOT_IMPLEMENTED:
- total width in MeV
- production rates: ggF, VBF, VH, ttH
- branching fractions: ZZ, WW, gamma gamma, tau tau, bb, mu mu
- signal-strength likelihood
- detector-level event distributions

CONSTRAINED:
- MCIFT collider limit must reduce to SM-like Higgs behavior within current LHC uncertainties
```

---

## Mass calibration note

For an ideal symmetric six-face Higgs-vortex excitation:

```text
ideal six-face vortex mass proxy = 5.826622
m_scale = 125.04 GeV / 5.826622
m_scale = 21.460119 GeV
```

This is a calibration to the CERN Higgs mass, not an independent prediction.

---

## Latest spatial result: v0.35

```text
v0.34 mode-level RMS = 0.302859
v0.35 spatial-lattice mapped RMS = 0.303948
shape verdict = PASS-LIKE
spatial pre-collapse peak = 617.87 Mpc, harmonic n=1
spatial post-collapse peak = 154.47 Mpc, harmonic n=4
mapped v0.35 global peak = 152.29 Mpc
mapped v0.35 BAO-window peak = 152.29 Mpc
```

---

## Next proof target

```text
v0.37 target:
Build a collider-Higgs effective model from MCIFT variables:
1. derive coupling modifiers kappa_W, kappa_Z, kappa_t, kappa_b, kappa_tau, kappa_mu
2. derive loop modifiers kappa_g and kappa_gamma
3. compute partial widths and total width
4. compute production times branching signal strengths
5. compare to ATLAS/CMS likelihood-style targets
```

---

## Safe wording

```text
MCIFT v0.36 is structurally compatible with a scalar Higgs-like mass-coupling excitation, but it is not yet a quantitative CERN/LHC Higgs model.
```
