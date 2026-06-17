# Test Reports Index

This folder contains reduced toy-model tests for the MCIFT / Quantum-field-hypothesis repository.

**Status:** speculative toy-model testing; not established physics.

---

## Reports

```text
report_v0.1.md    Initial toy-model test report
report_v0.2.md    Exchange-rate and shadow-amplitude calculations
report_v0.3.md    Motion-by-exchange calculation
report_v0.4.md    Shadow projection and Koide comparison
report_v0.5.md    Entanglement shared-amplitude correction
report_v0.6.md    Objective shared-channel entanglement
report_v0.7.md    Vibration-motion shadow-anchor derivation
report_v0.8.md    One-anchor spin-vortex correction test
report_v0.9.md    Fibonacci-Higgs source equation reduced tau test
report_v0.10.md   Funnel-speed Higgs capture-window reduced tau test
report_v0.11.md   Bounded fourth-mode reservoir field-source test
report_v0.13.md   Six-side sink dark-manifest ratio test
report_v0.14_cern_two_drill_event_shape.md   CERN two-drill event-shape published-results comparison
report_v0.14b_published_limits.md   Quick ATLAS/CMS published missing-momentum limits check
report_v0.15_matter_antimatter_toy_ratio.md   Matter-antimatter channel-geometry toy ratio
```

---

## Current latest test: v0.15

v0.15 tests the antimatter channel-geometry adjustment as a reduced toy calculation.

Antimatter is modeled as:

```text
positive mass with reversed charge / phase / channel orientation
```

not as negative mass.

The v0.15 geometry uses:

```text
matter visible drill      = center-tip collector
matter dark sink          = side-belt collector
antimatter dark sink      = Higgs-drop collector
antimatter light drill    = splash-ring collector with discarded middle
```

The reduced toy result is:

$$
\frac{A_M}{A_{\bar M}}=1.28669912372469.
$$

The corresponding asymmetry parameter is:

$$
\epsilon_{MCIFT}=0.125376845930524.
$$

Short verdict:

```text
matter aperture > antimatter aperture in this toy geometry
```

This is an internal toy-model consistency result, not physical confirmation of baryon asymmetry.

---

## Previous test: v0.14b

v0.14b performs the quick published-results check against ATLAS/CMS energetic-jet plus missing-transverse-momentum searches.

The collider proxy remains:

$$
R_{miss}=\frac{E_T^{miss}}{H_T}.
$$

The quick published-results verdict is:

```text
not confirmed; constrained by existing missing-momentum searches
```

This is not a full exclusion because MCIFT has not yet specified a production cross section, mass scale, lifetime, topology, coupling strength, or exact event selection.

The next collider step is still a direct open-data event-shape test using:

```text
analysis/cern_two_drill_event_shape_test.py
```

---

## Previous test: v0.14

v0.14 starts the CERN comparison.

It maps the MCIFT two-drill collision picture to collider observables:

```text
visible drill activity -> jets and visible transverse energy
dark side channel -> missing transverse momentum and event imbalance
```

Main proxy:

$$
R_{miss}=\frac{E_T^{miss}}{H_T}.
$$

The first comparison uses published ATLAS missing-momentum search results. These searches broadly report agreement with Standard Model expectations in monojet and multijet categories, so the first verdict is:

```text
not confirmed, not ruled out by this reduced comparison, now constrained
```

---

## Previous test: v0.13

v0.13 tests whether an eight-sector knot/shadow geometry can produce a dark-manifest side-sink sector close to the observed dark-to-baryonic matter ratio.

$$
\frac{A_{side}}{A_{tip}}=5.417
$$

compared with:

$$
\frac{\Omega_c}{\Omega_b}\approx\frac{0.120}{0.0224}=5.357.
$$

---

## Caveat

These tests are internal consistency checks of a speculative toy model. They are not experimental confirmation and do not establish a physical field theory.
