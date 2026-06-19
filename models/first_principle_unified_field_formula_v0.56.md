# MCIFT v0.56 Unified First-Principle Field Formula

**Status:** speculative MCIFT first-principle scaffold; not established physics.

## Purpose

v0.56 consolidates the old v0.33 cubic formula with the mechanics learned through v0.55.
The goal is to stop adding independent bridge patches and instead make every downstream
calculation a readout from one field object.

## Base inherited from v0.33

The v0.33 field is a cubic cell-complex field:

```text
Psi_i = (node_i, link_i, face_i, cell_i)
node_i = (K_i, phi_i, T_i)
link_i = {a_i,mu, chi_i,mu}
face_i = {H_i,mu, Omega_i,mu, m_i,mu}
cell_i = (q_i, m_i, Coh_i, S_i, B_i)
```

## v0.56 extended field object

```text
Psi_i^0.56 = (
  K_i, phi_i, T_i,
  {a_i,mu}, {chi_i,mu},
  {H_i,mu}, {Omega_i,mu}, {m_i,mu},
  E_i, R_lock_i, lambda_R_i, rho_ratio_i,
  L_i, omega_i, I_i,
  P_v,i, P_h,i,
  rho_v,i, rho_h,i, rho_rot,i, rho_s,i, rho_r,i,
  G_i, N_i,
  c_s,i, A_sound_i, Sigma_i,
  q_i, Coh_i, S_i, B_i,
  {Q_i->j}
)
```

## 1. Compatibility and face vortex

```text
A_ij,mu = sqrt(a_i,mu a_j,-mu)
chi_i,mu = A_ij,mu P_phase P_timing P_match
Omega_i,mu = H_i,mu sigma(chi_i,mu - chi_c)
m_i,mu = m_scale Omega_i,mu a_i,mu
m_i = sum_mu m_i,mu
```

## 2. Entanglement density and compression

```text
E_i = sum_mu chi_i,mu chi_j,-mu Omega_i,mu
R_link,i = E_i / (E_i + E_0)
lambda_R,i = exp[-lambda_E R_link,i]
rho_ratio_i = lambda_R,i^-3
```

## 3. Rhythm lock and discarded vibration

```text
Z_i = sum_mu sqrt(Omega_i,mu) exp(i phi_j)
R_lock_i = |Z_i| / sum_mu sqrt(Omega_i,mu)

E_core_i = eta_core R_lock_i E_i
E_discard_i = (1 - R_lock_i) E_i
```

## 4. Rotation from discarded vibration

```text
I_i = (2/5) M_dense_i R_dense_i^2
L_i = sqrt(2 I_i eta_rot E_discard_i)
omega_i = L_i / I_i
rho_rot,i = L_i^2 / (2 I_i)
```

## 5. Visible and hidden projections

```text
P_v,i = face_visibility_i vortex_capture_i
P_h,i = sink_gate_i [w_D density_shadow_i + w_R hidden_retention_i + w_O rotation_capture_i]

rho_v,i = P_v,i E_i
rho_h,i = P_h,i E_i
```

The hidden branch does not enter visible channels, but it contributes to gravitational load.

## 6. Gravity/load and lapse

```text
G_i = rho_v,i + C_h rho_h,i + C_rot rho_rot,i + C_s rho_s,i + rho_r,i

chi_G,i = 2 beta_G G_i / R_hidden_i
v_rot,i = omega_i R_dense_i
N_i = sqrt(1 - chi_G,i) sqrt(1 - v_rot,i^2)
```

## 7. Sound / pressure wave

```text
c_s,i^2 = Coh_i / (rho_ratio_i + G_i)
omega_sound_i = c_s,i / R_shell_i
R_sound_i = exp[-((omega_lab_i - omega_sound_i)/(sigma_sound omega_sound_i))^2]

A_sound_i = A0 + A_D E_discard_i/E_i + A_N(1 - N_i) + A_M(v_rot_i/c_s_i)
Sigma_i = 1 + alpha_S A_sound_i R_sound_i + beta_M(v_rot_i/c_s_i)
rho_s,i = A_sound_i^2 rho_shell_i
```

## 8. Channel projection, kappa, partial width

For channel c:

```text
W_c,i = W_c(Psi_i)
tau_c,i = tau_channel,i tau_sound,i
kappa_c^2 = <W_c,i tau_c,i> / <W_c,i>_SM

Gamma_c = kappa_c^2 Gamma_c^SM
BR_c = Gamma_c / sum_d Gamma_d
mu(p,c) = kappa_p^2 kappa_c^2 / kappa_H^2
```

This makes collider quantities readouts of the field projection, not separate proxy knobs.

## 9. Cosmology coarse-grain

For a domain D:

```text
rho_alpha(D,t) = (1/V_D) sum_i in D rho_alpha,i

rho_grav = rho_v + C_h rho_h + C_rot rho_rot + C_s rho_s + rho_r
H_core(a)^2 = sum_alpha Omega_alpha a^(-n_alpha)
H_lab(a) = H_core(a) / N(a)
```

## 10. Q_i transfer network

```text
dot(rho_alpha) + 3H(rho_alpha + p_alpha) = Q_alpha
sum_alpha Q_alpha = 0
```

Field-derived transfer form:

```text
Q_alpha->beta = kappa_alpha_beta F_alpha_beta(Psi) rho_alpha
Q_alpha = sum_beta Q_beta->alpha - sum_beta Q_alpha->beta
```

## 11. What v0.56 changes

Previous versions added separate bridge layers.
v0.56 defines where each bridge quantity must come from:

```text
collision stability -> S_i = Coh_i - q_i
visible channels -> W_c(Psi)
hidden matter -> P_h(Psi)
rotation -> L_i from discarded vibration
time dilation -> N_i from load and rotation
sound spread -> c_s and A_sound from coherence/load
cosmology -> coarse-grained rho_alpha and Q_i
```

## Limitation

This is a consolidated scaffold. It is not yet a fully predictive physics theory.
The next step is to implement this formula in code and remove assigned channel/category coefficients.
