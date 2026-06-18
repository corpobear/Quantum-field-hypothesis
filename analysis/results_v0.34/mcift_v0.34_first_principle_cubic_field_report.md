# MCIFT v0.34 First-Principle Cubic Field Toy Solver Report

**Status:** first toy solver for the v0.33 cubic cell-complex field formula; speculative scaffold, not established physics.

## Purpose

This run tests whether the v0.30 collapse-containment behavior survives when the v0.33 field variables are made active:

```text
connector activation a_i,mu
information compatibility chi_i,mu
Higgs face-plane vortex Omega_i,mu
vortex mass loading m_i
contained complexity q_i
connector coherence capacity Coh_i
containment score S_i
mode-coupled collapsed reservoir transfer B(k,a)
```

## Method

The solver reads the v0.28 thermodynamic residual spectrum and tracks, then applies the v0.33 field formula at each response epoch and each spectrum mode.

Core equations used:

```text
A_ij,mu      = sqrt(a_i,mu a_j,-mu)
chi_i,mu     = A_ij,mu P_phase P_timing P_match
Omega_i,mu   = H_i,mu sigma(chi_i,mu - chi_c)
m_i,mu       = m_scale Omega_i,mu a_i,mu
m_i          = sum_mu m_i,mu
Coh_i        = 6 a_i,mean - lambda_Delta Delta_i
q_i          = q_i,base + alpha_m m_i + alpha_Omega sum_mu |grad_mu Omega_i,mu|
S_i          = Coh_i - q_i
B transfer   = exp[-collapse_pressure * max(0,lambda/R_A - 1) * lambda/R_A]
```

## Result

```text
v0.30 dynamic-ordered RMS = 0.302859
v0.34 cubic-field RMS = 0.302859
shape verdict = PASS-LIKE
v0.28 global peak before cubic field = 617.87 Mpc
v0.34 global peak after cubic field = 152.29 Mpc
v0.34 BAO-window peak = 152.29 Mpc
```

## Transfer diagnostics

```text
v0.34 transfer at 617.87 Mpc = 0.449576
v0.30 transfer at 617.87 Mpc = 0.558702
v0.34 transfer at nearest BAO bin = 1.000000
```

## Final 617.87 Mpc field-state diagnostics

```text
chi_617 = 0.682207
Omega_617 = 0.379155
m_617 = 1.882739
q_617 = 36.197423
coherence_capacity_617 = 22.471565
S_617 = -13.725858
```

## Interpretation

```text
The first-principle cubic field toy solver preserves the main v0.30 behavior: the super-anchor 617.87 Mpc mode receives collapse-reservoir transfer, while the BAO bin remains untouched by B transfer. The scored window remains PASS-LIKE because the only strongly affected mode is outside the score window.
```

## Limitation

```text
This is still a minimal mode-level toy solver. It activates v0.33 variables per mode and epoch, but it is not yet a spatial 3D lattice simulation with neighboring cells evolved directly in real space.
```
