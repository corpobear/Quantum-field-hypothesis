# Vibration-Motion Shadow Merger Derivation

**Version:** v0.7 speculative derivation  
**Status:** toy-model proof sketch; not established physics  
**Purpose:** derive the one-point shadow-anchor rule from vibration-created motion and motion-driven origin-shadow merger.

---

## 1. Core claim

The shadow of a coherent information knot must satisfy two conditions:

```text
1. It must touch the origin at least once to remain correlated.
2. It must not create merger-motion back into the origin.
```

The first condition requires a nonzero contact count:

```math
k \ge 1.
```

The second condition forbids multiple vibrating contact points, because two or more contact points create a bridge. A vibrating bridge can create directional exchange. Directional exchange creates motion. That motion begins merging the shadow into the original.

Therefore the only stable contact count is:

```math
k=1.
```

For the tau-like eight-sector knot, this forces the independent shadow echo fraction:

```math
B_8(1)=\frac{8-1}{8}=\frac{7}{8}.
```

---

## 2. Contact count

Let the original eight-sector knot be `K_8` and its shadow be `S_8`.

Define the contact count:

```math
k = |K_8 \cap S_8|.
```

The independent shadow echo fraction is:

```math
B_8(k)=\frac{8-k}{8}.
```

The question is not merely how to compute `B_8(k)`. The deeper question is why stable geometry selects `k=1`.

---

## 3. Zero contact fails

If

```math
k=0,
```

then

```math
K_8 \cap S_8 = \varnothing.
```

The shadow is disconnected from the origin. It has no anchor and no channel gate.

```text
k = 0 -> no anchor -> no channel gate -> no stable shadow correction
```

Thus a real shadow requires:

```math
k \ge 1.
```

---

## 4. Multiple contact points create bridges

A single contact point anchors the shadow, but it does not define a bridge.

Two contact points define the first possible bridge.

For `k` contact points, the number of pairwise origin-shadow bridges is:

```math
M(k)=\frac{k(k-1)}{2}.
```

Therefore:

```math
M(0)=0,
```

```math
M(1)=0,
```

```math
M(2)=1,
```

```math
M(3)=3.
```

So `k=2` is the first contact number that creates a bridge.

Plainly:

```text
one point = anchor only
two points = first bridge
three points = three bridges
```

---

## 5. Vibration turns a bridge into directional exchange

In MCIFT, exchange is strongest when information states, vibration frequencies, and phases align:

```math
\Gamma_{ij}
=
g
\exp\left[-\frac{(I_i-I_j)^2}{2\sigma_I^2}\right]
\exp\left[-\frac{(\omega_i-\omega_j)^2}{2\sigma_\omega^2}\right]
\cos^2(\phi_i-\phi_j).
```

For two origin-shadow contact points `a` and `b`, define a bridge resonance strength:

```math
R_{ab}=\Gamma_a\Gamma_b\cos^2(\phi_a-\phi_b).
```

If the two contact points vibrate at similar phase:

```math
\phi_a \approx \phi_b,
```

then:

```math
\cos^2(\phi_a-\phi_b)\approx 1,
```

and the bridge becomes strong.

A strong bridge creates directional exchange along the origin-shadow connection.

---

## 6. Directional exchange creates motion

The motion sector of MCIFT treats directional exchange as the source of velocity.

For a knot:

```math
\vec{\Gamma}_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}\vec{d}_{ij}.
```

The bounded velocity rule is:

```math
\beta_n=\frac{v_n}{c_*}=\tanh(\mu_n),
```

where:

```math
\mu_n=\eta|\vec{\Gamma}_n|.
```

For the shadow-anchor problem, define merger-motion as the motion component directed from shadow back toward origin:

```math
v_{\mathrm{merge}}(k)
\propto
\sum_{a<b}^{k} R_{ab}.
```

This sum runs over contact-point pairs. Therefore it depends on bridges, not isolated anchors.

For one contact point:

```math
v_{\mathrm{merge}}(1)=0,
```

because there is no contact pair.

For two contact points:

```math
v_{\mathrm{merge}}(2)\propto R_{12}>0,
```

if the two points have nonzero resonance.

Thus two-point contact creates the first nonzero merger-motion.

---

## 7. Stability proof

A stable shadow must obey both conditions:

```math
k \ge 1
```

and

```math
v_{\mathrm{merge}}(k)=0.
```

Since

```math
v_{\mathrm{merge}}(k)
\propto
\sum_{a<b}^{k} R_{ab},
```

and the first pair exists only when `k=2`, the no-merger condition is equivalent to:

```math
M(k)=\frac{k(k-1)}{2}=0.
```

This equation is true only for:

```math
k=0
```

or

```math
k=1.
```

But `k=0` violates the connection requirement.

Therefore the only stable shadow anchor is:

```math
k=1.
```

This is the minimal stable shadow-anchor theorem.

---

## 8. Tau consequence

For the tau-like third mode:

```math
C_3=2^3=8.
```

The independent shadow echo fraction is:

```math
B_8(k)=\frac{8-k}{8}.
```

Because stability forces

```math
k=1,
```

we obtain:

```math
B_8(1)=\frac{8-1}{8}=\frac{7}{8}.
```

Thus the `7/8` echo is not only a chosen fraction. Inside the v0.7 toy geometry, it follows from:

```text
connection requirement -> k >= 1
no-merger-motion requirement -> k <= 1
therefore k = 1
therefore 7/8 for C_3 = 8
```

---

## 9. Physical-language interpretation

The shadow is a channel-making companion geometry. It must touch the source to know which source it shadows.

But if it touches twice, vibration can phase-lock the two contacts. Phase-locking produces directional exchange along the bridge. Directional exchange produces motion. That motion drives merger of shadow and origin.

Therefore:

> One point anchors the shadow. Two points create a vibrating bridge. A vibrating bridge creates merger-motion. So a stable shadow can touch only once.

---

## 10. Relation to predictions

This derivation supports the predictions that:

```text
1. zero anchor gives no true shadow correction,
2. one anchor gives stable shadow echo,
3. two anchors create phase-locking and merger pressure,
4. two-anchor geometry shifts the tau-like mass away from Koide,
5. the 7/8 tau echo is specific to C_3 = 8 plus k = 1.
```

---

## 11. Caveat

This is an internal derivation inside the MCIFT toy model. It does not prove real particle physics. Its purpose is to turn the one-anchor rule into a mathematical consequence of the model's own assumptions: vibration creates directional exchange, directional exchange creates motion, and motion merges a multi-contact shadow into its origin.
