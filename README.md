# Multi-Channel Information Field Theory (MCIFT)

**Status:** speculative theoretical framework / toy-field, collider, and cosmology scaffold  
**Author:** Adrian Newton / corpobear  
**Repository:** Quantum-field-hypothesis  
**Current version:** v0.64 unified first-principle formula consolidation

> MCIFT is not established physics and is not a replacement for quantum field theory, general relativity, the Standard Model of particle physics, or the standard cosmology model. This repository contains exploratory mechanics, toy calculations, and increasingly testable scaffolds.

---

## Current focus

The main branch now consolidates the v0.61-v0.63 work into a v0.64 first-principle formula:

```text
v0.61: first-principle inverse timeflow improved raw cosmology H(z=0.75)
v0.62: blind CERN ITF prediction improved branching ratios without backpropagation
v0.63: dark-visible gravitational envelope fixed the total-width deficit while retaining branching ratios
v0.64: paper/formula consolidation on master, including main.md
```

Current verdict:

```text
v0.64 = REWORKED_FIRST_PRINCIPLE_FORMULA_DOCUMENTED_ON_MASTER
```

---

## Reworked formula

```text
C_ITF = A_lock * N_D / (N_D + N_V + N_A)
tau_ITF = exp[-C_ITF / (N_V + N_A)]
O_DV = 2 sqrt(N_D N_V) / (N_D + N_V + N_A)
E_DV = exp[C_ITF * O_DV / (N_V + N_A)]
```

Current numerical values:

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
v0.62 blind width = 3.325981 MeV
v0.62 width delta = -18.280555 percent

v0.63 width after dark-visible envelope = 4.107221 MeV
v0.63 width delta vs 4.07 MeV = +0.914526 percent
```

The envelope is universal, so the branching-ratio pattern is retained while the total width is lifted.

---

## Cosmology result

```text
v0.59 raw H075 = 156.663819
v0.61 first-principle ITF H075 = 111.004443
LCDM compact reference H075 = 103.831075
raw-to-v0.61 error improvement = 7.364392x
```

This improves raw over-expansion without reference-derived smoothing, but it is not yet a full cosmology pass.

---

## Main documents

```text
main.md
models/mcift_first_principle_formula_v0.64.md
CURRENT_STATUS.md
analysis/results_v0.64/mcift_v0.64_master_formula_summary.csv
analysis/results_v0.62/mcift_v0.62_blind_itf_metrics.csv
analysis/results_v0.63/mcift_v0.63_width_metrics.csv
```

---

## Next version target

```text
v0.65 should replace sector-count C_ITF and O_DV with cell-resolved field quantities:
S_i = Coh_i - q_i
C_ITF(a) from weighted negative-stability stress
O_DV(a) from dark-visible density overlap
```

---

## Citation / attribution

If referencing this framework, please attribute it to Adrian Newton / corpobear and this repository.

See [`NOTICE.md`](NOTICE.md) for authorship and priority information.
