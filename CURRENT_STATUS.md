# Current MCIFT Status: v0.64 Unified First-Principle Formula Consolidation

**Status:** speculative research scaffold; not established physics.  
**Current layer:** v0.64 formula/paper consolidation on master.  
**Previous layers:** v0.61 cosmology ITF, v0.62 blind CERN ITF, v0.63 dark-visible width envelope.

---

## One-sentence status

```text
MCIFT v0.64 consolidates the inverse-timeflow and dark-visible gravitational-envelope work directly on the main branch. It updates the paper entry point, formula documentation, README, status file, and key result metrics.
```

---

## v0.64 verdict

```text
REWORKED_FIRST_PRINCIPLE_FORMULA_DOCUMENTED_ON_MASTER
```

---

## Formula summary

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
tau_ITF = exp[-C_ITF / (N_V + N_A)]
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

Current values:

```text
N_D = 6
N_V = 1
N_A = 1
A_lock = 0.918752
C_ITF = 0.689064
O_DV = 0.612372
E_DV = 1.234890
```

---

## CERN/Higgs result

```text
v0.62 blind max channel delta = 8.247649 percent
v0.62 blind total width = 3.325981 MeV
v0.62 width delta = -18.280555 percent

v0.63 width after dark-visible envelope = 4.107221 MeV
v0.63 width delta vs 4.07 MeV = +0.914526 percent
```

Status:

```text
branching-ratio pattern: PASS-LIKE / retained
absolute width: IMPROVED / pass-like scaffold
backpropagation used for v0.62 or v0.63 blind result: False
```

---

## Cosmology result

```text
v0.59 raw H075 = 156.663819
v0.61 first-principle ITF H075 = 111.004443
LCDM compact reference H075 = 103.831075
raw-to-v0.61 error improvement = 7.364392x
```

Status:

```text
raw H(z) over-expansion: improved
full BAO ladder: not implemented
CMB spectra: not implemented
BBN network: not implemented
```

---

## Main files on master

```text
main.md
README.md
CURRENT_STATUS.md
models/mcift_first_principle_formula_v0.64.md
analysis/results_v0.64/mcift_v0.64_master_formula_summary.csv
analysis/results_v0.62/mcift_v0.62_blind_itf_metrics.csv
analysis/results_v0.62/mcift_v0.62_blind_itf_channels.csv
analysis/results_v0.63/mcift_v0.63_width_metrics.csv
```

---

## Next target

```text
v0.65 should move from sector-count rules to cell-resolved rules:
S_i = Coh_i - q_i
C_ITF(a) from weighted negative stability stress
O_DV(a) from dark-visible density overlap
Then retest H(z), BAO, CERN total width, branching ratios, and signal-strength style observables separately.
```
