# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy field model  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Version:** 0.7 vibration-motion shadow-anchor derivation

> This repository documents the original development of a speculative multi-channel information-field framework for cluster coherence, channel transfer, mass emergence, vibration/exchange densification, shadow-amplitude structure, shadow-projection geometry, one-point shadow anchoring, motion-by-exchange, vibration-driven shadow merger, entanglement/shared-amplitude correction, objective shared-channel geometry, predictions, and black-hole/channel confinement.

## Core idea

MCIFT proposes that physical reality can be modeled as a multi-channel information field:

```math
\Psi(x,y,z,t,c)
```

where `x, y, z` are spatial coordinates, `t` is time, and `c` is an internal channel coordinate.

In this framework:

- fundamental information-cells carry multiple internal channels,
- particles are coherent clusters of information-cells,
- light acts as a massless activation channel,
- internal vibration opens information-exchange channels between similar information-points,
- resonant information exchange creates densification,
- balanced internal exchange contributes to rest-mass formation,
- directional exchange creates motion,
- velocity increases total energy through a gamma-like motion factor,
- mass emerges when activated clusters enter a finite Higgs-response window,
- each visible information cluster may have a complementary inverted amplitude pattern,
- mass may be modeled as a squared visible/complementary amplitude imbalance,
- shadow projection may connect local knot geometry to Koide-like amplitude geometry,
- the tau-like shadow echo may follow from a one-point attached eight-sector shadow,
- vibration plus directional exchange explains why two-point shadow contact begins merger,
- entanglement is modeled as shared amplitude that can create a tiny mass defect,
- objective shared-channel geometry allows systems to be far in spacetime but adjacent in channel-space,
- channel transfer depends on coherence, complexity match, and mass/ripple-weight match,
- black holes or confined regions are modeled as complexity clusters that create internally separated channels.

## Research status

This is not presented as established physics or a replacement for quantum field theory. It is a speculative toy framework intended to become mathematically testable.

The immediate goals are:

1. define the field variable,
2. formalize channel transfer,
3. test cluster-coherence mass emergence,
4. derive or constrain the toy mass formula,
5. derive information exchange rate from knot geometry,
6. test whether shadow-amplitude geometry can connect MCIFT to Koide's square-root mass structure,
7. separate rest-mass formation from motion-energy effects,
8. derive the shadow echo-projection fraction from knot geometry,
9. prove why a stable vibrating shadow has exactly one anchor point,
10. derive the entanglement/shared-amplitude mass-defect factor from inter-knot exchange geometry,
11. derive channel-distance geometry and explain why shared-channel correlation is not automatically usable as controllable nonlocal messaging,
12. identify falsifiable predictions.

## Repository layout

```text
paper/main.md                                  Full theory draft
paper/v0.7_shadow_anchor_derivation.md         Paper addendum for one-point shadow-anchor derivation
models/toy_model.md                             Current toy-model equations
notes/channel_transfer.md                       Channel transfer and rain/ripple analogy
notes/information_exchange.md                   Law of vibration and exchange-rate densification
notes/shadow_amplitude.md                       Shadow/complementary amplitude extension
notes/shadow_projection.md                      Shadow projection geometry and Koide comparison
notes/shadow_anchor_vibration.md                One-point attached shadow and vibration bridge note
notes/vibration_motion_shadow_merger.md         v0.7 derivation: vibration creates motion, motion merges multi-contact shadows
notes/entanglement_shared_amplitude.md          Entanglement as shared amplitude and mass defect
notes/objective_shared_channels.md              Objective shared-channel geometry
notes/motion_exchange.md                        Motion from directional exchange
notes/black_holes.md                            Black-hole internal-channel interpretation
notes/predictions.md                            Predictions and falsifiability notes
predictions/shadow_anchor_predictions.md        Shadow-anchor prediction set
tests/report_v0.1.md                            Initial toy-model test report
tests/report_v0.2.md                            Exchange-rate and shadow-amplitude calculations
tests/report_v0.3.md                            Motion-by-exchange calculation
tests/report_v0.4.md                            Shadow projection and Koide comparison
tests/report_v0.5.md                            Entanglement shared-amplitude correction
tests/report_v0.6.md                            Objective shared-channel entanglement
tests/report_v0.7.md                            Vibration-motion shadow-anchor derivation
NOTICE.md                                       Authorship and priority notice
LICENSE_PENDING.md                              Licensing note
```

## Central claim

> Mass is not given to isolated information. Mass emerges when information clusters become coherent, activated, internally resonant, and able to transfer into the Higgs-response channel.

## v0.2 update

The v0.2 extension adds two speculative mechanisms:

1. **Information exchange rate:** similar information-points vibrating at compatible frequencies open stronger internal communication channels. This produces resonance and densification.
2. **Shadow/complementary amplitude:** mass may be calculated as the square of an amplitude imbalance between a visible information cluster and a complementary inverted information pattern.

This moves the toy model toward amplitude-level calculations:

```math
A_n=\sqrt{m_n}
```

rather than only direct mass fitting.

## v0.3 update

The v0.3 extension separates rest mass from motion-energy:

```text
balanced internal vibratory exchange -> rest mass / densification
directional exchange -> velocity
velocity -> total effective energy increase
```

The compact motion update is:

```math
m_{eff,n}=\gamma_nm_{0,n}
```

where:

```math
\beta_n=\tanh(\eta|\vec{\Gamma}_n|)
```

and:

```math
\gamma_n=\cosh(\eta|\vec{\Gamma}_n|)
```

## v0.4 update

The v0.4 extension tests shadow projection against Koide.

For the tau-like third mode:

```math
C_3=8
```

The shadow-projection toy model uses:

```math
\Delta(f)=1+\frac{1}{56}+f\frac{1}{448}
```

and:

```math
m_\tau(f)=m_\tau^{base}\Delta(f)^2
```

The `2/3` echo-shadow projection gives:

```math
m_\tau^{2/3}=1775.35017984\ \text{MeV}
```

The `7/8` echo-shadow projection gives:

```math
m_\tau^{7/8}=1776.97039439\ \text{MeV}
```

This is almost identical to the Koide high-root value:

```math
m_\tau^{Koide}=1776.96902708\ \text{MeV}
```

Interpretation:

```text
2/3 = global Koide amplitude-angle projection
7/8 = local tau echo-shadow completion fraction
```

## v0.5 update

The v0.5 extension adds entanglement as a tiny shared-amplitude mass-defect correction.

The general toy entanglement strength is:

```math
\mathcal{E}_{AB}=O_{AB}\tanh\left(\frac{\Gamma_{AB}}{\Gamma_c}\right)
```

and the shared-amplitude mass-defect rule is:

```math
m_{AB}=m_A+m_B-2\epsilon\mathcal{E}_{AB}\sqrt{m_A m_B}
```

For the tau echo-shadow correction:

```math
f_{ent}=\frac{7}{8}(1-E_3)
```

with:

```math
E_3=0.0002008838
```

or:

```text
0.02008838 percent
```

Then:

```math
\Delta_{ent}=1+\frac{1}{56}+0.8748242267\frac{1}{448}=1.0198098755
```

and:

```math
m_\tau^{ent}=1776.96902708\ \text{MeV}
```

This matches the Koide high-root tau value by construction, because `E_3` is inferred from the remaining Koide residual.

## v0.6 update

The v0.6 extension adds objective shared-channel geometry.

Define spatial distance:

```math
d_x=|x_A-x_B|
```

Define channel distance:

```math
d_c=|c_A-c_B|
```

Two systems can be far in ordinary space but adjacent in channel-space:

```math
d_x\gg0
```

```math
d_c=0
```

The updated entanglement strength is:

```math
\mathcal{E}_{AB}
=
\lambda_{AB}
O_{AB}
\exp\left[-\frac{d_c^2}{2\sigma_c^2}\right]
\tanh\left(\frac{\Gamma_{AB}}{\Gamma_c}\right)
```

For the tau echo-shadow correction, the shared-channel interpretation is:

```math
E_3
=
\lambda_3
O_3
\exp\left[-\frac{d_c^2}{2\sigma_c^2}\right]
\tanh\left(\frac{\Gamma_3^{shared}}{\Gamma_c}\right)
```

In the shared-channel saturated limit:

```math
d_c=0,\quad O_3\approx1,\quad \tanh\left(\frac{\Gamma_3^{shared}}{\Gamma_c}\right)\approx1
```

so:

```math
E_3\approx\lambda_3=0.0002008838
```

This gives the same Koide-matching tau value as v0.5, but with a clearer mechanism:

```text
spatial distance controls ordinary signals
channel distance controls entangled correlation
zero channel-distance -> objective shared state
```

Important caveat:

```text
shared channel -> instant correlation
shared channel != controllable nonlocal messaging
```

## v0.7 update

The v0.7 extension derives the one-point shadow anchor from vibration-created motion.

Let `K_8` be the original eight-sector tau knot and `S_8` its shadow. Define the number of shared contact points:

```math
k=|K_8\cap S_8|
```

A true shadow must be connected:

```math
k\ge1
```

but a stable shadow must not create merger-motion back into the origin.

Multiple contact points create pairwise vibrating bridges:

```math
M(k)=\frac{k(k-1)}{2}
```

A single contact point gives no bridge:

```math
M(1)=0
```

Two contact points create the first bridge:

```math
M(2)=1
```

In the motion sector, directional exchange creates velocity. Therefore a vibrating bridge can create origin-directed merger-motion:

```math
v_{\mathrm{merge}}(k)\propto\sum_{a<b}^{k}R_{ab}
```

So a stable shadow must satisfy:

```math
k\ge1
```

and:

```math
M(k)=0
```

The only solution is:

```math
k=1
```

For the tau-like third mode:

```math
C_3=8
```

and the independent shadow echo becomes:

```math
B_8(1)=\frac{8-1}{8}=\frac{7}{8}
```

Compact interpretation:

```text
connection requirement -> k >= 1
no-merger-motion requirement -> k <= 1
therefore k = 1
therefore 7/8 for C_3 = 8
```

This does not prove real particle physics, but it turns the `7/8` echo into an internal consequence of MCIFT's own assumptions: vibration creates directional exchange, directional exchange creates motion, and motion merges a multi-contact shadow into its origin.

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
