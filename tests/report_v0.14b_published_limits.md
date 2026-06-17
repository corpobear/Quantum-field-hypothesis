# Test Report v0.14b

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Date:** 2026-06-17  
**Status:** quick published-results comparison; speculative toy-model test; not established physics

---

## 1. Purpose

This report performs the quick published-results version of the v0.14 CERN-facing test.

It does not use event-level open data. It checks whether existing ATLAS/CMS searches in the closest public channels already show the kind of unexplained missing-momentum behavior that the MCIFT side-channel picture would need.

---

## 2. MCIFT collider proxy

MCIFT translation:

```text
visible drill activity -> jets and visible transverse energy
side-channel activity  -> missing transverse momentum and event imbalance
```

Reduced event proxy:

$$
R_{miss}=\frac{E_T^{miss}}{H_T}
$$

with:

$$
H_T=\sum_{jets}p_T^{jet}.
$$

A candidate side-channel pattern would need to look like:

```text
high missing transverse momentum
+ hard jet or jet system
+ event-shape or angular imbalance
+ not explained by Standard Model backgrounds
```

---

## 3. Published comparison anchors

### ATLAS monojet / energetic jet plus missing transverse momentum

ATLAS searched 13 TeV proton-proton collision data with 139 inverse femtobarns. The analysis required at least one jet with transverse momentum above 150 GeV, no reconstructed leptons or photons, and missing transverse momentum signal regions starting at 200 GeV.

The published summary reports overall agreement between data and Standard Model predictions and sets model-independent 95 percent confidence-level limits on visible cross sections.

Reference: ATLAS Collaboration, arXiv:2102.10874.

### CMS energetic jets plus missing transverse momentum

CMS searched 13 TeV proton-proton collision data in events with energetic jets and large missing transverse momentum, using 2017-2018 data and a statistical combination with an earlier 2016 search.

The published summary reports no significant excess with respect to the Standard Model background expectation determined from control samples in data.

Reference: CMS Collaboration, arXiv:2107.13021.

---

## 4. v0.14b verdict

The quick published-results comparison gives:

```text
not confirmed; constrained by existing missing-momentum searches
```

This is not a full exclusion, because the MCIFT collider version has not yet specified:

```text
production cross section
mass scale
lifetime
event topology
coupling strength
exact event selection
```

But the quick test does rule out any loose claim that broad LHC missing-momentum data already support a large obvious MCIFT side-channel signal.

---

## 5. Next step

The next meaningful test remains the direct event-level open-data comparison:

```text
analysis/cern_two_drill_event_shape_test.py
```

That test should compare real data against Standard Model simulation in high MET/HT and angular-imbalance bins before making any stronger claim.
