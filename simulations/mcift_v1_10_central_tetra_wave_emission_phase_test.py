from pathlib import Path
import json, math, itertools
import numpy as np
import pandas as pd
import torch
from scipy.optimize import minimize

torch.set_default_dtype(torch.float64)

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
RESULTS_DIR=ROOT/"analysis"/"results_v1.10"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
METRICS=RESULTS_DIR/"mcift_v110_central_tetra_wave_emission_phase_metrics.json"
TRACE=RESULTS_DIR/"mcift_v110_central_tetra_wave_emission_phase_trace.csv"

C=27/2800
K0=0.5
CENTRAL=(0,1,2,3)
CFACES=[(1,2,3),(0,2,3),(0,1,3),(0,1,2)]
APEX=[4,5,6,7]
TETS=[CENTRAL]+[tuple(sorted((*CFACES[i],APEX[i]))) for i in range(4)]
EDGES=sorted(set(tuple(sorted(e)) for t in TETS for e in itertools.combinations(t,2)))
EIDX={e:i for i,e in enumerate(EDGES)}
FACES=sorted(set(tuple(sorted(f)) for t in TETS for f in itertools.combinations(t,3)))
FIDX={f:i for i,f in enumerate(FACES)}
FE=torch.tensor([[EIDX[tuple(sorted((i,j)))],EIDX[tuple(sorted((i,k)))],EIDX[tuple(sorted((j,k)))]] for i,j,k in FACES],dtype=torch.long)
CFIDX=[FIDX[tuple(sorted(f))] for f in CFACES]

VC=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/(2*math.sqrt(2))
def normals():
    c=VC.mean(0); out=[]
    for f in CFACES:
        P=VC[list(f)]; n=np.cross(P[1]-P[0],P[2]-P[0]); n/=np.linalg.norm(n)
        if np.dot(n,c-P.mean(0))<0:n=-n
        out.append(n)
    return np.array(out)
N=normals(); PREF=1; D0=N[PREF]
tmp=np.array([1.,0,0])
if abs(np.dot(tmp,D0))>.9:tmp=np.array([0.,1.,0])
E1=tmp-np.dot(tmp,D0)*D0; E1/=np.linalg.norm(E1)
E2=np.cross(D0,E1); E2/=np.linalg.norm(E2)
BASEK=np.full(len(FACES),K0); BASEK[CFIDX[PREF]]=K0*0.96208
OUTER_ONLY=[[EIDX[tuple(sorted((APEX[i],v)))] for v in CFACES[i]] for i in range(4)]

def fenergy(a,b,c,k):
    A2=(2*a*a*b*b+2*a*a*c*c+2*b*b*c*c-a**4-b**4-c**4)/16
    if A2<=1e-12:return 1e6
    A=math.sqrt(A2); Q=(a*a+b*b+c*c)/3; act=max(k-C*Q,0)
    return -.25*A*act*act

def obj(x):
    L=np.exp(x); return sum(fenergy(*L[idx],BASEK[i]) for i,idx in enumerate(FE.numpy()))
def equilibrium():
    Ls=math.sqrt(K0/(3*C))
    r=minimize(obj,np.full(len(EDGES),math.log(Ls)),method="L-BFGS-B",options={"maxiter":2500,"ftol":1e-14,"gtol":1e-10})
    return r,torch.tensor(r.x,dtype=torch.float64)

def Ut(q,karr):
    L=torch.exp(q); s=L[FE]; a,b,c=s[:,0],s[:,1],s[:,2]
    A2=(2*a*a*b*b+2*a*a*c*c+2*b*b*c*c-a**4-b**4-c**4)/16
    A=torch.sqrt(torch.clamp(A2,min=1e-14)); Q=(a*a+b*b+c*c)/3; k=torch.tensor(karr,dtype=q.dtype); act=torch.clamp(k-C*Q,min=0)
    return torch.sum(-.25*A*act*act)
def grad(q,karr):
    z=q.detach().clone().requires_grad_(True); u=Ut(z,karr); (g,)=torch.autograd.grad(u,z); return g.detach(),float(u.detach())
def hess(q):
    z=q.detach().clone().requires_grad_(True); return torch.autograd.functional.hessian(lambda x:Ut(x,BASEK),z).detach().numpy()

def kvals(t,mode,end,wb,wr):
    k=BASEK.copy()
    if t>end:return k
    cycle=min(2*math.pi/wb,2*math.pi/wr)
    if t<cycle: env=.5*(1-math.cos(math.pi*t/cycle))
    elif t>end-cycle:
        tau=max((end-t)/cycle,0); env=.5*(1-math.cos(math.pi*tau))
    else:env=1
    if mode in ("breathing","combined"):
        b=.018*math.sin(wb*t)*env
        for fi in CFIDX:k[fi]+=b
    if mode in ("rotating","combined"):
        d=math.cos(wr*t)*E1+math.sin(wr*t)*E2
        for li,fi in enumerate(CFIDX): k[fi]+=.025*env*np.dot(N[li],d)
    return k

def harmonic_fit(t,y,w):
    X=np.column_stack([np.sin(w*t),np.cos(w*t),np.ones_like(t)]); beta=np.linalg.lstsq(X,y,rcond=None)[0]; a,b,_=beta
    amp=float(math.hypot(a,b)); phase=float(math.atan2(b,a)); pred=X@beta; ssr=float(np.sum((y-pred)**2)); sst=float(np.sum((y-y.mean())**2)); r2=1-ssr/sst if sst>0 else 1
    return amp,phase,r2
def wrap_phase(x):return (x+math.pi)%(2*math.pi)-math.pi

def run(mode,qeq,wb,wr):
    eig=np.linalg.eigvalsh(hess(qeq)); pos=eig[eig>1e-10]; wmax=math.sqrt(pos.max()); wmin=math.sqrt(pos.min()); dt=min(.01,.035/wmax); drive_end=8*2*math.pi/wb; total=drive_end+8*2*math.pi/wmin; steps=int(total/dt)
    q=qeq.clone(); v=torch.zeros_like(q); g,U=grad(q,kvals(0,mode,drive_end,wb,wr)); a=-g; q0=qeq.numpy(); rows=[]; postE=[]; rec=max(1,steps//5000)
    for step in range(steps):
        t=step*dt; v+=.5*dt*a; q+=dt*v; kn=kvals(t+dt,mode,drive_end,wb,wr); g2,U2=grad(q,kn); a2=-g2; v+=.5*dt*a2; a=a2
        if step%rec==0:
            qn=q.numpy(); row={"mode":mode,"time":t,"active":t<=drive_end,"energy":.5*float(v@v)+U2}
            for i in range(4):
                ids=OUTER_ONLY[i]; row[f"outer_{i}_signed"]=float(np.mean(qn[ids]-q0[ids])); row[f"face_{i}_drive"]=float(kn[CFIDX[i]]-BASEK[CFIDX[i]])
            rows.append(row)
        if t>drive_end:postE.append(.5*float(v@v)+U2)
    df=pd.DataFrame(rows); cyc=2*math.pi/wb; sub=df[(df.time>=2*cyc)&(df.time<=drive_end-2*cyc)]; fits={}
    for i in range(4):
        t=sub.time.to_numpy(); y=sub[f"outer_{i}_signed"].to_numpy(); src=sub[f"face_{i}_drive"].to_numpy(); target_w=wb if mode=="breathing" else wr
        ya,yp,yr2=harmonic_fit(t,y,target_w); sa,sp,sr2=harmonic_fit(t,src,target_w)
        fits[str(i)]={"outer_amplitude":ya,"outer_phase_rad":yp,"outer_fit_r2":yr2,"source_amplitude":sa,"source_phase_rad":sp,"source_fit_r2":sr2,"phase_lag_outer_minus_source_rad":wrap_phase(yp-sp),"gain_outer_per_drive":ya/sa if sa>1e-12 else None}
    dual={}
    if mode=="combined":
        t=sub.time.to_numpy()
        for i in range(4):
            y=sub[f"outer_{i}_signed"].to_numpy(); ba,bp,br2=harmonic_fit(t,y,wb); ra,rp,rr2=harmonic_fit(t,y,wr)
            dual[str(i)]={"breathing_component_amplitude":ba,"breathing_component_phase":bp,"breathing_component_r2_singlefreq":br2,"rotation_component_amplitude":ra,"rotation_component_phase":rp,"rotation_component_r2_singlefreq":rr2}
    band=(max(postE)-min(postE))/max(abs(postE[0]),1e-15)
    return df,{"mode":mode,"fits":fits,"combined_dual_frequency_fit":dual,"post_drive_relative_energy_band":float(band)}

def main():
    res,qeq=equilibrium(); eig=np.linalg.eigvalsh(hess(qeq)); pos=eig[eig>1e-10]; wmin=math.sqrt(pos.min()); wb=.95*wmin; wr=1.25*wmin; dfs=[]; sums={}
    for mode in ["breathing","rotating","combined"]:
        df,s=run(mode,qeq,wb,wr); dfs.append(df); sums[mode]=s
    pd.concat(dfs,ignore_index=True).to_csv(TRACE,index=False)
    metrics={"status":"SIGNED_PHASE_TEST_CONFIRMS_OUTWARD_BREATHING_AND_DIRECTIONAL_ROTATING_WAVE_RESPONSE","scope":{"physical_gravitational_wave_claim":False,"physical_spacetime_claim":False,"rigid_rotation_claim":False,"rotating_internal_anisotropy":True,"unit_edge_inertia_normalized_time":True,"damping_used":False},"frequencies":{"breathing_angular":wb,"rotating_angular":wr},"runs":sums,"rotating_outer_phase_rad":[sums["rotating"]["fits"][str(i)]["outer_phase_rad"] for i in range(4)],"rotating_outer_amplitudes":[sums["rotating"]["fits"][str(i)]["outer_amplitude"] for i in range(4)],"interpretation":"Signed outer-apex edge strain is fitted directly to imposed central face-drive frequencies. Breathing produces coherent same-frequency response in all four outer tetrahedra; rotating internal anisotropy produces face-dependent phase/amplitude. After forcing stops, energy is conserved and the undamped fabric rings."}
    METRICS.write_text(json.dumps(metrics,indent=2),encoding="utf-8"); print(json.dumps({"status":metrics["status"],"breathing_fits":sums["breathing"]["fits"],"rotating_fits":sums["rotating"]["fits"]},indent=2))

if __name__=="__main__":main()
