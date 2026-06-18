#!/usr/bin/env python3
"""MCIFT v0.24 compact channel-exchange retest.

Derived A/V/D/R perturbation exchange scaffold. Does not use BBKS/Sugiyama in
model evolution; the reference transfer is only for external scoring.
"""
import csv, math, runpy
from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
v20=runpy.run_path(str(BASE/'mcift_big_bang_derived_scalelock_v0.20.py'))
OUT=BASE/'results_v0.24'; OUT.mkdir(exist_ok=True)
C=v20['C_LIGHT_KM_S']; H0=v20['H0_KM_S_MPC']; h=v20['h']; OM=v20['OMEGA_M']; OR=v20['OMEGA_R']; OL=v20['OMEGA_LAMBDA']; OB=v20['OMEGA_B']; NS=v20['N_S_PLANCK']; KP=v20['K_PIVOT']; P=v20['DAMPING_POWER']; ND=v20['N_DARK_SINKS']; WIN=v20['BAO_WINDOW_MPC']
A_TIP=0.01977858948; A_SIDE=0.10714285710; F_VISIBLE=A_TIP/(A_TIP+A_SIDE); F_DARK=A_SIDE/(A_TIP+A_SIDE); RATIO=A_SIDE/A_TIP
GAMMA_EXCHANGE=RATIO/ND; RADIATION_DRAG_STRENGTH=1/F_VISIBLE; RADIATION_PRESSURE_STRENGTH=2*RATIO; DARK_SINK_RESISTANCE=RATIO
KMIN,KMAX=.015,.22; V23_RMS=4.147615292094368

def E(a): return np.sqrt(OR/a**4+OM/a**3+OL)
def H(a): return H0*E(a)
def Om(a): return (OM/a**3)/E(a)**2
def Or(a): return (OR/a**4)/E(a)**2
def dlnH(a): return -.5*(4*Or(a)+3*Om(a))
def verdict(e): return 'PASS-LIKE' if e<.1 else ('WEAK' if e<.5 else 'FAIL')
def vshape(r): return 'PASS-LIKE' if r<.35 else ('WEAK' if r<1 else 'FAIL')
def gamma_ref(): return OM*h*math.exp(-OB*(1+math.sqrt(2*h)/OM))
def Tref(k):
    q=np.maximum((k/h)/gamma_ref(),1e-12); L=np.log(1+2.34*q)/(2.34*q); Cc=(1+3.89*q+(16.1*q)**2+(5.46*q)**3+(6.71*q)**4)**-.25; return L*Cc
def pref(k,rs): return np.maximum((np.maximum(k,1e-12)/KP)**NS*Tref(k)**2*(1+.12*np.sin(k*rs)*np.exp(-(k/.18)**1.4)),1e-300)
def wcsv(path,rows):
    with open(path,'w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
def interp(a,nodes,vals): return float(np.interp(np.log(a),np.log(nodes),vals,left=vals[0],right=vals[-1]))
def peak(k,p,win=None):
    m=np.ones_like(k,dtype=bool)
    if win: wl=2*np.pi/k; m=(wl>=win[0])&(wl<=win[1])
    ii=np.where(m)[0][np.argmax(p[m])]
    return {'k_1_per_Mpc':float(k[ii]),'power':float(p[ii]),'wavelength_Mpc':float(2*np.pi/k[ii])}
def slope(k,p,lo,hi):
    m=(k>=lo)&(k<=hi)&(p>0)
    return float(np.polyfit(np.log(k[m]),np.log(p[m]),1)[0]) if np.sum(m)>1 else math.nan

def tracks():
    X,Y,Z,R=v20['make_grids'](); rows=[]; final=None
    for years,label in v20['MILESTONES']:
        a=v20['scale_factor_at_age_Gyr'](years/1e9); ch=v20['apply_frw_channel_dilution'](v20['evolve_base_channels'](years,X,Y,Z),a)
        ratio,err,rv=v20['visible_dark_metrics'](ch)
        rows.append({'milestone':label,'age_Gyr':years/1e9,'a':a,'z':1/a-1,'R_A_Mpc':v20['anchor_rms_radius_Mpc'](ch,R),'k_cut_1_per_Mpc':v20['anchor_derived_k_cut'](ch,R),'A_lock':v20['derived_lock_amplitude'](ch),'visible_dark_ratio':ratio,'visible_dark_fractional_error':err,'visible_dark_verdict':rv})
        if label=='5B': final=(ch,R)
    return rows,final

def solve(k,rs,tr):
    nodes=np.array([r['a'] for r in tr]); RA=np.array([r['R_A_Mpc'] for r in tr]); KC=np.array([r['k_cut_1_per_Mpc'] for r in tr]); AL=np.array([r['A_lock'] for r in tr]); ks=2*np.pi/rs
    ag=np.geomspace(1e-5,nodes[-1],1200); x=np.log(ag); y=np.ones((len(k),8))*1e-5; y[:,4:]=0
    def rhs(a,y):
        om=Om(a); orr=Or(a); fr=2+dlnH(a); kh=a*H(a)/C; inside=k**2/(k**2+kh**2); kcut=interp(a,nodes,KC); ra=interp(a,nodes,RA); al=interp(a,nodes,AL)
        Tanc=1-np.exp(-(k/kcut)**P); sig=ks*(rs/ra); Tlock=1+al*np.exp(-.5*((k-ks)/sig)**2); Tsink=(k/(ND*ks))**2/(1+(k/(ND*ks))**2)
        qAV=GAMMA_EXCHANGE*F_VISIBLE*al*Tanc*Tlock*(1-orr); qAD=GAMMA_EXCHANGE*F_DARK*al*Tanc*(.5+.5*Tsink); qVD=GAMMA_EXCHANGE*F_DARK*Tsink*inside/(1+ND); qVR=RADIATION_DRAG_STRENGTH*F_VISIBLE*orr*inside
        rdrag=RADIATION_DRAG_STRENGTH*orr*inside*(k/ks)**2/(1+(k/ks)**2); rpress=RADIATION_PRESSURE_STRENGTH*orr*inside*(k/ks)**2/(1+(k/ks)**2); dsink=DARK_SINK_RESISTANCE*(1-al)*Tsink
        dA,dV,dD,dR,uA,uV,uD,uR=[y[:,i] for i in range(8)]; dm=(F_VISIBLE*dV+F_DARK*dD)/(F_VISIBLE+F_DARK); seed=Tanc*Tlock*1e-5; out=np.zeros_like(y)
        out[:,0]=uA; out[:,1]=uV; out[:,2]=uD; out[:,3]=uR
        out[:,4]=-1.2*uA-qAV*(dA-dV)-qAD*(dA-dD)-.3*(dA-seed)
        out[:,5]=-(fr+rdrag+qVR)*uV+1.5*om*dm+qAV*(dA-dV)-qVD*(dV-dD)-rpress*(dV-dR)
        out[:,6]=-(fr+dsink)*uD+1.5*om*dm+qAD*(dA-dD)+qVD*(dV-dD)
        out[:,7]=-(fr+rdrag+qVR)*uR-rpress*dR+qVR*(dV-dR)
        return out
    for i in range(len(ag)-1):
        hstep=x[i+1]-x[i]; amid=math.sqrt(ag[i]*ag[i+1]); k1=rhs(ag[i],y); k2=rhs(amid,y+.5*hstep*k1); k3=rhs(amid,y+.5*hstep*k2); k4=rhs(ag[i+1],y+hstep*k3); y+=hstep*(k1+2*k2+2*k3+k4)/6
    dm=(F_VISIBLE*y[:,1]+F_DARK*y[:,2])/(F_VISIBLE+F_DARK)
    return np.abs(dm)/1e-5,y

def main():
    tr,(ch,R)=tracks(); rs=v20['sound_horizon_Mpc'](); raw=v20['apply_anchor_damping'](v20['density_proxy'](ch,R,rs,locked=True),tr[-1]['k_cut_1_per_Mpc']); rr=v20['isotropic_power_spectrum'](raw,k_cut=tr[-1]['k_cut_1_per_Mpc'],n_bins=44); k=np.array([r['k_1_per_Mpc'] for r in rr]); praw=np.array([r['power'] for r in rr])
    T,y=solve(k,rs,tr); pn=(np.maximum(k,1e-12)/KP)**NS*T**2; pr=pref(k,rs); mask=(k>=KMIN)&(k<=KMAX)&(pn>0)&(pr>0); amp=np.mean(np.log(pn[mask])-np.log(pr[mask])); prs=pr*math.exp(amp); res=np.log(pn)-np.log(prs); rms=float(np.sqrt(np.mean(res[mask]**2))); rawp=peak(k,praw); ng=peak(k,pn); nb=peak(k,pn,WIN); rp=peak(k[mask],pr[mask]); ib=int(np.argmin(abs(k-2*np.pi/rs)))
    metrics=[{'metric':'channel_exchange_shape_rms_log_residual','value':rms,'unit':'ln_power','verdict':vshape(rms)},{'metric':'channel_exchange_shape_mean_abs_log_residual','value':float(np.mean(abs(res[mask]))),'unit':'ln_power','verdict':'diagnostic'},{'metric':'channel_exchange_shape_max_abs_log_residual','value':float(np.max(abs(res[mask]))),'unit':'ln_power','verdict':'diagnostic'},{'metric':'v0.23_native_shape_rms_log_residual','value':V23_RMS,'unit':'ln_power','verdict':'prior_FAIL'},{'metric':'improvement_vs_v0.23_rms','value':V23_RMS-rms,'unit':'ln_power','verdict':'improved' if rms<V23_RMS else 'not_improved'},{'metric':'raw_geometric_global_peak','value':rawp['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(abs(rawp['wavelength_Mpc']-rs)/rs)},{'metric':'native_channel_exchange_global_peak','value':ng['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(abs(ng['wavelength_Mpc']-rs)/rs)},{'metric':'native_channel_exchange_BAO_window_peak','value':nb['wavelength_Mpc'],'unit':'Mpc','verdict':verdict(abs(nb['wavelength_Mpc']-rs)/rs)},{'metric':'reference_scoring_peak','value':rp['wavelength_Mpc'],'unit':'Mpc','verdict':'reference'},{'metric':'nearest_BAO_bin_wavelength','value':float(2*np.pi/k[ib]),'unit':'Mpc','verdict':verdict(abs(2*np.pi/k[ib]-rs)/rs)},{'metric':'nearest_BAO_bin_log_residual','value':float(res[ib]),'unit':'ln_power','verdict':'diagnostic'},{'metric':'sound_horizon_rs','value':rs,'unit':'Mpc','verdict':'reference'},{'metric':'anchor_radius_R_A_5B','value':tr[-1]['R_A_Mpc'],'unit':'Mpc','verdict':'derived'},{'metric':'derived_k_cut_5B','value':tr[-1]['k_cut_1_per_Mpc'],'unit':'1/Mpc','verdict':'derived_not_fit'},{'metric':'derived_A_lock_5B','value':tr[-1]['A_lock'],'unit':'fraction','verdict':'derived_not_fit'},{'metric':'A_tip','value':A_TIP,'unit':'source_aperture','verdict':'from_source_math'},{'metric':'A_side','value':A_SIDE,'unit':'source_aperture','verdict':'from_source_math'},{'metric':'aperture_ratio_A_side_over_A_tip','value':RATIO,'unit':'dimensionless','verdict':'from_source_math'},{'metric':'F_visible','value':F_VISIBLE,'unit':'fraction','verdict':'derived'},{'metric':'F_dark','value':F_DARK,'unit':'fraction','verdict':'derived'},{'metric':'gamma_exchange','value':GAMMA_EXCHANGE,'unit':'dimensionless','verdict':'A_side_over_A_tip_div_N_dark_sinks'},{'metric':'radiation_drag_strength','value':RADIATION_DRAG_STRENGTH,'unit':'dimensionless','verdict':'inverse_visible_fraction'},{'metric':'radiation_pressure_strength','value':RADIATION_PRESSURE_STRENGTH,'unit':'dimensionless','verdict':'two_transverse_modes_times_aperture_ratio'},{'metric':'dark_sink_resistance','value':DARK_SINK_RESISTANCE,'unit':'dimensionless','verdict':'aperture_ratio'},{'metric':'large_scale_slope_native_0.015_0.05','value':slope(k,pn,.015,.05),'unit':'dlnP_dlnk','verdict':'diagnostic'},{'metric':'large_scale_slope_reference_0.015_0.05','value':slope(k,prs,.015,.05),'unit':'dlnP_dlnk','verdict':'diagnostic'},{'metric':'small_scale_slope_native_0.08_0.22','value':slope(k,pn,.08,.22),'unit':'dlnP_dlnk','verdict':'diagnostic'},{'metric':'small_scale_slope_reference_0.08_0.22','value':slope(k,prs,.08,.22),'unit':'dlnP_dlnk','verdict':'diagnostic'}]
    wcsv(OUT/'mcift_v0.24_channel_exchange_metrics.csv',metrics)
    wcsv(OUT/'mcift_v0.24_channel_exchange_tracks.csv',tr)
    wcsv(OUT/'mcift_v0.24_channel_exchange_residuals.csv',[{'k_1_per_Mpc':float(k[i]),'wavelength_Mpc':float(2*np.pi/k[i]),'raw_geometric_power':float(praw[i]),'T_growth_channel_exchange':float(T[i]),'native_channel_exchange_power':float(pn[i]),'reference_power_scaled':float(prs[i]),'log_residual':float(res[i]),'score_window':bool(mask[i]),'delta_A_final':float(y[i,0]),'delta_V_final':float(y[i,1]),'delta_D_final':float(y[i,2]),'delta_R_final':float(y[i,3])} for i in range(len(k))])
    print(f'v0.24 channel-exchange RMS={rms:.3f}; verdict={vshape(rms)}')
if __name__=='__main__': main()
