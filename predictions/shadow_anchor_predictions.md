# Shadow-Anchor Predictions

**Version:** v0.6.2 speculative prediction note  
**Status:** toy-model predictions / falsifiability targets; not established physics  
**Related notes:** `notes/shadow_anchor_vibration.md`, `notes/shadow_projection.md`, `notes/objective_shared_channels.md`

---

## 1. Why this prediction note exists

The MCIFT toy model is now close to Koide-like charged-lepton amplitude geometry through the tau shadow-projection correction. The key structure is the tau-like third mode:

```math
C_3 = 2^3 = 8.
```

The shadow-anchor interpretation says that the tau shadow remains attached to the original eight-sector knot at one shared vibrating anchor point. That point is not counted as an independent echo sector. The remaining seven sectors form the independent shadow echo:

```math
f_0 = \frac{8-1}{8}=\frac{7}{8}.
```

This note separates **retrodiction** from **prediction**.

The existing tau/Koide closeness is not yet a fully independent prediction, because the tiny shared-channel residual `E_3` was inferred from the remaining Koide gap. However, the shadow-anchor/vibration mechanism now makes new internal predictions about what must happen if the shadow contact geometry changes.

---

## 2. Core contact-count law

Let

```math
k = |K_8 \cap S_8|
```

be the number of shared contact points between the original eight-sector knot `K_8` and its shadow `S_8`.

The independent shadow echo fraction is

```math
B_8(k)=\frac{8-k}{8}.
```

The model predicts that only

```math
k=1
```

is stable for a true shadow.

Therefore:

```math
B_8(1)=\frac{8-1}{8}=\frac{7}{8}.
```

Plainly:

```text
zero contact -> disconnected duplicate, not a true shadow
one contact -> stable shadow anchor
two contacts -> resonance bridge; merger begins
many contacts -> shadow collapses toward origin
```

---

## 3. Prediction 1: stable shadow contact is one point

The model predicts:

> A stable tau shadow must be attached to the original eight-sector knot by exactly one vibrating anchor point.

Zero contact does not work because the shadow is not channel-anchored to the origin.

```text
k = 0 -> no channel gate -> no stable origin-shadow correction
```

Two or more contacts do not work because vibration turns multiple shared nodes into resonance bridges.

```text
k >= 2 -> shared vibrating bridge -> phase-locking -> origin-shadow merger pressure
```

So the preferred stable contact number is:

```math
k_* = 1.
```

This is the minimal stable shadow anchoring principle.

---

## 4. Prediction 2: two-point contact shifts the tau-like mass away from Koide

The tau correction structure uses

```math
\Delta(f)=1+\frac{1}{56}+f\frac{1}{448}
```

and

```math
m_\tau(f)=m_\tau^{base}\Delta(f)^2.
```

If the contact number changes, then the echo fraction changes:

```math
f(k)=\frac{8-k}{8}.
```

So:

```math
f(0)=1,
```

```math
f(1)=\frac{7}{8},
```

```math
f(2)=\frac{6}{8}=\frac{3}{4}.
```

Using the same base tau value and shadow-projection structure, the toy model gives approximately:

```text
k = 0, f = 1       -> 1777.94287783 MeV
k = 1, f = 7/8     -> 1776.97039439 MeV
k = 2, f = 3/4     -> 1775.99817698 MeV
```

The observed Koide high-root benchmark used in the model is

```math
m_\tau^{Koide}=1776.96902708\ \mathrm{MeV}.
```

Therefore:

> If the tau shadow attached at two points instead of one, the tau-like mass would shift downward by about `0.97 MeV` from the `7/8` value and would no longer sit near the Koide high-root.

This makes the one-point contact geometrically necessary inside the toy model.

---

## 5. Prediction 3: vibration makes two-point contact unstable

In MCIFT, exchange strengthens when information states, vibration frequencies, and phases match:

```math
\Gamma_{ij}
= g
\exp\!\left[-\frac{(I_i-I_j)^2}{2\sigma_I^2}\right]
\exp\!\left[-\frac{(\omega_i-\omega_j)^2}{2\sigma_\omega^2}\right]
\cos^2(\phi_i-\phi_j).
```

This means two same-frequency origin-shadow contact points should not behave like two independent anchors. They should form a phase-locking bridge.

```text
one point = anchor
two points = bridge
bridge = phase-locking path
phase-locking path = beginning of origin-shadow merger
```

Prediction:

> Multi-contact shadows should be unstable. They should either merge with the original knot or lose independent shadow-echo behavior.

---

## 6. Prediction 4: the `7/8` fraction belongs specifically to the third mode

The same one-anchor rule gives

```math
B_n=\frac{C_n-1}{C_n}.
```

For the first few complexity modes:

```text
mode 1: C_1 = 2  -> B_1 = 1/2
mode 2: C_2 = 4  -> B_2 = 3/4
mode 3: C_3 = 8  -> B_3 = 7/8
mode 4: C_4 = 16 -> B_4 = 15/16
```

Prediction:

> The `7/8` echo is not universal. It is specific to the eight-sector third mode. Other stable modes should have different one-anchor shadow fractions.

This makes the tau-like mode special because it is the first mode whose one-anchor shadow echo is large enough to nearly saturate the Koide-like tau geometry.

---

## 7. Prediction 5: no clean fourth charged-lepton-like mode

The earlier MCIFT complexity-stability rule already suggests that the fourth mode fails or delocalizes because complexity overwhelms coherence.

The shadow-anchor rule adds another reason.

For a hypothetical fourth mode:

```math
C_4=16
```

and

```math
B_4=\frac{15}{16}.
```

This is a very high shadow-completion fraction. The model should therefore predict either:

```text
no stable fourth charged lepton
```

or:

```text
a broad unstable resonance, not a clean electron/muon/tau-like particle
```

Prediction:

> A clean fourth charged-lepton-like particle should not appear in the same stable family as electron, muon, and tau.

---

## 8. Prediction 6: shared-channel correction is tiny

The v0.6 objective shared-channel interpretation treats entanglement/shared-channel effects as small residual corrections to the main shadow-projection geometry.

For the tau echo-shadow correction:

```math
f_{ent}=\frac{7}{8}(1-E_3)
```

with

```math
E_3=0.0002008838.
```

That is only about

```text
0.02008838 percent.
```

Prediction:

> Shared-channel effects should appear as tiny cleanup terms, not dominant mass-generating terms.

The main mass geometry comes from shadow projection. The shared-channel effect only adjusts the remaining residual.

---

## 9. Prediction 7: changing channel distance should suppress the shared-channel correction

In the v0.6 shared-channel model, channel distance is

```math
d_c = |c_A-c_B|.
```

The shared-channel strength contains the factor

```math
\exp\!\left[-\frac{d_c^2}{2\sigma_c^2}\right].
```

Prediction:

> If channel distance is nonzero, the shared-channel correction should be suppressed exponentially.

In the saturated shared-channel limit:

```math
d_c=0
```

and the correction can approach

```math
E_3 \approx \lambda_3.
```

But when

```math
d_c \gg \sigma_c,
```

the correction should become negligible.

---

## 10. Strongest compact prediction set

```text
1. The stable tau shadow uses one anchor point.
2. Zero anchor gives no true shadow correction.
3. Two anchors create phase-locking and merger pressure.
4. Two-anchor geometry shifts the tau-like mass away from Koide.
5. The 7/8 echo is specific to the third mode because C_3 = 8.
6. A clean fourth charged-lepton-like mode should not appear.
7. Shared-channel corrections should be tiny residual terms.
8. Nonzero channel distance should suppress the shared-channel residual.
```

---

## 11. Caveat

These are predictions of the MCIFT toy model, not established physics. The current tau/Koide connection remains partly retrodictive because the tiny residual `E_3` is inferred from the Koide gap. The useful new step is that the one-point shadow-anchor rule makes concrete failure cases: zero contact, two-point contact, and higher-mode contact should not reproduce the same stable tau-like behavior.
