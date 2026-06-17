# Test Report v0.14

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Author:** Adrian Newton / corpobear  
**Date:** 2026-06-17  
**Status:** first CERN-facing published-results comparison  
**Revision:** v0.14.0

---

## 1. Purpose

This report compares the MCIFT two-drill collision picture with existing public LHC search categories.

MCIFT picture:

```text
proton beam A = boosted drill-like composite knot
proton beam B = boosted drill-like composite knot
collision = two drill-like knots overlapping at high energy
possible dark-manifest side channel = invisible recoil / missing transverse momentum
```

Collider translation:

```text
visible drill activity -> jets and visible transverse energy
dark side channel -> missing transverse momentum and event imbalance
```

---

## 2. Observable proxy

Visible scale:

$$
H_T=\sum_{jets}p_T^{jet}.
$$

Missing fraction:

$$
R_{miss}=\frac{E_T^{miss}}{H_T}.
$$

Basic MCIFT event proxy:

$$
\frac{|S_{dark}|}{|S_{visible}|}\sim \frac{E_T^{miss}}{H_T}.
$$

A candidate side-channel pattern should appear as a structured excess in high missing-momentum regions, especially when paired with jet or event-shape imbalance.

---

## 3. Relevant published search class

The closest public LHC search class is:

```text
monojet or multijet plus missing transverse momentum
```

These channels are the right first comparison because a light-inactive but momentum-carrying sector would most naturally appear as missing transverse momentum.

Relevant comparison categories:

```text
energetic jet plus large missing transverse momentum
large jet multiplicity plus missing transverse momentum
hadronic vector boson plus missing transverse momentum
long-lived weakly interacting signatures with displaced jets
```

---

## 4. Published-results outcome

Published ATLAS missing-momentum searches report broad agreement with Standard Model expectations in the relevant monojet and multijet categories.

Therefore the first published-results comparison gives:

```text
MCIFT dark-manifest side-channel behavior is not confirmed by current broad ATLAS missing-momentum searches.
```

The result is constraint-like, not discovery-like.

---

## 5. Interpretation for MCIFT

The two-drill collision idea remains possible only in a constrained form:

```text
possible if the production rate is below current search sensitivity
possible if the topology is not targeted by standard monojet or multijet selections
possible if the effect is absorbed into known backgrounds
not supported if it predicts a large already-visible missing-momentum excess
```

This makes the model more testable because it must now respect published collider limits.

---

## 6. First pass/fail rule

Support condition:

```text
Data show a structured excess in high MET/HT plus side-flow or event-shape bins
that is not explained by Standard Model backgrounds.
```

Constraint condition:

```text
High MET/HT and side-flow patterns remain consistent with Standard Model backgrounds,
including neutrinos, QCD effects, electroweak processes, detector response, and simulation.
```

Current published-result verdict:

```text
No support yet. Existing published searches place constraints on the idea.
```

---

## 7. Why this is not a complete exclusion

MCIFT has not yet predicted:

```text
production cross section
mass scale
lifetime
event topology
coupling strength
exact event selection
```

So the current comparison is not a complete exclusion. It is a first boundary condition:

```text
Any collider version of the dark-manifest side channel must be small, hidden, or geometrically different from already-tested missing-momentum signatures.
```

---

## 8. Direct open-data test plan

A future direct event-level test should use ATLAS or CMS open data plus matching Standard Model simulation.

Minimum variables:

```text
jet_pt
jet_eta
jet_phi
met
met_phi
lepton counts
photon counts
b-tag counts if available
```

Derived variables:

$$
H_T=\sum p_T^{jet}
$$

$$
R_{miss}=E_T^{miss}/H_T
$$

$$
\Delta\phi_{min}=\min_i\Delta\phi(jet_i,E_T^{miss})
$$

$$
N_{jets}
$$

Suggested regions:

```text
monojet-like: at least 1 high-pT jet, no leptons, high MET
multijet-like: many jets, high HT, moderate-to-high MET
side-channel-like: high MET/HT plus angular imbalance
```

---

## 9. v0.14 verdict

```text
The CERN comparison can begin now.
The first published-results comparison does not confirm MCIFT.
It constrains the dark-manifest side-channel idea to be below existing missing-momentum sensitivity or outside the topologies those searches target.
```

Short verdict:

```text
not confirmed, not ruled out by this reduced comparison, now constrained
```

---

## 10. Next repository task

Use `analysis/cern_two_drill_event_shape_test.py` on local ATLAS/CMS open-data-derived tables.

Expected output:

```text
hist_MET_over_HT.png
hist_delta_phi_min.png
hist_njets.png
data_vs_mc_summary.csv
```

The next meaningful result should compare actual data histograms to Standard Model Monte Carlo histograms.
