#!/usr/bin/env python3
"""MCIFT v0.27 compact mass-gravity-time spin-blur retest.

Uses v0.26 helper functions, but replaces the aperture-only spin-blur proxy with:
    rho_G     ~ A + 0.6 V + 0.45 D + exchange
    theta_G   = sum(rho_G) / sum(rho_G + R)
    Gamma_rot = A_lock * (A_side/A_tip)
    beta_spin = tanh(Gamma_rot)
    chi_MGT   = (N_internal / 2pi) * beta_spin * (1 + theta_G)
    N_eff     = 4 + 2 exp[-chi_MGT^2]

Reference P(k) is used only for external scoring, not native evolution.
"""
import csv, math, runpy, zipfile
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
v26=runpy.run_path(str(BASE/'mcift_big_bang_spin_blur_v0.26.py'))
v20=v26['v20']; OUT=BASE/'results_v0.27'; OUT.mkdir(parents=True,exist_ok=True)
N_INT=v26['N_DARK_INTERNAL']; N_FLOOR=v26['N_TRANSVERSE_3D']; AP=v26['APERTURE_RATIO']
V23=4.147615292094368; V24=0.4685105160480104; V25=0.8069467814614266; V26=0.4685105158774012

def wc(path,rows):
    with open(path,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)

def mgt_load(ch):
    rm=np.maximum(ch['A']+0.6*ch['V']+0.45*ch['D'],0); rg=np.maximum(rm+ch['exchange'],0); rr=np.maximum(ch['R'],0)
    gt=float(rg.sum()); rt=float(rr.sum()); return gt/(gt+rt) if gt+rt>0 else 0.0, float(rm.sum()), gt

def make_tracks():
    X,Y,Z,R=v20['make_grids'](); rows=[]; final=None
    for years,label in v20['MILESTONES']:
        age=years/1e9; a=v20['scale_factor_at_age_Gyr'](age); ch=v20['apply_frw_channel_dilution'](v20['evolve_base_channels'](years,X,Y,Z),a)
        ratio,err,rv=v20['visible_dark_metrics'](ch); A=v20['derived_lock_amplitude'](ch); th,mt,gt=mgt_load(ch)
        grot=A*AP; beta=math.tanh(grot); chi=N_INT/(2*math.pi)*beta*(1+th); neff=N_FLOOR+(N_INT-N_FLOOR)*math.exp(-chi**2)
        rows.append({'milestone':label,'age_Gyr':age,'a':a,'z':1/a-1,'R_A_Mpc':v20['anchor_rms_radius_Mpc'](ch,R),'k_cut_1_per_Mpc':v20['anchor_derived_k_cut'](ch,R),'A_lock':A,'theta_mass_gravity_time':th,'mass_proxy_total':mt,'gravity_proxy_total':gt,'gamma_rot':grot,'beta_spin':beta,'spin_blur_chi_MGT':chi,'N_eff_dark_sinks':neff,'P_damping_eff':neff,'gamma_exchange_eff':AP/neff,'visible_dark_ratio':ratio,'visible_dark_fractional_error':err,'visible_dark_verdict':rv})
        if label=='5B': final=ch
    return rows,final,R

def main():
    tr,ch,R=make_tracks(); rs=v20['sound_horizon_Mpc'](); kcut=tr[-1]['k_cut_1_per_Mpc']
    raw=v20['apply_anchor_damping'](v20['density_proxy'](ch,R,rs,locked=True),kcut); rr=v20['isotropic_power_spectrum'](raw,k_cut=kcut,n_bins=44)
    k=np.array([r['k_1_per_Mpc'] for r in rr]); rawp=np.array([r['power'] for r in rr])
    T,y=v26['spin_blur_exchange_solver'](k,rs,tr); native=(np.maximum(k,1e-12)/v26['K_PIVOT'])**v26['N_S']*T**2
    ref=v26['reference_pk'](k,rs); mask=(k>=v26['K_MIN_SCORE'])&(k<=v26['K_MAX_SCORE'])&(native>0)&(ref>0)
    amp=float(np.mean(np.log(native[mask])-np.log(ref[mask]))); ref_s=ref*math.exp(amp); resid=np.log(native)-np.log(ref_s); rms=float(np.sqrt(np.mean(resid[mask]**2)))
    rawpk=v26['pick_peak_from_arrays'](k,rawp); gpk=v26['pick_peak_from_arrays'](k,native); bpk=v26['pick_peak_from_arrays'](k,native,v26['BAO_WINDOW']); rpk=v26['pick_peak_from_arrays'](k[mask],ref[mask]); ib=int(np.argmin(abs(k-2*math.pi/rs))); fin=tr[-1]
    metrics=[
      {'metric':'mgt_spin_blur_shape_rms_log_residual','value':rms,'unit':'ln_power','verdict':v26['verdict_shape'](rms)},
      {'metric':'mgt_spin_blur_shape_mean_abs_log_residual','value':float(np.mean(abs(resid[mask]))),'unit':'ln_power','verdict':'diagnostic'},
      {'metric':'mgt_spin_blur_shape_max_abs_log_residual','value':float(np.max(abs(resid[mask]))),'unit':'ln_power','verdict':'diagnostic'},
      {'metric':'v0.23_native_shape_rms_log_residual','value':V23,'unit':'ln_power','verdict':'prior_FAIL'},
      {'metric':'v0.24_four_sink_channel_exchange_rms','value':V24,'unit':'ln_power','verdict':'comparison_WEAK'},
      {'metric':'v0.25_first_principle_six_sink_rms','value':V25,'unit':'ln_power','verdict':'comparison_WEAK'},
      {'metric':'v0.26_aperture_spin_blur_rms','value':V26,'unit':'ln_power','verdict':'comparison_WEAK'},
      {'metric':'improvement_vs_v0.23_rms','value':V23-rms,'unit':'ln_power','verdict':'improved'},
      {'metric':'improvement_vs_v0.25_rms','value':V25-rms,'unit':'ln_power','verdict':'improved'},
      {'metric':'delta_vs_v0.26_rms','value':rms-V26,'unit':'ln_power','verdict':'worse_than_v026' if rms>V26 else 'better_than_v026'},
      {'metric':'raw_geometric_global_peak','value':rawpk['wavelength_Mpc'],'unit':'Mpc','verdict':v26['verdict_fractional_error'](abs(rawpk['wavelength_Mpc']-rs)/rs)},
      {'metric':'native_mgt_spin_blur_global_peak','value':gpk['wavelength_Mpc'],'unit':'Mpc','verdict':v26['verdict_fractional_error'](abs(gpk['wavelength_Mpc']-rs)/rs)},
      {'metric':'native_mgt_spin_blur_BAO_window_peak','value':bpk['wavelength_Mpc'],'unit':'Mpc','verdict':v26['verdict_fractional_error'](abs(bpk['wavelength_Mpc']-rs)/rs)},
      {'metric':'reference_scoring_peak','value':rpk['wavelength_Mpc'],'unit':'Mpc','verdict':'reference'},
      {'metric':'nearest_BAO_bin_wavelength','value':float(2*math.pi/k[ib]),'unit':'Mpc','verdict':v26['verdict_fractional_error'](abs(2*math.pi/k[ib]-rs)/rs)},
      {'metric':'nearest_BAO_bin_log_residual','value':float(resid[ib]),'unit':'ln_power','verdict':'diagnostic'},
      {'metric':'sound_horizon_rs','value':rs,'unit':'Mpc','verdict':'reference'},
      {'metric':'anchor_radius_R_A_5B','value':fin['R_A_Mpc'],'unit':'Mpc','verdict':'derived'},
      {'metric':'derived_k_cut_5B','value':kcut,'unit':'1/Mpc','verdict':'derived_not_fit'},
      {'metric':'derived_A_lock_5B','value':fin['A_lock'],'unit':'fraction','verdict':'derived_not_fit'},
      {'metric':'theta_mass_gravity_time_final','value':fin['theta_mass_gravity_time'],'unit':'fraction','verdict':'derived_from_channel_load'},
      {'metric':'theta_mass_gravity_time_track_average','value':float(np.mean([r['theta_mass_gravity_time'] for r in tr])),'unit':'fraction','verdict':'derived_from_channel_load'},
      {'metric':'gamma_rot_final','value':fin['gamma_rot'],'unit':'dimensionless','verdict':'A_lock_times_aperture_ratio'},
      {'metric':'beta_spin_final','value':fin['beta_spin'],'unit':'fraction_capped','verdict':'tanh_gamma_rot'},
      {'metric':'chi_MGT_final','value':fin['spin_blur_chi_MGT'],'unit':'sector_intervals_per_response','verdict':'mass_gravity_time_spin_blur'},
      {'metric':'chi_MGT_track_average','value':float(np.mean([r['spin_blur_chi_MGT'] for r in tr])),'unit':'sector_intervals_per_response','verdict':'mass_gravity_time_spin_blur'},
      {'metric':'N_eff_dark_sinks_final','value':fin['N_eff_dark_sinks'],'unit':'effective_sinks','verdict':'spin_blur_projection'},
      {'metric':'N_eff_dark_sinks_track_average','value':float(np.mean([r['N_eff_dark_sinks'] for r in tr])),'unit':'effective_sinks','verdict':'spin_blur_projection'},
      {'metric':'gamma_exchange_eff_final','value':fin['gamma_exchange_eff'],'unit':'dimensionless','verdict':'aperture_ratio_over_N_eff'},
      {'metric':'internal_dark_sectors','value':N_INT,'unit':'sectors','verdict':'first_principle'},
      {'metric':'transverse_3D_sink_floor','value':N_FLOOR,'unit':'effective_sinks','verdict':'projection_floor'},
      {'metric':'aperture_ratio_A_side_over_A_tip','value':AP,'unit':'dimensionless','verdict':'from_source_math'},
      {'metric':'large_scale_slope_native_0.015_0.05','value':v26['slope'](k,native,0.015,0.05),'unit':'dlnP_dlnk','verdict':'diagnostic'},
      {'metric':'large_scale_slope_reference_0.015_0.05','value':v26['slope'](k,ref_s,0.015,0.05),'unit':'dlnP_dlnk','verdict':'diagnostic'},
      {'metric':'small_scale_slope_native_0.08_0.22','value':v26['slope'](k,native,0.08,0.22),'unit':'dlnP_dlnk','verdict':'diagnostic'},
      {'metric':'small_scale_slope_reference_0.08_0.22','value':v26['slope'](k,ref_s,0.08,0.22),'unit':'dlnP_dlnk','verdict':'diagnostic'}]
    wc(OUT/'mcift_v0.27_mgt_spin_blur_metrics.csv',metrics); wc(OUT/'mcift_v0.27_mgt_spin_blur_tracks.csv',tr)
    wc(OUT/'mcift_v0.27_mgt_spin_blur_residuals.csv',[{'k_1_per_Mpc':float(k[i]),'wavelength_Mpc':float(2*math.pi/k[i]),'raw_geometric_power':float(rawp[i]),'T_growth_mgt_spin_blur':float(T[i]),'native_mgt_spin_blur_power':float(native[i]),'reference_power_scaled':float(ref_s[i]),'log_residual':float(resid[i]),'score_window':bool(mask[i]),'delta_A_final':float(y[i,0]),'delta_V_final':float(y[i,1]),'delta_D_final':float(y[i,2]),'delta_R_final':float(y[i,3])} for i in range(len(k))])
    print(f'v0.27 MGT spin-blur RMS={rms:.3f}; N_eff={fin["N_eff_dark_sinks"]:.6f}; chi={fin["spin_blur_chi_MGT"]:.6f}; theta_G={fin["theta_mass_gravity_time"]:.6f}')
if __name__=='__main__': main()
