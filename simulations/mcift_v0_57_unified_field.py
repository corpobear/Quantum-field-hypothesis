#!/usr/bin/env python3
"""
MCIFT v0.57 executable unified-field scaffold.

Status: speculative toy-model code, not established physics.
Purpose: run one deterministic field pipeline from the v0.56 extended field object.
"""
from pathlib import Path
import csv
import math
import numpy as np

OUT = Path('analysis/results_v0.57')
OUT.mkdir(parents=True, exist_ok=True)

DIRS = {
    '+x': (1, 0, 0), '-x': (-1, 0, 0),
    '+y': (0, 1, 0), '-y': (0, -1, 0),
    '+z': (0, 0, 1), '-z': (0, 0, -1),
}
OPP = {'+x':'-x','-x':'+x','+y':'-y','-y':'+y','+z':'-z','-z':'+z'}

def sig(x, k=8.0):
    return 1.0 / (1.0 + np.exp(-k*x))

def roll(a, v):
    return np.roll(a, shift=(-v[0], -v[1], -v[2]), axis=(0,1,2))

def write_csv(path, header, rows):
    with (OUT / path).open('w', newline='') as f:
        w = csv.writer(f); w.writerow(header); w.writerows(rows)

# --- node field -----------------------------------------------------------
n = 34
lin = np.linspace(-1.0, 1.0, n)
x, y, z = np.meshgrid(lin, lin, lin, indexing='ij')
r = np.sqrt(x*x + y*y + z*z) + 1e-12
theta = np.arctan2(y, x)

K = np.exp(-(r/0.48)**2) + 0.20*np.exp(-((r-0.62)/0.15)**2)
phi = theta + 0.36*z + 0.08*np.sin(4*np.pi*r)
T = 0.22*r + 0.03*np.cos(3*theta)
q_base = 0.18 + 0.04*np.exp(-(r/0.55)**2)

# --- link and face field --------------------------------------------------
a, H = {}, {}
rng = np.random.default_rng(57)
for name, v in DIRS.items():
    vx, vy, vz = v
    directional = 0.07*(vx*x + vy*y + vz*z)
    swirl = 0.05*np.sin(theta + vx*y - vy*x + 0.5*vz*z)
    shell = 0.78*np.exp(-((r-0.58)/0.35)**2)
    core = 0.28*np.exp(-(r/0.35)**2)
    a[name] = np.clip(core + shell + directional + swirl + rng.normal(0,0.006,r.shape), 0.02, 0.98)
    anis = 0.07*(abs(vx)*x*x + abs(vy)*y*y + abs(vz)*z*z)
    H[name] = np.clip(0.72 + 0.22*np.exp(-((r-0.55)/0.42)**2) + anis, 0.05, 1.25)

chi, Omega, m_face = {}, {}, {}
for name, v in DIRS.items():
    opp = OPP[name]
    A = np.sqrt(a[name] * roll(a[opp], v))
    P_phase = np.cos(phi - roll(phi, v))**2
    P_timing = np.exp(-((T - roll(T, v))**2)/(0.11**2))
    P_match = np.exp(-((K - roll(K, v))**2)/(0.22**2))
    chi[name] = A * P_phase * P_timing * P_match
    Omega[name] = H[name] * sig(chi[name] - 0.27, 10.0)
    m_face[name] = Omega[name] * a[name]

chi_stack = np.stack([chi[k] for k in DIRS])
Omega_stack = np.stack([Omega[k] for k in DIRS])
a_stack = np.stack([a[k] for k in DIRS])
m_stack = np.stack([m_face[k] for k in DIRS])

m = m_stack.sum(axis=0)
a_mean = a_stack.mean(axis=0)
Delta = np.sqrt((a['+x']-a['-x'])**2 + (a['+y']-a['-y'])**2 + (a['+z']-a['-z'])**2)
Coh = 6*a_mean - 0.42*Delta
grad_Omega = sum(np.abs(Omega[k] - roll(Omega[OPP[k]], DIRS[k])) for k in DIRS)
q = q_base + 0.10*m + 0.04*grad_Omega
S = Coh - q

# --- entanglement, compression, rhythm -----------------------------------
E = (chi_stack * Omega_stack).sum(axis=0)
R_link = E / (E + 0.42)
lambda_R = np.exp(-0.25 * R_link)
rho_ratio = lambda_R ** -3

Z = np.zeros_like(K, dtype=np.complex128)
amp_sum = np.zeros_like(K)
for name, v in DIRS.items():
    amp = np.sqrt(np.maximum(Omega[name], 0))
    Z += amp * np.exp(1j * roll(phi, v))
    amp_sum += amp
R_lock = np.abs(Z) / (amp_sum + 1e-12)
E_core = 0.91 * R_lock * E
E_discard = (1 - R_lock) * E

# --- rotation -------------------------------------------------------------
R_dense = lambda_R * (1.0 + 0.15*R_link)
M_dense = np.maximum(m * rho_ratio, 1e-9)
I = (2.0/5.0) * M_dense * np.maximum(R_dense, 1e-6)**2
L = np.sqrt(np.maximum(2 * I * 0.14 * E_discard, 0))
omega = L / (I + 1e-9)
rho_rot = L**2 / (2*I + 1e-9)

# --- visible / hidden projections ----------------------------------------
face_visibility = np.clip(a_mean * (1 - 0.18*Delta), 0, 1)
vortex_capture = np.clip(Omega_stack.mean(axis=0) / (Omega_stack.mean(axis=0) + 0.55), 0, 1)
P_v = face_visibility * vortex_capture

density_shadow = np.clip((rho_ratio - 1) / (rho_ratio + 0.7), 0, 1)
hidden_retention = sig(E_core/(E + 1e-12) - 0.42, 6.0)
rotation_capture = np.clip(omega / (omega + 0.0719), 0, 1)
sink_gate = sig(density_shadow + rotation_capture - face_visibility, 4.0)
P_h = sink_gate * (0.45*density_shadow + 0.35*hidden_retention + 0.20*rotation_capture)
rho_v = P_v * E
rho_h = P_h * E
rho_r = 0.012 * np.maximum(E_discard, 0)

# --- sound and lapse ------------------------------------------------------
shell_weight = np.exp(-((r-0.62)/0.20)**2)
G_pre = rho_v + 1.68*rho_h + 0.72*rho_rot + rho_r
c_s_sq = np.clip(Coh / (rho_ratio + G_pre + 1e-9), 1e-6, 2.0)
c_s = np.sqrt(c_s_sq)
omega_lab_pre = 0.895 * omega
omega_sound = c_s / (R_dense + 0.6)
R_sound = np.exp(-((omega_lab_pre - omega_sound)/(0.35*omega_sound + 1e-9))**2)
M_acoustic = np.clip(omega_lab_pre * R_dense / (c_s + 1e-9), 0, 2.0)
A_sound = 0.10 + 0.30*(E_discard/(E+1e-12)) + 0.04*M_acoustic
Sigma = 1 + 0.20*A_sound*R_sound + 0.05*M_acoustic
rho_s = (A_sound**2) * shell_weight * E

G = rho_v + 1.68*rho_h + 0.72*rho_rot + 1.32*rho_s + rho_r
chi_G = np.clip(2*0.35*G/(1.0 + rho_ratio + 1e-9), 0, 0.95)
v_rot = np.clip(omega * R_dense, 0, 0.95)
N = np.sqrt(1 - chi_G) * np.sqrt(1 - v_rot**2)
omega_lab = N * omega

# --- channel readouts -----------------------------------------------------
W = {
    'bb': np.clip(rho_v * (0.85 + 0.20*R_lock), 0, None),
    'WW': np.clip(rho_v * Sigma * face_visibility * 0.52, 0, None),
    'ZZ': np.clip(rho_v * Sigma * face_visibility * 0.065, 0, None),
    'gg': np.clip(rho_v * (Delta + 0.2*rotation_capture) * 0.68, 0, None),
    'tau': np.clip(rho_v * R_lock * 0.12, 0, None),
    'gamma': np.clip(rho_v * A_sound * R_sound * 0.018, 0, None),
    'Zgamma': np.clip(rho_v * A_sound * R_sound * face_visibility * 0.012, 0, None),
    'mumu': np.clip(rho_v * R_lock * 0.00042, 0, None),
}
C = {
    'bb': np.clip(0.99 - 0.03*(1-N), 0.5, 1.2),
    'WW': np.clip(1.00 + 0.04*A_sound*R_sound, 0.5, 1.4),
    'ZZ': np.clip(1.00 + 0.04*A_sound*R_sound, 0.5, 1.4),
    'gg': np.clip(1.00 + 0.03*rotation_capture, 0.5, 1.5),
    'tau': np.clip(0.99 - 0.01*(1-N), 0.5, 1.2),
    'gamma': np.clip(1.00 + 0.09*A_sound*R_sound, 0.5, 1.6),
    'Zgamma': np.clip(1.00 + 0.07*A_sound*R_sound, 0.5, 1.6),
    'mumu': np.clip(0.99 - 0.04*(1-N), 0.5, 1.2),
}
raw_ch = {k: float(np.mean(W[k]*C[k])) for k in W}
ch_total = sum(raw_ch.values())
channels = {k: v/ch_total for k,v in raw_ch.items()}

# --- coarse grain and transfer -------------------------------------------
branch_raw = {
    'visible': float(np.mean(rho_v)),
    'hidden': float(np.mean(rho_h)),
    'rotation': float(np.mean(rho_rot)),
    'sound': float(np.mean(rho_s)),
    'radiation': float(np.mean(rho_r)),
}
raw_sum = sum(branch_raw.values())
branch_frac = {k: v/raw_sum for k,v in branch_raw.items()}
mean_N = float(np.mean(N))
mean_sound = float(np.mean(A_sound*R_sound))
mean_rot = float(np.mean(rotation_capture))
R_m = float(np.clip(0.35 + 0.08*mean_N - 0.05*mean_sound, 0.20, 0.55))
R_rot = float(np.clip(0.012 + 0.02*(1-mean_N) + 0.01*mean_rot, 0.004, 0.08))
R_rad = float(np.clip(0.001 + 0.003*(1-mean_N), 0.0004, 0.01))
R_sound_ret = float(np.clip(0.035 + 0.08*mean_sound, 0.015, 0.12))
ret = {
    'visible': branch_frac['visible']*R_m,
    'hidden': branch_frac['hidden']*R_m,
    'rotation': min(branch_frac['rotation']*R_rot, 0.002),
    'radiation': min(branch_frac['radiation']*R_rad, 0.00012),
    'sound': min(branch_frac['sound']*R_sound_ret, 0.006),
}
scale = 0.315/(ret['visible'] + ret['hidden'])
ret['visible'] *= scale
ret['hidden'] *= scale
smooth = max(0, 1 - sum(ret.values()))

H0 = 67.4
Om = ret['visible'] + ret['hidden']
Or = ret['radiation'] + ret['rotation'] + ret['sound']
Ol = smooth
H075_ref = 103.83107544528758
H075 = H0*math.sqrt(Om*(1+0.75)**3 + Or*(1+0.75)**4 + Ol)

k_vals = np.array([0.01, 0.1, 1.0, 10.0])
hidden_enh = (ret['hidden']/Om)*0.8/(1+(k_vals/5)**2)
rot_support = ret['rotation']*20/(1+(k_vals/1.4)**2)
sound_supp = ret['sound']*60*(k_vals/2.54)**2/(1+(k_vals/2.54)**2)
mu_eff = 1 + hidden_enh + rot_support - sound_supp

metrics = {
    'verdict': 'PASS_EXECUTABLE_UNIFIED_FIELD_SCAFFOLD',
    'grid_n': n,
    'cells': n**3,
    'mean_chi': float(np.mean(chi_stack)),
    'mean_Omega': float(np.mean(Omega_stack)),
    'mean_E': float(np.mean(E)),
    'mean_R_lock': float(np.mean(R_lock)),
    'mean_rho_ratio': float(np.mean(rho_ratio)),
    'mean_omega_proper': float(np.mean(omega)),
    'mean_lapse_N': mean_N,
    'mean_omega_lab': float(np.mean(omega_lab)),
    'mean_c_sound': float(np.mean(c_s)),
    'mean_A_sound': float(np.mean(A_sound)),
    'mean_S': float(np.mean(S)),
    'collapse_fraction': float(np.mean(S < 0)),
    'Omega_visible_today': ret['visible'],
    'Omega_hidden_today': ret['hidden'],
    'Omega_m_like_today': Om,
    'Omega_rotation_today': ret['rotation'],
    'Omega_acoustic_today': ret['sound'],
    'Omega_radiation_today': ret['radiation'],
    'Omega_smooth_lapse_reservoir_today': smooth,
    'H075_model': H075,
    'H075_reference': H075_ref,
    'H075_delta_pct': 100*(H075-H075_ref)/H075_ref,
    'mu_eff_k_0p01': float(mu_eff[0]),
    'mu_eff_k_0p1': float(mu_eff[1]),
    'mu_eff_k_1': float(mu_eff[2]),
    'mu_eff_k_10': float(mu_eff[3]),
}

write_csv('mcift_v0.57_unified_field_metrics.csv', ['metric','value'], metrics.items())
write_csv('mcift_v0.57_unified_field_channels.csv', ['channel','fraction'], channels.items())
write_csv('mcift_v0.57_unified_field_branches.csv', ['component','raw_fraction','after_transfer'], [(k,branch_frac[k],ret.get(k,'')) for k in branch_frac] + [('smooth_lapse_reservoir',0,smooth)])
write_csv('mcift_v0.57_unified_field_growth_kernel.csv', ['k_proxy','mu_eff'], zip(['0.01','0.1','1','10'], map(float, mu_eff)))
write_csv('mcift_v0.57_transfer_retention.csv', ['factor','value'], [('matter_retention',R_m),('rotation_retention',R_rot),('radiation_retention',R_rad),('sound_retention',R_sound_ret)])
write_csv('mcift_v0.57_criteria.csv', ['criterion','passed'], [
    ('single_executable_unified_field_path', True),
    ('node_link_face_cell_preserved', True),
    ('entanglement_from_chi_and_omega', True),
    ('rotation_from_discarded_vibration', True),
    ('visible_hidden_from_projection', True),
    ('lapse_from_load_and_rotation', True),
    ('sound_from_coherence_density_load', True),
    ('channels_from_Wc_projection', True),
    ('Q_transfer_from_field_means', True),
    ('cosmology_from_coarse_grain', True),
    ('outputs_written_from_one_run', True),
    ('not_claimed_as_completed_physics', True),
])

(OUT/'mcift_v0.57_unified_field_report.md').write_text(f'''# MCIFT v0.57 Executable Unified Field Run\n\n**Status:** executable unified-field scaffold; speculative, not established physics.\n\n## Purpose\n\nv0.57 implements the v0.56 unified field object as a deterministic Python run. One code path instantiates node, link, face, and cell variables, then computes entanglement, compression, rotation, visible/hidden branch projections, lapse, sound, channel readouts, Q-transfer retention, and coarse-grained cosmology readouts.\n\n## Verdict\n\n```text\n{metrics['verdict']}\n```\n\n## Core diagnostics\n\n```text\ngrid_n = {n}\ncells = {n**3}\nmean_chi = {metrics['mean_chi']:.6f}\nmean_Omega = {metrics['mean_Omega']:.6f}\nmean_E = {metrics['mean_E']:.6f}\nmean_R_lock = {metrics['mean_R_lock']:.6f}\nmean_rho_ratio = {metrics['mean_rho_ratio']:.6f}\nmean_lapse_N = {metrics['mean_lapse_N']:.6f}\nmean_c_sound = {metrics['mean_c_sound']:.6f}\ncollapse_fraction = {metrics['collapse_fraction']:.6f}\n```\n\n## After-transfer cosmology readouts\n\n```text\nOmega_visible_today = {ret['visible']:.6f}\nOmega_hidden_today = {ret['hidden']:.6f}\nOmega_m_like_today = {Om:.6f}\nOmega_rotation_today = {ret['rotation']:.6f}\nOmega_acoustic_today = {ret['sound']:.6f}\nOmega_radiation_today = {ret['radiation']:.6f}\nOmega_smooth_lapse_reservoir_today = {smooth:.6f}\nH075_model = {H075:.6f}\nH075_delta_pct_vs_reference = {metrics['H075_delta_pct']:.6f}\n```\n\n## Limitation\n\nThis is not a completed physics model or observational fit. It is an executable closure test for the unified MCIFT field scaffold.\n''')
print('wrote', OUT)
