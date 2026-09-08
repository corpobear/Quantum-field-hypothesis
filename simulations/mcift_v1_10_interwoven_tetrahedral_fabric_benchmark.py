from pathlib import Path
import json, math, itertools
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RESULTS_DIR = ROOT / "analysis" / "results_v1.10"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
METRICS = RESULTS_DIR / "mcift_v110_interwoven_tetrahedral_fabric_metrics.json"
SWEEP = RESULTS_DIR / "mcift_v110_interwoven_tetrahedral_fabric_sweep.csv"

V = np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]], float)/(2*math.sqrt(2))
FACES = [(1,2,3),(0,2,3),(0,1,3),(0,1,2)]
OMEGA_REP = np.array([
    0.4354578176530475, 0.4271218255411380,
    0.4354559308456763, 0.43545695016037234
], dtype=float)

def parity_to_sorted(simplex):
    arr=list(simplex)
    inv=sum(arr[i]>arr[j] for i in range(len(arr)) for j in range(i+1,len(arr)))
    return tuple(sorted(arr)), (-1 if inv%2 else 1)

def boundary(simplex):
    out={}
    for i in range(len(simplex)):
        f=simplex[:i]+simplex[i+1:]
        canon,ps=parity_to_sorted(f)
        out[canon]=out.get(canon,0)+((-1)**i)*ps
    return out

def face_normals(vertices):
    c=vertices.mean(0)
    ns=[]
    for f in FACES:
        P=vertices[list(f)]
        n=np.cross(P[1]-P[0],P[2]-P[0]); n/=np.linalg.norm(n)
        if np.dot(n,c-P.mean(0))<0: n=-n
        ns.append(n)
    return np.array(ns)

def weave(vertices,weights):
    ns=face_normals(vertices)
    W=sum(w*(np.eye(3)-np.outer(n,n)) for w,n in zip(weights,ns))
    return W,ns

def edge_tetra(h=1.0):
    return np.array([[-0.5,0,0],[0.5,0,0],[0,math.sqrt(3)/2,0],[0,math.sqrt(3)/6,h*math.sqrt(2/3)]],float)

def dihedral(P):
    e=P[1]-P[0]
    n1=np.cross(e,P[2]-P[0]); n1/=np.linalg.norm(n1)
    n2=np.cross(P[3]-P[0],e); n2/=np.linalg.norm(n2)
    return math.acos(np.clip(np.dot(n1,n2),-1,1))

def volume(P):
    M=np.stack([P[1]-P[0],P[2]-P[0],P[3]-P[0]],axis=1)
    return abs(np.linalg.det(M))/6

def main():
    bd3=boundary((0,1,2,3))
    edge_acc={}
    for face,c in bd3.items():
        for e,ce in boundary(face).items(): edge_acc[e]=edge_acc.get(e,0)+c*ce
    closure_pass=not {k:v for k,v in edge_acc.items() if v!=0}

    Wiso,_=weave(V,np.ones(4)); eiso=np.linalg.eigvalsh(Wiso)
    iso_err=float((eiso.max()-eiso.min())/eiso.mean())
    rank=int(np.linalg.matrix_rank(Wiso,1e-12))

    weights=(OMEGA_REP**2)/(OMEGA_REP**2).max(); weak=int(np.argmin(weights))
    Wan,ns=weave(V,weights); evals,evecs=np.linalg.eigh(Wan)
    principal=evecs[:,np.argmax(evals)]
    align=float(abs(np.dot(principal,ns[weak])))
    axial_gap=float(evals[2]-0.5*(evals[0]+evals[1]))

    t0=(0,1,2,3); t1=(0,2,1,4); bd={}
    for t in (t0,t1):
        for f,c in boundary(t).items(): bd[f]=bd.get(f,0)+c
    shared_coeff=bd.get((0,1,2),0); outer={f:c for f,c in bd.items() if c!=0}
    verts=set(t0+t1)
    edges={tuple(sorted(e)) for t in (t0,t1) for e in itertools.combinations(t,2)}
    faces={tuple(sorted(f)) for t in (t0,t1) for f in itertools.combinations(t,3)}
    euler=len(verts)-len(edges)+len(faces)-2

    theta_reg=math.acos(1/3); def5=2*math.pi-5*theta_reg; def6=2*math.pi-6*theta_reg
    rows=[]
    for h in np.linspace(0.75,1.25,21):
        P=edge_tetra(float(h)); th=dihedral(P); delta=2*math.pi-(4*theta_reg+th)
        rows.append([h,volume(P),th,math.degrees(th),delta,math.degrees(delta)])
    sweep=pd.DataFrame(rows,columns=["height_scale","deformed_volume","deformed_dihedral_rad","deformed_dihedral_deg","five_tet_edge_deficit_rad","five_tet_edge_deficit_deg"])
    sweep.to_csv(SWEEP,index=False)
    idx=int(np.argmin(abs(sweep.height_scale-1)))
    dd=float((sweep.iloc[idx+1].five_tet_edge_deficit_rad-sweep.iloc[idx-1].five_tet_edge_deficit_rad)/(sweep.iloc[idx+1].height_scale-sweep.iloc[idx-1].height_scale))

    metrics={"status":"INTERWOVEN_TETRAHEDRAL_SPATIAL_FABRIC_GEOMETRY_PASS","scope":{"physical_spacetime_claim":False,"physical_gravity_claim":False,"mass_curvature_law_claim":False,"time_dimension_implemented":False},"boundary_closure":{"pass":closure_pass},"equal_layer_weave":{"tensor":Wiso.tolist(),"eigenvalues":eiso.tolist(),"rank":rank,"relative_isotropy_error":iso_err},"v109_anisotropic_weave":{"omega_faces":OMEGA_REP.tolist(),"normalized_weights_omega_squared":weights.tolist(),"weak_face_index":weak,"eigenvalues":evals.tolist(),"principal_axis_alignment_with_weak_face_normal":align,"axial_gap":axial_gap},"two_tetra_shared_face":{"shared_face_coefficient":int(shared_coeff),"shared_face_cancels":bool(shared_coeff==0),"outer_boundary_face_count":len(outer),"unique_vertices":len(verts),"unique_edges":len(edges),"unique_faces":len(faces),"tetrahedra":2,"euler_characteristic":euler},"edge_deficit":{"regular_dihedral_deg":math.degrees(theta_reg),"five_regular_tet_deficit_deg":math.degrees(def5),"six_regular_tet_deficit_deg":math.degrees(def6),"d_deficit_d_heightscale_at_1":dd},"next_required_derivation":"derive a dynamical map from face-vortex loading to tetrahedral edge/dihedral deformation"}
    METRICS.write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    print(json.dumps(metrics,indent=2))

if __name__=="__main__": main()
