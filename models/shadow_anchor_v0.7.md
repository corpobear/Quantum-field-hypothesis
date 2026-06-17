# Shadow Anchor v0.7 Model Equations

**Version:** v0.7 model supplement  
**Status:** speculative toy-model equations; not established physics  
**Purpose:** collect the compact mathematical proof that vibration-created motion forces one-point shadow anchoring.

---

## 1. Tau knot complexity

The tau-like third mode is modeled as an eight-sector knot:

$$
C_3=2^3=8.
$$

---

## 2. Contact count

Let `K_8` be the original eight-sector knot and `S_8` its shadow.

Define the number of shared origin-shadow contact points:

$$
k=|K_8\cap S_8|.
$$

The independent shadow echo fraction is:

$$
B_8(k)=\frac{8-k}{8}.
$$

---

## 3. Connection requirement

A true shadow must be channel-anchored to its origin.

Therefore:

$$
k\ge1.
$$

If `k=0`, the shadow is an unanchored duplicate and cannot provide a stable correction.

---

## 4. Bridge count

Multiple contact points create pairwise origin-shadow bridges.

The number of contact bridges is:

$$
M(k)=\frac{k(k-1)}{2}.
$$

Thus:

$$
M(0)=0,
$$

$$
M(1)=0,
$$

$$
M(2)=1.
$$

So `k=2` is the first contact number that creates a bridge.

---

## 5. Vibration exchange

The MCIFT exchange-rate term is:

$$
\Gamma_{ij}
=
g
\exp\left[-\frac{(I_i-I_j)^2}{2\sigma_I^2}\right]
\exp\left[-\frac{(\omega_i-\omega_j)^2}{2\sigma_\omega^2}\right]
\cos^2(\phi_i-\phi_j).
$$

For bridge contact points `a` and `b`, define bridge resonance:

$$
R_{ab}=\Gamma_a\Gamma_b\cos^2(\phi_a-\phi_b).
$$

If:

$$
\phi_a\approx\phi_b,
$$

then:

$$
R_{ab}\ \text{is large}.
$$

---

## 6. Motion from directional exchange

Directional exchange is written:

$$
\vec{\Gamma}_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}\vec{d}_{ij}.
$$

Velocity is modeled by:

$$
\beta_n=\frac{v_n}{c_*}=\tanh(\eta|\vec{\Gamma}_n|).
$$

For the shadow-anchor problem, define the origin-directed merger-motion:

$$
v_{\mathrm{merge}}(k)
\propto
\sum_{a<b}^{k}R_{ab}.
$$

For `k=1`, there is no pair:

$$
v_{\mathrm{merge}}(1)=0.
$$

For `k=2`, there is one pair:

$$
v_{\mathrm{merge}}(2)\propto R_{12}>0
$$

when the bridge resonates.

---

## 7. Stability theorem

A stable shadow requires:

$$
k\ge1
$$

and:

$$
v_{\mathrm{merge}}(k)=0.
$$

The no-merger condition is satisfied when no contact bridges exist:

$$
M(k)=0.
$$

Since:

$$
M(k)=\frac{k(k-1)}{2},
$$

we have:

$$
M(k)=0 \quad\Rightarrow\quad k=0\ \text{or}\ k=1.
$$

But the connection requirement excludes `k=0`.

Therefore:

$$
k_*=1.
$$

---

## 8. Tau echo result

Using:

$$
B_8(k)=\frac{8-k}{8}
$$

and:

$$
k_*=1,
$$

we obtain:

$$
B_8(1)=\frac{8-1}{8}=\frac{7}{8}.
$$

Thus:

$$
f_0=B_8(1)=\frac{7}{8}.
$$

---

## 9. Failure cases

```text
k = 0 -> disconnected duplicate; no true shadow correction
k = 1 -> stable anchor; no merger bridge
k = 2 -> first vibrating bridge; merger-motion begins
k > 2 -> many bridges; shadow collapses toward origin
```

---

## 10. Compact proof chain

```text
shadow must touch origin -> k >= 1
multi-contact bridges create merger-motion -> require M(k)=0
M(k)=0 gives k=0 or k=1
k=0 is disconnected
therefore k=1
C_3=8 and k=1 -> 7/8
```

---

## 11. Caveat

This supplement is a mathematical consistency argument inside the MCIFT toy model. It is not a proof of real particle physics.
