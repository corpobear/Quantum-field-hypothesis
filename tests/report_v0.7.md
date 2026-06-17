# Test Report v0.7 — Vibration-Motion Shadow Anchor Derivation

**Status:** speculative toy-model derivation / falsifiability report  
**Scope:** one-point shadow anchoring, vibration-created motion, and two-point merger failure  
**Main result:** inside the toy model, stable shadow anchoring forces `k = 1`, which gives the tau echo fraction `7/8` for `C_3 = 8`.

---

## 1. Question tested

Can the one-point shadow-anchor rule be derived rather than assumed?

Earlier notes proposed:

$$
f_0 = \frac{7}{8}
$$

for the tau-like third mode because:

$$
C_3=8
$$

and the shadow shares one point with the origin.

The v0.7 question is deeper:

> Why does the shadow share exactly one point, not zero or two?

---

## 2. Model assumptions

The derivation uses three assumptions already present in the MCIFT toy framework.

### Assumption A — a true shadow must be connected

A shadow with no contact is an unanchored duplicate, not a real shadow.

$$
k \ge 1
$$

where

$$
k=|K_8\cap S_8|.
$$

### Assumption B — vibration opens exchange

Exchange strengthens when information states, vibration frequencies, and phases align:

$$
\Gamma_{ij}
=
g
\exp\left[-\frac{(I_i-I_j)^2}{2\sigma_I^2}\right]
\exp\left[-\frac{(\omega_i-\omega_j)^2}{2\sigma_\omega^2}\right]
\cos^2(\phi_i-\phi_j).
$$

### Assumption C — directional exchange creates motion

Directional exchange gives a velocity-like motion term:

$$
\vec{\Gamma}_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}\vec{d}_{ij}
$$

and

$$
\beta_n=\frac{v_n}{c_*}=\tanh(\eta|\vec{\Gamma}_n|).
$$

---

## 3. Bridge-count test

If a shadow has `k` contact points with the original knot, the number of pairwise contact bridges is:

$$
M(k)=\frac{k(k-1)}{2}.
$$

Values:

```text
k = 0 -> M = 0
k = 1 -> M = 0
k = 2 -> M = 1
k = 3 -> M = 3
k = 4 -> M = 6
```

Interpretation:

```text
one contact point = anchor only
two contact points = first bridge
three contact points = multiple bridges
```

Thus two points are the first geometry that can create a vibrating origin-shadow bridge.

---

## 4. Merger-motion test

Define bridge resonance between two contact points `a` and `b`:

$$
R_{ab}=\Gamma_a\Gamma_b\cos^2(\phi_a-\phi_b).
$$

Define merger-motion as the origin-directed motion created by all contact bridges:

$$
v_{\mathrm{merge}}(k)
\propto
\sum_{a<b}^{k}R_{ab}.
$$

Then:

$$
v_{\mathrm{merge}}(1)=0
$$

because there is no pair of contact points.

But:

$$
v_{\mathrm{merge}}(2)\propto R_{12}>0
$$

whenever the two contact points resonate.

So two-point contact creates the first nonzero merger-motion.

---

## 5. Stability condition

A stable shadow must satisfy:

$$
k\ge1
$$

and

$$
v_{\mathrm{merge}}(k)=0.
$$

Since merger-motion appears when pairwise bridges exist, the no-merger condition requires:

$$
M(k)=0.
$$

That means:

$$
\frac{k(k-1)}{2}=0.
$$

Solutions:

$$
k=0
$$

or

$$
k=1.
$$

But `k=0` violates the connection requirement.

Therefore:

$$
k_*=1.
$$

This is the minimal stable shadow-anchor result.

---

## 6. Tau consequence

The independent shadow echo fraction is:

$$
B_8(k)=\frac{8-k}{8}.
$$

With the stable value:

$$
k=1,
$$

we get:

$$
B_8(1)=\frac{8-1}{8}=\frac{7}{8}.
$$

Thus the tau echo fraction follows from:

```text
connection requirement + no-merger-motion requirement
```

rather than being inserted only as a numerical guess.

---

## 7. Failure cases

### Case `k = 0`

```text
no contact -> no channel gate -> no real shadow correction
```

### Case `k = 1`

```text
one contact -> stable anchor -> no bridge -> no merger-motion
```

### Case `k = 2`

```text
two contacts -> first bridge -> phase-locking -> merger-motion
```

### Case `k > 2`

```text
many contacts -> many bridges -> accelerated merger pressure
```

---

## 8. Prediction check

The model predicts that if the tau shadow geometry were forced into two-contact form, the echo fraction would become:

$$
f(2)=\frac{6}{8}=\frac{3}{4}.
$$

Using the same shadow-projection correction structure, this shifts the tau-like mass away from the Koide high-root by roughly `0.97 MeV` compared with the `7/8` case.

Therefore, the one-point anchor is not decorative. It is structurally required inside the toy model.

---

## 9. Result

The v0.7 derivation gives the clean proof stack:

```text
A shadow must be connected -> k >= 1
A stable shadow cannot have merger-motion -> M(k)=0
M(k)=0 allows k=0 or k=1
k=0 is disconnected
therefore k=1
C_3=8 and k=1 -> 7/8
```

---

## 10. Caveat

This is not a proof of real particle physics. It is an internal consistency derivation inside MCIFT. The next step is to connect this proof to a full field equation, dimensional scales, and independent experimental predictions.
