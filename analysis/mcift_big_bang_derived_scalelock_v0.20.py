#!/usr/bin/env python3
"""MCIFT v0.20 derived scale-lock rerun.

Uses existing v0.19 equations and removes remaining toy scale-lock knobs:
A_lock=sum(rho_A)/sum(rho_total_positive), R_env=R_A, k_cut=2*pi/R_A.
"""
from __future__ import annotations
import csv, runpy
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
v19=runpy.run_path(str(BASE/'mcift_big_bang_anchor_cutoff_v0.19.py'))
OUT=BASE/'results_v0.20'; OUT.mkdir(parents=True,exist_ok=True)

def base_density(ch):
    return ch['A']+0.6*ch['V']+0.45*ch['D']+ch['R']+ch['exchange']
def a_lock(ch):
    return float(np.sum(np.maximum(ch['A'],0.0))/np.sum(np.maximum(base_density(ch),0.0)))
def m_lock(ch,R,r_s):
    A=a_lock(ch); R_A=v19['anchor_radius'](ch,R)
    return np.maximum(1.0 + A*np.cos((2*np.pi/r_s)*R)*np.exp(-(R/R_A)**2), 1e-6)
def density(ch,R,r_s,locked):
    b=base_density(ch)
    return b*m_lock(ch,R,r_s) if locked else b
def write_csv(path,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
def pick(rows,window=None): return v19['v17']['pick_peak'](rows,window)
def verdict(err): return v19['verdict'](err)
def ps(d,k=None): return v19['isotropic_power_spectrum'](d,k)
def main():
    X,Y,Z,R=v19['v17']['make_grids'](); r_s=v19['v17']['sound_horizon_Mpc'](); summary=[]
    final_ch=unlocked=locked=damped=None
    for years,label in v19['MILESTONES']:
        age=years/1e9; a=v19['v17']['scale_factor_at_age_Gyr'](age); z=1/a-1
        ch=v19['v17']['apply_frw_channel_dilution'](v19['v17']['evolve_base_channels'](years,X,Y,Z),a)
        ratio,err,rv=v19['v17']['visible_dark_metrics'](ch)
        R_A=v19['anchor_radius'](ch,R); k=v19['k_cut_from_anchor'](ch,R); A=a_lock(ch)
        summary.append({'milestone':label,'actual_years':years,'age_Gyr':age,'a':a,'z':z,'visible_dark_weighted_ratio':ratio,'planck_baryon_cdm_ratio':v19['PLANCK_BARYON_CDM_RATIO'],'ratio_fractional_error':err,'ratio_verdict':rv,'anchor_radius_Mpc':R_A,'derived_k_cut_1_per_Mpc':k,'derived_lock_amplitude':A,'derived_R_env_Mpc':R_A,'damping_power':v19['DAMPING_POWER']})
        if label=='5B':
            final_ch=ch; unlocked=density(ch,R,r_s,False); locked=density(ch,R,r_s,True); damped=v19['apply_longmode_damping'](locked,k)
    R_A=v19['anchor_radius'](final_ch,R); k=v19['k_cut_from_anchor'](final_ch,R); A=a_lock(final_ch)
    ps_unlocked=ps(unlocked); ps_locked=ps(locked); ps_final=ps(damped,k)
    p_unlocked=pick(ps_unlocked); p_locked=pick(ps_locked); p_final=pick(ps_final); p_bao=pick(ps_final,v19['BAO_WINDOW_MPC'])
    gerr=abs(p_final['wavelength_Mpc']-r_s)/r_s; berr=abs(p_bao['wavelength_Mpc']-r_s)/r_s
    metrics=[
        {'metric':'unlocked_global_peak','value':p_unlocked['wavelength_Mpc'],'unit':'Mpc','verdict':'diagnostic'},
        {'metric':'derived_scalelock_global_peak','value':p_locked['wavelength_Mpc'],'unit':'Mpc','verdict':'diagnostic'},
        {'metric':'v0.20_global_peak','value':p_final['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(gerr)},
        {'metric':'v0.20_BAO_window_peak','value':p_bao['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(berr)},
        {'metric':'sound_horizon_rs','value':r_s,'unit':'Mpc','verdict':'reference'},
        {'metric':'anchor_radius_R_A_5B','value':R_A,'unit':'Mpc','verdict':'derived'},
        {'metric':'derived_k_cut_5B','value':k,'unit':'1/Mpc','verdict':'derived_not_fit'},
        {'metric':'derived_A_lock_5B','value':A,'unit':'fraction','verdict':'derived_not_fit'},
        {'metric':'derived_R_env_5B','value':R_A,'unit':'Mpc','verdict':'derived_not_fit'},
        {'metric':'damping_power','value':v19['DAMPING_POWER'],'unit':'dimensionless','verdict':'derived_from_4_dark_sinks'},
        {'metric':'global_fractional_error','value':gerr,'unit':'ratio','verdict':verdict(gerr)},
        {'metric':'BAO_window_fractional_error','value':berr,'unit':'ratio','verdict':verdict(berr)}]
    write_csv(OUT/'mcift_v0.20_summary.csv',summary); write_csv(OUT/'mcift_v0.20_structure_metrics.csv',metrics); write_csv(OUT/'mcift_v0.20_power_final.csv',ps_final)
    plt.figure(figsize=(8,5));
    for rows,label in [(ps_unlocked,'unlocked'),(ps_locked,'derived scale-lock'),(ps_final,'final')]: plt.loglog([r['k_1_per_Mpc'] for r in rows],[r['power'] for r in rows],marker='o',label=label)
    plt.axvline(2*np.pi/r_s,linestyle='--',label='sound-horizon k'); plt.axvline(k,linestyle=':',label='derived k_cut'); plt.legend(); plt.tight_layout(); plt.savefig(OUT/'mcift_v0.20_power_spectrum.png',dpi=140); plt.close()
    print(f'R_A={R_A:.3f} Mpc; k_cut={k:.6f}; A_lock={A:.6f}; global={p_final["wavelength_Mpc"]:.2f} Mpc {verdict(gerr)}')
if __name__=='__main__': main()
