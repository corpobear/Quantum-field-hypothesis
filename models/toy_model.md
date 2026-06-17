# Toy Model Equations

**Status:** speculative toy-model equations; not established physics  
**Version:** v0.14 consolidated toy model, GitHub math-display fix  
**Scope:** compact math for MCIFT through activation terminology, one-anchor spin-vortex correction, Fibonacci-Higgs source, funnel-speed capture, bounded reservoir gate, six-side dark-manifest sink geometry, and the first CERN-facing event-shape proxy.

---

## 0. Core field

The field is written as:

```math
\Psi(x,y,z,t,c)
```

where:

- `x,y,z` are ordinary spatial coordinates,
- `t` is time,
- `c` is an internal channel coordinate.

Possible channels include identity, light/visibility, Higgs response, phase, charge, knot structure, exchange, shadow amplitude, motion, gravity, entanglement/shared channel, confinement, reservoir availability, and dark-manifest side intake.

---

## 1. Channel activation rules

v0.12 corrected the activation language.

Use:

```text
light activation = electromagnetic / visibility-channel activation
```

Do not use:

```text
light activation = existence itself
```

Separate channel factors:

```math
L_i=\text{light / electromagnetic visibility activation}
```

```math
H_i=\text{Higgs / mass-capture activation}
```

```math
G_i=\text{gravitational projection}
```

```math
K_i=\text{knot coherence}
```

Then:

```math
\mathrm{Visibility}_i=L_iK_i
```

```math
\mathrm{Mass}_i=H_iK_i
```

```math
\mathrm{Gravity}_i=G_iH_iK_i
```

Matter-state classes:

```text
unmanifest        no stable visible, mass, or gravitational projection
visible-manifest  light-active, mass-active, gravity-active, knot-coherent
dark-manifest     mass-active and gravity-active, but light-inactive
```

Dark-manifest condition:

```math
L_i\approx0,\quad H_i>0,\quad G_i>0,\quad K_i>0
```

---

## 2. Cluster complexity

Binary complexity growth:

```math
C_n=2^n
```

| Mode | Complexity |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |

The eight-sector knot used in the tau-like and dark-manifest tests is:

```math
C_3=8
```

---

## 3. Coherence and stability

Simple coherence law:

```math
Q_n=an
```

Original stability:

```math
S_n=Q_n-C_n=an-2^n
```

Survival condition:

```math
S_n>0
```

Failure condition:

```math
S_n<0
```

Exactly three stable modes and fourth failure require:

```math
\frac{8}{3}<a<4
```

Central toy value:

```math
a=3.5
```

| Mode | Complexity | Coherence | Stability | Outcome |
|---:|---:|---:|---:|---|
| 1 | 2 | 3.5 | +1.5 | survives |
| 2 | 4 | 7.0 | +3.0 | survives |
| 3 | 8 | 10.5 | +2.5 | survives |
| 4 | 16 | 14.0 | -2.0 | fails |

The failed fourth mode later becomes a bounded reservoir availability term, not a fourth stable particle.

---

## 4. Fractal catching surface

Cluster catching surface:

```math
A_n=(C_n-1)^{D_f}
```

Default toy exponent:

```math
D_f=3.5+\epsilon
```

Interpretation:

```text
cluster complexity creates surface structure;
surface structure controls how much response can be caught.
```

---

## 5. Finite Higgs-response window

Linear complexity window:

```math
H(C_n)=\exp\left[-\frac{(C_n-C_\star)^2}{2\sigma_H^2}\right]
```

Log-fractal window:

```math
H(C_n)=\exp\left[-\frac{(\ln C_n-\ln C_\star)^2}{2w^2}\right]
```

The Higgs channel is separated from the light channel. A knot can be mass-active while light-inactive.

---

## 6. Vibration and internal exchange

Pairwise exchange rate:

```math
\Gamma_{ij}
=
g
\exp\left[-\frac{(I_i-I_j)^2}{2\sigma_I^2}\right]
\exp\left[-\frac{(\omega_i-\omega_j)^2}{2\sigma_\omega^2}\right]
\cos^2(\phi_i-\phi_j)
```

Knot-level exchange rate:

```math
\Gamma_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}
```

Exchange/densification factor:

```math
X_n=\exp(\eta\Gamma_n)
```

Weak-exchange approximation:

```math
X_n\approx1+\eta\Gamma_n
```

---

## 7. Exchange-updated stability and base rest mass

Exchange-updated stability:

```math
S_n=3.5\,nX_n-C_n
```

with:

```math
C_n=2^n
```

Mode 4 still fails if:

```math
S_4=14X_4-16<0
```

Therefore:

```math
X_4<1.1428571429
```

or:

```math
\eta\Gamma_4<0.1335313926
```

Exchange-rate rest-mass formula:

```math
m_{0,n}=m_{\mathrm{scale}}(C_n-1)^{D_f}X_nH(C_n)\max(S_n,0)
```

---

## 8. Amplitude-first mass

Visible cluster:

```math
I_n
```

Complementary/shadow pattern:

```math
I_n^s
```

Full knot state:

```math
K_n=(I_n,I_n^s)
```

Mass amplitude:

```math
A_n=I_n-I_n^s
```

Mass:

```math
m_n=A_n^2
```

If a base model gives:

```math
m_n^{\mathrm{base}}
```

then:

```math
A_n^{\mathrm{base}}=\sqrt{m_n^{\mathrm{base}}}
```

Introduce an amplitude correction:

```math
\Delta_n
```

Then:

```math
A_n=A_n^{\mathrm{base}}\Delta_n
```

and:

```math
m_n=m_n^{\mathrm{base}}\Delta_n^2
```

---

## 9. Shadow projection geometry

For the tau-like third mode:

```math
C_3=8
```

Primary shadow term:

```math
s_1=\frac{1}{C_3(C_3-1)}=\frac{1}{56}
```

Echo-shadow term:

```math
s_2=\frac{s_1}{C_3}=\frac{1}{448}
```

Amplitude correction:

```math
\Delta(f)=1+s_1+fs_2
```

Mass prediction:

```math
m_\tau(f)=m_\tau^{\mathrm{base}}\Delta(f)^2
```

Koide amplitude clue:

```math
\frac{A_1^2+A_2^2+A_3^2}{(A_1+A_2+A_3)^2}=\frac{2}{3}
```

with:

```math
A_i=\sqrt{m_i}
```

Local tau echo-shadow completion fraction:

```math
f_0=1-\frac{1}{C_3}=\frac{7}{8}
```

Then:

```math
\Delta_{7/8}=1+\frac{1}{56}+\frac{7}{8}\frac{1}{448}=1.0198102679
```

and:

```math
m_\tau^{(7/8)}=1776.97039439\ \mathrm{MeV}
```

Koide high-root comparison:

```math
m_\tau^{\mathrm{Koide}}=1776.96902708\ \mathrm{MeV}
```

This is an internal toy-model clue, not confirmation.

---

## 10. One-point shadow anchor

Contact count:

```math
k=|K_8\cap S_8|
```

A true shadow must connect:

```math
k\ge1
```

Multiple contact points create bridges:

```math
M(k)=\frac{k(k-1)}{2}
```

Stable non-merger condition:

```math
M(k)=0
```

Together:

```math
k_*=1
```

For a `C`-sector knot, one pinned anchor leaves the free circulation fraction:

```math
B_C(1)=\frac{C-1}{C}
```

For `C=8`:

```math
B_8(1)=\frac{7}{8}
```

---

## 11. Spin-vortex anchor correction

The one-point anchor can be interpreted as:

```text
one pinned sector
-> remaining sectors circulate freely
-> free spin-vortex fraction B_C(1)
-> spin-vortex amplitude correction
```

For the tau-like knot:

```math
B_8(1)=\frac{7}{8}
```

Anchor spin transfer:

```math
\Omega_K=\Omega_0\left(1+\lambda_{anchor}\frac{C-1}{C}\right)
```

For the tau-like case:

```math
\Omega_K=\Omega_0\left(1+\lambda_{anchor}\frac{7}{8}\right)
```

---

## 12. Fibonacci-Higgs anchor-tip source

Golden ratio:

```math
\varphi=\frac{1+\sqrt5}{2}
```

Minimal golden wobble around the Higgs-response resonance:

```math
\omega_\varphi(t)=\omega_H+\Delta\omega\sin(\varphi t)
```

Higgs overlap:

```math
O_{\varphi,a}(t)
=
\exp\left[-\frac{(\omega_{\varphi,a}(t)-\omega_H)^2}{2\sigma_\omega^2}\right]
\cos^2(\theta_{\varphi,a}(t)-\theta_H)
\exp\left[-\frac{d_{c,H,a}^2}{2\sigma_c^2}\right]
```

Reduced tau-like average:

```math
\langle O_\varphi\rangle=0.9837806705
```

The resonance-overlap tau aperture becomes:

```math
A_{tip,8}
=
\frac{1}{56}
+
\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
```

Using the reduced average:

```math
A_{tip,8}=0.01977858948
```

---

## 13. Funnel-speed capture window

Speed-dependent capture factor:

```math
W_v(v)
=
\frac{
\left(1-e^{-(v/v_{min})^2}\right)
e^{-(v/v_{scatter})^2}
}{W_{max}}
```

Interpretation:

```text
too slow   -> no channel connection
just right -> source captured in knot
too fast   -> source scatters or is not retained
```

---

## 14. Bounded fourth-mode reservoir

Bounded reservoir gate:

```math
R_4^{gate}=\frac{R_4}{R_4+R_*}
```

Limits:

```math
R_4\ll R_*\Rightarrow R_4^{gate}\approx0
```

```math
R_4\gg R_*\Rightarrow R_4^{gate}\approx1
```

---

## 15. Current visible field-source equation

Let:

```math
\mathcal{D}=\partial_t^2-c_*^2\nabla^2-D_c\partial_c^2+V'(\psi)
```

Then:

```math
\mathcal{D}\psi=\sum_a S_{tip,a}
```

Visible/tip source:

```math
S_{tip,a}
=
\lambda_a
\Omega_{OS,a}
W_v(v_{tip,a})
\left[
P_{C_a}+B_{C_a}(1)E_{C_a}\langle O_{\varphi,a}\rangle
\right]
R_{4,a}^{gate}
\delta_{\epsilon,a}^{(\varphi)}
```

For the tau-like eight-sector case:

```math
P_8=\frac{1}{56},\quad E_8=\frac{1}{448},\quad B_8(1)=\frac{7}{8}
```

Integrated source:

```math
\Sigma_\tau
=
W_v
\left[
\frac{1}{56}
+
\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
\right]
R_4^{gate}
```

Mass rule:

```math
m_\tau=m_\tau^{base}(1+\Sigma_\tau)^2
```

At:

```math
W_v=1,\quad R_4^{gate}=1,\quad \langle O_\varphi\rangle=0.9837806705
```

the reduced tau-like result is:

```math
m_\tau=1776.86\ \mathrm{MeV}
```

---

## 16. Dark-manifest six-side sink geometry

Visible-manifest matter:

```text
one axial tip intake
```

Dark-manifest matter:

```text
six lateral side intakes
```

Eight-sector split:

```text
1 sector  = visible axial tip
1 sector  = opposite axis
6 sectors = lateral side-intake belt
```

Visible aperture:

```math
A_{tip}=\frac{1}{56}+\frac{7}{8}\frac{1}{448}\langle O_\varphi\rangle
```

Dark side aperture:

```math
A_{side}=6\left(\frac{1}{56}\right)=0.1071428571
```

Using:

```math
\langle O_\varphi\rangle=0.9837806705
```

gives:

```math
A_{tip}=0.01977858948
```

and:

```math
\frac{A_{side}}{A_{tip}}=5.417
```

Planck 2018 comparison values used in this toy check:

```math
\Omega_c h^2\approx0.120,\quad \Omega_b h^2\approx0.0224
```

so:

```math
\frac{\Omega_c}{\Omega_b}\approx5.357
```

Side-efficiency factor needed to match the central value:

```math
\epsilon_{sink}=\frac{5.357}{5.417}\approx0.989
```

---

## 17. Dark-manifest source form

Visible source:

```math
S_{visible}
=
\lambda_+
\Omega_z
W_{tip}
A_{tip}
R_4^{gate}
\delta_{tip}^{(\varphi)}
```

Dark side source:

```math
S_{dark}
=
-
\lambda_-
\kappa_{sink}
W_{side}
A_{side}
R_4^{gate}
\delta_{side}^{(\varphi)}
```

where:

```math
\kappa_{sink}=-\nabla_\perp\cdot J_\perp
```

The negative sign means inverse field orientation, not negative mass.

Mass density uses magnitude:

```math
\rho_{dark}\propto |S_{dark}|
```

Light visibility is suppressed:

```math
L_{dark}\approx0
```

Reduced dark-to-visible ratio:

```math
\frac{\rho_{dark}}{\rho_{visible}}
\approx
\frac{
\epsilon_{sink}(6/56)
}{
1/56+(7/8)(1/448)\langle O_\varphi\rangle
}
```

---

## 18. Motion from directional exchange

Directional exchange:

```math
\vec{\Gamma}_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}\vec{d}_{ij}
```

Simple velocity rule:

```math
\frac{\vec{v}_n}{c_*}=\frac{\vec{\Gamma}_n}{\Gamma_n}
```

Bounded form:

```math
\beta_n=\frac{v_n}{c_*}=\tanh(\mu_n)
```

where:

```math
\mu_n=\eta|\vec{\Gamma}_n|
```

Motion-energy factor:

```math
\gamma_n=\frac{1}{\sqrt{1-\beta_n^2}}=\cosh(\mu_n)
```

Effective total mass-energy:

```math
m_{eff,n}=\gamma_nm_{0,n}
```

---

## 19. Entanglement and shared-channel geometry

For two knots `A` and `B`:

```math
\Psi_A=\Psi(x_A,t,c_A)
```

```math
\Psi_B=\Psi(x_B,t,c_B)
```

Spatial and channel distances:

```math
d_x=|x_A-x_B|,\quad d_c=|c_A-c_B|
```

A shared channel-state:

```math
\Omega_{AB}(c_s)
```

Joint state:

```math
\Psi_{AB}
=
\Psi_A(x_A,t,c_s)
\Psi_B(x_B,t,c_s)
\Omega_{AB}(c_s)
```

Shared-channel strength:

```math
\mathcal{E}_{AB}
=
\lambda_{AB}
O_{AB}
\exp\left[-\frac{d_c^2}{2\sigma_c^2}\right]
\tanh\left(\frac{\Gamma_{AB}}{\Gamma_c}\right)
```

Mass-defect rule:

```math
m_{AB}=m_A+m_B-2\epsilon\mathcal{E}_{AB}\sqrt{m_A m_B}
```

Caveat:

```text
shared channel -> correlation
shared channel != controllable nonlocal messaging
```

---

## 20. High-complexity confinement / black-hole interpretation

Schematic confinement proxy:

```math
\mathcal{C}_{conf}(C)=\frac{1}{1+e^{-(C-C_{conf})/w_{conf}}}
```

Interpretation:

```text
large coherent complexity
-> strong internal channel separation
-> trapped or confined information pathways
```

---

## 21. CERN two-drill event-shape proxy

Collider translation:

```text
visible drill activity -> jets and visible transverse energy
dark side channel -> missing transverse momentum and event imbalance
```

Visible scale:

```math
H_T=\sum_{jets}p_T^{jet}
```

Missing fraction:

```math
R_{miss}=\frac{E_T^{miss}}{H_T}
```

Collider proxy:

```math
\frac{|S_{dark}|}{|S_{visible}|}\sim\frac{E_T^{miss}}{H_T}
```

Current v0.14 verdict:

```text
not confirmed, not ruled out by the reduced comparison, now constrained
```

---

## 22. Reduced test summary

| Version | Mechanic | Reduced result |
|---|---|---|
| v0.7 | one-point shadow anchor | stable shadow requires `k*=1` |
| v0.8 | spin-vortex anchor | `7/8` free fraction gives near-Koide tau correction |
| v0.9 | Fibonacci-Higgs source | `⟨O_phi⟩≈0.9837806705` gives tau-like match |
| v0.10 | funnel-speed capture | mass capture peaks only in speed window |
| v0.11 | bounded reservoir | large failed fourth-mode supply saturates via `R_4^gate` |
| v0.12 | activation terminology | light controls visibility, not existence |
| v0.13 | six-side dark sink | side/tip ratio `5.417` vs cosmological `5.357` |
| v0.14 | CERN proxy | broad published MET searches constrain, not confirm |

---

## 23. Open derivation targets

1. Derive the field operator `D` from an action.
2. Derive the finite Fibonacci-shaped source core.
3. Derive `lambda_a Omega_OS,a` from original/shadow vortex geometry.
4. Derive capture-window parameters from knot dynamics.
5. Derive `R_*` and `R_4` from the failed fourth-mode sector.
6. Derive the six-side split from explicit eight-sector knot/shadow geometry.
7. Derive the side-flow convergence term `kappa_sink`.
8. Test whether dark-manifest knots reproduce galaxy-scale gravitational behavior.
9. Check compatibility with Lorentz and gauge structure.
10. Identify falsifiable predictions or reject the mechanism.

---

## 24. Related files

```text
models/shadow_anchor_v0.7.md
models/spin_vortex_anchor_v0.8.md
models/fibonacci_higgs_source_v0.9.md
models/funnel_speed_capture_v0.10.md
models/field_source_reservoir_v0.11.md
models/six_side_sink_dark_manifest_v0.13.md
models/two_drill_collision_cern_v0.14.md
mechanics/mechanics_v0.13.md
mechanics/plot_mechanics.py
tests/report_v0.14_cern_two_drill_event_shape.md
```
