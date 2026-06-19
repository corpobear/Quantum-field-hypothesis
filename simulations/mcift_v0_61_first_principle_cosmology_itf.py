#!/usr/bin/env python3
"""
MCIFT v0.61 first-principle inverse-timeflow cosmology retest.

Status:
    Speculative cosmology scaffold, not established physics.

Purpose:
    Implement a first-principle-style inverse-timeflow cosmology formula after
    v0.60. Unlike v0.60 cosmology smoothing, this script does not derive the
    smoothing factor from the reference H(z) target. Instead, it derives the
    inverse-timeflow load from the MCIFT six-sink / one-anchor sector rule and
    the retained scale-lock amplitude.

Core formula:
    C_ITF = A_lock * N_dark / (N_dark + N_visible + N_anchor)
    tau_ITF = exp[-C_ITF / (N_visible + N_anchor)]
    H_lab(a) = tau_ITF * H_core(a)

This is still not a full CLASS/CAMB, CMB, BAO-ladder, or BBN calculation.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

RESULT_DIR = Path("analysis/results_v0.61")
RESULT_DIR.mkdir(parents=True, exist_ok=True)

# External compact anchors retained from the repo's previous cosmology tests.
H0 = 67.4
OMEGA_M = 0.315
OMEGA_L = 1.0 - OMEGA_M
RD_DESI_MPC = 147.09
CC_H075 = 105.0
CC_H075_SIGMA = 10.756393447619885

# v0.59 / v0.60 cosmology baseline readouts.
H075_RAW_3D = 156.66381928473376
H075_TRANSFER_3D = 103.8977087338893
V020_BAO_PEAK_MPC = 152.29

# MCIFT internal sector/anchor values from prior first-principle sink retests.
N_DARK = 6
N_VISIBLE = 1
N_ANCHOR = 1
A_LOCK_5B = 0.918752


def h_lcdm(z: float) -> float:
    return H0 * math.sqrt(OMEGA_M * (1.0 + z) ** 3 + OMEGA_L)


def inverse_timeflow_load() -> float:
    return A_LOCK_5B * N_DARK / (N_DARK + N_VISIBLE + N_ANCHOR)


def tau_itf_first_principle() -> float:
    c_itf = inverse_timeflow_load()
    return math.exp(-c_itf / (N_VISIBLE + N_ANCHOR))


def percent_delta(value: float, reference: float) -> float:
    return 100.0 * (value / reference - 1.0)


def sigma_residual(value: float, observed: float, sigma: float) -> float:
    return (value - observed) / sigma


def write_csv(path: Path, rows) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main() -> None:
    h075_ref = h_lcdm(0.75)
    c_itf = inverse_timeflow_load()
    tau = tau_itf_first_principle()
    h075_v061 = tau * H075_RAW_3D
    h075_v060 = H075_TRANSFER_3D

    bao_error = abs(V020_BAO_PEAK_MPC / RD_DESI_MPC - 1.0)

    rows = [
        ["metric", "value"],
        ["verdict", "FIRST_PRINCIPLE_ITF_IMPROVES_RAW_HZ_NOT_FULL_COSMOLOGY_PASS"],
        ["formula", "H_lab = exp[-C_ITF/(N_visible+N_anchor)] * H_core"],
        ["C_ITF", f"{c_itf:.15g}"],
        ["tau_ITF", f"{tau:.15g}"],
        ["N_dark", N_DARK],
        ["N_visible", N_VISIBLE],
        ["N_anchor", N_ANCHOR],
        ["A_lock_5B", f"{A_LOCK_5B:.15g}"],
        ["H0_anchor", f"{H0:.15g}"],
        ["Omega_m_reference", f"{OMEGA_M:.15g}"],
        ["H075_reference_LCDM", f"{h075_ref:.15g}"],
        ["H075_CC_observed", f"{CC_H075:.15g}"],
        ["H075_CC_sigma", f"{CC_H075_SIGMA:.15g}"],
        ["v0_59_H075_raw_3d", f"{H075_RAW_3D:.15g}"],
        ["v0_59_H075_raw_delta_pct_vs_LCDM", f"{percent_delta(H075_RAW_3D, h075_ref):.15g}"],
        ["v0_59_H075_raw_sigma_vs_CC", f"{sigma_residual(H075_RAW_3D, CC_H075, CC_H075_SIGMA):.15g}"],
        ["v0_60_H075_transfer_scaffold", f"{h075_v060:.15g}"],
        ["v0_60_H075_transfer_delta_pct_vs_LCDM", f"{percent_delta(h075_v060, h075_ref):.15g}"],
        ["v0_60_H075_transfer_sigma_vs_CC", f"{sigma_residual(h075_v060, CC_H075, CC_H075_SIGMA):.15g}"],
        ["v0_61_H075_first_principle_ITF", f"{h075_v061:.15g}"],
        ["v0_61_H075_first_principle_ITF_delta_pct_vs_LCDM", f"{percent_delta(h075_v061, h075_ref):.15g}"],
        ["v0_61_H075_first_principle_ITF_sigma_vs_CC", f"{sigma_residual(h075_v061, CC_H075, CC_H075_SIGMA):.15g}"],
        ["raw_to_v061_delta_pct_improvement_factor", f"{abs(percent_delta(H075_RAW_3D, h075_ref))/abs(percent_delta(h075_v061, h075_ref)):.15g}"],
        ["v0_20_BAO_peak_Mpc", f"{V020_BAO_PEAK_MPC:.15g}"],
        ["DESI_rd_reference_Mpc", f"{RD_DESI_MPC:.15g}"],
        ["v0_20_BAO_peak_fractional_error", f"{bao_error:.15g}"],
        ["uses_reference_derived_smoothing", "False"],
        ["full_BAO_ladder_implemented", "False"],
        ["CMB_power_spectrum_implemented", "False"],
        ["BBN_network_implemented", "False"],
    ]
    write_csv(RESULT_DIR / "mcift_v0.61_first_principle_cosmology_metrics.csv", rows)

    comparison = [
        ["stage", "H075", "delta_pct_vs_LCDM", "sigma_vs_CC", "status"],
        [
            "v0.59 raw 3D",
            f"{H075_RAW_3D:.12f}",
            f"{percent_delta(H075_RAW_3D, h075_ref):.12f}",
            f"{sigma_residual(H075_RAW_3D, CC_H075, CC_H075_SIGMA):.12f}",
            "FAIL_OVEREXPANDS",
        ],
        [
            "v0.60 reference-derived transfer scaffold",
            f"{h075_v060:.12f}",
            f"{percent_delta(h075_v060, h075_ref):.12f}",
            f"{sigma_residual(h075_v060, CC_H075, CC_H075_SIGMA):.12f}",
            "PASS_LIKE_SCAFFOLD",
        ],
        [
            "v0.61 first-principle ITF",
            f"{h075_v061:.12f}",
            f"{percent_delta(h075_v061, h075_ref):.12f}",
            f"{sigma_residual(h075_v061, CC_H075, CC_H075_SIGMA):.12f}",
            "IMPROVED_NOT_FULL_PASS",
        ],
    ]
    write_csv(RESULT_DIR / "mcift_v0.61_Hz_comparison.csv", comparison)

    report = f"""# MCIFT v0.61 First-Principle Inverse-Timeflow Cosmology Retest

**Status:** first-principle-style cosmology retest scaffold; not established physics.  
**Generated by:** `simulations/mcift_v0_61_first_principle_cosmology_itf.py`

---

## Purpose

v0.60 implemented inverse-timeflow backpropagation for the particle/channel bridge, but cosmology still used the v0.59 transfer/smoothing scaffold. v0.61 implements a cosmology-specific inverse-timeflow formula that acts inside the expansion rule rather than after the output.

---

## Formula implemented

The inverse-timeflow load is derived from the six-sink / one-visible / one-anchor sector rule:

```text
C_ITF = A_lock * N_dark / (N_dark + N_visible + N_anchor)
```

Then:

```text
tau_ITF = exp[-C_ITF / (N_visible + N_anchor)]
H_lab(a) = tau_ITF * H_core(a)
```

Numerical values:

```text
N_dark = {N_DARK}
N_visible = {N_VISIBLE}
N_anchor = {N_ANCHOR}
A_lock_5B = {A_LOCK_5B:.6f}
C_ITF = {c_itf:.6f}
tau_ITF = {tau:.6f}
```

This is different from v0.60 smoothing because `tau_ITF` is not solved from the target H(z) value.

---

## H(z=0.75) retest

Reference compact anchors:

```text
Planck-like LCDM H(0.75) = {h075_ref:.6f}
Cosmic-chronometer compact point H(0.75) = {CC_H075:.6f} +/- {CC_H075_SIGMA:.6f}
```

| stage | H(0.75) | delta vs LCDM | residual vs CC point | status |
|---|---:|---:|---:|---|
| v0.59 raw 3D | {H075_RAW_3D:.6f} | {percent_delta(H075_RAW_3D, h075_ref):+.6f}% | {sigma_residual(H075_RAW_3D, CC_H075, CC_H075_SIGMA):+.6f} sigma | FAIL_OVEREXPANDS |
| v0.60 transfer scaffold | {h075_v060:.6f} | {percent_delta(h075_v060, h075_ref):+.6f}% | {sigma_residual(h075_v060, CC_H075, CC_H075_SIGMA):+.6f} sigma | PASS_LIKE_SCAFFOLD |
| v0.61 first-principle ITF | {h075_v061:.6f} | {percent_delta(h075_v061, h075_ref):+.6f}% | {sigma_residual(h075_v061, CC_H075, CC_H075_SIGMA):+.6f} sigma | IMPROVED_NOT_FULL_PASS |

Improvement factor versus raw percent error:

```text
{abs(percent_delta(H075_RAW_3D, h075_ref))/abs(percent_delta(h075_v061, h075_ref)):.6f}x
```

---

## BAO scale sanity check

The v0.61 formula targets expansion-timeflow first, not the BAO ladder. The existing compact BAO-scale sanity check remains:

```text
v0.20 BAO/global peak = {V020_BAO_PEAK_MPC:.6f} Mpc
DESI-style r_d reference = {RD_DESI_MPC:.6f} Mpc
fractional error = {bao_error:.6f}
```

---

## Verdict

```text
FIRST_PRINCIPLE_ITF_IMPROVES_RAW_HZ_NOT_FULL_COSMOLOGY_PASS
```

Meaning:

```text
v0.61 improves raw over-expansion without using reference-derived smoothing.
It does not yet replace a real cosmology pipeline.
Full BAO ladder, CMB spectra, growth data, and BBN are still not implemented.
```

---

## Next target

```text
v0.62 should make C_ITF redshift-dependent from actual 3D field cells:
C_ITF(a) = sum_i W_i(a) max(0, -S_i(a))^2 / sum_i W_i(a)(Coh_i(a)^2 + q_i(a)^2 + epsilon)
```

That would move from a sector-derived global inverse-timeflow factor to a cell-resolved cosmology model.
"""
    (RESULT_DIR / "mcift_v0.61_first_principle_cosmology_report.md").write_text(report)


if __name__ == "__main__":
    main()
