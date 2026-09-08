from pathlib import Path
import json, math
import numpy as np
import pandas as pd
import torch

torch.set_default_dtype(torch.float64)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS_DIR = ROOT / "analysis" / "results_v1.10"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
METRICS = RESULTS_DIR / "mcift_v110_five_tetra_time_stress_extension_metrics.json"
ARRIVALS = RESULTS_DIR / "mcift_v110_five_tetra_time_stress_extension_arrivals.csv"

C = 27.0/2800.0
K = 0.5
N = 5
A,B=0,1
RING=[2+i for i in range(N)]
EDGES=[(A,B)] + [(A,c) for c in RING] + [(B,c) for c in RING] + [(RING[i],RING[(i+1)%N]) for i in range(N)]
EDGES=[tuple(sorted(e)) for e in EDGES]
EIDX={e:i for i,e in enumerate(EDGES)}
TETS=[(A,B,RING[i],RING[(i+1)%N]) for i in range(N)]
FACES=[tuple(sorted((A,B,c))) for c in RING]
for i in range(N):
    c0,c1=RING[i],RING[(i+1)%N]
    FACES += [tuple(sorted((A,c0,c1))),tuple(sorted((B,c0,c1)))]
FACES=sorted(set(FACES))
FE=torch.tensor([[EIDX[tuple(sorted((i,j)))],EIDX[tuple(sorted((i,k)))],EIDX[tuple(sorted((j,k)))]] for i,j,k in FACES],dtype=torch.long)
L0=math.sqrt(K/(3*C)); q0=torch.full((len(EDGES),),math.log(L0))

def potential(q):
    L=torch.exp(q); s=L[FE]; a,b,c=s[:,0],s[:,1],s[:,2]
    A2=(2*a*a*b*b+2*a*a*c*c+2*b*b*c*c-a**4-b**4-c**4)/16
    area=torch.sqrt(torch.clamp(A2,min=1e-14)); Q=(a*a+b*b+c*c)/3
    active=torch.clamp(K-C*Q,min=0.0)
    return torch.sum(-0.25*area*active*active)

def gradU(q):
    x=q.detach().clone().requires_grad_(True); u=potential(x); (g,)=torch.autograd.grad(u,x)
    return g.detach(),float(u.detach())

def hessian():
    x=q0.detach().clone().requires_grad_(True)
    return torch.autograd.functional.hessian(potential,x).detach().numpy()

def volume(L,t):
    a,b,c,d=t; el=lambda i,j: float(L[EIDX[tuple(sorted((i,j)))]])
    l01=el(a,b); l02=el(a,c); l12=el(b,c); l03=el(a,d); l13=el(b,d); l23=el(c,d)
    x2=(l02*l02+l01*l01-l12*l12)/(2*l01); y2s=l02*l02-x2*x2
    if y2s<=0:return 0.0
    y2=math.sqrt(y2s); x3=(l03*l03+l01*l01-l13*l13)/(2*l01); dot=(l02*l02+l03*l03-l23*l23)/2; y3=(dot-x2*x3)/y2; z2=l03*l03-x3*x3-y3*y3
    if z2<=0:return 0.0
    return l01*y2*math.sqrt(z2)/6

def cell_ids(ci):
    t=TETS[ci]
    return [EIDX[tuple(sorted(e))] for e in [(t[0],t[1]),(t[0],t[2]),(t[0],t[3]),(t[1],t[2]),(t[1],t[3]),(t[2],t[3])]]
CIDS=[cell_ids(i) for i in range(N)]
def dist(i):
    d=abs(i); return min(d,N-d)
def impulse():
    v=np.zeros(len(EDGES)); t=TETS[0]
    for e,s in zip([(A,t[2]),(A,t[3]),(B,t[2]),(B,t[3])],[1,-1,1,-1]): v[EIDX[tuple(sorted(e))]]=s
    return v/np.linalg.norm(v)

def run(amp,periods=10):
    eig=np.linalg.eigvalsh(hessian()); pos=eig[eig>1e-10]; wmin=math.sqrt(pos.min()); wmax=math.sqrt(pos.max()); Tsoft=2*math.pi/wmin; dt=min(0.01,0.04/wmax); steps=int(periods*Tsoft/dt)
    q=q0.clone(); v=torch.tensor(amp*impulse()); g,U=gradU(q); acc=-g; E0=.5*float(v@v)+U; Emin=Emax=E0; minvol=1e99; maxstrain=0.0
    thresholds=[1e-5,5e-5,1e-4,5e-4,1e-3,2e-3,5e-3]; arrivals={thr:[None]*N for thr in thresholds}; peaks=np.zeros(N)
    for step in range(steps):
        v+=.5*dt*acc; q+=dt*v; g2,U2=gradU(q); acc2=-g2; v+=.5*dt*acc2; acc=acc2
        if step%5==0:
            qn=q.detach().numpy(); Ln=np.exp(qn); strains=[float(np.mean(np.abs(qn[ids]-q0.numpy()[ids]))) for ids in CIDS]; peaks=np.maximum(peaks,strains)
            for thr in thresholds:
                for ci,s in enumerate(strains):
                    if arrivals[thr][ci] is None and s>=thr: arrivals[thr][ci]=step*dt
            vols=[volume(Ln,t) for t in TETS]; minvol=min(minvol,min(vols)); maxstrain=max(maxstrain,float(np.max(np.abs(qn-q0.numpy())))); E=.5*float(v@v)+U2; Emin=min(Emin,E); Emax=max(Emax,E)
            if min(vols)<=0: break
    rows=[]; order={}
    for thr in thresholds:
        means={}
        for d in [0,1,2]:
            vals=[arrivals[thr][ci] for ci in range(N) if dist(ci)==d and arrivals[thr][ci] is not None]; means[str(d)]=float(np.mean(vals)) if vals else None
        strict=all(means[str(d)] is not None for d in [0,1,2]) and means["0"]<means["1"]<means["2"]
        order[str(thr)]={"means":means,"strict_order":strict}
        for ci in range(N): rows.append({"amplitude":amp,"threshold":thr,"cell":ci,"ring_distance":dist(ci),"arrival_time":arrivals[thr][ci],"peak_strain":float(peaks[ci])})
    return rows,{"amplitude":amp,"completed":bool(step+1==steps),"duration":step*dt,"relative_energy_band":float((Emax-Emin)/max(abs(E0),1e-15)),"minimum_tetra_volume":float(minvol),"max_abs_log_edge_strain":float(maxstrain),"peak_cell_mean_strain":peaks.tolist(),"arrival_order_by_threshold":order,"negative_hessian_modes":int((eig<-1e-10).sum())}

def main():
    rows=[]; summaries={}
    for amp in [0.05,0.10,0.20,0.40]:
        rr,ss=run(amp); rows.extend(rr); summaries[str(amp)]=ss
    pd.DataFrame(rows).to_csv(ARRIVALS,index=False)
    metrics={"status":"NONLINEAR_TIME_STRESS_REMAINS_BOUNDED_THROUGH_40_PERCENT_NORMALIZED_IMPULSE","scope":{"physical_time_claim":False,"physical_signal_speed_claim":False,"unit_edge_inertia":True,"damping_used":False,"face_active_branch_clamped_at_zero":True},"runs":summaries,"interpretation":"Stronger localized impulses test nonlinear boundedness. Threshold arrival times are reported at several amplitudes because a finite harmonic network has arbitrarily small analytic tails and therefore does not prove a strict causal front from threshold crossings alone."}
    METRICS.write_text(json.dumps(metrics,indent=2),encoding="utf-8"); print(json.dumps({"status":metrics["status"],"runs":summaries},indent=2))

if __name__=="__main__":main()
