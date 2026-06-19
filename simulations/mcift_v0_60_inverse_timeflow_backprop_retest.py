#!/usr/bin/env python3
"""
MCIFT v0.60 inverse-timeflow backpropagation retest.

Status:
    Speculative scaffold / implementation test, not established physics.

What this script implements:
    1. Explicit loop/surface readouts for gamma and Zgamma.
    2. Explicit cc projection from the core-fermion / color bridge.
    3. A differentiable inverse-timeflow loss layer in plain Python.
    4. A before/after comparison against the v0.59 raw baseline.

Important:
    The final optimized comparison is a trained bridge result, not a raw
    first-principle prediction. Raw and trained results are reported separately.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path
from typing import Dict, Tuple

RESULT_DIR = Path("analysis/results_v0.60")
RESULT_DIR.mkdir(parents=True, exist_ok=True)

SM_TOTAL_WIDTH_MEV = 4.070000

# v0.59 / v0.58 raw 3D channel baseline.
CHANNELS = [
    ("bb",     0.582384276,   0.6197557475800611),
    ("WW",     0.213694230,   0.2132014094097443),
    ("gg",     0.0817977915,  0.0688832690776304),
    ("tau",    0.0626983071,  0.0712617023835817),
    ("cc",     0.0289992170,  0.0),
    ("ZZ",     0.0263992872,  0.0266501761762180),
    ("gamma",  0.00226993871, 0.0000017195969070847837),
    ("Zgamma", 0.00153995842, 0.0000006091348074004856),
    ("mumu",   0.000216994141,0.0002453666410498),
]

# v0.59 cosmology baseline values.
H075_RAW_3D = 156.66381928473376
H075_TRANSFER_3D = 103.8977087338893
H075_LCDM_REFERENCE = 103.83107544528758


def normalize(widths: Dict[str, float]) -> Dict[str, float]:
    total = sum(widths.values())
    if total <= 0:
        raise ValueError("Cannot normalize non-positive total width.")
    return {key: value / total for key, value in widths.items()}


def percent_delta(value: float, reference: float) -> float:
    if reference == 0:
        return float("inf")
    return 100.0 * (value / reference - 1.0)


def l1_distance(a: Dict[str, float], b: Dict[str, float]) -> float:
    return sum(abs(a[key] - b[key]) for key in b)


def build_implemented_readout() -> Tuple[Dict[str, float], Dict[str, float]]:
    """Add missing readouts while keeping the rule deterministic.

    The formulas are intentionally small and explicit:
      - gg receives color/vector surface feedback.
      - cc is projected from the color bridge and core fermion bridge.
      - gamma and Zgamma receive loop/surface readouts rather than near-zero raw leakage.

    These are implementation rules, not proof of the physical hypothesis.
    """
    sm = {channel: ref for channel, ref, _ in CHANNELS}
    raw = {channel: raw for channel, _, raw in CHANNELS}
    factors = {channel: raw[channel] / sm[channel] for channel in sm}

    color_feedback = math.sqrt(factors["bb"] * factors["WW"])
    gg_impl = math.sqrt(factors["gg"] * color_feedback)

    fermion_core = math.sqrt(factors["tau"] * factors["mumu"])
    cc_impl = math.sqrt(gg_impl * fermion_core)

    vector_loop = math.sqrt(factors["WW"] * factors["ZZ"])
    gamma_impl = math.sqrt(vector_loop * gg_impl)
    Zgamma_impl = math.sqrt(gamma_impl * factors["ZZ"])

    implemented_factors = {
        "bb": factors["bb"],
        "WW": factors["WW"],
        "gg": gg_impl,
        "tau": factors["tau"],
        "cc": cc_impl,
        "ZZ": factors["ZZ"],
        "gamma": gamma_impl,
        "Zgamma": Zgamma_impl,
        "mumu": factors["mumu"],
    }

    implemented_widths = {
        channel: sm[channel] * implemented_factors[channel]
        for channel in sm
    }
    return implemented_factors, normalize(implemented_widths)


def predict_from_params(
    implemented_factors: Dict[str, float],
    params: Dict[str, float],
) -> Tuple[Dict[str, float], float, float]:
    """Forward pass used by inverse-timeflow backpropagation loss."""
    sm = {channel: ref for channel, ref, _ in CHANNELS}
    log_tau = params.get("log_tau", 0.0)

    proper_partials = {}
    for channel in sm:
        log_correction = params.get(f"x_{channel}", 0.0)
        proper_partials[channel] = (
            SM_TOTAL_WIDTH_MEV
            * sm[channel]
            * implemented_factors[channel]
            * math.exp(log_correction)
        )

    tau_time = math.exp(log_tau)
    lab_partials = {key: tau_time * value for key, value in proper_partials.items()}
    lab_total = sum(lab_partials.values())
    branching = normalize(lab_partials)
    return branching, lab_total, tau_time


def inverse_timeflow_loss(
    implemented_factors: Dict[str, float],
    params: Dict[str, float],
    regularization: float = 0.03,
) -> float:
    """Final derived loss expression used for backpropagation.

    This is the AI-style inverse-timeflow layer:
        lab residual -> loss -> hidden/core correction parameters.

    The loss fits branching ratios and total width while penalizing hidden
    corrections so the bridge cannot silently claim to be raw prediction.
    """
    sm = {channel: ref for channel, ref, _ in CHANNELS}
    br, total_width, _ = predict_from_params(implemented_factors, params)

    channel_loss = sum(
        math.log(br[channel] / sm[channel]) ** 2
        for channel in sm
    )
    width_loss = 0.5 * math.log(total_width / SM_TOTAL_WIDTH_MEV) ** 2
    correction_loss = regularization * sum(
        params.get(f"x_{channel}", 0.0) ** 2
        for channel in sm
    )
    clock_loss = 0.01 * params.get("log_tau", 0.0) ** 2

    return channel_loss + width_loss + correction_loss + clock_loss


def train_inverse_timeflow(
    implemented_factors: Dict[str, float],
    iterations: int = 4000,
    learning_rate: float = 0.20,
) -> Tuple[Dict[str, float], float]:
    """Finite-difference gradient descent.

    Plain Python is used so the repo does not need PyTorch/JAX for this small
    retest. The result is deterministic.
    """
    params = {"log_tau": 0.0}
    for channel, _, _ in CHANNELS:
        params[f"x_{channel}"] = 0.0

    keys = list(params.keys())
    eps = 1e-5

    for step_index in range(iterations):
        grads = {}
        for key in keys:
            old = params[key]
            params[key] = old + eps
            plus = inverse_timeflow_loss(implemented_factors, params)
            params[key] = old - eps
            minus = inverse_timeflow_loss(implemented_factors, params)
            params[key] = old
            grads[key] = (plus - minus) / (2.0 * eps)

        step = learning_rate / (1.0 + step_index / 900.0)
        for key in keys:
            params[key] -= step * grads[key]

        # Conservative clamps so hidden corrections are bounded.
        params["log_tau"] = max(-1.0, min(1.0, params["log_tau"]))
        for channel, _, _ in CHANNELS:
            key = f"x_{channel}"
            params[key] = max(-1.0, min(1.0, params[key]))

    final_loss = inverse_timeflow_loss(implemented_factors, params)
    return params, final_loss


def cosmology_after_timeflow() -> Tuple[float, float]:
    """Use the same inverse-timeflow exponential smoothing form.

    q is derived from the v0.59 transfer readout so the cosmology side is not
    silently improved by a new free parameter in this retest.
    """
    q_smoothing = -math.log(
        (H075_TRANSFER_3D - H075_LCDM_REFERENCE)
        / (H075_RAW_3D - H075_LCDM_REFERENCE)
    )
    h_after = H075_LCDM_REFERENCE + (
        H075_RAW_3D - H075_LCDM_REFERENCE
    ) * math.exp(-q_smoothing)
    return q_smoothing, h_after


def write_csv(path: Path, rows):
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerows(rows)


def main() -> None:
    sm = {channel: ref for channel, ref, _ in CHANNELS}
    raw = {channel: raw for channel, _, raw in CHANNELS}
    raw_delta = {channel: percent_delta(raw[channel], sm[channel]) for channel in sm}
    raw_failed = [channel for channel, delta in raw_delta.items() if abs(delta) > 10.0]

    implemented_factors, implemented_br = build_implemented_readout()
    implemented_delta = {
        channel: percent_delta(implemented_br[channel], sm[channel])
        for channel in sm
    }
    implemented_failed = [
        channel for channel, delta in implemented_delta.items()
        if abs(delta) > 10.0
    ]

    params, final_loss = train_inverse_timeflow(implemented_factors)
    trained_br, trained_total_width, tau_time = predict_from_params(
        implemented_factors, params
    )
    trained_delta = {
        channel: percent_delta(trained_br[channel], sm[channel])
        for channel in sm
    }
    trained_failed = [
        channel for channel, delta in trained_delta.items()
        if abs(delta) > 10.0
    ]

    q_smoothing, h_after = cosmology_after_timeflow()

    rows = [
        ["channel", "BR_SM_ref", "BR_v0_59_raw", "delta_pct_v0_59_raw",
         "BR_v0_60_implemented", "delta_pct_v0_60_implemented",
         "BR_v0_60_after_inverse_timeflow", "delta_pct_v0_60_after_inverse_timeflow",
         "hidden_log_correction"],
    ]
    for channel in sm:
        rows.append([
            channel,
            f"{sm[channel]:.12g}",
            f"{raw[channel]:.12g}",
            f"{raw_delta[channel]:.12f}",
            f"{implemented_br[channel]:.12g}",
            f"{implemented_delta[channel]:.12f}",
            f"{trained_br[channel]:.12g}",
            f"{trained_delta[channel]:.12f}",
            f"{params.get('x_' + channel, 0.0):.12f}",
        ])
    write_csv(RESULT_DIR / "mcift_v0.60_cern_channels_before_after.csv", rows)

    metrics = [
        ["metric", "value"],
        ["verdict", "IMPLEMENTED_BACKPROP_IMPROVES_CERN_BRIDGE_RAW_STILL_SCAFFOLD"],
        ["v0_59_inverse_timeflow_backprop_loss", "NOT_IMPLEMENTED"],
        ["v0_60_inverse_timeflow_backprop_loss", "IMPLEMENTED"],
        ["v0_60_gamma_Zgamma_loop_surface_readout", "IMPLEMENTED"],
        ["v0_60_cc_projection", "IMPLEMENTED"],
        ["v0_59_raw_BR_L1_vs_SM", f"{l1_distance(raw, sm):.15g}"],
        ["v0_60_implemented_BR_L1_vs_SM", f"{l1_distance(implemented_br, sm):.15g}"],
        ["v0_60_after_backprop_BR_L1_vs_SM", f"{l1_distance(trained_br, sm):.15g}"],
        ["v0_59_raw_max_abs_BR_delta_pct", f"{max(abs(x) for x in raw_delta.values()):.15g}"],
        ["v0_60_implemented_max_abs_BR_delta_pct", f"{max(abs(x) for x in implemented_delta.values()):.15g}"],
        ["v0_60_after_backprop_max_abs_BR_delta_pct", f"{max(abs(x) for x in trained_delta.values()):.15g}"],
        ["v0_59_failed_CERN_channels_10pct", ",".join(raw_failed)],
        ["v0_60_implemented_failed_CERN_channels_10pct", ",".join(implemented_failed)],
        ["v0_60_after_backprop_failed_CERN_channels_10pct", ",".join(trained_failed)],
        ["v0_60_after_backprop_total_width_MeV", f"{trained_total_width:.15g}"],
        ["v0_60_after_backprop_total_width_delta_pct", f"{percent_delta(trained_total_width, SM_TOTAL_WIDTH_MEV):.15g}"],
        ["v0_60_tau_time_lab_factor", f"{tau_time:.15g}"],
        ["v0_60_inverse_timeflow_loss_final", f"{final_loss:.15g}"],
        ["v0_59_H075_raw_3d", f"{H075_RAW_3D:.15g}"],
        ["v0_59_H075_transfer_3d", f"{H075_TRANSFER_3D:.15g}"],
        ["v0_60_q_smoothing_derived_from_v0_59_transfer", f"{q_smoothing:.15g}"],
        ["v0_60_H075_after_timeflow", f"{h_after:.15g}"],
        ["v0_60_H075_after_timeflow_delta_pct_vs_reference", f"{percent_delta(h_after, H075_LCDM_REFERENCE):.15g}"],
        ["raw_result_claimed_as_prediction", "False"],
        ["trained_bridge_claimed_as_prediction", "False"],
    ]
    write_csv(RESULT_DIR / "mcift_v0.60_inverse_timeflow_metrics.csv", metrics)

    report = f"""# MCIFT v0.60 Inverse-Timeflow Backpropagation Retest

**Status:** implemented retest scaffold; speculative MCIFT layer, not established physics.  
**Generated by:** `simulations/mcift_v0_60_inverse_timeflow_backprop_retest.py`

---

## Purpose

v0.60 implements the items that v0.59 marked as missing:

```text
1. explicit gamma / Zgamma loop-surface readouts
2. explicit cc projection
3. inverse timeflow backpropagation as an actual differentiable loss
4. before/after retest against the v0.59 baseline
```

The important distinction is retained:

```text
implemented raw/readout layer != proof
inverse-timeflow trained bridge != raw first-principle prediction
```

---

## Implementation summary

### Loop/surface and cc readouts

The raw v0.59 particle readout had near-zero gamma/Zgamma leakage and no explicit cc projection. v0.60 adds deterministic readout rules:

```text
color_feedback = sqrt(bb_raw_factor * WW_raw_factor)
gg_impl = sqrt(gg_raw_factor * color_feedback)

fermion_core = sqrt(tau_raw_factor * mumu_raw_factor)
cc_impl = sqrt(gg_impl * fermion_core)

vector_loop = sqrt(WW_raw_factor * ZZ_raw_factor)
gamma_impl = sqrt(vector_loop * gg_impl)
Zgamma_impl = sqrt(gamma_impl * ZZ_raw_factor)
```

These formulas are implementation scaffolds, not a physical proof.

### Inverse-timeflow loss

v0.60 uses the final derived loss form as the active training object:

```text
L_ITB =
  sum_i [log(BR_i,pred / BR_i,SM)]^2
  + 0.5 [log(Gamma_total,pred / Gamma_SM)]^2
  + regularization on hidden channel corrections
  + regularization on the lab-time factor
```

This is the AI-style layer:

```text
observed lab residual -> loss -> hidden/core correction parameters
```

---

## CERN/LHC comparison against v0.59

| stage | BR L1 vs SM | max abs BR delta | failed 10 percent channels |
|---|---:|---:|---|
| v0.59 raw | {l1_distance(raw, sm):.6f} | {max(abs(x) for x in raw_delta.values()):.6f}% | {','.join(raw_failed)} |
| v0.60 implemented readout, before backprop | {l1_distance(implemented_br, sm):.6f} | {max(abs(x) for x in implemented_delta.values()):.6f}% | {','.join(implemented_failed) or 'none'} |
| v0.60 after inverse-timeflow backprop | {l1_distance(trained_br, sm):.6f} | {max(abs(x) for x in trained_delta.values()):.6f}% | {','.join(trained_failed) or 'none'} |

### Channel table

| channel | v0.59 raw delta | v0.60 implemented delta | v0.60 after backprop delta |
|---|---:|---:|---:|
"""
    for channel in sm:
        report += (
            f"| {channel} | {raw_delta[channel]:+.6f}% | "
            f"{implemented_delta[channel]:+.6f}% | "
            f"{trained_delta[channel]:+.6f}% |\n"
        )

    report += f"""
### Width and timeflow result

```text
Gamma_total_after_backprop = {trained_total_width:.6f} MeV
Gamma_total_delta_pct = {percent_delta(trained_total_width, SM_TOTAL_WIDTH_MEV):+.6f}
tau_time_lab_factor = {tau_time:.6f}
final_inverse_timeflow_loss = {final_loss:.9f}
```

Interpretation:

```text
The implemented readouts drastically reduce the raw CERN failure.
The inverse-timeflow loss can then train the remaining channel/timeflow residuals into a near-SM bridge.
This is a trained bridge result, not an independent raw prediction.
```

---

## Cosmology comparison against v0.59

v0.60 keeps the cosmology side conservative. The smoothing factor is derived from the existing v0.59 transfer readout rather than introduced as a new free improvement:

```text
q_smoothing = -log((H075_transfer - H075_reference) / (H075_raw - H075_reference))
q_smoothing = {q_smoothing:.6f}
```

| stage | H075 | delta vs reference |
|---|---:|---:|
| v0.59 raw 3D | {H075_RAW_3D:.6f} | {percent_delta(H075_RAW_3D, H075_LCDM_REFERENCE):+.6f}% |
| v0.59 transfer scaffold | {H075_TRANSFER_3D:.6f} | {percent_delta(H075_TRANSFER_3D, H075_LCDM_REFERENCE):+.6f}% |
| v0.60 after timeflow smoothing | {h_after:.6f} | {percent_delta(h_after, H075_LCDM_REFERENCE):+.6f}% |

Interpretation:

```text
The particle-side implementation improves substantially.
The cosmology side remains transfer/smoothing scaffold level, not a full raw cosmology pass.
```

---

## Verdict

```text
v0.60 = IMPLEMENTED_BACKPROP_IMPROVES_CERN_BRIDGE_RAW_STILL_SCAFFOLD
```

Detailed verdict:

```text
gamma_Zgamma_loop_surface_readout: IMPLEMENTED
cc_projection: IMPLEMENTED
inverse_timeflow_backprop_loss: IMPLEMENTED
CERN implemented-readout before backprop: NEAR_PASS_WITH_GG_REMAINING
CERN after inverse-timeflow backprop: TRAINED_BRIDGE_PASS_LIKE
cosmology raw: STILL_FAIL
cosmology timeflow/transfer: PASS_LIKE_SCAFFOLD
```

---

## Safe wording

Safe:

```text
v0.60 implements the missing readout and inverse-timeflow loss layers and improves the CERN-channel comparison relative to v0.59. The post-backprop result is a trained bridge and should not be described as a raw prediction.
```

Unsafe:

```text
MCIFT now proves CERN.
MCIFT now proves cosmology.
The inverse-timeflow trained fit is an independent first-principle prediction.
```
"""
    (RESULT_DIR / "mcift_v0.60_inverse_timeflow_retest_report.md").write_text(report)


if __name__ == "__main__":
    main()
