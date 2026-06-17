# Two-Drill Collision CERN Test Model v0.14

**Status:** speculative collider-facing toy model; not established physics  
**Purpose:** translate the MCIFT visible-drill / dark-sink mechanics into collider observables that can be compared with ATLAS/CMS public results and open data.

---

## 1. Physical picture in MCIFT language

A proton-proton collider event is modeled as two boosted composite knots colliding head-on:

```text
beam A: drill-like composite knot moving +z
beam B: drill-like composite knot moving -z
collision: tip/tip overlap plus possible side/sink leakage
```

Visible Standard-Model-like activity corresponds to light-active visible-manifest channels.

Dark-manifest leakage would correspond to mass/gravity-active but light-inactive source flow, visible only as missing transverse momentum or event imbalance.

---

## 2. Collider translation

Use standard collider observables rather than private MCIFT terms.

```text
MCIFT axial drill collision  -> leading jets / hard visible activity
MCIFT side/sink leakage      -> missing transverse momentum and event imbalance
knot breakup                 -> jet multiplicity
directional exchange         -> transverse momentum flow
side/tip geometry            -> event-shape anisotropy
```

Suggested observables:

```math
H_T=\sum_{jets} p_T^{jet}
```

```math
R_{miss}=\frac{E_T^{miss}}{H_T}
```

```math
\Delta\phi(j_i,E_T^{miss})
```

```math
N_{jets}
```

and, when available:

```math
\text{sphericity},\quad \text{thrust},\quad \text{centrality}.
```

---

## 3. v0.14 hypothesis

The two-drill collision hypothesis predicts that if a side/sink dark-manifest channel exists, it should not appear as random missing energy alone.

It should appear as a structured event-shape class:

```text
large missing transverse momentum
+ large visible recoil jet or jet system
+ side/sink-like imbalance
+ not fully explained by known Standard Model backgrounds
```

The most basic proxy is:

```math
R_{dark}^{event}=\frac{E_T^{miss}}{H_T}.
```

A stronger geometry proxy is:

```math
R_{side/tip}^{event}
=
\frac{\text{transverse imbalance or side-flow}}{\text{leading visible jet scale}}.
```

---

## 4. Visible and dark source terms

Visible drill source:

```math
S_{visible}
=\lambda_+\Omega_z W_{tip}A_{tip}R_4^{gate}\delta_{tip}^{(\varphi)}.
```

Dark side source:

```math
S_{dark}
= -\lambda_-\kappa_{sink}W_{side}A_{side}R_4^{gate}\delta_{side}^{(\varphi)}.
```

The sign marks inverse orientation, not negative mass.

Collider proxy:

```math
|S_{dark}| \rightarrow E_T^{miss}\ \text{or invisible recoil}
```

```math
|S_{visible}| \rightarrow H_T\ \text{or visible jet scale}
```

Thus:

```math
\frac{|S_{dark}|}{|S_{visible}|}
\sim
\frac{E_T^{miss}}{H_T}.
```

---

## 5. Published-results first test

A first CERN-facing comparison should use published ATLAS/CMS missing-energy searches.

The broad pass/fail rule is:

```text
If published monojet/MET and multijet/MET searches show significant unexplained excesses,
MCIFT side/sink leakage gains a target region.

If published searches agree with Standard Model expectations,
MCIFT side/sink leakage is not confirmed and must be below the published limits or hidden inside known backgrounds.
```

Current published ATLAS monojet and multijet missing-energy searches report agreement with Standard Model predictions, so v0.14 is constrained rather than confirmed.

---

## 6. Open-data event-level test

A direct open-data test should compare real data against Standard Model Monte Carlo with the same selections.

Minimal analysis steps:

```text
1. Load ATLAS/CMS open data or derived ntuples.
2. Select events with at least one high-pT jet.
3. Veto isolated leptons/photons for monojet-like regions.
4. Compute HT, MET, MET/HT, jet multiplicity, and delta-phi(jet, MET).
5. Compare data and Standard Model Monte Carlo histograms.
6. Look for structured excess in high MET/HT plus side-flow bins.
```

The repository script `analysis/cern_two_drill_event_shape_test.py` implements this shape-test scaffold for local CSV or ROOT-derived tables.

---

## 7. Verdict at v0.14

The first published-results confrontation is negative/constraint-like:

```text
No broad published ATLAS MET excess has been established in the relevant monojet or multijet channels.
```

Therefore:

```text
MCIFT dark-manifest side/sink leakage is not confirmed by existing published CERN searches.
```

The model remains viable only if its collider production rate is below current limits, has a topology not targeted by those searches, or is absorbed into known backgrounds.

This is useful: it turns the theory into a constrained toy model rather than an unconstrained metaphor.
