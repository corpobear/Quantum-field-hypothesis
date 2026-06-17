# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy field model  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Version:** 0.4 shadow-projection and Koide-comparison update  

> This repository documents the original development of a speculative multi-channel information-field framework for cluster coherence, channel transfer, mass emergence, vibration/exchange densification, shadow-amplitude structure, shadow-projection geometry, motion-by-exchange, and black-hole/channel confinement.

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
9. identify falsifiable predictions.

## Repository layout

```text
paper/main.md                    Full theory draft
models/toy_model.md               Current toy-model equations
notes/channel_transfer.md         Channel transfer and rain/ripple analogy
notes/information_exchange.md     Law of vibration and exchange-rate densification
notes/shadow_amplitude.md         Shadow/complementary amplitude extension
notes/shadow_projection.md        Shadow projection geometry and Koide comparison
notes/motion_exchange.md          Motion from directional exchange
notes/black_holes.md              Black-hole internal-channel interpretation
notes/predictions.md              Predictions and falsifiability notes
tests/report_v0.1.md              Initial toy-model test report
tests/report_v0.2.md              Exchange-rate and shadow-amplitude calculations
tests/report_v0.3.md              Motion-by-exchange calculation
tests/report_v0.4.md              Shadow projection and Koide comparison
NOTICE.md                         Authorship and priority notice
LICENSE_PENDING.md                Licensing note
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

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
