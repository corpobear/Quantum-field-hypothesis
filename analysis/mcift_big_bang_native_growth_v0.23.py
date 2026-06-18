#!/usr/bin/env python3
"""MCIFT v0.23 compact native-growth attempt.
No BBKS/Sugiyama/CLASS/CAMB transfer is used inside the model evolution.
A reference curve is used only for external shape scoring.
"""
import csv, math, runpy
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
v20=runpy.run_path(str(BASE/'mcift_big_bang_derived_scalelock_v0.20.py'))
OUT=BASE/'results_v0.23'; OUT.mkdir(exist_ok=True)
C=v20['C_LIGHT_KM_S']; OM=v20['OMEGA_M']; OR=v20['OMEGA_R']; OL=v20['OMEGA_LAMBDA']; OB=v20['OMEGA_B']; h=v20['h']; H0=v20['H0_KM_S_MPC']; NS=v20['N_S_PLANCK']; KP=v20['K_PIVOT']; P=v20['DAMPING_POWER']; WIN=v20['BAO_WINDOW_MPC']
KMIN,KMAX=0.015,0.22

def E(a): return np.sqrt(OR/a**4+OM/a**3+OL)
def H(a): return H0*E(a)
def Om(a): return (OM/a**3)/E(a)**2
def Or(a): return (OR/a**4)/E(a)**2
def verdict(e): return 'PASS-LIKE' if e<.1 else ('WEAK' if e<.5 else 'FAIL')
def shape_verdict(r): return 'PASS-LIKE' if r<.35 else ('WEAK' if r<1 else 'FAIL')
def gamma(): return OM*h*math.exp(-OB*(1+math.sqrt(2*h)/OM))
def Tbbks(k):
    q=np.maximum((k/h)/gamma(),1e-12); L=np.log(1+2.34*q)/(2.34*q); Cc=(1+3.89*q+(16.1*q)**2+(5.46*q)**3+(6.71*q)**4)**-.25; return L*Cc
def ref_pk(k,rs): return np.maximum((k/KP)**NS*Tbbks(k)**2*(1+.12*np.sin(k*rs)*np.exp(-(k/.18)**1.4)),1e-300)
def wc(path,rows):
    with open(path,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
def interp(a,nodes,vals): return np.interp(np.log(a),np.log(nodes),vals,left=vals[0],right=vals[-1])
def peak(k,p,window=None):
    m=np.ones_like(k,dtype=bool)
    if window: wl=2*np.pi/k; m=(wl>=window[0])&(wl<=window[1])
    idx=np.where(m)[0][np.argmax(p[m])]
    return {'k_1_per_Mpc':float(k[idx]),'power':float(p[idx]),'wavelength_Mpc':float(2*np.pi/k[idx])}
def slope(k,p,lo,hi):
    m=(k>=lo)&(k<=hi)&(p>0)
    return float(np.polyfit(np.log(k[m]),np.log(p[m]),1)[0]) if np.sum(m)>1 else math.nan

def tracks():
    X,Y,Z,R=v20['make_grids'](); out=[]; ratios=[]; final=None
    for years,label in v20['MILESTONES']:
        a=v20['scale_factor_at_age_Gyr'](years/1e9); ch=v20['apply_frw_channel_dilution'](v20['evolve_base_channels'](years,X,Y,Z),a)
        ratio,err,rv=v20['visible_dark_metrics'](ch); out.append((a,v20['anchor_rms_radius_Mpc'](ch,R),v20['anchor_derived_k_cut'](ch,R),v20['derived_lock_amplitude'](ch)))
        ratios.append({'milestone':label,'a':a,'visible_dark_ratio':ratio,'ratio_error':err,'ratio_verdict':rv})
        if label=='5B': final=(ch,R)
    return np.array(out),ratios,final

def native_T(k,af,nodes,RA,kc,A,rs):
    ks=2*np.pi/rs; ag=np.geomspace(1e-4,af,420); x=np.log(ag); T=np.ones_like(k)
    for i,a in enumerate(ag[:-1]):
        kcut=interp(a,nodes,kc); Ra=interp(a,nodes,RA); Al=interp(a,nodes,A)
        anchor=1-np.exp(-((k/kcut)**P)); sig=ks*(rs/Ra); lock=1+Al*np.exp(-.5*((k-ks)/sig)**2)
        kh=a*H(a)/C; inside=k**2/(k**2+kh**2); rad=Or(a)/(Or(a)+Om(a)+1e-30)
        drag=1+rad*inside*(k/ks)**2; sink=1+(1-Al)*(k/(P*ks))**2
        f=(Om(a)**.55)*anchor*lock/(drag*sink); T*=np.exp(f*(x[i+1]-x[i]))
    return T

def main():
    tr,ratio_rows,(ch,R)=tracks(); nodes,RA,kc,A=tr[:,0],tr[:,1],tr[:,2],tr[:,3]; rs=v20['sound_horizon_Mpc']()
    raw=v20['apply_anchor_damping'](v20['density_proxy'](ch,R,rs,locked=True),kc[-1]); raw_rows=v20['isotropic_power_spectrum'](raw,k_cut=kc[-1],n_bins=44)
    k=np.array([r['k_1_per_Mpc'] for r in raw_rows]); praw=np.array([r['power'] for r in raw_rows]); T=native_T(k,nodes[-1],nodes,RA,kc,A,rs)
    pn=(np.maximum(k,1e-12)/KP)**NS*T**2; pr=ref_pk(k,rs); m=(k>=KMIN)&(k<=KMAX)&(pn>0)&(pr>0); amp=np.mean(np.log(pn[m])-np.log(pr[m])); prs=pr*np.exp(amp); res=np.log(pn)-np.log(prs); rms=float(np.sqrt(np.mean(res[m]**2))); mean=float(np.mean(np.abs(res[m]))); mx=float(np.max(np.abs(res[m])))
    rg,ng,nb,rf=peak(k,praw),peak(k,pn),peak(k,pn,WIN),peak(k[m],pr[m])
    metrics=[{'metric':'native_shape_rms_log_residual','value':rms,'unit':'ln_power','verdict':shape_verdict(rms)},{'metric':'native_shape_mean_abs_log_residual','value':mean,'unit':'ln_power','verdict':'diagnostic'},{'metric':'native_shape_max_abs_log_residual','value':mx,'unit':'ln_power','verdict':'diagnostic'},{'metric':'raw_geometric_global_peak','value':rg['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(abs(rg['wavelength_Mpc']-rs)/rs)},{'metric':'native_growth_global_peak','value':ng['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(abs(ng['wavelength_Mpc']-rs)/rs)},{'metric':'native_growth_BAO_window_peak','value':nb['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(abs(nb['wavelength_Mpc']-rs)/rs)},{'metric':'reference_scoring_peak','value':rf['wavelength_Mpc'],'unit':'Mpc','verdict':'reference'},{'metric':'sound_horizon_rs','value':rs,'unit':'Mpc','verdict':'reference'},{'metric':'anchor_radius_R_A_5B','value':RA[-1],'unit':'Mpc','verdict':'derived'},{'metric':'derived_k_cut_5B','value':kc[-1],'unit':'1/Mpc','verdict':'derived_not_fit'},{'metric':'derived_A_lock_5B','value':A[-1],'unit':'fraction','verdict':'derived_not_fit'},{'metric':'large_scale_slope_native_0.015_0.05','value':slope(k,pn,.015,.05),'unit':'dlnP_dlnk','verdict':'diagnostic'},{'metric':'large_scale_slope_reference_0.015_0.05','value':slope(k,prs,.015,.05),'unit':'dlnP_dlnk','verdict':'diagnostic'},{'metric':'small_scale_slope_native_0.08_0.22','value':slope(k,pn,.08,.22),'unit':'dlnP_dlnk','verdict':'diagnostic'},{'metric':'small_scale_slope_reference_0.08_0.22','value':slope(k,prs,.08,.22),'unit':'dlnP_dlnk','verdict':'diagnostic'}]
    wc(OUT/'mcift_v0.23_native_growth_metrics.csv',metrics); wc(OUT/'mcift_v0.23_channel_tracks.csv',[{'a':float(nodes[i]),'R_A_Mpc':float(RA[i]),'k_cut_1_per_Mpc':float(kc[i]),'A_lock':float(A[i]),**ratio_rows[i]} for i in range(len(nodes))]); wc(OUT/'mcift_v0.23_native_growth_residuals.csv',[{'k_1_per_Mpc':float(k[i]),'wavelength_Mpc':float(2*np.pi/k[i]),'raw_geometric_power':float(praw[i]),'native_growth_transfer':float(T[i]),'native_growth_power':float(pn[i]),'reference_power_scaled':float(prs[i]),'log_residual':float(res[i]),'score_window':bool(KMIN<=k[i]<=KMAX)} for i in range(len(k))])
    plt.figure(figsize=(8.8,5.7)); plt.loglog(k,praw/np.max(praw),marker='o',label='raw MCIFT normalized',alpha=.65); plt.loglog(k,pn/np.max(pn),marker='s',label='v0.23 native growth'); plt.loglog(k,prs/np.max(prs),marker='^',label='reference shape'); plt.axvline(2*np.pi/rs,ls='--',label='sound-horizon k'); plt.xlabel('k [1/Mpc]'); plt.ylabel('normalized P(k)'); plt.title(f'MCIFT v0.23 native growth: RMS={rms:.3f}, {shape_verdict(rms)}'); plt.legend(); plt.grid(True,which='both',alpha=.25); plt.tight_layout(); plt.savefig(OUT/'mcift_v0.23_native_growth_comparison.png',dpi=140); plt.close()
    (OUT/'mcift_v0.23_native_growth_report.md').write_text(f'''# MCIFT v0.23 Native Growth Attempt Report\n\n**Status:** first MCIFT-native growth attempt; not established physics; not a CLASS/CAMB replacement.  \n**Script:** `analysis/mcift_big_bang_native_growth_v0.23.py`  \n**Main change from v0.22:** removes the imported BBKS/Sugiyama transfer layer from model evolution and tries to grow `T_growth(k)` from MCIFT channel mechanics.\n\n## Native growth closure\n\n```text\nT_growth_MCIFT(k,a_final) = exp[ integral f_MCIFT(k,a) d ln a ]\nf_MCIFT = Omega_m(a)^0.55 * T_anchor(k,a) * T_lock(k,a) / [radiation_drag(k,a) * dark_sink_resistance(k,a)]\nT_anchor = 1 - exp[-(k/k_cut(a))^p]\nk_cut(a) = 2 pi / R_A(a)\nT_lock = 1 + A_lock(a) exp[-0.5 ((k-k_s)/sigma_lock)^2]\nk_s = 2 pi / r_s\nsigma_lock = k_s * r_s / R_A(a)\np = 4 dark-side sinks\n```\n\nThis uses background expansion/horizon timing, but does not import the BBKS/Sugiyama transfer curve into the native growth evolution. A Lambda-CDM-like curve is used only as the external shape-scoring reference.\n\n## Result\n\n```text\nnative shape RMS log residual = {rms:.3f}\nnative shape verdict = {shape_verdict(rms)}\nraw geometric global peak = {rg['wavelength_Mpc']:.2f} Mpc\nnative growth global peak = {ng['wavelength_Mpc']:.2f} Mpc\nnative growth BAO-window peak = {nb['wavelength_Mpc']:.2f} Mpc\nreference scoring peak = {rf['wavelength_Mpc']:.2f} Mpc\n```\n\n## Derived values retained\n\n```text\nR_A(5B) = {RA[-1]:.3f} Mpc\nk_cut(5B) = {kc[-1]:.6f} 1/Mpc\nA_lock(5B) = {A[-1]:.6f}\nsound horizon r_s = {rs:.3f} Mpc\n```\n\n## Interpretation\n\n```text\nv0.23 is the first no-import native-growth attempt.\nIt keeps the BAO-like peak but fails the full broadband shape.\nThis means the missing ingredient is a stronger coupled perturbation system, not only a scalar growth-rate closure.\n```\n\n## Next target\n\nEvolve coupled perturbations directly:\n\n```text\ndelta_A(k,a), delta_V(k,a), delta_D(k,a), delta_R(k,a)\n```\n\nwith explicit channel-exchange terms:\n\n```text\nQ_A_to_V(k,a), Q_A_to_D(k,a), Q_V_to_D(k,a), Q_V_to_R(k,a)\n```\n''',encoding='utf-8')
    print(f'v0.23 native growth RMS={rms:.3f}; verdict={shape_verdict(rms)}')
if __name__=='__main__': main()
