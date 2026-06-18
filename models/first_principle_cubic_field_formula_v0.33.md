# First-Principle Cubic Field Formula v0.33

**Status:** speculative MCIFT first-principle formulation; not established physics.  
**Purpose:** build the MCIFT field formula directly from the updated cubic model: cube-center knots, six connector states, Higgs face-plane vortices, mass loading, contained complexity, and collapse-containment.

---

## 1. Why v0.33 is different

Earlier MCIFT notes introduced the pieces separately:

```text
v0.31  cube-center six-connector knot geometry
v0.32  cube-face Higgs vortex mass mechanism
v0.30  dynamic ordered collapse-containment retest
```

v0.33 combines these into a single first-principle field formula.

The MCIFT field is not just a scalar at a point. It is a cubic cell-complex field with:

```text
node variables      at cube centers
link variables      along center-to-center connectors
face variables      on Higgs-coupled cube planes
cell variables      for contained complexity and collapse state
```

---

## 2. Cubic spacetime cell index

Let cube-cell centers be indexed by:

```text
i in Z^3
```

with center position:

```text
x_i = ell * (n_x, n_y, n_z)
```

where `ell` is the MCIFT cell scale.

The six connector directions are:

```text
D = {+x, -x, +y, -y, +z, -z}
```

For direction `mu`, the neighboring cell is:

```text
j = i + mu
```

---

## 3. Primitive field variables

At each cube-center knot:

```text
K_i(t)        knot information amplitude / state
q_i(t)        contained information complexity
B_i(t)        collapsed-knot reservoir content
phi_i(t)      local information phase
T_i(t)        local timing / response coordinate
```

On each connector:

```text
a_i,mu(t)     connector activation, 0 <= a_i,mu <= 1
chi_i,mu(t)   information compatibility across the face
```

On each cube face:

```text
H_i,mu(t)      Higgs face-plane mass-coupling availability
Omega_i,mu(t)  face-plane vortex strength
m_i,mu(t)      mass gathered from that face vortex
```

At the cell level:

```text
m_i(t)         total gathered vortex mass
Coh_i(t)       local connector-supported coherence capacity
S_i(t)         containment stability
```

---

## 4. The MCIFT field object

The local MCIFT field at cube-cell `i` is the tuple:

```text
Psi_i(t) = {
  K_i,
  q_i,
  B_i,
  phi_i,
  T_i,
  {a_i,mu},
  {chi_i,mu},
  {H_i,mu},
  {Omega_i,mu},
  {m_i,mu},
  m_i,
  Coh_i,
  S_i
}
```

for all `mu in D`.

In compact notation:

```text
Psi_i = (node_i, link_i, face_i, cell_i)
```

where:

```text
node_i = (K_i, phi_i, T_i)
link_i = {a_i,mu, chi_i,mu}
face_i = {H_i,mu, Omega_i,mu, m_i,mu}
cell_i = (q_i, m_i, Coh_i, S_i, B_i)
```

This is the first-principle MCIFT field object for the cubic model.

---

## 5. Connector activation and neighbor agreement

Each connector has activation:

```text
0 <= a_i,mu <= 1
```

The symmetric connection between neighboring centers `i` and `j = i + mu` is:

```text
A_ij,mu = sqrt(a_i,mu * a_j,-mu)
```

This makes the shared connection strong only when both sides participate.

---

## 6. Information compatibility

A connector creates a vortex only when the center-to-center information relation is sufficiently compatible.

Define:

```text
chi_i,mu = sqrt(a_i,mu a_j,-mu)
         * P_phase(i,j)
         * P_timing(i,j)
         * P_match(i,j)
```

with:

```text
P_phase  = cos^2(phi_i - phi_j)
P_timing = exp[-(T_i - T_j)^2 / tau_0^2]
P_match  = exp[-|K_i - K_j|^2 / sigma_K^2]
```

The connector is vortex-ready when:

```text
chi_i,mu >= chi_c
```

---

## 7. Higgs face-plane vortex

Each connector crosses a Higgs-coupled cube face with response:

```text
H_i,mu >= 0
```

The vortex strength is:

```text
Omega_i,mu = H_i,mu * sigma(chi_i,mu - chi_c)
```

where a smooth threshold can be:

```text
sigma(x) = 0.5 * [1 + tanh(kappa x)]
```

Thus:

```text
poor compatibility      -> weak or absent vortex
correct compatibility   -> stable face-plane vortex
```

---

## 8. Mass gathered from vortex response

Mass is gathered from retained Higgs-plane vortex response:

```text
m_i,mu = m_scale * Omega_i,mu * a_i,mu
```

Total mass gathered by the knot:

```text
m_i = sum_mu m_i,mu
```

This keeps the mechanism clear:

```text
connector state   = information/anchor coupling
Higgs face plane  = mass-coupling availability
vortex            = conversion/capture mechanism
mass              = retained Higgs response
```

---

## 9. Connector coherence capacity

Mean connector activation:

```text
a_i,mean = (1/6) sum_mu a_i,mu
```

Directional imbalance:

```text
Delta_i = sqrt[(a_i,+x-a_i,-x)^2
             + (a_i,+y-a_i,-y)^2
             + (a_i,+z-a_i,-z)^2]
```

Local connector coherence capacity:

```text
Coh_i = 6 a_i,mean - lambda_Delta Delta_i
```

Balanced connectors maximize coherence. Imbalanced connectors reduce the ability of the knot to remain centered and open.

---

## 10. Contained complexity

The contained complexity has three parts:

```text
q_i = q_i,base + alpha_m m_i + alpha_Omega sum_mu |grad_mu Omega_i,mu|
```

Interpretation:

```text
q_i,base                         base information complexity
alpha_m m_i                      mass loading from vortex capture
alpha_Omega grad(Omega) term      vortex strain / curvature complexity
```

A discrete face-gradient may be written:

```text
grad_mu Omega_i,mu = Omega_i,mu - Omega_j,-mu
```

where `j = i + mu`.

---

## 11. Containment stability and collapse

The containment score is:

```text
S_i = Coh_i - q_i
```

Stable/open knot:

```text
S_i >= 0
```

Containment failure:

```text
S_i < 0
```

Collapsed-knot transfer:

```text
Q_i->B = gamma_B * max(0, -S_i)
```

Reservoir update:

```text
dB_i/dt = Q_i->B - decay_B B_i
```

The core rule is:

```text
collapse occurs when contained complexity exceeds connector-supported coherence capacity
```

---

## 12. First-principle field formula

The first-principle cubic MCIFT formula is the combined node-link-face-cell field:

```text
Psi_MCIFT(i,t) = (
  K_i,
  phi_i,
  T_i,
  {a_i,mu},
  {chi_i,mu},
  {H_i,mu},
  {Omega_i,mu},
  {m_i,mu},
  m_i,
  q_i,
  Coh_i,
  S_i,
  B_i
)
```

with definitions:

```text
A_ij,mu      = sqrt(a_i,mu a_j,-mu)
chi_i,mu     = A_ij,mu P_phase P_timing P_match
Omega_i,mu   = H_i,mu sigma(chi_i,mu - chi_c)
m_i,mu       = m_scale Omega_i,mu a_i,mu
m_i          = sum_mu m_i,mu
Coh_i        = 6 a_i,mean - lambda_Delta Delta_i
q_i          = q_i,base + alpha_m m_i + alpha_Omega sum_mu |grad_mu Omega_i,mu|
S_i          = Coh_i - q_i
dB_i/dt      = gamma_B max(0,-S_i) - decay_B B_i
```

This is the v0.33 MCIFT field formula.

---

## 13. Optional energy functional form

A compact energy/action-like scaffold can be written:

```text
F_MCIFT = sum_i [ U_K(K_i) + U_q(q_i) + U_B(B_i) + lambda_S max(0,-S_i)^2 ]
        + sum_i,mu [ U_a(a_i,mu)
                   + U_H(H_i,mu)
                   + kappa_Omega (Omega_i,mu - H_i,mu sigma(chi_i,mu-chi_c))^2
                   + kappa_link (1 - chi_i,mu)^2 a_i,mu ]
```

Then a relaxation/update law can be represented schematically as:

```text
dPsi/dt = - delta F_MCIFT / delta Psi + source - loss
```

This is not a claim of a complete physical action. It is a structured way to keep the cubic model internally consistent.

---

## 14. Continuum embedding

A continuum-looking field can be reconstructed from cell data using local basis functions:

```text
Psi(x,t,c) = sum_i W_node(x-x_i) node_i(c,t)
           + sum_i,mu W_face(x-x_i,mu) face_i,mu(c,t)
           + sum_i,mu W_link(x-x_i,mu) link_i,mu(c,t)
```

This lets the cubic model be interpreted as a discrete first-principle scaffold whose large-scale behavior may approximate smooth fields.

---

## 15. Safe wording

Safe:

```text
v0.33 defines MCIFT as a cubic cell-complex information field with node, connector, face-vortex, mass-loading, complexity, and collapse-reservoir variables.
```

Safe:

```text
The v0.33 field formula is a first-principle scaffold for MCIFT, not a completed replacement for established quantum field theory or general relativity.
```

Not safe:

```text
This proves spacetime is literally cubic.
This proves the Higgs mechanism is literally a face vortex.
This replaces standard quantum field theory or Lambda-CDM.
```
