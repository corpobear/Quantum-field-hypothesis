# MCIFT Findings History v0.1 to v0.80

**Status:** speculative research-history document; not established physics.  
**Purpose:** consolidate the project findings so far, including missing or underdocumented early layers.

---

## Reading rules

Use these labels consistently:

```text
PASS-LIKE: internally close inside a toy/scaffold benchmark.
FAIL: did not match the selected benchmark.
BRIDGE: connects model layers but is not an independent first-principle derivation.
TRAINED: uses optimization/backpropagation or target-informed correction.
RAW: direct model output before bridge/training corrections.
NOT_IMPLEMENTED: not yet computed.
```

Nothing below should be read as experimental confirmation of new physics.

---

## v0.1 to v0.15: early concept / missing archive

The repository currently does not expose clearly versioned v0.1-v0.15 result files. These should be treated as pre-archive / concept-building layers unless older files are recovered.

Likely role:

```text
v0.1-v0.5: early Probability Field / light-texture-angle intuition.
v0.6-v0.10: early channel/knot language and matter-manifestation ideas.
v0.11-v0.15: early cosmology and visible/dark ratio experiments before archived v0.16.
```

Documentation gap:

```text
No authoritative committed result reports found for v0.1-v0.15.
Do not cite exact metrics for these versions unless files are recovered.
```

---

## v0.16 to v0.18: first archived cosmology comparisons

### v0.16 Big Bang comparison

Purpose:

```text
First toy comparison of MCIFT density/structure behavior against cosmology-style anchors.
```

Key finding:

```text
Visible/dark ratio produced a partial/weak match.
BAO/global scale behavior was not yet solved.
CMB, BBN, and H(z) were still undefined.
```

### v0.17 expansion-coupled scale lock

Purpose:

```text
Added Planck-like FRW expansion, radiation placeholder, sound horizon, and scale-lock ripple.
```

Key result:

```text
2B visible/dark ratio: PASS-LIKE.
5B visible/dark ratio: WEAK.
BAO-window peak: 152.29 Mpc vs 147.11 Mpc, PASS-LIKE.
Global long-mode peak: 617.87 Mpc, FAIL.
```

Interpretation:

```text
Scale-lock can place a BAO-like ripple in the right window, but the huge coherent long mode still dominates globally.
```

### v0.18 long-mode damping

Purpose:

```text
Added primordial gate and scalar tilt to suppress oversized coherent long modes.
```

Key result:

```text
Global peak improved from 617.87 Mpc to 152.29 Mpc.
BAO-window and global scale both became PASS-LIKE in this toy diagnostic.
```

Limitation:

```text
k_cut and p were chosen toy parameters, so this is not an independent prediction.
```

---

## v0.19 to v0.25: derived scale-lock and first-principle sink attempts

### v0.19 anchor cutoff

Purpose:

```text
Tried to tie long-mode damping/cutoff to anchor dynamics instead of a free damping choice.
```

Finding:

```text
Moved toward a more mechanistic cutoff, but remained scaffold-level.
```

### v0.20 derived scale-lock

Purpose:

```text
Derived scale-lock parameters and retested sound-horizon behavior.
```

Key result:

```text
R_A = 505.830 Mpc.
k_cut = 0.012422.
A_lock = 0.918752.
sound horizon = 147.111 Mpc.
structure scale = 152.29 Mpc, fractional error ~0.035, PASS-LIKE.
```

Limitation:

```text
CMB and BBN still undefined.
```

### v0.21 to v0.24 growth/transfer/channel-exchange stages

Purpose:

```text
Explored P(k) shape, native growth, and channel exchange to connect MCIFT geometry to cosmological structure.
```

Key finding:

```text
Transfer-style modeling improved broadband shape, but imported established shape behavior and was not fully first-principle.
```

### v0.25 first-principle sinks

Purpose:

```text
Attempted more grounded six-sink perturbation structure.
```

Key result:

```text
Six-sink RMS was weaker than transfer-smoothed versions.
Raw scale behavior still needed a projection from internal geometry into 3D growth.
```

Interpretation:

```text
More first-principle, but less numerically successful than transfer bridge.
```

---

## v0.26 to v0.35: collapse, containment, cubic field, and spatial solver

Purpose of this era:

```text
Move from pure cosmology outputs toward internal dynamics: spin blur, mass/gravity/time/spin, thermodynamic growth, collapse containment, ordered collapse, cubic-field first-principle geometry, and minimal spatial solver.
```

Important conceptual findings:

```text
Containment reservoir became necessary.
Stable structure required coherence, timing, phase matching, and bounded complexity.
Cubic field geometry became the major candidate for first-principle internal structure.
```

Representative formula layer:

```text
cell variables: K_i, q_i, B_i, phi_i, T_i
connector variables: a_i,mu and chi_i,mu
face/vortex variables: H_i,mu, Omega_i,mu, m_i,mu
```

Key limitation:

```text
This era built model mechanics, but not a validated QFT, GR, or cosmology solver.
```

---

## v0.36 to v0.40: CERN-facing and explicit 3D tests

### v0.36 CERN/Higgs comparison

Purpose:

```text
First collider-facing Higgs-sector scaffold.
```

Key result:

```text
Structural compatibility only.
Mass calibration required.
Widths, branching ratios, signal strengths, and detector-level comparisons were NOT_IMPLEMENTED.
```

Verdict:

```text
STRUCTURAL_ONLY_NOT_A_CERN_PASS
```

### v0.37 to v0.39 spin/leakage refinements

Purpose:

```text
Line-chain spin-drill, vibration/leakage, and spherical leakage tests to shape channel hierarchies.
```

Finding:

```text
Improved internal toy geometry but still not collider-good.
```

### v0.40 explicit 3D spherical leakage

Purpose:

```text
Ran a six-direction cubic packet collision in a 48^3 3D lattice.
```

Key result:

```text
criteria_pass_count = 11/11.
weighted_sphericity = 0.782404.
weighted_shape_anisotropy = 0.217596.
```

Channel issue:

```text
bb-like too high, WZ-like too low, gamma-like too small.
```

Interpretation:

```text
Explicit 3D geometry passed shell/stability checks, but the shape-derived channel hierarchy was not yet collider-good.
```

---

## v0.41 to v0.49: merging, visible/dark separation, and core-load feedback

Purpose:

```text
Build from 3D shell behavior toward dense merge, rhythm-lock, discarded vibration, visible/dark branch split, and dark/hidden load feedback into a rotating core.
```

Key findings:

```text
v0.43 rhythm-locked merge improved coherent collapse behavior.
v0.44 explicit 3D rhythm lock moved the merge idea into a 3D scaffold.
v0.45 dense entangled merge explored higher compression.
v0.46 discarded vibration/rotation tested whether lost vibration becomes rotation.
v0.48 visible/dark branch split separated visible face/vortex matter from sink-like branch.
v0.49 hidden-load feedback raised effective rotating-core load while preserving containment.
```

v0.49 verdict:

```text
PASS_DARK_GRAVITY_FEEDBACK
```

Interpretation:

```text
The model needed a non-visible load sector to explain core/gravity-like behavior without counting it as a visible decay channel.
```

---

## v0.50 to v0.53: kappa bridge, clock rotation, sound spread

### v0.50 kappa bridge

Purpose:

```text
Translate MCIFT geometry into kappa-style Higgs width/branching comparisons.
```

Finding:

```text
SM-like kappa = 1 benchmark passes by construction.
Geometry-prior versions warned that this is a bridge/calibration layer, not a first-principle derivation.
```

### v0.52 channel-clock rotation bridge

Purpose:

```text
Account for lab/proper time differences in internal channel rotation.
```

Key result:

```text
tau_core_to_lab = 0.868528.
universal kappa time needed = 1.013131.
max BR delta = 3.31%.
max signal delta = 5.21%.
```

### v0.53 sound-spread bridge

Purpose:

```text
Use an internal acoustic/spread bridge to handle total width and channel shifts.
```

Key result:

```text
Gamma_lab_sound_raw = 3.964892 MeV.
max BR shift = 4.91%.
max signal shift = 7.79%.
```

Limitation:

```text
Scaffold bridge, not real acoustic/collider evidence.
```

---

## v0.54 to v0.58: unified 3D field and real-data retest

Purpose:

```text
Coarse-grain cosmology, transfer network, unified formula, executable unified field run, and real-data retest.
```

Key result v0.58:

```text
Raw CERN particle channels failed.
Raw cosmology over-expanded.
Transfer/smoothing cosmology remained close as a scaffold.
```

v0.58 verdict:

```text
CERN_RAW_FAIL_COSMOLOGY_TRANSFER_PASS_SCAFFOLD
```

Important failure channels:

```text
gg, tau, cc, gamma, Zgamma, mumu failed in raw particle-channel comparison.
```

---

## v0.59 to v0.64: audit, inverse timeflow, first-principle cosmology, dark-visible envelope

### v0.59 audit

Purpose:

```text
Retested existing v0.58 against real-world cosmology and CERN anchors before new implementation.
```

Verdict:

```text
REALDATA_RETEST_FAILS_RAW_BUT_IDENTIFIES_NEXT_IMPLEMENTATION_TARGETS
```

### v0.60 inverse-timeflow backprop retest

Purpose:

```text
Implement inverse-timeflow/backprop bridge for CERN channels.
```

Key result:

```text
BR_L1 improved from 0.092428 raw to 0.000938 after training.
failed channels went from six to none after backprop.
```

Limitation:

```text
Trained bridge, not raw prediction.
```

### v0.61 first-principle ITF cosmology

Purpose:

```text
Derive an inverse-timeflow cosmology correction from sector counts, not a reference-derived smoothing factor.
```

Key result:

```text
H075 improved from 156.663819 raw to 111.004443.
Delta vs compact LCDM = +6.908691%.
```

### v0.62 blind CERN ITF

Purpose:

```text
Apply first-principle ITF channel readout without backpropagation.
```

Key result:

```text
max channel delta improved to 8.247649%, but total width was low at 3.325981 MeV.
```

### v0.63 dark-visible width envelope

Purpose:

```text
Add universal dark-visible gravitational envelope to fix total width while preserving branching ratios.
```

Key result:

```text
width improved to 4.107221 MeV, +0.914526% vs 4.07 MeV.
```

### v0.64 formula consolidation

Purpose:

```text
Document the unified first-principle formula on master and create main.md.
```

Finding:

```text
MCIFT now had a common C_ITF / O_DV / E_DV structure linking CERN width and cosmology corrections.
```

---

## v0.70 to v0.73: dual prediction, expanded cosmology, spatial lapse, cell action

### v0.70 dual prediction

Purpose:

```text
Use the same formula for CERN/Higgs and compact cosmology predictions.
```

Key result:

```text
CERN width = 4.107221 MeV.
H075 = 103.465987, delta = -0.351618%.
```

### v0.71 expanded cosmology benchmark

Purpose:

```text
Compare against Planck-like H0, SH0ES H0, DESI LyA BAO, BBN baryon density, S8-style anchors.
```

Verdict:

```text
EXPANDED_COSMOLOGY_MIXED_CLOSE_ON_EARLY_AND_LENSING_FAILS_LOCAL_H0
```

### v0.72 spatial scale-lapse

Purpose:

```text
Make the spatial ruler correction explicit: sigma_X = E_DV^(1/3).
```

Finding:

```text
Improved H(z) and distance-style anchors, but did not solve local H0 or raw BAO peak scale.
```

### v0.73 cell-action spatial lapse

Purpose:

```text
Derive sigma_X from a minimal one-zone strain-energy action.
```

Key formula:

```text
F_X(phi_X) = 1/2 K_X phi_X^2 - J_X phi_X
phi_X = J_X / K_X
sigma_X = exp(phi_X)
```

Finding:

```text
More principled than v0.72, but still a one-zone action, not a full cell-resolved field solver.
```

---

## v0.80: weak-field GR bridge

Purpose:

```text
Test whether time-lapse and spatial-lapse can form a weak-field metric bridge.
```

Metric bridge:

```text
psi = GM / (c^2 r)
ds^2 = -exp(-2 psi)c^2dt^2 + exp(2 psi)(dx^2 + dy^2 + dz^2)
```

Key results:

```text
PPN gamma = 1.
Newtonian inverse-square limit recovered.
solar-limb light bending = 1.751243 arcsec.
Mercury precession = 42.981975 arcsec / century.
Shapiro coefficient = 2.
```

Verdict:

```text
WEAK_FIELD_GR_BRIDGE_PASSES_CLASSIC_LIMITS_FULL_GR_NOT_DERIVED
```

Limitations:

```text
No full Einstein field equations.
No anisotropic metric tensor.
No frame dragging.
No gravitational waves.
No Friedmann equation derived from action.
```

---

## Current top-level status

Best honest summary:

```text
MCIFT has progressed from toy cosmology and collider scaffolds into a unified bridge structure linking time lapse, spatial lapse, dark-visible width envelope, and weak-field metric behavior.
```

But:

```text
It is still a speculative scaffold.
It has not derived full QFT, full GR, full CMB spectra, full SN likelihoods, or full BAO covariance.
```

---

## Documentation gaps still open

```text
1. Recover or reconstruct v0.1-v0.15 history.
2. Add per-version summaries for v0.31-v0.35 if reports exist.
3. Add per-version summaries for v0.41-v0.48 beyond the current compact notes.
4. Add result-index links for all analysis/results_v* folders.
5. Add a glossary for C_ITF, O_DV, E_DV, sigma_X, phi_X, tau, kappa, and channel stress.
6. Add a clear validation matrix: raw, bridge, trained, transfer, not implemented.
```
