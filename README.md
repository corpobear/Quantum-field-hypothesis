# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy field model  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** 0.11 normalized fourth-mode reservoir field-source test

> This is not established physics and is not a replacement for quantum field theory. It is a speculative framework being developed into a more testable mathematical toy model.

---

## Core idea

MCIFT models physical reality as a multi-channel information field:

```math
\Psi(x,y,z,t,c)
```

where `x,y,z` are spatial coordinates, `t` is time, and `c` is an internal channel coordinate.

The current research chain is:

```text
coherent information cluster
-> original/shadow knot structure
-> one-point anchor
-> 7/8 free spin-vortex fraction
-> Fibonacci-shaped anchor-tip source
-> Higgs-response resonance overlap
-> funnel-speed capture window
-> bounded fourth-mode reservoir availability
-> accumulated mass amplitude
-> squared rest mass
```

---

## Current v0.11 field-source equation

The latest source equation is:

```math
\left(\partial_t^2-c_*^2\nabla^2-D_c\partial_c^2+V'(\psi)\right)\psi
=
\sum_a S_{tip,a}
```

with:

```math
S_{tip,a}
=
\lambda_a
\Omega_{OS,a}
W_v(v_{tip,a})
\left[
P_{C_a}+B_{C_a}(1)E_{C_a}\langle O_{\varphi,a}\rangle\right]
R_{4,a}^{gate}
\delta_{\epsilon,a}^{(\varphi)}.
```

The fourth-mode reservoir is bounded by:

```math
R_4^{gate}=\frac{R_4}{R_4+R_*}.
```

This keeps the reservoir contribution finite:

```math
0\le R_4^{gate}\le1.
```

Interpretation:

```text
reservoir -> bounded availability
funnel aperture -> tiny captured fraction
Higgs overlap -> conversion condition
speed window -> capture/scatter condition
knot -> amplitude accumulator
mass -> squared amplitude
```

---

## Latest reduced test

The v0.11 integrated field-source test uses:

```math
\Sigma_\tau
=
W_v
\left[
\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
\right]
R_4^{gate}
```

and:

```math
m_\tau=m_\tau^{base}(1+\Sigma_\tau)^2.
```

At:

```math
W_v=1,
```

```math
R_4^{gate}=1,
```

```math
\langle O_\varphi\rangle=0.9837806705,
```

the reduced tau-like result is:

```math
m_\tau=1776.86\ \mathrm{MeV}.
```

---

## Repository layout

```text
paper/main.md                                  Full theory draft
paper/README.md                                Paper folder index
paper/v0.7_shadow_anchor_derivation.md         One-point shadow-anchor paper addendum
paper/v0.11_field_source_reservoir_addendum.md Bounded reservoir field-source paper addendum

models/toy_model.md                            Current toy-model equations
models/shadow_anchor_v0.7.md                   Compact v0.7 shadow-anchor equations
models/spin_vortex_anchor_v0.8.md              One-anchor spin-vortex correction
models/fibonacci_higgs_source_v0.9.md          Fibonacci-Higgs anchor-tip source equation
models/funnel_speed_capture_v0.10.md           Funnel-speed capture-window model
models/field_source_reservoir_v0.11.md         Bounded reservoir source normalization

notes/channel_transfer.md                      Channel transfer and rain/ripple analogy
notes/information_exchange.md                  Vibration and exchange-rate densification
notes/shadow_amplitude.md                      Shadow/complementary amplitude extension
notes/shadow_projection.md                     Shadow projection and Koide comparison
notes/shadow_anchor_vibration.md               One-point attached shadow and vibration bridge note
notes/vibration_motion_shadow_merger.md        Vibration creates motion and multi-contact merger
notes/spin_vortex_anchor.md                    One-anchor spin-vortex interpretation
notes/fourth_mode_reservoir_normalization.md   Bounded fourth-mode reservoir normalization
notes/v0.11_update_index.md                    v0.11 quick update index
notes/entanglement_shared_amplitude.md         Entanglement as shared amplitude and mass defect
notes/objective_shared_channels.md             Objective shared-channel geometry
notes/motion_exchange.md                       Motion from directional exchange
notes/black_holes.md                           Black-hole internal-channel interpretation
notes/predictions.md                           Predictions and falsifiability notes

predictions/shadow_anchor_predictions.md       Shadow-anchor prediction set

tests/README.md                                Test report index
tests/report_v0.1.md                           Initial toy-model test report
tests/report_v0.2.md                           Exchange-rate and shadow-amplitude calculations
tests/report_v0.3.md                           Motion-by-exchange calculation
tests/report_v0.4.md                           Shadow projection and Koide comparison
tests/report_v0.5.md                           Entanglement shared-amplitude correction
tests/report_v0.6.md                           Objective shared-channel entanglement
tests/report_v0.7.md                           Vibration-motion shadow-anchor derivation
tests/report_v0.8.md                           One-anchor spin-vortex correction test
tests/report_v0.9.md                           Fibonacci-Higgs source equation reduced tau test
tests/report_v0.10.md                          Funnel-speed Higgs capture-window test
tests/report_v0.11.md                          Bounded reservoir field-source test

NOTICE.md                                      Authorship and priority notice
LICENSE_PENDING.md                             Licensing note
```

---

## Research status

Immediate derivation targets:

1. derive the field operator from an action,
2. derive the finite Fibonacci-shaped source core,
3. derive `lambda_a Omega_OS,a` from original/shadow vortex geometry,
4. derive the funnel-speed capture window from knot dynamics,
5. derive `R_*` and `R_4` from the failed fourth-mode sector,
6. test the field-source equation beyond the tau-like reduced model,
7. check compatibility with Lorentz and gauge structure.

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
