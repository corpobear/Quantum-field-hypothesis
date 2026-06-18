#!/usr/bin/env python3
"""
MCIFT v0.16 Big-Bang / cosmology comparison scaffold

This script compares toy observables from the 5-billion-year MCIFT 3D Fibonacci
field against a small set of published cosmology targets. It is intentionally
limited: it does not solve Einstein-Boltzmann equations, does not perform CMB
radiation transfer, and does not model Big Bang nucleosynthesis. It converts the
MCIFT toy field into measurable proxies that can be versioned and challenged.

Outputs:
- analysis/results_v0.16/mcift_big_bang_summary.csv
- analysis/results_v0.16/mcift_power_spectrum_5by.csv
- analysis/results_v0.16/mcift_radial_profile_5by.csv
- analysis/results_v0.16/mcift_power_spectrum_5by.png
- analysis/results_v0.16/mcift_power_spectrum_5by.svg
- analysis/results_v0.16/mcift_radial_profile_5by.png
- analysis/results_v0.16/mcift_radial_profile_5by.svg
- analysis/results_v0.16/mcift_big_bang_comparison_report.md
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


PHI = (1 + np.sqrt(5.0)) / 2.0
BASE_TOY_YEARS = 1_000_000
TOTAL_YEARS = 5_000_000_000
TIME_STRETCH = TOTAL_YEARS / BASE_TOY_YEARS
N_SIDE = 64
FIELD_LIMIT_TOY = 5.0
BOX_SIZE_MPC = 1_000.0  # arbitrary calibration for first-pass BAO-scale diagnostics
RESULTS_DIR = Path(__file__).resolve().parent / "results_v0.16"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)

# Planck 2018 base-LambdaCDM combined values from arXiv:1807.06209 abstract.
PLANCK = {
    "omega_b_h2": 0.0224,
    "omega_c_h2": 0.120,
    "baryon_to_cdm": 0.0224 / 0.120,
    "H0_km_s_Mpc": 67.4,
    "Omega_m": 0.315,
    "sigma8": 0.811,
    "ns": 0.965,
    "theta_star_100": 1.0411,
}

# DESI 2024 BAO uses the sound horizon rd as the standard-ruler reference.
DESI = {
    "rd_reference_Mpc": 147.09,
    "Omega_m_DESI_BAO_only": 0.295,
    "Omega_m_DESI_CMB_combo": 0.307,
}

MILESTONES = [
    (1_000_000_000, "1B"),
    (2_000_000_000, "2B"),
    (3_000_000_000, "3B"),
    (4_000_000_000, "4B"),
    (5_000_000_000, "5B"),
]


def scaled_t(actual_years: float) -> float:
    return actual_years / TIME_STRETCH


def make_grid(n: int = N_SIDE):
    axis = np.linspace(-FIELD_LIMIT_TOY, FIELD_LIMIT_TOY, n)
    return np.meshgrid(axis, axis, axis, indexing="ij"), axis


def evolve_3d_field(actual_years: float, X: np.ndarray, Y: np.ndarray, Z: np.ndarray):
    """Same 5B-year stretched toy dynamics as simulations/mcift_3d_fibonacci_5by.py."""
    t = scaled_t(actual_years)
    r = np.sqrt(X**2 + Y**2 + Z**2)

    fib_mod = 1 + 0.15 * np.sin(2 * np.pi * np.log(r + 1e-6) / np.log(PHI))
    coherence = (1 - np.exp(-t / 40000)) * np.exp(-r**2 / (4 + 0.002 * t)) * fib_mod
    anchor = np.exp(-r**2 / (1.5 + 0.001 * t))

    if t > 40000:
        visible = 0.7 * (1 - np.exp(-(t - 40000) / 90000)) * np.exp(
            -((X) ** 2 + (Y) ** 2 + (Z - 2) ** 2) / 3
        )
    else:
        visible = np.zeros_like(X)

    if t > 180000:
        dark_factor = 1 - np.exp(-(t - 180000) / 150000)
        dark = dark_factor * (
            np.exp(-((X - 2) ** 2 + (Y) ** 2 + (Z) ** 2) / 4)
            + np.exp(-((X + 2) ** 2 + (Y) ** 2 + (Z) ** 2) / 4)
            + np.exp(-((X) ** 2 + (Y - 2) ** 2 + (Z) ** 2) / 4)
            + np.exp(-((X) ** 2 + (Y + 2) ** 2 + (Z) ** 2) / 4)
        )
    else:
        dark = np.zeros_like(X)

    exchange = 0.35 * np.tanh(t / 200000) * np.exp(-r**2 / 5)

    signed_field = coherence + 0.6 * visible - 0.45 * dark + exchange + 0.3 * anchor
    positive_density_proxy = coherence + 0.6 * visible + 0.45 * dark + exchange + 0.3 * anchor

    return {
        "signed_field": signed_field,
        "positive_density_proxy": positive_density_proxy,
        "visible": visible,
        "dark": dark,
        "coherence": coherence,
        "anchor": anchor,
        "exchange": exchange,
    }


def verdict_ratio(value: float, target: float) -> str:
    if not np.isfinite(value):
        return "UNDEFINED"
    frac = abs(value - target) / target
    if frac < 0.10:
        return "PASS-LIKE"
    if frac < 0.50:
        return "WEAK"
    return "FAIL"


def visible_dark_metrics(fields: dict[str, np.ndarray]) -> dict[str, float | str]:
    visible_sum = float(np.sum(fields["visible"]))
    dark_sum = float(np.sum(fields["dark"]))
    weighted_visible_sum = float(np.sum(0.6 * fields["visible"]))
    weighted_dark_sum = float(np.sum(0.45 * fields["dark"]))
    raw_ratio = visible_sum / dark_sum if dark_sum > 0 else math.nan
    weighted_ratio = weighted_visible_sum / weighted_dark_sum if weighted_dark_sum > 0 else math.nan
    target = PLANCK["baryon_to_cdm"]
    return {
        "visible_sum": visible_sum,
        "dark_sum": dark_sum,
        "visible_dark_raw_ratio": raw_ratio,
        "visible_dark_weighted_ratio": weighted_ratio,
        "target_planck_baryon_cdm_ratio": target,
        "weighted_ratio_error_fraction": abs(weighted_ratio - target) / target if np.isfinite(weighted_ratio) else math.nan,
        "weighted_ratio_verdict": verdict_ratio(weighted_ratio, target),
    }


def isotropic_power_spectrum(density: np.ndarray, box_size_mpc: float = BOX_SIZE_MPC, n_bins: int = 44):
    delta = density / np.mean(density) - 1.0
    fft = np.fft.fftn(delta)
    power = np.abs(fft) ** 2 / delta.size

    n = density.shape[0]
    spacing = box_size_mpc / n
    freq = np.fft.fftfreq(n, d=spacing)
    k1 = 2 * np.pi * freq
    kx, ky, kz = np.meshgrid(k1, k1, k1, indexing="ij")
    kvals = np.sqrt(kx**2 + ky**2 + kz**2).ravel()
    pvals = power.ravel()

    keep = kvals > 0
    kvals = kvals[keep]
    pvals = pvals[keep]

    bins = np.linspace(kvals.min(), kvals.max(), n_bins + 1)
    rows = []
    for i in range(n_bins):
        mask = (kvals >= bins[i]) & (kvals < bins[i + 1])
        if not np.any(mask):
            continue
        k_center = float(0.5 * (bins[i] + bins[i + 1]))
        rows.append(
            {
                "k_1_per_Mpc": k_center,
                "power": float(np.mean(pvals[mask])),
                "modes": int(np.sum(mask)),
                "wavelength_Mpc": float(2 * np.pi / k_center),
            }
        )
    return rows


def radial_profile(density: np.ndarray, X: np.ndarray, Y: np.ndarray, Z: np.ndarray, n_bins: int = 80):
    r_toy = np.sqrt(X**2 + Y**2 + Z**2)
    mpc_per_toy = BOX_SIZE_MPC / (2 * FIELD_LIMIT_TOY)
    r_mpc = r_toy * mpc_per_toy
    bins = np.linspace(0, float(r_mpc.max()), n_bins + 1)
    rows = []
    for i in range(n_bins):
        mask = (r_mpc >= bins[i]) & (r_mpc < bins[i + 1])
        if not np.any(mask):
            continue
        rows.append(
            {
                "r_Mpc": float(0.5 * (bins[i] + bins[i + 1])),
                "mean_density_proxy": float(np.mean(density[mask])),
                "cell_count": int(np.sum(mask)),
            }
        )
    return rows


def local_peak_radii(profile_rows: list[dict[str, float]], top_n: int = 5):
    # Ignore central monotonic core; look for outer radial bumps.
    rs = np.array([row["r_Mpc"] for row in profile_rows])
    vals = np.array([row["mean_density_proxy"] for row in profile_rows])
    vals_norm = vals / np.max(vals)
    peaks = []
    for i in range(2, len(vals_norm) - 2):
        if rs[i] < 80:
            continue
        if vals_norm[i] > vals_norm[i - 1] and vals_norm[i] > vals_norm[i + 1]:
            peaks.append((float(vals_norm[i]), float(rs[i])))
    peaks.sort(reverse=True)
    return [r for _, r in peaks[:top_n]]


def write_csv(path: Path, rows: list[dict]):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def plot_power(rows: list[dict], path: Path):
    k = [row["k_1_per_Mpc"] for row in rows]
    p = [row["power"] for row in rows]
    plt.figure(figsize=(8, 5))
    plt.loglog(k, p, marker="o", linewidth=1)
    plt.xlabel("k [1/Mpc] under arbitrary 1000 Mpc box calibration")
    plt.ylabel("Toy P(k)")
    plt.title("MCIFT v0.16 positive-density proxy power spectrum at 5B years")
    plt.grid(True, which="both", alpha=0.25)
    plt.tight_layout()
    plt.savefig(path, dpi=140)
    plt.savefig(path.with_suffix(".svg"))
    plt.close()


def plot_radial(rows: list[dict], path: Path):
    r = [row["r_Mpc"] for row in rows]
    v = [row["mean_density_proxy"] for row in rows]
    plt.figure(figsize=(8, 5))
    plt.plot(r, v, marker="o", linewidth=1)
    plt.axvline(DESI["rd_reference_Mpc"], linestyle="--", linewidth=1, label="BAO rd reference 147.09 Mpc")
    plt.xlabel("Radius [Mpc] under arbitrary 1000 Mpc box calibration")
    plt.ylabel("Mean positive density proxy")
    plt.title("MCIFT v0.16 radial density profile at 5B years")
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.savefig(path, dpi=140)
    plt.savefig(path.with_suffix(".svg"))
    plt.close()


def report_markdown(summary_rows, power_rows, radial_rows, peak_radii):
    final = summary_rows[-1]
    peak_wavelength = max(power_rows, key=lambda row: row["power"])["wavelength_Mpc"]
    bao = DESI["rd_reference_Mpc"]
    peak_bao_error = abs(peak_wavelength - bao) / bao
    if peak_bao_error < 0.20:
        bao_verdict = "WEAK/PASS-LIKE SCALE ONLY"
    elif peak_bao_error < 0.75:
        bao_verdict = "WEAK"
    else:
        bao_verdict = "FAIL"

    rows_md = "\n".join(
        f"| {row['milestone']} | {row['actual_years']:,} | {row['visible_dark_weighted_ratio']:.6f} | "
        f"{row['target_planck_baryon_cdm_ratio']:.6f} | {row['weighted_ratio_error_fraction']:.2f} | {row['weighted_ratio_verdict']} |"
        for row in summary_rows
    )

    peaks_text = ", ".join(f"{r:.1f} Mpc" for r in peak_radii) if peak_radii else "none found"

    return f"""# MCIFT v0.16 Big-Bang / Cosmology Comparison Report

**Status:** first-pass toy-observable comparison, not a physical validation.  
**Generated by:** `analysis/mcift_big_bang_comparison_v0.16.py`  
**Simulation basis:** `simulations/mcift_3d_fibonacci_5by.py` style stretched 5-billion-year field.

## External comparison anchors

- Planck 2018 base-LambdaCDM combined CMB result: baryon density `Omega_b h^2 = 0.0224 +/- 0.0001`, cold-dark-matter density `Omega_c h^2 = 0.120 +/- 0.001`, scalar index `n_s = 0.965 +/- 0.004`, `H0 = 67.4 +/- 0.5 km/s/Mpc`, `Omega_m = 0.315 +/- 0.007`, and `sigma8 = 0.811 +/- 0.006`.
- DESI 2024 BAO context: DESI DR1 BAO spans tracers across `0.1 < z < 4.2`, and the Ly-alpha BAO paper expresses distances using a sound-horizon reference `r_d = 147.09 Mpc`.

## What this script actually compares

The MCIFT field is converted into three toy observables:

1. `visible_dark_weighted_ratio = integral(0.6 * visible) / integral(0.45 * dark)`.
2. A 3D isotropic power spectrum `P(k)` of a positive density proxy.
3. A radial density profile, calibrated only for plotting by mapping the toy box `[-5,5]^3` to `1000 Mpc` across.

The physical calibration is arbitrary. Therefore the BAO comparison below is a **scale sanity check only**, not a cosmological fit.

## Visible/dark ratio result

Planck target used here:

```text
Omega_b h^2 / Omega_c h^2 = {PLANCK['omega_b_h2']} / {PLANCK['omega_c_h2']} = {PLANCK['baryon_to_cdm']:.6f}
```

| Milestone | Actual years | MCIFT weighted visible/dark | Planck baryon/CDM target | Fractional error | Verdict |
|---:|---:|---:|---:|---:|---|
{rows_md}

**Interpretation:** the toy geometry is strongly dark-weighted by late time and falls below the Planck baryon/CDM ratio at 5B years. The 5B milestone gives `{final['visible_dark_weighted_ratio']:.6f}`, about `{final['weighted_ratio_error_fraction']:.2f}` fractional error from the Planck target, so the current verdict is **{final['weighted_ratio_verdict']}**.

## Power-spectrum result

File: `analysis/results_v0.16/mcift_power_spectrum_5by.csv`  
Plot: `analysis/results_v0.16/mcift_power_spectrum_5by.svg`

The strongest toy power-spectrum bin corresponds to an effective wavelength of approximately `{peak_wavelength:.2f} Mpc` under the arbitrary 1000 Mpc box calibration. Compared to the DESI/BAO reference scale `{bao:.2f} Mpc`, this is a fractional scale offset of `{peak_bao_error:.2f}`. Verdict: **{bao_verdict}**.

This is not a CMB TT spectrum and not a matter transfer-function fit. It is a diagnostic that lets future MCIFT versions track whether geometry changes push structure toward or away from observed large-scale-clustering scales.

## Radial shell / Fibonacci ripple result

File: `analysis/results_v0.16/mcift_radial_profile_5by.csv`  
Plot: `analysis/results_v0.16/mcift_radial_profile_5by.svg`

Detected outer radial bumps: `{peaks_text}`.

The current radial profile is dominated by the central coherent pocket and sink geometry. The Fibonacci logarithmic modulation is present in the formula, but this run does not yet isolate a clean BAO-like shell sequence.

## Verdict

```text
visible/dark density-ratio comparison: {final['weighted_ratio_verdict']}
power-spectrum BAO-scale sanity check: {bao_verdict}
CMB acoustic peaks: UNDEFINED - no radiation-transfer model yet
BBN light-element abundances: UNDEFINED - no nuclear reaction network yet
expansion history H(z): UNDEFINED - no Friedmann/metric sector yet
```

## Next required physics to make this a real cosmology test

1. Define a physical mapping from MCIFT coordinates to comoving Mpc and redshift.
2. Add an expansion history `a(t)` or `H(z)` rather than stretching toy time.
3. Produce a CMB-like angular projection `C_l` and compare to Planck TT/TE/EE data.
4. Add a baryon-photon / radiation sector before attempting Big Bang nucleosynthesis.
5. Fit parameters against data instead of visually selecting scales.

## References

- Planck Collaboration, *Planck 2018 results. VI. Cosmological parameters*, arXiv:1807.06209.
- DESI Collaboration, *DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations*, arXiv:2404.03002.
- DESI Collaboration, *DESI 2024 IV: Baryon Acoustic Oscillations from the Lyman-alpha Forest*, arXiv:2404.03001.
"""


def main():
    (X, Y, Z), axis = make_grid()

    summary_rows = []
    final_fields = None
    for actual_years, label in MILESTONES:
        fields = evolve_3d_field(actual_years, X, Y, Z)
        metrics = visible_dark_metrics(fields)
        row = {
            "milestone": label,
            "actual_years": actual_years,
            "scaled_toy_years": scaled_t(actual_years),
            **metrics,
        }
        summary_rows.append(row)
        final_fields = fields

    density = final_fields["positive_density_proxy"]
    power_rows = isotropic_power_spectrum(density)
    radial_rows = radial_profile(density, X, Y, Z)
    peak_radii = local_peak_radii(radial_rows)

    write_csv(RESULTS_DIR / "mcift_big_bang_summary.csv", summary_rows)
    write_csv(RESULTS_DIR / "mcift_power_spectrum_5by.csv", power_rows)
    write_csv(RESULTS_DIR / "mcift_radial_profile_5by.csv", radial_rows)
    plot_power(power_rows, RESULTS_DIR / "mcift_power_spectrum_5by.png")
    plot_radial(radial_rows, RESULTS_DIR / "mcift_radial_profile_5by.png")

    report = report_markdown(summary_rows, power_rows, radial_rows, peak_radii)
    (RESULTS_DIR / "mcift_big_bang_comparison_report.md").write_text(report, encoding="utf-8")

    print("MCIFT v0.16 Big-Bang comparison complete")
    print(f"Report: {RESULTS_DIR / 'mcift_big_bang_comparison_report.md'}")
    print(f"5B visible/dark weighted ratio: {summary_rows[-1]['visible_dark_weighted_ratio']:.6f}")
    print(f"Planck baryon/CDM target: {PLANCK['baryon_to_cdm']:.6f}")
    print(f"Verdict: {summary_rows[-1]['weighted_ratio_verdict']}")


if __name__ == "__main__":
    main()
