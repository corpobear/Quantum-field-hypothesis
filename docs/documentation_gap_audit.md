# MCIFT Documentation Gap Audit

**Status:** living documentation audit.  
**Purpose:** identify missing or stale documentation and make the repo easier to navigate.

---

## Fixed in this pass

Added:

```text
docs/mcift_findings_v0.1_to_v0.80.md
```

This consolidates:

```text
v0.1-v0.15 missing/pre-archive note
v0.16-v0.30 archived cosmology development
v0.36-v0.40 collider/3D shell phase
v0.41-v0.49 merge/dark-load feedback phase
v0.50-v0.53 bridge phase
v0.54-v0.58 unified 3D/retest phase
v0.59-v0.64 audit/inverse-timeflow/envelope phase
v0.70-v0.73 dual prediction/cosmology/spatial-lapse phase
v0.80 weak-field GR bridge
```

---

## Still stale or incomplete

### 1. v0.1-v0.15

```text
No clear committed result reports found.
Need reconstruction from notes or prior local files.
```

### 2. Paper folder index

```text
paper/README.md was still pointing to v0.58 before this audit.
It should link to the consolidated findings history and current v0.80 state.
```

### 3. Per-version result folders

Some folders have README files; others only have reports/CSV outputs. Need a consistent index pattern:

```text
analysis/results_vX/README.md
```

for each major result folder.

### 4. v0.31-v0.35

```text
Cubic-field and minimal spatial solver phase needs clearer per-version summary.
```

### 5. v0.41-v0.48

```text
Dense merge / rhythm-lock / visible-dark split phase exists in scripts and result reports but needs a compact narrative.
```

### 6. Glossary

Needed:

```text
C_ITF
O_DV
E_DV
sigma_X
phi_X
tau_ITF
kappa
channel stress
visible branch
dark/sink branch
bridge vs trained vs raw vs transfer
```

### 7. Validation matrix

Needed table columns:

```text
version
claim tested
raw/bridge/trained/transfer
external anchor
pass/fail/mixed
not implemented pieces
```

---

## Recommended next documentation files

```text
docs/glossary.md
docs/validation_matrix.md
docs/results_index.md
docs/cosmology_data_anchors.md
docs/collider_data_anchors.md
```

---

## Safe wording rule

Use this wording:

```text
MCIFT is a speculative scaffold. The repository records toy models, bridges, trained checks, and raw tests. PASS-LIKE means internally close to a selected benchmark, not experimental confirmation.
```

Avoid this wording:

```text
MCIFT proves new physics.
MCIFT replaces GR, QFT, Lambda-CDM, or the Standard Model.
```
