# Test Report v0.15

**Project:** Multi-Channel Information Field Theory / Quantum-field-hypothesis  
**Date:** 2026-06-17  
**Status:** speculative toy-model calculation; not established physics  
**Script:** `analysis/matter_antimatter_toy_v0.15.py`  
**Result CSV:** `analysis/results_v0.15/matter_antimatter_toy_ratio.csv`

---

## 1. Purpose

This report tests the v0.15 antimatter channel geometry as a reduced toy calculation.

The question is:

```text
If antimatter is modeled as positive-mass channel-reversed geometry,
and if its dark sink pulls Higgs drops while its light drill pulls surrounding splashes after discarding the middle,
does the toy geometry give more matter aperture than antimatter aperture?
```

This is not a physical proof of baryon asymmetry. It is an internal consistency calculation for the current MCIFT geometry.

---

## 2. Sign convention

Antimatter is not modeled as negative mass.

Use:

```text
antimatter = positive mass with reversed charge / phase / channel orientation
```

The negative source sign marks inverse orientation, not negative mass. Mass density uses magnitude.

---

## 3. Geometry assumptions

Use the eight-sector constants already used in the repository:

$$
C=8
$$

$$
P_8=\frac{1}{56}
$$

$$
E_8=\frac{1}{448}
$$

$$
B_8(1)=\frac{7}{8}
$$

and the reduced Fibonacci-Higgs overlap:

$$
\langle O_\varphi\rangle=0.9837806705.
$$

---

## 4. Matter aperture

Matter keeps the previous center-tip collector form:

$$
A_M=P_8+B_8(1)E_8\langle O_\varphi\rangle.
$$

Numerically:

$$
A_M=0.0197785894792132.
$$

---

## 5. Antimatter aperture

The v0.15 antimatter geometry uses:

```text
antimatter dark sink = one Higgs-response drop
antimatter light drill = seven local splash units minus one discarded middle
```

So:

$$
A_{Hdrop}=E_8\langle O_\varphi\rangle.
$$

$$
A_{splash,total}=7E_8\langle O_\varphi\rangle.
$$

$$
A_{mid}=E_8\langle O_\varphi\rangle.
$$

$$
A_{splash,captured}=A_{splash,total}-A_{mid}=6E_8\langle O_\varphi\rangle.
$$

Total antimatter aperture:

$$
A_{\bar M}=A_{Hdrop}+A_{splash,captured}.
$$

Numerically:

$$
A_{\bar M}=0.0153715729765625.
$$

---

## 6. Matter-to-antimatter ratio

The reduced toy ratio is:

$$
\frac{A_M}{A_{\bar M}}=1.28669912372469.
$$

The corresponding MCIFT asymmetry parameter is:

$$
\epsilon_{MCIFT}
=
\frac{A_M-A_{\bar M}}{A_M+A_{\bar M}}
=0.125376845930524.
$$

The matter excess aperture is:

$$
A_M-A_{\bar M}=0.00440701650265067.
$$

---

## 7. Verdict

The v0.15 toy geometry gives:

```text
matter aperture > antimatter aperture
```

Short verdict:

```text
more matter remains in this toy channel calculation
```

This result only follows from the chosen v0.15 routing assumptions. It is not yet a confirmed physical prediction.

---

## 8. Important caveat

The asymmetry is much too large to be treated as an observed baryon-asymmetry prediction without additional dilution, thermal history, expansion, annihilation efficiency, or survival dynamics.

Therefore the result should be interpreted as:

```text
internal toy consistency: pass
physical confirmation: no
next task: derive a suppression or evolution law for epsilon_MCIFT
```

---

## 9. Next task

Derive or constrain:

```text
A_Hdrop
A_splash
A_mid
W_Hdrop
W_splash
annihilation overlap
thermal dilution / survival efficiency
final baryon-scale epsilon_MCIFT
```

Only after that can this be compared seriously with cosmological matter-antimatter asymmetry.
