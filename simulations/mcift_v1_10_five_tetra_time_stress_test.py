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
METRICS = RESULTS_DIR / "mcift_v110_five_tetra_time_stress_metrics.json"
TRACE = RESULTS_DIR / "mcift_v110_five_tetra_time_stress_trace.csv"
ARRIVALS = RESULTS_DIR / "mcift_v110_five_tetra_time_stress_arrivals.csv"

C = 27.0/2800.0
K = 0.5
N = 5
A, B = 0, 1
RING = [2+i for i in range(N)]
EDGES = [(A,B)] + [(A,c) for c in RING] + [(B,c) for c in RING] + [(RING[i],RING[(i+1)%N]) for i in range(N)]
EDGES = [tuple(sorted(e)) for e in EDGES]
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
TETS = [(A,B,RING[i],RING[(i+1)%N]) for i in range(N)]
FACES = [tuple(sorted((A,B,c))) for c in RING]
for i in range(N):
    c0,c1=RING[i],RING[(i+1)%N]
    FACES += [tuple(sorted((A,c0,c1))),tuple(sorted((B,c0,c1)))]
FACES=sorted(set(FACES))
FACE_EDGE_IDX=torch.tensor([[EDGE_INDEX[tuple(sorted((i,j)))],EDGE_INDEX[tuple(sorted((i,k)))],EDGE_INDEX[tuple(sorted((j,k)))]] for i,j,k in FACES],dtype=torch.long)
L0=math.sqrt(K/(3*C)); q0=torch.full((len(EDGES),),math.log(L0))

def potential(q):
    L=torch.exp(q); s=L[FACE_EDGE_IDX]; a,b,c=s[:,0],s[:,1],s[:,2]
    A2=(2*a*a*b*b+2*a*a*c*c+2*b*b*c*c-a**4-b**4-c**4)/16.0
    area=torch.sqrt(torch.clamp(A2,min=1e-14)); Q=(a*a+b*b+c*c)/3.0
    return torch.sum(-0.25*area*(K-C*Q)**2)

def grad_potential(q):
    qv=q.detach().clone().requires_grad_(True); U=potential(qv); (g,)=torch.autograd.grad(U,qv)
    return g.detach(),float(U.detach())

def hessian_at(q):
    qv=q.detach().clone().requires_grad_(True)
    return torch.autograd.functional.hessian(potential,qv).detach().numpy()

def tet_volume_from_lengths(L,tet):
    a,b,c,d=tet
    el=lambda i,j: float(L[EDGE_INDEX[tuple(sorted((i,j)))]]); l01=el(a,b); l02=el(a,c); l12=el(b,c); l03=el(a,d); l13=el(b,d); l23=el(c,d)
    x2=(l02*l02+l01*l01-l12*l12)/(2*l01); y2sq=l02*l02-x2*x2
    if y2sq<=0:return 0.0
    y2=math.sqrt(y2sq); x3=(l03*l03+l01*l01-l13*l13)/(2*l01); dot23=(l02*l02+l03*l03-l23*l23)/2; y3=(dot23-x2*x3)/y2; z3sq=l03*l03-x3*x3-y3*y3
    if z3sq<=0:return 0.0
    return l01*y2*math.sqrt(z3sq)/6

def cell_edge_ids(ci):
    t=TETS[ci]
    return [EDGE_INDEX[tuple(sorted(e))] for e in [(t[0],t[1]),(t[0],t[2]),(t[0],t[3]),(t[1],t[2]),(t[1],t[3]),(t[2],t[3])]]
CELL_EDGE_IDS=[cell_edge_ids(i) for i in range(N)]
def ring_distance(i,j=0):
    d=abs(i-j); return min(d,N-d)
def local_impulse_vector():
    v=np.zeros(len(EDGES)); t=TETS[0]
    local_edges=[tuple(sorted((A,t[2]))),tuple(sorted((A,t[3]))),tuple(sorted((B,t[2]))),tuple(sorted((B,t[3]))),tuple(sorted((t[2],t[3])))]
    for e,s in zip(local_edges,[1,-1,1,-1,0]): v[EDGE_INDEX[e]]=s
    return v/np.linalg.norm(v)

def simulate(amplitude,periods=18.0):
    H=hessian_at(q0); eig=np.linalg.eigvalsh(H); pos=eig[eig>1e-10]; wmax=math.sqrt(pos.max()); wmin=math.sqrt(pos.min())
    dt=min(0.01,0.04/wmax); Tsoft=2*math.pi/wmin; steps=int(periods*Tsoft/dt)
    q=q0.detach().clone(); v=torch.tensor(amplitude*local_impulse_vector(),dtype=torch.float64); g,U=grad_potential(q); a=-g
    qeq=q0.detach().numpy(); records=[]; peak=np.zeros(N); first=[None]*N; threshold=5e-4; E0=0.5*float(v@v)+U; Emin=Emax=E0; minvol=1e99; maxstrain=0.0; rec=max(1,steps//2500)
    for step in range(steps):
        v+=0.5*dt*a; q+=dt*v; g2,U2=grad_potential(q); a2=-g2; v+=0.5*dt*a2; a=a2
        if step%5==0:
            qn=q.detach().numpy(); Ln=np.exp(qn); strains=[]
            for ci,ids in enumerate(CELL_EDGE_IDS):
                s=float(np.mean(np.abs(qn[ids]-qeq[ids]))); strains.append(s); peak[ci]=max(peak[ci],s)
                if first[ci] is None and s>=threshold:first[ci]=step*dt
            vols=[tet_volume_from_lengths(Ln,t) for t in TETS]; minvol=min(minvol,min(vols)); maxstrain=max(maxstrain,float(np.max(np.abs(qn-qeq))))
            E=0.5*float(v@v)+U2; Emin=min(Emin,E); Emax=max(Emax,E)
            if step%rec==0:
                row={"time":step*dt,"energy":E,"min_tetra_volume":min(vols),"max_abs_log_edge_strain":float(np.max(np.abs(qn-qeq)))}
                for ci,s in enumerate(strains):row[f"cell_{ci}_mean_abs_log_edge_strain"]=s
                records.append(row)
        if minvol<=0:break
    arrivals=[{"amplitude":amplitude,"cell":ci,"ring_distance":ring_distance(ci),"arrival_time":first[ci],"peak_mean_abs_log_edge_strain":float(peak[ci])} for ci in range(N)]
    return pd.DataFrame(records),{"amplitude":amplitude,"completed":bool(step+1==steps),"dt":dt,"duration":step*dt,"softest_frequency":wmin,"fastest_frequency":wmax,"softest_period":Tsoft,"hessian_min_eigenvalue":float(eig.min()),"hessian_positive_count":int((eig>1e-10).sum()),"hessian_zero_count":int((np.abs(eig)<=1e-10).sum()),"hessian_negative_count":int((eig<-1e-10).sum()),"relative_energy_band":float((Emax-Emin)/max(abs(E0),1e-15)),"minimum_tetra_volume":float(minvol),"max_abs_log_edge_strain":float(maxstrain),"arrival_threshold":threshold,"arrivals":arrivals},H

def main():
    amps=[0.0025,0.005,0.01,0.02]; traces=[]; summaries={}; arrivals=[]; H=None
    for amp in amps:
        df,s,H=simulate(amp); df["amplitude"]=amp; traces.append(df); summaries[str(amp)]=s; arrivals.extend(s["arrivals"])
    pd.concat(traces,ignore_index=True).to_csv(TRACE,index=False); pd.DataFrame(arrivals).to_csv(ARRIVALS,index=False)
    primary=summaries["0.01"]; bydist={}
    for d in [0,1,2]:
        vals=[x["arrival_time"] for x in primary["arrivals"] if x["ring_distance"]==d and x["arrival_time"] is not None]; bydist[str(d)]=float(np.mean(vals)) if vals else None
    finite=all(bydist[str(d)] is not None for d in [0,1,2]) and bydist["0"]<bydist["1"]<bydist["2"]
    metrics={"status":"UNDAMPED_SHARED_EDGE_DYNAMICS_STABLE_WITH_FINITE_ORDERED_RESPONSE" if finite else "UNDAMPED_SHARED_EDGE_DYNAMICS_RUN_RESPONSE_ORDER_NOT_STRICTLY_FINITE","scope":{"physical_time_claim":False,"physical_signal_speed_claim":False,"physical_gravity_claim":False,"unit_edge_inertia_normalization":True,"damping_used":False,"global_reoptimization_used":False,"external_force_after_t0":False,"face_vortices_adiabatically_eliminated":True},"equilibrium":{"edge_count":len(EDGES),"tetra_count":N,"regular_edge_length":L0,"unit_inertia_hessian_eigenvalues":np.linalg.eigvalsh(H).tolist()},"stress_runs":summaries,"primary_1pct_impulse":{"mean_arrival_time_by_ring_distance":bydist,"strict_topological_arrival_order":finite},"interpretation":"A localized initial velocity impulse is applied only at t=0; shared-edge coordinates then evolve conservatively under the intrinsic face energy. Unit edge inertia defines normalized toy time only."}
    METRICS.write_text(json.dumps(metrics,indent=2),encoding="utf-8"); print(json.dumps({"status":metrics["status"],"primary_1pct_impulse":metrics["primary_1pct_impulse"]},indent=2))

if __name__=="__main__":main()
