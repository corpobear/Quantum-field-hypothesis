# Test Report v0.2: Vibration, Exchange Rate, and Shadow Amplitude

**Status:** speculative toy-model calculations.  
**Purpose:** document the numerical effect of adding information exchange rate and shadow-amplitude correction to the existing MCIFT toy mass model.

## 1. Baseline from v0.1.1

The earlier fixed-core linear Gaussian toy model used electron and muon as calibration anchors and then predicted the tau-like third mode.

Baseline result:

$$
m_\tau^{MCIFT}=1708.60405054\ \text{MeV}
$$

Observed tau input used in this toy comparison:

$$
m_\tau=1776.86\ \text{MeV}
$$

Mass ratio required to reach the tau value:

$$
\frac{1776.86}{1708.60405054}=1.0399483716
$$

So the old static model was low by about:

```text
3.995 percent
```

## 2. Information exchange correction

Introduce an exchange/densification factor:

$$
X_n=e^{\eta\Gamma_n}
$$

where:

```text
Gamma_n = internal coherent information exchange rate of the nth knot
eta    = exchange-to-density scale
```

The updated stability rule is:

$$
S_n=3.5nX_n-2^n
$$

The updated mass rule is:

$$
m_n=m_0(C_n-1)^{D_f}X_nH(C_n)\max(S_n,0)
$$

with:

$$
C_n=2^n
$$

## 3. Tau exchange factor when exchange also strengthens stability

For the third mode:

$$
S_3=3.5(3)X_3-8=10.5X_3-8
$$

The old third-mode stability was:

$$
S_3^{old}=2.5
$$

Because the new factor affects both mass and stability, solve:

$$
X_3\frac{10.5X_3-8}{2.5}=1.0399483716
$$

Positive solution:

$$
X_3=1.0076352925
$$

This means the tau-like third knot needs only about:

```text
0.7635 percent coherent exchange boost
```

when exchange strengthens both densification and stability.

The updated third-mode stability becomes:

$$
S_3=10.5(1.0076352925)-8=2.5801705718
$$

## 4. Fourth-mode constraint

Mode 4 must still fail.

For mode 4:

$$
S_4=3.5(4)X_4-16=14X_4-16
$$

Failure requires:

$$
14X_4-16<0
$$

Therefore:

$$
X_4<1.1428571429
$$

In exchange-density form:

$$
\eta\Gamma_4<\ln(1.1428571429)=0.1335313926
$$

So the fourth mode may contain exchange, but coherent exchange must remain below the threshold that would incorrectly stabilize it.

## 5. Shadow-amplitude correction

The shadow-amplitude extension says that MCIFT should calculate mass amplitude first:

$$
A_n=\sqrt{m_n}
$$

and then square it:

$$
m_n=A_n^2
$$

The amplitude correction required to move the baseline MCIFT tau value to the observed tau value is:

$$
\Delta_3=\sqrt{\frac{1776.86}{1708.60405054}}=1.0197785895
$$

So the old 3.995 percent mass gap becomes only about:

```text
1.978 percent amplitude gap
```

Base MCIFT tau amplitude:

$$
\sqrt{1708.60405054}=41.3352640071
$$

Observed tau amplitude:

$$
\sqrt{1776.86}=42.1528172249
$$

Amplitude difference:

$$
42.1528172249-41.3352640071=0.8175532178
$$

## 6. Comparison with Koide

Koide high-root tau value from the v0.1.1 benchmark:

$$
m_\tau^{Koide}=1776.9690270830\ \text{MeV}
$$

Koide's tau value has an error of about:

```text
+0.006136 percent
```

relative to 1776.86 MeV.

The amplitude correction needed to move baseline MCIFT to Koide is:

$$
\sqrt{\frac{1776.9690270830}{1708.60405054}}=1.0198098755
$$

Compare shadow-amplitude factors:

| Target | Amplitude factor from baseline MCIFT |
|---|---:|
| Observed tau | 1.0197785895 |
| Koide tau | 1.0198098755 |

Difference:

$$
1.0198098755-1.0197785895=0.0000312860
$$

This shows that the shadow-amplitude correction needed by MCIFT is almost the same correction needed to land on the Koide high-root tau value.

## 7. Koide angle check

In amplitude space, Koide corresponds to the charged-lepton amplitude vector being almost exactly 45 degrees from the equal-symmetry direction.

| Case | Koide-style angle |
|---|---:|
| observed masses | 44.999735 degrees |
| old MCIFT linear prediction | 44.829743 degrees |
| old MCIFT log prediction | 45.098291 degrees |
| exact Koide high root | 45.000000 degrees |

Interpretation:

```text
The old MCIFT linear model was slightly below the Koide amplitude angle. The shadow-amplitude correction pushes it toward the Koide structure.
```

## 8. Interpretation

The v0.2 additions suggest:

```text
information cluster
-> internal vibration
-> information exchange rate
-> coherent densification
-> visible/complementary amplitude imbalance
-> squared mass
```

The most important change is that mass should probably not be calculated directly at the deepest toy level. The model should calculate a mass amplitude first, then square it.

## 9. Honest status

This does not yet beat Koide.

Koide remains the stronger numerical mass relation. MCIFT currently offers a possible mechanism-path: knot complexity, finite Higgs response, information exchange, and visible/complementary amplitude imbalance.

The next goal is not to fit the tau correction after seeing tau. The next goal is to derive:

$$
X_n=e^{\eta\Gamma_n}
$$

and:

$$
\Delta_n
$$

from a concrete knot geometry.

## 10. Summary

- Static MCIFT tau prediction: `1708.60405054 MeV`.
- Observed tau input: `1776.86 MeV`.
- Direct mass correction required: `1.0399483716`.
- Shadow-amplitude correction required: `1.0197785895`.
- Exchange-stability correction required: `X_3=1.0076352925`.
- Fourth mode still fails if `X_4<1.1428571429`.
- Koide still wins numerically, but shadow-amplitude MCIFT moves naturally toward Koide's square-root mass geometry.
