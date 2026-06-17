# Test Report v0.3: Motion from Directional Exchange

**Status:** speculative toy-model calculation.  
**Purpose:** add motion to the MCIFT toy model by separating internal vibratory exchange from external directional motion.

## 1. Key distinction

The v0.3 model separates:

```text
internal vibratory motion -> contributes to rest-mass formation
external directional motion -> contributes to total energy / effective mass-energy
```

In standard relativistic language, rest mass does not increase merely because an object moves faster. Total energy increases. This report keeps that distinction.

## 2. Rest mass from balanced internal exchange

The v0.2 exchange-rest-mass formula is:

$$
m_{0,n}=m_{scale}(C_n-1)^{D_f}X_nH(C_n)\max(S_n,0)
$$

with:

$$
X_n=e^{\eta\Gamma_n}
$$

$$
S_n=3.5nX_n-C_n
$$

$$
C_n=2^n
$$

Here `X_n` is the balanced internal exchange/densification factor.

## 3. Velocity from directional exchange

Define directional exchange:

$$
\vec{\Gamma}_n=\frac{1}{C_n}\sum_{i<j}\Gamma_{ij}\vec d_{ij}
$$

The simple motion law is:

$$
\frac{\vec v_n}{c_*}=\frac{\vec{\Gamma}_n}{\Gamma_n}
$$

A bounded version is:

$$
\beta_n=\frac{v_n}{c_*}=\tanh(\mu_n)
$$

where:

$$
\mu_n=\eta|\vec{\Gamma}_n|
$$

Then:

$$
\gamma_n=\frac{1}{\sqrt{1-\beta_n^2}}=\cosh(\mu_n)
$$

and:

$$
m_{eff,n}=\gamma_nm_{0,n}
$$

## 4. Numerical input from v0.2

From the v0.2 tau-like exchange calculation:

$$
X_3=1.0076352925
$$

Thus:

$$
\ln(X_3)=0.0076062912
$$

If that amount is treated as a possible directional exchange scale:

$$
\mu_3=0.0076062912
$$

then:

$$
\beta_3=\tanh(0.0076062912)=0.0076061445
$$

and:

$$
\gamma_3=\cosh(0.0076062912)=1.0000289280
$$

So the motion-energy increase is only:

```text
0.0028928 percent
```

for this small exchange imbalance.

## 5. Effective mass-energy example

Using the observed tau input from earlier reports:

$$
m_{0,\tau}=1776.86\ \text{MeV}
$$

then:

$$
m_{eff,\tau}=1.0000289280\times1776.86=1776.91140096\ \text{MeV}
$$

This is the total effective mass-energy for that small motion factor, not a new rest mass.

Using the old baseline MCIFT tau prediction:

$$
m_{0,\tau}^{base}=1708.60405054\ \text{MeV}
$$

then:

$$
m_{eff,\tau}^{base}=1.0000289280\times1708.60405054=1708.65347699\ \text{MeV}
$$

## 6. Directional fraction table

Let a fraction `f` of the v0.2 exchange scale become directional:

$$
\mu=f\ln(X_3)
$$

Then:

$$
\beta=\tanh(\mu)
$$

and:

$$
\gamma=\cosh(\mu)
$$

| Directional fraction `f` | `mu` | `beta=v/c_*` | `gamma` | energy increase | tau effective mass-energy MeV |
|---:|---:|---:|---:|---:|---:|
| 0 | 0.0000000000 | 0.0000000000 | 1.0000000000 | 0.000000% | 1776.86000000 |
| 0.25 | 0.0019015728 | 0.0019015705 | 1.0000018080 | 0.0001808% | 1776.86321255 |
| 0.5 | 0.0038031456 | 0.0038031273 | 1.0000072320 | 0.0007232% | 1776.87285019 |
| 1 | 0.0076062912 | 0.0076061445 | 1.0000289280 | 0.0028928% | 1776.91140096 |
| 2 | 0.0152125824 | 0.0152114090 | 1.0001157136 | 0.0115714% | 1777.06560680 |
| 5 | 0.0380314559 | 0.0380131304 | 1.0007232830 | 0.0723283% | 1778.14517262 |
| 10 | 0.0760629118 | 0.0759165615 | 1.0028941782 | 0.2894178% | 1782.00254956 |

## 7. Standard velocity table

| `beta=v/c_*` | `gamma` | energy increase |
|---:|---:|---:|
| 0.0010000000 | 1.0000005000 | 0.0000500% |
| 0.0076061445 | 1.0000289280 | 0.0028928% |
| 0.0100000000 | 1.0000500038 | 0.0050004% |
| 0.1000000000 | 1.0050378153 | 0.5037815% |
| 0.5000000000 | 1.1547005384 | 15.4700538% |
| 0.9000000000 | 2.2941573387 | 129.4157339% |
| 0.9900000000 | 7.0888120501 | 608.8812050% |

## 8. Can motion alone explain the tau mass gap?

The old static MCIFT tau prediction was:

$$
1708.60405054\ \text{MeV}
$$

Observed tau input was:

$$
1776.86\ \text{MeV}
$$

The required ratio is:

$$
\gamma=\frac{1776.86}{1708.60405054}=1.0399483716
$$

If this were explained by external motion alone, it would require:

$$
\beta=\sqrt{1-\frac{1}{\gamma^2}}=0.2745031606
$$

and:

$$
\mu=\operatorname{atanh}(\beta)=0.2817274939
$$

This is far larger than the v0.2 exchange scale:

$$
\ln(X_3)=0.0076062912
$$

Therefore motion alone is not a good explanation for the tau rest-mass gap.

## 9. Interpretation

The calculation supports this split:

```text
balanced internal vibratory exchange -> rest mass / densification
external directional exchange -> velocity
velocity -> total energy increase
```

Motion should not replace the internal rest-mass mechanism. It should be added as a separate energy layer.

## 10. Updated compact toy formula

$$
m_{0,n}=m_{scale}(C_n-1)^{D_f}X_nH(C_n)\max(S_n,0)
$$

$$
m_{eff,n}=\gamma_nm_{0,n}
$$

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

## 11. Summary

- Internal vibration/exchange remains the rest-mass mechanism.
- Directional exchange creates motion.
- Motion increases total effective mass-energy through a gamma-like factor.
- At the current v0.2 exchange scale, the motion-energy increase is tiny: about `0.0028928 percent`.
- Motion alone would require `v/c_* = 0.2745` to explain the old tau mass gap, so motion should not be used as the main tau rest-mass correction.
