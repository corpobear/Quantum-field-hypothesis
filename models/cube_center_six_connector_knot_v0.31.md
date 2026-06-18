# Cube-Center Six-Connector Knot Model v0.31

**Status:** speculative MCIFT geometry note; not established physics.  
**Purpose:** formalize the cube-centered six-connector picture for knots, anchor states, coherence capacity, and containment failure.

---

## 1. Core picture

A knot is placed at the exact center of a spacetime cube-cell:

```text
knot position = center of cube-cell
```

Each knot has six axial connector directions through the cube faces:

```text
+x, -x, +y, -y, +z, -z
```

Each connector links the center of one cube-cell to the center of a neighboring cube-cell.

A connector may be:

```text
inactive
partially active
fully active
```

This gives a connector activation variable:

```text
0 <= a_mu <= 1
```

where:

```text
a_mu = 0   inactive
a_mu = 1   fully active
0<a_mu<1   partially active
```

---

## 2. Six connector states

For knot `i`, define six connector activations:

```text
a_i,+x
a_i,-x
a_i,+y
a_i,-y
a_i,+z
a_i,-z
```

or compactly:

```text
a_i,mu ,  mu in {+x,-x,+y,-y,+z,-z}
```

The total connector activation is:

```text
A_i,total = sum_mu a_i,mu
```

The mean connector activation is:

```text
a_i,mean = (1/6) sum_mu a_i,mu
```

---

## 3. Directional balance

A centered knot is strongest when opposite connectors balance each other.

Directional imbalance:

```text
Delta_i = sqrt[(a_+x-a_-x)^2 + (a_+y-a_-y)^2 + (a_+z-a_-z)^2]
```

Perfect directional balance:

```text
a_+x = a_-x
a_+y = a_-y
a_+z = a_-z
Delta_i = 0
```

A large imbalance means the knot is being pulled away from cube-center containment.

---

## 4. Coherence capacity

The six connectors supply coherence capacity.

First local connector capacity:

```text
Coh_i = 6 a_i,mean - lambda_Delta Delta_i
```

where `lambda_Delta` is a penalty for directional imbalance.

For a balanced knot:

```text
Coh_i = 6 a_i,mean
```

For an imbalanced knot:

```text
Coh_i < 6 a_i,mean
```

---

## 5. Complexity contained by the knot

Let the knot contain internal complexity:

```text
Q_i
```

The basic containment condition is:

```text
coherence capacity >= contained complexity
```

or:

```text
S_i = Coh_i - Q_i
```

Stable/open knot:

```text
S_i >= 0
```

Containment failure / collapsed-knot condition:

```text
S_i < 0
```

Plain statement:

```text
A collapsed-knot sink forms when the coherence supplied by the six connector anchors is not enough to contain the complexity held by the knot.
```

---

## 6. Relation to MCIFT stability mechanics

The older MCIFT stability form is:

```text
C_n = 2^n
S_n = 3.5 n X_n - C_n
```

The cube-center connector picture makes this geometric:

```text
C_n                         contained complexity
3.5 n X_n                   abstract coherence capacity
six connector activations    local geometric coherence support
Delta_i                     imbalance / off-center strain
```

A geometry-aware containment score can therefore be written as:

```text
S_contain = 3.5 n X_n Coh_i - C_n Load_i
```

where `Load_i` may include mass/gravity time load, thermal pressure, and local exchange strain.

---

## 7. Connector dynamics

Connector activations can evolve:

```text
d a_i,mu / dt = source_on - strain_off - thermal_noise - overload_loss
```

One schematic form:

```text
d a_i,mu / dt = alpha Compatibility_i,mu (1-a_i,mu)
              - beta Strain_i,mu a_i,mu
              - gamma Thermal_i a_i,mu
              - zeta Overload_i a_i,mu
```

Interpretation:

```text
compatibility strengthens a connector
strain weakens a connector
thermal/noise disrupts retention
overload appears when contained complexity exceeds coherence capacity
```

---

## 8. Neighbor coupling

For neighboring cube-center knots `i` and `j`, the connector between them has a symmetric effective activation:

```text
A_ij = sqrt(a_i,mu a_j,-mu)
```

The connection is strongest when both knots agree on the same shared direction.

If either side is inactive:

```text
A_ij = 0
```

If both sides are fully active:

```text
A_ij = 1
```

If one or both sides are partial:

```text
0 < A_ij < 1
```

---

## 9. Six internal sectors and four projected channels

The cube-center model naturally gives six internal axial connector sectors:

```text
+x, -x, +y, -y, +z, -z
```

In a rotating or projected system, not all six internal directions need remain separately resolved. Depending on anchor-axis selection and spin blur, the observable transverse response can reduce toward four effective transverse channels.

This supports the prior MCIFT distinction:

```text
six internal connector sectors
four effective projected transverse growth channels
```

---

## 10. Role in collapse-containment

This model clarifies the collapse rule used in the cosmology scaffold.

Collapse is not defined as simply "mass is high." Collapse is defined as:

```text
contained complexity > available coherence capacity
```

In cube-center language:

```text
six connector anchors fail to hold the knot centered and open
```

The excess can then be transferred into:

```text
B = collapsed-knot reservoir
```

Future dynamic versions should couple `B(k,a)` directly into the perturbation equations.

---

## 11. Safe wording

Safe:

```text
MCIFT can be visualized as a cube-centered six-connector information geometry, where each knot sits at a cube-cell center and coherence is supplied by six axial connector states to neighboring cube centers.
```

Safe:

```text
A connector is a partial anchor/coherence coupling, not a classical on/off wire.
```

Safe:

```text
Collapse-containment occurs when the six-connector coherence capacity cannot hold the knot's contained complexity.
```

Not safe:

```text
This proves spacetime is literally a cubic lattice.
This proves black-hole physics.
This replaces standard quantum theory or Lambda-CDM.
```
