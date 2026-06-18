#!/usr/bin/env python3
"""MCIFT v0.21 full matter-power-shape scoring rerun.

Builds on v0.20 derived mechanics and adds the next missing ingredient:
a full P(k) shape comparison instead of peak-only scoring.

The reference curve is an analytic Lambda-CDM-like BBKS/Sugiyama transfer
shape with a small sound-horizon BAO wiggle. This is still not a replacement
for CLASS/CAMB or survey likelihoods; it is a stricter toy gate before those.
"""
from __future__ import annotations
import csv, math, runpy
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
v20 = runpy.run_path(str(BASE / 'mcift_big_bang_derived_scalelock_v0.20.py'))
OUT = BASE / 'results_v0.21'
OUT.mkdir(parents=True, exist_ok=True)
OMEGA_M = v20['OMEGA_M']; OMEGA_B = v20['OMEGA_B']; h = v20['h']
N_S = v20['N_S_PLANCK']; K_PIVOT = v20['K_PIVOT']; BAO_WINDOW = v20['BAO_WINDOW_MPC']
K_MIN_SCORE = 0.015; K_MAX_SCORE = 0.22

def gamma_sugiyama():
    return OMEGA_M * h * math.exp(-OMEGA_B * (1.0 + math.sqrt(2.0*h) / OMEGA_M))
def transfer_bbks(k):
    k_h = k / h
    q = np.maximum(k_h / gamma_sugiyama(), 1e-12)
    L = np.log(1.0 + 2.34*q) / (2.34*q)
    C = (1.0 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)
    return L*C
def lcdm_like_reference_pk(k, r_s):
    T = transfer_bbks(k)
    smooth = (np.maximum(k,1e-12)/K_PIVOT)**N_S * T**2
    wiggle = 1.0 + 0.12*np.sin(k*r_s)*np.exp(-(k/0.18)**1.4)
    return np.maximum(smooth*wiggle, 1e-300)
def shape_verdict(rms_log):
    if rms_log < 0.35: return 'PASS-LIKE'
    if rms_log < 1.0: return 'WEAK'
    return 'FAIL'
def write_csv(path, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
def slope(rows, lo, hi):
    x=[]; y=[]
    for r in rows:
        k=float(r['k_1_per_Mpc']); p=float(r['power'])
        if lo <= k <= hi and p > 0: x.append(math.log(k)); y.append(math.log(p))
    return float(np.polyfit(x,y,1)[0]) if len(x) > 1 else math.nan

def main():
    X,Y,Z,R = v20['make_grids'](); r_s = v20['sound_horizon_Mpc'](); final_ch = None
    for years,label in v20['MILESTONES']:
        if label == '5B':
            a = v20['scale_factor_at_age_Gyr'](years/1e9)
            final_ch = v20['apply_frw_channel_dilution'](v20['evolve_base_channels'](years,X,Y,Z),a)
    R_A = v20['anchor_rms_radius_Mpc'](final_ch,R)
    k_cut = v20['anchor_derived_k_cut'](final_ch,R)
    A_lock = v20['derived_lock_amplitude'](final_ch)
    locked = v20['density_proxy'](final_ch,R,r_s,locked=True)
    final_density = v20['apply_anchor_damping'](locked,k_cut)
    mcift_rows = v20['isotropic_power_spectrum'](final_density,k_cut=k_cut,n_bins=44)
    k_arr = np.array([r['k_1_per_Mpc'] for r in mcift_rows], dtype=float)
    p_arr = np.array([r['power'] for r in mcift_rows], dtype=float)
    pref = lcdm_like_reference_pk(k_arr,r_s)
    mask = (k_arr>=K_MIN_SCORE)&(k_arr<=K_MAX_SCORE)&(p_arr>0)&(pref>0)
    log_m = np.log(p_arr[mask]); log_r = np.log(pref[mask])
    amp = float(np.mean(log_m-log_r))
    resid = log_m - (log_r+amp)
    rms = float(np.sqrt(np.mean(resid**2))); mean_abs = float(np.mean(np.abs(resid))); max_abs = float(np.max(np.abs(resid)))
    verdict = shape_verdict(rms)
    rows=[]
    for i,r in enumerate(mcift_rows):
        ref = float(pref[i]*math.exp(amp)); res = math.log(max(r['power'],1e-300))-math.log(max(ref,1e-300))
        rows.append({'k_1_per_Mpc':r['k_1_per_Mpc'],'wavelength_Mpc':r['wavelength_Mpc'],'mcift_power':r['power'],'reference_power_scaled':ref,'log_residual':res,'score_window':bool(K_MIN_SCORE<=r['k_1_per_Mpc']<=K_MAX_SCORE)})
    peak_global = v20['pick_peak'](mcift_rows); peak_bao = v20['pick_peak'](mcift_rows,BAO_WINDOW)
    score_k = k_arr[mask]; ref_peak_wav = float(2*np.pi/score_k[int(np.argmax(pref[mask]))])
    s_mcift_large = slope(mcift_rows,0.015,0.05)
    s_ref_large = float(np.polyfit(np.log(k_arr[mask & (k_arr<=0.05)]), np.log((pref*np.exp(amp))[mask & (k_arr<=0.05)]),1)[0])
    s_mcift_small = slope(mcift_rows,0.08,0.22)
    s_ref_small = float(np.polyfit(np.log(k_arr[mask & (k_arr>=0.08)]), np.log((pref*np.exp(amp))[mask & (k_arr>=0.08)]),1)[0])
    metrics=[
        {'metric':'shape_rms_log_residual','value':rms,'unit':'ln_power','verdict':verdict},
        {'metric':'shape_mean_abs_log_residual','value':mean_abs,'unit':'ln_power','verdict':'diagnostic'},
        {'metric':'shape_max_abs_log_residual','value':max_abs,'unit':'ln_power','verdict':'diagnostic'},
        {'metric':'score_k_min','value':K_MIN_SCORE,'unit':'1/Mpc','verdict':'setting'},
        {'metric':'score_k_max','value':K_MAX_SCORE,'unit':'1/Mpc','verdict':'setting'},
        {'metric':'mcift_global_peak','value':peak_global['wavelength_Mpc'],'unit':'Mpc','verdict':v20['verdict'](abs(peak_global['wavelength_Mpc']-r_s)/r_s)},
        {'metric':'mcift_BAO_window_peak','value':peak_bao['wavelength_Mpc'],'unit':'Mpc','verdict':v20['verdict'](abs(peak_bao['wavelength_Mpc']-r_s)/r_s)},
        {'metric':'lcdm_like_reference_peak_in_score_window','value':ref_peak_wav,'unit':'Mpc','verdict':'diagnostic'},
        {'metric':'sound_horizon_rs','value':r_s,'unit':'Mpc','verdict':'reference'},
        {'metric':'anchor_radius_R_A_5B','value':R_A,'unit':'Mpc','verdict':'derived'},
        {'metric':'derived_k_cut_5B','value':k_cut,'unit':'1/Mpc','verdict':'derived_not_fit'},
        {'metric':'derived_A_lock_5B','value':A_lock,'unit':'fraction','verdict':'derived_not_fit'},
        {'metric':'large_scale_slope_mcift_0.015_0.05','value':s_mcift_large,'unit':'dlnP_dlnk','verdict':'diagnostic'},
        {'metric':'large_scale_slope_reference_0.015_0.05','value':s_ref_large,'unit':'dlnP_dlnk','verdict':'diagnostic'},
        {'metric':'small_scale_slope_mcift_0.08_0.22','value':s_mcift_small,'unit':'dlnP_dlnk','verdict':'diagnostic'},
        {'metric':'small_scale_slope_reference_0.08_0.22','value':s_ref_small,'unit':'dlnP_dlnk','verdict':'diagnostic'}]
    write_csv(OUT/'mcift_v0.21_power_shape_residuals.csv',rows); write_csv(OUT/'mcift_v0.21_shape_metrics.csv',metrics)
    plt.figure(figsize=(8.8,5.7)); plt.loglog(k_arr,p_arr,marker='o',label='MCIFT v0.20 final P(k)'); plt.loglog(k_arr,pref*np.exp(amp),marker='s',label='LCDM-like reference shape, scaled'); plt.axvline(2*np.pi/r_s,linestyle='--',label='sound-horizon k'); plt.xlabel('k [1/Mpc]'); plt.ylabel('arbitrary normalized P(k)'); plt.title('MCIFT v0.21 full P(k) shape comparison'); plt.legend(); plt.grid(True,which='both',alpha=0.25); plt.tight_layout(); plt.savefig(OUT/'mcift_v0.21_pk_shape_comparison.png',dpi=140); plt.savefig(OUT/'mcift_v0.21_pk_shape_comparison.svg'); plt.close()
    plt.figure(figsize=(8.8,4.8)); plt.axhline(0,linewidth=1); plt.plot(k_arr,[r['log_residual'] for r in rows],marker='o'); plt.axvspan(K_MIN_SCORE,K_MAX_SCORE,alpha=0.12,label='score window'); plt.xscale('log'); plt.xlabel('k [1/Mpc]'); plt.ylabel('ln(P_MCIFT/P_ref_scaled)'); plt.title(f'MCIFT v0.21 log-shape residuals: RMS={rms:.3f}, {verdict}'); plt.legend(); plt.grid(True,which='both',alpha=0.25); plt.tight_layout(); plt.savefig(OUT/'mcift_v0.21_shape_residuals.png',dpi=140); plt.savefig(OUT/'mcift_v0.21_shape_residuals.svg'); plt.close()
    print(f'MCIFT v0.21 full-shape test complete: RMS={rms:.3f}, verdict={verdict}')
if __name__ == '__main__': main()
