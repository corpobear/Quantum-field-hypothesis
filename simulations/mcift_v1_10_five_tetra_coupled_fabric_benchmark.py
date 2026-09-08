from pathlib import Path
import json, math
import numpy as np
import pandas as pd
from scipy.optimize import minimize

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS_DIR = ROOT / "analysis" / "results_v1.10"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
METRICS = RESULTS_DIR / "mcift_v110_five_tetra_coupled_fabric_metrics.json"
SWEEP = RESULTS_DIR / "mcift_v110_five_tetra_coupled_fabric_sweep.csv"

C_TRI = 27.0 / 2800.0
K0 = 0.5
N = 5
A, B = 0, 1
RING = [2+i for i in range(N)]
EDGES = [(A,B)] + [(A,c) for c in RING] + [(B,c) for c in RING] + [(RING[i], RING[(i+1)%N]) for i in range(N)]
EDGES = [tuple(sorted(e)) for e in EDGES]
EDGE_INDEX = {e:i for i,e in enumerate(EDGES)}
TETS = [(A,B,RING[i],RING[(i+1)%N]) for i in range(N)]
FACES = []
for c in RING: FACES.append(tuple(sorted((A,B,c))))
for i in range(N):
    c0,c1=RING[i],RING[(i+1)%N]
    FACES += [tuple(sorted((A,c0,c1))),tuple(sorted((B,c0,c1)))]
FACES=sorted(set(FACES)); FACE_INDEX={f:i for i,f in enumerate(FACES)}

def edge_len(L,i,j): return L[EDGE_INDEX[tuple(sorted((i,j)))]]
def triangle_sides(L,face):
    i,j,k=face; return edge_len(L,i,j),edge_len(L,i,k),edge_len(L,j,k)
def triangle_area2(a,b,c): return (2*a*a*b*b+2*a*a*c*c+2*b*b*c*c-a**4-b**4-c**4)/16.0

def face_effective_energy(a,b,c,k):
    A2=triangle_area2(a,b,c)
    if A2<=1e-12: return 1e5+1e5*(1e-12-A2)**2
    area=math.sqrt(A2); Q=(a*a+b*b+c*c)/3.0; active=k-C_TRI*Q
    if active<=0: return 0.0
    return -0.25*area*active*active

def tetra_local_geometry(L,tet):
    a,b,c,d=tet
    l01=edge_len(L,a,b); l02=edge_len(L,a,c); l12=edge_len(L,b,c); l03=edge_len(L,a,d); l13=edge_len(L,b,d); l23=edge_len(L,c,d)
    if min(l01,l02,l12,l03,l13,l23)<=0: return False,0.0,float("nan")
    x2=(l02*l02+l01*l01-l12*l12)/(2*l01); y2sq=l02*l02-x2*x2
    if y2sq<=1e-12: return False,0.0,float("nan")
    y2=math.sqrt(y2sq); x3=(l03*l03+l01*l01-l13*l13)/(2*l01)
    dot23=(l02*l02+l03*l03-l23*l23)/2.0; y3=(dot23-x2*x3)/y2; z3sq=l03*l03-x3*x3-y3*y3
    if z3sq<=1e-12: return False,0.0,float("nan")
    z3=math.sqrt(z3sq); volume=l01*y2*z3/6.0
    theta=math.acos(max(-1.0,min(1.0,y3/math.sqrt(y3*y3+z3*z3))))
    return True,volume,theta

def objective(logL,face_k):
    L=np.exp(logL); E=0.0
    for face,k in zip(FACES,face_k): E+=face_effective_energy(*triangle_sides(L,face),k)
    for tet in TETS:
        ok,vol,_=tetra_local_geometry(L,tet)
        if not ok: E+=1e6
        elif vol<1e-4: E+=1e5*(1e-4-vol)**2
    return E

def solve(logL0,face_k,maxiter=1800):
    return minimize(objective,logL0,args=(face_k,),method="L-BFGS-B",options={"maxiter":maxiter,"ftol":1e-13,"gtol":1e-9,"maxls":50})

def face_omega(L,face,k):
    a,b,c=triangle_sides(L,face); Q=(a*a+b*b+c*c)/3.0
    return math.sqrt(max(k-C_TRI*Q,0.0))

def summarize(L,face_k):
    thetas=[]; vols=[]
    for tet in TETS:
        ok,vol,theta=tetra_local_geometry(L,tet)
        if not ok: raise RuntimeError("invalid tetrahedron")
        vols.append(vol); thetas.append(theta)
    return {"energy":objective(np.log(L),face_k),"common_edge":float(edge_len(L,A,B)),"A_spokes":[float(edge_len(L,A,c)) for c in RING],"B_spokes":[float(edge_len(L,B,c)) for c in RING],"ring_edges":[float(edge_len(L,RING[i],RING[(i+1)%N])) for i in range(N)],"tetra_volumes":[float(v) for v in vols],"common_edge_dihedrals_deg":[math.degrees(t) for t in thetas],"common_edge_deficit_deg":math.degrees(2*math.pi-sum(thetas)),"face_omegas":[float(face_omega(L,f,k)) for f,k in zip(FACES,face_k)],"edge_cv":float(np.std(L)/np.mean(L))}

def target_cell_faces(cell):
    t=TETS[cell]
    return [tuple(sorted(x)) for x in [(t[1],t[2],t[3]),(t[0],t[2],t[3]),(t[0],t[1],t[3]),(t[0],t[1],t[2])]]

def cell_edge_indices(cell):
    t=TETS[cell]
    return [EDGE_INDEX[tuple(sorted(e))] for e in [(t[0],t[1]),(t[0],t[2]),(t[0],t[3]),(t[1],t[2]),(t[1],t[3]),(t[2],t[3])]]
def circular_distance(i,j):
    d=abs(i-j); return min(d,N-d)

def main():
    L_regular=math.sqrt(K0/(3*C_TRI)); L0=np.full(len(EDGES),L_regular); uniform_k=np.full(len(FACES),K0)
    res0=solve(np.log(L0),uniform_k); L_eq=np.exp(res0.x); base=summarize(L_eq,uniform_k)
    rows=[{"load_delta":0.0,"target_cell":-1,"common_edge_deficit_deg":base["common_edge_deficit_deg"],"edge_cv":base["edge_cv"],"common_edge":base["common_edge"],"energy":base["energy"],"optimizer_success":bool(res0.success)}]
    localized={}; previous_log=np.log(L_eq)
    for delta in [0.02,0.05,0.10,0.20]:
        fk=uniform_k.copy()
        for f in target_cell_faces(0): fk[FACE_INDEX[f]]*=1.0+delta
        res=solve(previous_log,fk); L=np.exp(res.x); s=summarize(L,fk)
        base_thet=np.array(base["common_edge_dihedrals_deg"]); new_thet=np.array(s["common_edge_dihedrals_deg"]); cell_response=[]
        for ci in range(N):
            inds=cell_edge_indices(ci); rel=np.mean(np.abs(L[inds]-L_eq[inds])/L_eq[inds])
            cell_response.append({"cell":ci,"ring_distance_from_loaded_cell":circular_distance(ci,0),"mean_abs_relative_edge_change":float(rel),"common_edge_dihedral_change_deg":float(new_thet[ci]-base_thet[ci])})
        localized[str(delta)]={"optimizer_success":bool(res.success),"summary":s,"cell_response":cell_response,"loaded_faces":[list(f) for f in target_cell_faces(0)]}
        for cr in cell_response:
            rows.append({"load_delta":delta,"target_cell":0,"cell":cr["cell"],"ring_distance":cr["ring_distance_from_loaded_cell"],"mean_abs_relative_edge_change":cr["mean_abs_relative_edge_change"],"dihedral_change_deg":cr["common_edge_dihedral_change_deg"],"common_edge_deficit_deg":s["common_edge_deficit_deg"],"edge_cv":s["edge_cv"],"common_edge":s["common_edge"],"energy":s["energy"],"optimizer_success":bool(res.success)})
        previous_log=res.x
    pd.DataFrame(rows).to_csv(SWEEP,index=False)
    r10=localized["0.1"]["cell_response"]; by_dist={}
    for d in sorted(set(x["ring_distance_from_loaded_cell"] for x in r10)):
        by_dist[str(d)]=float(np.mean([x["mean_abs_relative_edge_change"] for x in r10 if x["ring_distance_from_loaded_cell"]==d]))
    metrics={"status":"COUPLED_FIVE_TETRA_FABRIC_RESPONDS_COLLECTIVELY_TO_LOCALIZED_LOADING","scope":{"physical_spacetime_claim":False,"physical_gravity_claim":False,"mass_curvature_calibration_claim":False,"time_dimension_implemented":False,"global_Euclidean_embedding_imposed":False,"shared_edge_lengths_enforced":True,"shared_triangular_layers_counted_once":True,"face_vortex_amplitudes_adiabatically_minimized":True},"topology":{"tetrahedra":N,"unique_vertices":7,"unique_edges":len(EDGES),"unique_faces":len(FACES),"common_edge":[A,B]},"regular_intrinsic_reference":{"isolated_regular_edge_length":L_regular,"five_regular_tet_common_edge_deficit_deg":360.0-5*math.degrees(math.acos(1/3))},"equal_loading_coupled_equilibrium":{"optimizer_success":bool(res0.success),**base},"localized_loading":localized,"propagation_10pct_mean_edge_response_by_ring_distance":by_dist,"interpretation":"Localized face-vortex loading changes shared edge lengths and dihedral angles in neighboring tetrahedra. This is a toy collective fabric response, not physical gravity."}
    METRICS.write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    print(json.dumps({"status":metrics["status"],"equal_loading":{"common_edge_deficit_deg":base["common_edge_deficit_deg"],"edge_cv":base["edge_cv"]},"localized_10pct":{"common_edge_deficit_deg":localized["0.1"]["summary"]["common_edge_deficit_deg"],"response_by_ring_distance":by_dist}},indent=2))

if __name__=="__main__": main()
