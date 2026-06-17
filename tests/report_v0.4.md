# Test Report v0.4: Shadow Projection and Koide Comparison

**Status:** speculative toy-model calculation.  
**Purpose:** input the `2/3` shadow-projection idea into the MCIFT tau toy model and compare it against observed tau and Koide.

## 1. Baseline values

Baseline MCIFT tau prediction from the fixed-core linear Gaussian toy model:

```math
m_\tau^{base}=1708.60405054\ \text{MeV}
```

Observed tau input used in previous reports:

```math
m_\tau^{obs}=1776.86\ \text{MeV}
```

Koide high-root tau value from the earlier benchmark:

```math
m_\tau^{Koide}=1776.9690270830\ \text{MeV}
```

## 2. Shadow projection formula

For the tau-like third mode:

```math
C_3=2^3=8
```

Primary shadow term:

```math
s_1=\frac{1}{C_3(C_3-1)}=\frac{1}{8\cdot7}=\frac{1}{56}=0.0178571429
```

Echo-shadow term:

```math
s_2=\frac{s_1}{C_3}=\frac{1}{448}=0.0022321429
```

Amplitude correction:

```math
\Delta(f)=1+s_1+fs_2
```

Mass prediction:

```math
m_\tau(f)=m_\tau^{base}\Delta(f)^2
```

## 3. Two-thirds projection test

Input:

```math
f=\frac{2}{3}
```

Then:

```math
\Delta_{2/3}=1.0193452381
```

and:

```math
m_\tau^{2/3}=1775.35017984\ \text{MeV}
```

Error against observed tau:

```math
1775.35017984-1776.86=-1.50982016\ \text{MeV}
```

```text
-0.0849713 percent
```

Error against Koide:

```math
1775.35017984-1776.96902708=-1.61884724\ \text{MeV}
```

```text
-0.0911016 percent
```

Koide angle using electron, muon, and the two-thirds shadow tau value:

```math
44.9960703985^\circ
```

This is only:

```math
0.0039296015^\circ
```

below the exact Koide 45-degree angle.

## 4. Exact echo-shadow fractions

The exact echo-shadow fraction needed to reach observed tau is:

```math
f_{obs}=0.8608080867
```

The exact echo-shadow fraction needed to reach Koide is:

```math
f_{Koide}=0.8748242267
```

This is close to:

```math
\frac{7}{8}=0.875
```

## 5. Seven-eighths projection test

Because the tau-like knot has:

```math
C_3=8
```

try:

```math
f=1-\frac{1}{C_3}=\frac{7}{8}
```

Then:

```math
\Delta_{7/8}=1.0198102679
```

and:

```math
m_\tau^{7/8}=1776.97039439\ \text{MeV}
```

Error against observed tau:

```math
1776.97039439-1776.86=0.11039439\ \text{MeV}
```

```text
+0.0062129 percent
```

Error against Koide:

```math
1776.97039439-1776.96902708=0.00136731\ \text{MeV}
```

```text
+0.0000769 percent
```

Koide angle using electron, muon, and the seven-eighths shadow tau value:

```math
45.0000033170^\circ
```

This is only:

```math
0.0000033170^\circ
```

above the exact Koide angle.

## 6. Comparison table

| Model | Tau mass MeV | Error vs observed | Error vs Koide | Koide angle |
|---|---:|---:|---:|---:|
| Baseline MCIFT | 1708.60405054 | -3.841% | -3.847% | 44.8297434154 deg |
| `2/3` echo-shadow | 1775.35017984 | -0.084971% | -0.091102% | 44.9960703985 deg |
| `7/8` echo-shadow | 1776.97039439 | +0.006213% | +0.0000769% | 45.0000033170 deg |
| Koide high-root | 1776.96902708 | +0.006136% | 0.000000% | 45.0000000000 deg |

## 7. Interpretation

The `2/3` projection is conceptually important because Koide's relation is equivalent to a 45-degree amplitude angle.

However, in this specific tau echo-shadow model, the best simple structural fraction is:

```math
\frac{7}{8}
```

This is natural because:

```math
C_3=8
```

and:

```math
\frac{7}{8}=1-\frac{1}{C_3}
```

Therefore:

```text
2/3 = global Koide amplitude-angle projection
7/8 = local tau echo-shadow completion fraction
```

## 8. Honest status

This is not yet a derivation of Koide.

It is a strong toy-model clue: when the tau mode is treated as an 8-point knot with one primary shadow and a complexity-limited echo-shadow, the fraction `7/8` lands almost exactly on Koide.

The next step is to derive:

```math
f_n=1-\frac{1}{C_n}
```

from knot geometry rather than introducing it after the numerical comparison.

## 9. Summary

- `2/3` echo-shadow projection moves MCIFT very close to Koide.
- `7/8` echo-shadow projection lands almost exactly on Koide.
- The `7/8` value is structurally natural for tau because tau has `C_3=8`.
- The result suggests that Koide's global `2/3` angle and tau's local `7/8` echo-completion may be two different parts of the same shadow-amplitude geometry.
