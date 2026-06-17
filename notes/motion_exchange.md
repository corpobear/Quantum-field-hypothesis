# Motion from Directional Information Exchange

**Status:** speculative toy-model extension, v0.3.

This note adds motion to the MCIFT toy framework.

## Core distinction

The model now separates two kinds of motion:

```text
internal vibratory motion -> affects rest-mass formation
external directional motion -> affects total energy / effective mass-energy
```

This distinction matters. In standard relativistic language, rest mass does not increase merely because an object moves faster. Total energy increases. MCIFT should preserve that distinction.

## Balanced exchange and rest mass

Balanced internal exchange contributes to rest mass through resonance and densification:

$$
X_n=e^{\eta\Gamma_n}
$$

where:

$$
\Gamma_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}
$$

The rest-mass toy formula is:

$$
m_{0,n}=m_{scale}(C_n-1)^{D_f}X_nH(C_n)\max(S_n,0)
$$

with:

$$
S_n=3.5nX_n-C_n
$$

and:

$$
C_n=2^n
$$

## Directional exchange and velocity

Motion appears when exchange is not directionally balanced.

Define the directional exchange vector:

$$
\vec{\Gamma}_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}\vec{d}_{ij}
$$

where `d_ij` is the direction of the exchange link.

The simplest velocity rule is:

$$
\frac{\vec v_n}{c_*}=\frac{\vec{\Gamma}_n}{\Gamma_n}
$$

or, in bounded form:

$$
\beta_n=\frac{v_n}{c_*}=\tanh(\mu_n)
$$

where:

$$
\mu_n=\eta|\vec{\Gamma}_n|
$$

This prevents the toy velocity from exceeding the maximum channel-update speed `c_*`.

## Motion-energy factor

Define:

$$
\gamma_n=\frac{1}{\sqrt{1-\beta_n^2}}
$$

If:

$$
\beta_n=\tanh(\mu_n)
$$

then:

$$
\gamma_n=\cosh(\mu_n)
$$

The total effective mass-energy is then:

$$
m_{eff,n}=\gamma_nm_{0,n}
$$

where `m_0,n` is the rest mass produced by internal exchange and Higgs response.

## Interpretation

Balanced exchange produces rest-mass structure.

Directional exchange produces motion.

Motion then increases total energy, not the invariant rest mass:

```text
balanced internal exchange -> rest mass
unbalanced directional exchange -> velocity
velocity -> increased total energy
```

## Compact law

$$
m_{eff,n}
=
\gamma_n
m_{scale}(C_n-1)^{D_f}X_nH(C_n)\max(S_n,0)
$$

with:

$$
X_n=e^{\eta\Gamma_n}
$$

$$
S_n=3.5nX_n-C_n
$$

$$
\beta_n=\tanh(\eta|\vec{\Gamma}_n|)
$$

$$
\gamma_n=\cosh(\eta|\vec{\Gamma}_n|)
$$

## Best summary

**Internal vibratory exchange contributes to rest mass. Directional exchange creates velocity. Velocity increases total energy through a gamma-like factor.**
