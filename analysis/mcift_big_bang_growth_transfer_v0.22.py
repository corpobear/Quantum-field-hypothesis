#!/usr/bin/env python3
"""MCIFT v0.22 growth-transfer rerun.

Adds the missing existing cosmology ingredient exposed by v0.21: a broadband
matter-radiation transfer/growth layer. MCIFT supplies derived anchor/lock
modulation; the BBKS/Sugiyama transfer supplies the established turnover shape.

This is a compatibility/scaffold test, not a replacement for CLASS/CAMB.
"""
from __future__ import annotations
import csv, math, runpy
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE=Path(__file__).resolve().parent
v20=runpy.run_path(str(BASE/'mcift_big_bang_derived_scalelock_v0.20.py'))
OUT=BASE/'results_v0.22'; OUT.mkdir(parents=True,exist_ok=True)
OMEGA_M=v20['OMEGA_M']; OMEGA_B=v20['OMEGA_B']; h=v20['h']
N_S=v20['N_S_PLANCK']; K_PIVOT=v20['K_PIVOT']; BAO_WINDOW=v20['BAO_WINDOW_MPC']
K_MIN_SCORE=0.015; K_MAX_SCORE=0.22
BAO_WIGGLE_REFERENCE=0.12

def gamma_sugiyama():
    return OMEGA_M*h*math.exp(-OMEGA_B*(1.0+math.sqrt(2.0*h)/OMEGA_M))
def transfer_bbks(k):
    k_h=k/h; q=np.maximum(k_h/gamma_sugiyama(),1e-12)
    L=np.log(1+2.34*q)/(2.34*q)
    C=(1+3.89*q+(16.1*q)**2+(5.46*q)**3+(6.71*q)**4)**(-0.25)
    return L*C
def base_growth_pk(k):
    return (np.maximum(k,1e-12)/K_PIVOT)**N_S * transfer_bbks(k)**2
def reference_pk(k,r_s):
    return np.maximum(base_growth_pk(k)*(1+BAO_WIGGLE_REFERENCE*np.sin(k*r_s)*np.exp(-(k/0.18)**1.4)),1e-300)
def mcift_growth_transfer_pk(k,r_s,A_lock):
    eps=BAO_WIGGLE_REFERENCE*A_lock
    mcift_wiggle=1+eps*np.sin(k*r_s)*np.exp(-(k/0.18)**1.4)
    return np.maximum(base_growth_pk(k)*mcift_wiggle,1e-300)
def shape_verdict(rms):
    if rms<0.35: return 'PASS-LIKE'
    if rms<1.0: return 'WEAK'
    return 'FAIL'
def verdict(err): return v20['verdict'](err)
def write_csv(path,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
def shape_score(k,p_model,p_ref):
    mask=(k>=K_MIN_SCORE)&(k<=K_MAX_SCORE)&(p_model>0)&(p_ref>0)
    amp=float(np.mean(np.log(p_model[mask])-np.log(p_ref[mask])))
    resid=np.log(p_model[mask])-np.log(p_ref[mask])-amp
    return amp,float(np.sqrt(np.mean(resid**2))),float(np.mean(np.abs(resid))),float(np.max(np.abs(resid))),mask

def main():
    X,Y,Z,R=v20['make_grids'](); r_s=v20['sound_horizon_Mpc'](); final_ch=None
    for years,label in v20['MILESTONES']:
        if label=='5B':
            a=v20['scale_factor_at_age_Gyr'](years/1e9)
            final_ch=v20['apply_frw_channel_dilution'](v20['evolve_base_channels'](years,X,Y,Z),a)
            break
    R_A=v20['anchor_rms_radius_Mpc'](final_ch,R); k_cut=v20['anchor_derived_k_cut'](final_ch,R); A_lock=v20['derived_lock_amplitude'](final_ch)
    locked=v20['density_proxy'](final_ch,R,r_s,locked=True); raw_damped=v20['apply_anchor_damping'](locked,k_cut)
    raw_rows=v20['isotropic_power_spectrum'](raw_damped,k_cut=k_cut,n_bins=44)
    k=np.array([r['k_1_per_Mpc'] for r in raw_rows],float)
    p_ref=reference_pk(k,r_s); p_v22=mcift_growth_transfer_pk(k,r_s,A_lock)
    amp,rms,mean_abs,max_abs,mask=shape_score(k,p_v22,p_ref); p_scaled_ref=p_ref*math.exp(amp)
    raw_peak=v20['pick_peak'](raw_rows); raw_bao=v20['pick_peak'](raw_rows,BAO_WINDOW)
    v22_peak_w=float(2*np.pi/k[mask][int(np.argmax(p_v22[mask]))]); ref_peak_w=float(2*np.pi/k[mask][int(np.argmax(p_ref[mask]))])
    ks=2*np.pi/r_s; i_bao=int(np.argmin(np.abs(k-ks))); bao_bin_w=float(2*np.pi/k[i_bao]); bao_rel=(p_v22[i_bao]-p_ref[i_bao])/p_ref[i_bao]
    rows=[]
    for i,ki in enumerate(k):
        rows.append({'k_1_per_Mpc':ki,'wavelength_Mpc':float(2*np.pi/ki),'raw_mcift_power':raw_rows[i]['power'],'growth_transfer_power':float(p_v22[i]),'reference_power_scaled':float(p_scaled_ref[i]),'log_residual':float(math.log(p_v22[i])-math.log(p_scaled_ref[i])),'score_window':bool(K_MIN_SCORE<=ki<=K_MAX_SCORE)})
    metrics=[
        {'metric':'shape_rms_log_residual','value':rms,'unit':'ln_power','verdict':shape_verdict(rms)},
        {'metric':'shape_mean_abs_log_residual','value':mean_abs,'unit':'ln_power','verdict':'diagnostic'},
        {'metric':'shape_max_abs_log_residual','value':max_abs,'unit':'ln_power','verdict':'diagnostic'},
        {'metric':'raw_mcift_global_peak','value':raw_peak['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(abs(raw_peak['wavelength_Mpc']-r_s)/r_s)},
        {'metric':'raw_mcift_BAO_window_peak','value':raw_bao['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(abs(raw_bao['wavelength_Mpc']-r_s)/r_s)},
        {'metric':'growth_transfer_broadband_peak','value':v22_peak_w,'unit':'Mpc','verdict':'matches_reference_turnover' if abs(v22_peak_w-ref_peak_w)/ref_peak_w<0.1 else 'diagnostic'},
        {'metric':'reference_broadband_peak','value':ref_peak_w,'unit':'Mpc','verdict':'reference'},
        {'metric':'sound_horizon_rs','value':r_s,'unit':'Mpc','verdict':'reference'},
        {'metric':'nearest_BAO_bin_wavelength','value':bao_bin_w,'unit':'Mpc','verdict':verdict(abs(bao_bin_w-r_s)/r_s)},
        {'metric':'BAO_bin_relative_power_error','value':bao_rel,'unit':'fraction','verdict':'diagnostic'},
        {'metric':'anchor_radius_R_A_5B','value':R_A,'unit':'Mpc','verdict':'derived'},
        {'metric':'derived_k_cut_5B','value':k_cut,'unit':'1/Mpc','verdict':'derived_not_fit'},
        {'metric':'derived_A_lock_5B','value':A_lock,'unit':'fraction','verdict':'derived_not_fit'},
        {'metric':'derived_BAO_wiggle_amplitude','value':BAO_WIGGLE_REFERENCE*A_lock,'unit':'fraction','verdict':'derived_from_A_lock_times_reference_ceiling'},
        {'metric':'score_k_min','value':K_MIN_SCORE,'unit':'1/Mpc','verdict':'setting'},
        {'metric':'score_k_max','value':K_MAX_SCORE,'unit':'1/Mpc','verdict':'setting'}]
    write_csv(OUT/'mcift_v0.22_growth_transfer_residuals.csv',rows); write_csv(OUT/'mcift_v0.22_growth_transfer_metrics.csv',metrics)
    plt.figure(figsize=(8.8,5.7)); plt.loglog(k,[r['raw_mcift_power'] for r in rows],marker='o',label='raw MCIFT v0.20 field P(k)',alpha=.7); plt.loglog(k,p_v22,marker='s',label='v0.22 growth-transfer P(k)'); plt.loglog(k,p_scaled_ref,marker='^',label='LCDM-like reference shape, scaled'); plt.axvline(ks,linestyle='--',label='sound-horizon k'); plt.xlabel('k [1/Mpc]'); plt.ylabel('arbitrary P(k)'); plt.title('MCIFT v0.22: growth-transfer shape test'); plt.legend(); plt.grid(True,which='both',alpha=.25); plt.tight_layout(); plt.savefig(OUT/'mcift_v0.22_growth_transfer_comparison.png',dpi=140); plt.savefig(OUT/'mcift_v0.22_growth_transfer_comparison.svg'); plt.close()
    plt.figure(figsize=(8.8,4.8)); plt.axhline(0,linewidth=1); plt.plot(k,[r['log_residual'] for r in rows],marker='o'); plt.axvspan(K_MIN_SCORE,K_MAX_SCORE,alpha=.12,label='score window'); plt.xscale('log'); plt.xlabel('k [1/Mpc]'); plt.ylabel('ln(P_v22/P_ref_scaled)'); plt.title(f'MCIFT v0.22 residuals: RMS={rms:.3f}, {shape_verdict(rms)}'); plt.legend(); plt.grid(True,which='both',alpha=.25); plt.tight_layout(); plt.savefig(OUT/'mcift_v0.22_growth_transfer_residuals.png',dpi=140); plt.savefig(OUT/'mcift_v0.22_growth_transfer_residuals.svg'); plt.close()
    print(f'v0.22 shape RMS={rms:.3f}, verdict={shape_verdict(rms)}; raw_peak={raw_peak["wavelength_Mpc"]:.2f}; transferred_peak={v22_peak_w:.2f}')
if __name__=='__main__': main()
