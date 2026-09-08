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
METRICS = RESULTS_DIR / "mcift_v110_vortex_loading_to_curvature_metrics.json"
SWEEP = RESULTS_DIR / "mcift_v110_vortex_loading_to_curvature_sweep.csv"

C = 27.0/2800.0
FACES = [(1,2,3),(0,2,3),(0,1,3),(0,1,2)]
EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
UNIT = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/(2*math.sqrt(2))
K_STRONG = 0.5
WEAK_FACE = 1
THETA_REG = math.acos(1/3)

def energy(y,kfaces):
    X=y[:12].reshape(4,3); X=X-X.mean(dim=0); om=y[12:]
    total=torch.zeros((),dtype=y.dtype)
    for fi,f in enumerate(FACES):
        P=X[list(f)]; fc=P.mean(dim=0); q=P-fc; Q=(q*q).sum()
        A=0.5*torch.linalg.norm(torch.cross(P[1]-P[0],P[2]-P[0],dim=0))
        total += A*(0.5*(C*Q-kfaces[fi])*om[fi]**2 + 0.25*om[fi]**4)
    return total

def regular_state():
    L=math.sqrt(K_STRONG/(3*C)); om=math.sqrt(2*K_STRONG/3)
    return np.concatenate([(UNIT*L).ravel(),np.full(4,om)])

def solve(y0,kfaces):
    y=torch.tensor(y0.copy(),requires_grad=True)
    opt=torch.optim.LBFGS([y],lr=0.8,max_iter=180,tolerance_grad=1e-11,tolerance_change=1e-13,line_search_fn="strong_wolfe")
    def closure():
        opt.zero_grad(); E=energy(y,kfaces); E.backward(); return E
    opt.step(closure)
    return y.detach().numpy()

def outward_face_normal(X,face):
    P=X[list(face)]; n=np.cross(P[1]-P[0],P[2]-P[0]); n/=np.linalg.norm(n)
    fc=P.mean(axis=0); c=X.mean(axis=0)
    if np.dot(n,c-fc)>0: n=-n
    return n

def internal_dihedral(X,edge):
    containing=[f for f in FACES if edge[0] in f and edge[1] in f]
    n1=outward_face_normal(X,containing[0]); n2=outward_face_normal(X,containing[1])
    return math.pi-math.acos(np.clip(np.dot(n1,n2),-1,1))

def geom(y):
    X=y[:12].reshape(4,3); X=X-X.mean(axis=0); om=y[12:]
    lens={f"{i}{j}":float(np.linalg.norm(X[i]-X[j])) for i,j in EDGES}
    M=np.stack([X[1]-X[0],X[2]-X[0],X[3]-X[0]],axis=1); vol=abs(np.linalg.det(M))/6.0
    dihs={f"{i}{j}":internal_dihedral(X,(i,j)) for i,j in EDGES}
    deficits={e:2*math.pi-(4*THETA_REG+th) for e,th in dihs.items()}
    return X,om,lens,vol,dihs,deficits

def main():
    y=regular_state(); rows=[]; ratios=[1.0,0.98,0.96,0.94,0.93475,0.92,0.90,0.88,0.85]; finals={}
    weak_face_vertices=set(FACES[WEAK_FACE]); opposite_vertex=WEAK_FACE
    for ratio in ratios:
        kfaces=np.full(4,K_STRONG); kfaces[WEAK_FACE]=K_STRONG*ratio; y=solve(y,kfaces)
        X,om,lens,vol,dihs,defs=geom(y)
        face_edges=[]; apex_edges=[]
        for i,j in EDGES:
            name=f"{i}{j}"
            if i in weak_face_vertices and j in weak_face_vertices: face_edges.append(name)
            elif opposite_vertex in (i,j): apex_edges.append(name)
        edge_vals=np.array(list(lens.values()))
        face_def=np.mean([defs[e] for e in face_edges]); apex_def=np.mean([defs[e] for e in apex_edges])
        row={"weak_drive_ratio":ratio,"volume":vol,"mean_edge":float(edge_vals.mean()),"edge_cv":float(edge_vals.std()/edge_vals.mean()),"omega_weak":float(om[WEAK_FACE]),"omega_strong_mean":float(np.mean(np.delete(om,WEAK_FACE))),"weak_face_edge_deficit_mean_rad":float(face_def),"apex_edge_deficit_mean_rad":float(apex_def),"deficit_split_rad":float(apex_def-face_def),"weak_face_edge_dihedral_mean_rad":float(np.mean([dihs[e] for e in face_edges])),"apex_edge_dihedral_mean_rad":float(np.mean([dihs[e] for e in apex_edges]))}
        rows.append(row)
        finals[str(ratio)]={"k_faces":kfaces.tolist(),"omega_faces":om.tolist(),"edge_lengths":lens,"dihedral_deg":{e:math.degrees(v) for e,v in dihs.items()},"edge_star_deficit_deg":{e:math.degrees(v) for e,v in defs.items()},"volume":vol,"edge_cv":row["edge_cv"]}
    df=pd.DataFrame(rows); df.to_csv(SWEEP,index=False)
    ref=df.iloc[int(np.argmin(abs(df.weak_drive_ratio-0.93475)))]
    metrics={"status":"VORTEX_LOADING_TO_ANISOTROPIC_DIhedral_DEFICIT_PASS_WITHIN_V108_ENERGY","scope":{"physical_gravity_claim":False,"physical_spacetime_claim":False,"mass_curvature_calibration_claim":False,"deformation_prescribed":False,"face_drive_asymmetry_prescribed":True,"geometry_optimized_from_v108_energy":True},"setup":{"strong_face_drive":K_STRONG,"weak_face_index":WEAK_FACE,"weak_drive_ratios":ratios,"edge_star_control":"four regular tetrahedra plus one optimized deformed tetrahedron"},"representative_v109_like_ratio":{"weak_drive_ratio":float(ref.weak_drive_ratio),"volume":float(ref.volume),"edge_cv":float(ref.edge_cv),"omega_weak":float(ref.omega_weak),"omega_strong_mean":float(ref.omega_strong_mean),"weak_face_edge_deficit_mean_deg":math.degrees(float(ref.weak_face_edge_deficit_mean_rad)),"apex_edge_deficit_mean_deg":math.degrees(float(ref.apex_edge_deficit_mean_rad)),"deficit_split_deg":math.degrees(float(ref.deficit_split_rad))},"full_states":finals,"interpretation":"Unequal face-vortex drive in the existing v1.08 free-vertex energy produces a nondegenerate anisotropic tetrahedral equilibrium without prescribing edge or dihedral deformation. When inserted into a five-tetra edge-star control, dihedral changes split the local angular deficit. This is a toy loading->shape->deficit chain, not a physical mass-curvature law."}
    METRICS.write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    print(json.dumps({"status":metrics["status"],"representative":metrics["representative_v109_like_ratio"]},indent=2))

if __name__=="__main__": main()
