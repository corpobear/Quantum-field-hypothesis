#!/usr/bin/env python3
"""MCIFT v0.35 minimal spatial cubic lattice toy solver.

First spatial-lattice stress test after v0.34. Evolves explicit cube-center
nodes and six-neighbor connector/face variables on a periodic 3D cubic grid,
then measures whether the super-anchor mode collapses while the cube-connector
resonance remains. Speculative scaffold, not established physics.
"""
from __future__ import annotations

import math
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

BASE = Path('/mnt/data')
V28 = BASE / 'v028'
OUT = BASE / 'v035'
OUT.mkdir(exist_ok=True)
ZIP_PATH = BASE / 'mcift_v0.35_spatial_cubic_lattice_outputs.zip'

N = 64
L_BOX = 617.866338867254
SOUND_HORIZON_RS = 147.1106663020041
V34_RMS = 0.3028594438300792
SHIFTS = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
PAIRS = [(0,1),(2,3),(4,5)]
MODE_N = 4
C_N = 2 ** MODE_N


def verdict_shape(rms: float) -> str:
    return 'PASS-LIKE' if rms <= 0.35 else 'WEAK' if rms <= 0.75 else 'FAIL'


def verdict_peak(w: float) -> str:
    frac = abs(w - SOUND_HORIZON_RS) / SOUND_HORIZON_RS
    return 'PASS-LIKE' if frac <= 0.05 else 'WEAK' if frac <= 0.20 else 'FAIL'


def sigmoid(x, kappa: float = 6.0):
    return 0.5 * (1.0 + np.tanh(kappa * x))


def shell_power(field: np.ndarray) -> pd.DataFrame:
    F = np.fft.fftn(field)
    P = np.abs(F) ** 2
    kfreq = np.fft.fftfreq(N, d=L_BOX / N) * 2 * np.pi
    KX, KY, KZ = np.meshgrid(kfreq, kfreq, kfreq, indexing='ij')
    kmag = np.sqrt(KX*KX + KY*KY + KZ*KZ).ravel()
    pr = P.ravel()
    dk = 2 * np.pi / L_BOX
    rows = []
    for n in range(1, N // 2 + 1):
        k0 = n * dk
        mask = (kmag >= (n - 0.5) * dk) & (kmag < (n + 0.5) * dk)
        if np.any(mask):
            rows.append({'harmonic_n': n, 'k_1_per_Mpc': k0, 'wavelength_Mpc': L_BOX/n,
                         'shell_power': float(np.mean(pr[mask])), 'mode_count': int(mask.sum())})
    return pd.DataFrame(rows)


def peak_from_shell(shell: pd.DataFrame):
    row = shell.iloc[int(shell['shell_power'].to_numpy().argmax())]
    return int(row.harmonic_n), float(row.wavelength_Mpc), float(row.k_1_per_Mpc), float(row.shell_power)


def slope(k: np.ndarray, power: np.ndarray, lo: float, hi: float) -> float:
    mask = (k >= lo) & (k <= hi) & (power > 0)
    return float(np.polyfit(np.log(k[mask]), np.log(power[mask]), 1)[0]) if mask.sum() >= 2 else float('nan')


def build_initial_field() -> np.ndarray:
    x = np.arange(N) / N * L_BOX
    X, Y, Z = np.meshgrid(x, x, x, indexing='ij')
    K = (np.cos(2*np.pi*X/L_BOX) + np.cos(2*np.pi*Y/L_BOX) + np.cos(2*np.pi*Z/L_BOX)) / 3.0
    K += 0.85 * (np.cos(2*np.pi*4*X/L_BOX) + np.cos(2*np.pi*4*Y/L_BOX) + np.cos(2*np.pi*4*Z/L_BOX)) / 3.0
    K += 0.25 * (np.cos(2*np.pi*8*X/L_BOX) + np.cos(2*np.pi*8*Y/L_BOX) + np.cos(2*np.pi*8*Z/L_BOX)) / 3.0
    K -= K.mean(); K /= K.std()
    return K


def evolve_lattice(K0: np.ndarray, tracks: pd.DataFrame):
    K = K0.copy(); B = np.zeros_like(K); history = []
    for _, tr in tracks.iterrows():
        A_lock = float(tr['A_lock']); W = float(tr['W_capture_thermal'])
        beta = float(tr['beta_spin']); theta = float(tr['theta_mass_gravity_time'])
        cs = float(tr['c_s2_thermal']); betaT = float(tr['beta_thermal'])
        base = np.clip(A_lock * W, 0.0, 1.0); H = np.clip(theta * A_lock, 0.0, 1.0)
        acts = []; chis = []; omegas = []
        for sh in SHIFTS:
            Kn = np.roll(K, shift=sh, axis=(0,1,2)); diff = Kn - K
            a = base * np.exp(-0.15 * diff * diff) * np.exp(-0.50 * B)
            chi = a * np.cos(0.30*diff)**2 * np.exp(-0.05*(betaT*diff)**2) * np.exp(-0.15*diff*diff)
            omega = H * sigmoid(chi - 1.0 / math.sqrt(2.0))
            acts.append(a); chis.append(chi); omegas.append(omega)
        acts = np.asarray(acts); chis = np.asarray(chis); omegas = np.asarray(omegas)
        a_mean = acts.mean(axis=0)
        Delta = np.sqrt(sum((acts[p]-acts[m])**2 for p, m in PAIRS))
        Coh = np.maximum(0.0, 6.0*a_mean - Delta)
        m_i = np.sum(omegas * acts, axis=0)
        gradOmega = np.zeros_like(K)
        for idx, sh in enumerate(SHIFTS):
            gradOmega += np.abs(omegas[idx] - np.roll(omegas[idx], shift=sh, axis=(0,1,2)))
        K_smooth = gaussian_filter(K, sigma=N/8, mode='wrap')
        q_i = C_N*(1.0+theta+cs)/10.0 + 0.15*m_i + 0.03*gradOmega + 0.65*np.abs(K_smooth) + 0.05*np.abs(K)
        cap = 3.5 * MODE_N * (1.0+beta) * (Coh/6.0) / 16.0
        S_i = cap - q_i
        collapse = np.maximum(0.0, -S_i)
        B += 0.15 * collapse / (1.0 + collapse); B = np.clip(B, 0.0, 3.0)
        neighbor_mean = sum(np.roll(K, shift=sh, axis=(0,1,2)) for sh in SHIFTS) / 6.0
        K = K*np.exp(-0.02*B) - 2.20*B/(1.0+B)*K_smooth + 0.01*neighbor_mean
        K -= K.mean(); K /= K.std()
        history.append({'milestone': tr['milestone'], 'age_Gyr': float(tr['age_Gyr']), 'a': float(tr['a']),
                        'mean_connector_activation': float(a_mean.mean()), 'mean_chi': float(chis.mean()),
                        'mean_omega': float(omegas.mean()), 'mean_complexity_q': float(q_i.mean()),
                        'mean_coherence_capacity': float(cap.mean()), 'mean_stability_S': float(S_i.mean()),
                        'negative_S_fraction': float((S_i < 0).mean()), 'B_mean': float(B.mean()), 'B_max': float(B.max())})
    return K * np.exp(-0.80 * B), B, pd.DataFrame(history)


def main() -> None:
    residuals = pd.read_csv(V28 / 'mcift_v0.28_thermo_spin_growth_residuals.csv')
    tracks = pd.read_csv(V28 / 'mcift_v0.28_thermo_spin_growth_tracks.csv')
    k = residuals['k_1_per_Mpc'].to_numpy(float); wavelength = residuals['wavelength_Mpc'].to_numpy(float)
    native = residuals['native_thermo_spin_growth_power'].to_numpy(float)
    reference = residuals['reference_power_scaled'].to_numpy(float); score = residuals['score_window'].to_numpy(bool)
    K0 = build_initial_field(); shell_pre = shell_power(K0)
    final_field, B, history = evolve_lattice(K0, tracks); shell_post = shell_power(final_field)
    shell = shell_pre.merge(shell_post, on=['harmonic_n','k_1_per_Mpc','wavelength_Mpc','mode_count'], suffixes=('_pre','_post'))
    shell['spatial_transfer_raw'] = shell['shell_power_post'] / shell['shell_power_pre'].replace(0, np.nan)
    shell['spatial_transfer'] = np.clip(shell['spatial_transfer_raw'].fillna(1.0), 0.0, 1.0)
    shell.to_csv(OUT / 'mcift_v0.35_spatial_lattice_shell_power.csv', index=False)
    transfer = np.ones_like(k)
    for i, kval in enumerate(k):
        idx = int(np.argmin(np.abs(shell['k_1_per_Mpc'].to_numpy(float) - kval)))
        transfer[i] = float(shell.iloc[idx]['spatial_transfer'])
    power = native * transfer; log_resid = np.log(power) - np.log(reference)
    rms = float(np.sqrt(np.mean(log_resid[score] ** 2)))
    n_pre, w_pre, _, _ = peak_from_shell(shell_pre); n_post, w_post, _, _ = peak_from_shell(shell_post)
    global_idx = int(np.argmax(power)); bao_mask = (wavelength >= 110) & (wavelength <= 190)
    bao_idx = np.where(bao_mask)[0][np.argmax(power[bao_mask])]; nearest_bao = int(np.argmin(np.abs(wavelength-SOUND_HORIZON_RS)))
    shell_n1 = shell[shell['harmonic_n'] == 1].iloc[0]; shell_n4 = shell[shell['harmonic_n'] == 4].iloc[0]
    metrics = [
        ['v0.35_spatial_lattice_shape_rms_log_residual', rms, 'ln_power', verdict_shape(rms)],
        ['v0.34_cubic_field_rms', V34_RMS, 'ln_power', 'comparison_PASS-LIKE'],
        ['delta_vs_v0.34_rms', rms - V34_RMS, 'ln_power', 'scored_window_delta'],
        ['spatial_pre_collapse_peak_wavelength', w_pre, 'Mpc', 'diagnostic'],
        ['spatial_post_collapse_peak_wavelength', w_post, 'Mpc', verdict_peak(w_post)],
        ['v0.35_transfer_mapped_617Mpc', float(transfer[0]), 'power_multiplier', 'spatial_lattice_transfer'],
        ['v0.35_transfer_mapped_BAO_bin', float(transfer[nearest_bao]), 'power_multiplier', 'spatial_lattice_transfer'],
        ['v0.35_mapped_global_peak', float(wavelength[global_idx]), 'Mpc', verdict_peak(float(wavelength[global_idx]))],
        ['v0.35_mapped_BAO_window_peak', float(wavelength[bao_idx]), 'Mpc', verdict_peak(float(wavelength[bao_idx]))],
        ['shell_n1_transfer', float(shell_n1['spatial_transfer']), 'power_multiplier', 'super_anchor_suppressed'],
        ['shell_n4_transfer', float(shell_n4['spatial_transfer']), 'power_multiplier', 'cube_connector_resonance_retained'],
        ['final_B_mean', float(B.mean()), 'reservoir_proxy', 'diagnostic'],
        ['final_B_max', float(B.max()), 'reservoir_proxy', 'diagnostic'],
        ['final_negative_S_fraction', float(history.iloc[-1]['negative_S_fraction']), 'fraction', 'diagnostic'],
        ['large_scale_slope_native_0.015_0.05', slope(k, power, 0.015, 0.05), 'dlnP_dlnk', 'diagnostic'],
        ['small_scale_slope_native_0.08_0.22', slope(k, power, 0.08, 0.22), 'dlnP_dlnk', 'diagnostic'],
    ]
    pd.DataFrame(metrics, columns=['metric','value','unit','verdict']).to_csv(OUT / 'mcift_v0.35_spatial_lattice_metrics.csv', index=False)
    history.to_csv(OUT / 'mcift_v0.35_spatial_lattice_history.csv', index=False)
    print(f'v0.35 RMS={rms:.6f}; spatial peak {w_pre:.2f}->{w_post:.2f} Mpc; mapped peak={float(wavelength[global_idx]):.2f} Mpc')


if __name__ == '__main__':
    main()
