# Shadow Anchor Vibration Note

**Version:** v0.6.2 speculative extension  
**Status:** toy-model geometry; not established physics  
**Purpose:** explain why the tau shadow echo can naturally take the form `7/8` when the shadow is attached to the original eight-sector knot by exactly one vibrating anchor point.

---

## 1. Starting point

In the current MCIFT toy model, the tau-like third mode has complexity

$$
C_3 = 2^3 = 8.
$$

The shadow projection previously used the local echo fraction

$$
f_0 = 1 - \frac{1}{C_3} = \frac{7}{8}.
$$

This note gives a geometric reason for that fraction.

The proposed interpretation is:

> The tau knot is an eight-sector closed information knot. Its shadow remains connected to the original knot at one shared anchor point. That anchor point is not an independent echo sector; it is the channel-gate connecting origin and shadow. The remaining seven sectors form the independent shadow echo.

---

## 2. One-point attached shadow

Let the original eight-sector knot be

$$
K_8 = \{p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8\}.
$$

Let its shadow be

$$
S_8 = \{s_1,s_2,s_3,s_4,s_5,s_6,s_7,s_8\}.
$$

Assume the shadow shares one anchor point with the original:

$$
K_8 \cap S_8 = \{p_*\}.
$$

That shared point is not counted as an independent shadow echo, because it already belongs to the original-shadow bridge.

The independent shadow sector count is therefore

$$
N_{\mathrm{echo}} = C_3 - 1 = 7.
$$

The independent shadow completion is

$$
B_3 = \frac{N_{\mathrm{echo}}}{C_3}
    = \frac{C_3 - 1}{C_3}
    = \frac{7}{8}.
$$

So the old tau echo factor can be reinterpreted as

$$
f_0 = B_3.
$$

Plainly:

```text
7/8 = independent shadow echo
1/8 = shared anchor point
```

The missing `1/8` is not destroyed. It is the common point where origin and shadow touch.

---

## 3. Why not zero points?

If the shadow does not touch the original knot, then

$$
K_8 \cap S_8 = \varnothing.
$$

The formal echo count would be

$$
B_3(0) = \frac{8}{8} = 1.
$$

But this is not a true shadow in the model. It is an unanchored duplicate.

Without a shared anchor:

```text
no touch -> no channel gate
no channel gate -> no origin-shadow correlation
no correlation -> no stable shadow correction
```

A disconnected shadow cannot reliably correct the original knot because it has no defined channel relation to it.

Thus `k = 0` gives duplication, not shadowing.

---

## 4. Why not two points?

Now add vibration.

In MCIFT, exchange is strongest when information states and vibration frequencies are similar. A simplified exchange term has the form

$$
\Gamma_{ij}
= g
\exp\!\left[-\frac{(I_i-I_j)^2}{2\sigma_I^2}\right]
\exp\!\left[-\frac{(\omega_i-\omega_j)^2}{2\sigma_\omega^2}\right]
\cos^2(\phi_i-\phi_j).
$$

So if two origin-shadow contact points vibrate at similar frequency and phase, they do not merely touch. They begin to phase-lock.

One shared point gives an anchor:

```text
one point -> correlation without merger
```

Two shared points define a bridge:

```text
two points -> vibrating bridge -> phase-locking path -> merger begins
```

Geometrically:

```text
one point fixes contact
two points fix alignment
```

With vibration:

```text
one shared node = stable anchor
two shared nodes = resonance bridge
```

A resonance bridge reduces the independence of the shadow. The shadow begins to merge with the origin instead of remaining a separate echo.

---

## 5. Contact-count rule

Let

$$
k = |K_8 \cap S_8|
$$

be the number of shared origin-shadow contact points.

The independent echo fraction is

$$
B_8(k)=\frac{8-k}{8}.
$$

The cases are:

```text
k = 0 -> disconnected duplicate, not a shadow
k = 1 -> stable one-point anchored shadow
k = 2 -> first resonance bridge; merger begins
k > 2 -> many resonance bridges; shadow collapses toward origin
k = 8 -> total merger; no independent shadow echo
```

For `k = 1`,

$$
B_8(1) = \frac{8-1}{8} = \frac{7}{8}.
$$

This is the desired tau echo fraction.

---

## 6. Merger-pressure argument

The reason two points are dangerous is that multiple contact points create pairwise vibrating bridges.

For `k` shared contact points, the number of pairwise bridges is

$$
M(k)=\frac{k(k-1)}{2}.
$$

For one contact point:

$$
M(1)=0.
$$

So there is no bridge along which the origin and shadow can phase-lock.

For two contact points:

$$
M(2)=1.
$$

This is the first possible merger bridge.

For three contact points:

$$
M(3)=3.
$$

The merger pressure grows quickly.

A toy shadow-stability function can therefore be written as

$$
\mathcal{S}_{\mathrm{shadow}}(k)
= \alpha k
- \beta\frac{k(k-1)}{2}
- \frac{\gamma}{k+1}.
$$

Interpretation:

- `+ alpha k`: contact gives correlation.
- `- beta k(k-1)/2`: multiple contacts create resonance bridges and merger pressure.
- `- gamma/(k+1)`: too little contact leaves the shadow unanchored.

Under the minimal-anchor condition, the preferred stable contact number is

$$
k_* = 1.
$$

This gives an anchored shadow with no merger bridge.

---

## 7. Minimal stable shadow anchoring principle

The proposed principle is:

> A vibrating shadow must touch the origin at least once to remain correlated, but two or more same-frequency contact points create phase-locked bridges that begin origin-shadow merger. Therefore the stable shadow uses the smallest nonzero contact: one shared point.

This forces

$$
k=1
$$

and therefore, for the eight-sector tau knot,

$$
f_0 = \frac{8-1}{8}=\frac{7}{8}.
$$

---

## 8. Interpretation

The shadow is not merely absence. It is a channel-making companion geometry.

```text
original knot = source structure
shadow knot = complementary echo structure
shared point = channel anchor
remaining seven sectors = independent echo body
```

Thus:

> The shadow creates channels by touching the original knot at one vibrating anchor point. One point is enough to keep the shadow correlated; two points create a vibrating bridge and start merger. The one-point rule leaves seven independent sectors out of eight, giving the `7/8` tau echo.

---

## 9. Caveat

This is a speculative internal consistency argument for the MCIFT toy model. It is not a proof of real particle physics. Its purpose is to turn the `7/8` tau echo from a fitted-looking fraction into a geometric consequence of one-point shadow anchoring plus vibration-induced merger pressure.
