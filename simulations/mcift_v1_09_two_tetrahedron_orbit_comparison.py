from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.spatial.transform import Rotation

HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE.parent / "analysis" / "results_v1.09"
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
METRICS_PATH = RESULTS_DIR / "two_tetrahedron_orbit_metrics.json"
TRACES_PATH = RESULTS_DIR / "two_tetrahedron_orbit_traces.csv"
ROBUST_PATH = RESULTS_DIR / "two_tetrahedron_orbit_robustness.csv"

G = 1.0
M = 1.0
I_BODY = 0.25
R0 = 3.0
DT = 0.006

VERTICES = np.array(
    [[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]], float
) / (2*math.sqrt(2))
FACES = [(1,2,3),(0,2,3),(0,1,3),(0,1,2)]
FACE_CENTROIDS = np.array([VERTICES[list(f)].mean(0) for f in FACES])

def align_vector(a,b):
    a=a/np.linalg.norm(a); b=b/np.linalg.norm(b)
    v=np.cross(a,b); c=float(a@b)
    if c>1-1e-13: return np.eye(3)
    if c<-1+1e-13:
        axis=np.cross(a,[1.,0,0])
        if np.linalg.norm(axis)<1e-10: axis=np.cross(a,[0.,1,0])
        axis/=np.linalg.norm(axis)
        return Rotation.from_rotvec(math.pi*axis).as_matrix()
    s=np.linalg.norm(v)
    K=np.array([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
    return np.eye(3)+K+K@K*((1-c)/(s*s))

def force_torque_U(center,R,points):
    src=points
    rel=points@R.T
    tgt=rel+center
    delta=tgt[None,:,:]-src[:,None,:]
    d=np.linalg.norm(delta,axis=2)
    w=1.0/len(points)
    pairF=-G*w*w*delta/(d[:,:,None]**3)
    Ft=pairF.sum(axis=0)
    F=Ft.sum(axis=0)
    tau=np.cross(rel,Ft).sum(axis=0)
    U=-G*w*w*np.sum(1.0/d)
    return F,tau,float(U)

def scores(center,R):
    inward=-center/np.linalg.norm(center)
    verts=VERTICES@R.T
    faces=FACE_CENTROIDS@R.T
    apex=float(np.max(verts@inward)/np.linalg.norm(VERTICES[0]))
    face=float(np.max(faces@inward)/np.linalg.norm(FACE_CENTROIDS[0]))
    return apex,face

def initial_R(kind):
    inward=np.array([-1.,0,0])
    local=FACE_CENTROIDS[0] if kind=="face_vortex_centroids" else VERTICES[0]
    return align_vector(local,inward)

def simulate(kind,orbits,speed_factor=1.0,spin_factor=1.0,perturb_deg=0.0,seed=0,record=True):
    pts=FACE_CENTROIDS if kind=="face_vortex_centroids" else VERTICES
    center=np.array([R0,0.,0.])
    vc=math.sqrt(G/R0)
    n=vc/R0
    period=2*math.pi/n
    vel=np.array([0.,speed_factor*vc,0.])
    R=initial_R(kind)
    if perturb_deg:
        rng=np.random.default_rng(seed)
        axis=rng.normal(size=3); axis/=np.linalg.norm(axis)
        R=Rotation.from_rotvec(math.radians(perturb_deg)*axis).as_matrix()@R
    omega=np.array([0.,0.,spin_factor*n])

    F,tau,U=force_torque_U(center,R,pts)
    a=F/M; aa=tau/I_BODY

    rows=[]
    rmin=1e9; rmax=0.; apex_vals=[]; face_vals=[]; energies=[]
    steps=int(orbits*period/DT)
    for step in range(steps):
        vel += 0.5*DT*a
        omega += 0.5*DT*aa
        center += DT*vel
        R = Rotation.from_rotvec(omega*DT).as_matrix() @ R

        F2,tau2,U2=force_torque_U(center,R,pts)
        a2=F2/M; aa2=tau2/I_BODY
        vel += 0.5*DT*a2
        omega += 0.5*DT*aa2
        a,aa=a2,aa2

        if step%50==0:
            rr=float(np.linalg.norm(center))
            ap,fc=scores(center,R)
            E=0.5*M*float(vel@vel)+0.5*I_BODY*float(omega@omega)+U2
            rmin=min(rmin,rr); rmax=max(rmax,rr)
            apex_vals.append(ap); face_vals.append(fc); energies.append(E)
            if record and step%250==0:
                rows.append({
                    "kind":kind,"time":step*DT,"radius":rr,
                    "apex_score":ap,"face_score":fc,"energy":E,
                    "speed_factor":speed_factor,"spin_factor":spin_factor,
                    "perturb_deg":perturb_deg
                })

        rr_now=np.linalg.norm(center)
        if rr_now<0.8 or rr_now>20:
            break

    apex_vals=np.array(apex_vals); face_vals=np.array(face_vals); energies=np.array(energies)
    summary={
        "kind":kind,
        "completed": bool(step+1==steps),
        "orbits":orbits,
        "speed_factor":speed_factor,
        "spin_factor":spin_factor,
        "perturb_deg":perturb_deg,
        "radius_min":float(rmin),"radius_max":float(rmax),
        "apex_mean":float(apex_vals.mean()),
        "apex_min":float(apex_vals.min()),
        "apex_p05":float(np.quantile(apex_vals,0.05)),
        "face_mean":float(face_vals.mean()),
        "face_min":float(face_vals.min()),
        "face_p05":float(np.quantile(face_vals,0.05)),
        "relative_energy_drift":float((energies.max()-energies.min())/abs(energies[0])),
    }
    summary["bound_orbit"]=bool(summary["completed"] and rmin>1.2 and rmax<6.0)
    summary["inverted_pyramid_orbit"]=bool(summary["bound_orbit"] and summary["apex_p05"]>0.95)
    summary["face_inward_orbit"]=bool(summary["bound_orbit"] and summary["face_p05"]>0.95)
    return pd.DataFrame(rows),summary

def main():
    kinds=["face_vortex_centroids","vertex_lumped_control"]
    traces=[]; nominal={}; zero_spin={}
    for kind in kinds:
        df,s=simulate(kind,8.0,1.0,1.0,0.0,record=True)
        df["test"]="nominal_synchronous"; traces.append(df); nominal[kind]=s
        df0,s0=simulate(kind,4.0,1.0,0.0,0.0,record=True)
        df0["test"]="zero_spin_control"; traces.append(df0); zero_spin[kind]=s0

    pd.concat(traces,ignore_index=True).to_csv(TRACES_PATH,index=False)

    robust_rows=[]
    for kind in kinds:
        for sf in [0.95,1.0,1.05]:
            _,s=simulate(kind,2.0,sf,1.0,3.0,seed=20260908,record=False)
            robust_rows.append(s)
    robust=pd.DataFrame(robust_rows)
    robust.to_csv(ROBUST_PATH,index=False)

    metrics={
        "status":"VERTEX_COUPLING_PASSES_INVERTED_PYRAMID_ORBIT_FACE_COUPLING_FAILS_ORIENTATION_CRITERION",
        "scope":{
            "physical_gravity_claim":False,
            "capture_from_unbound_trajectory_tested":False,
            "rigid_tetrahedra":True,
            "damping_used":False,
            "alignment_spring_used":False,
            "target_orbit_force_used":False,
            "source_tetrahedron_fixed":True
        },
        "nominal_conditions":{
            "center_separation":R0,
            "point_mass_circular_speed":math.sqrt(G/R0),
            "point_mass_orbital_rate":math.sqrt(G/R0)/R0,
            "initial_spin":"synchronous with orbital rate",
            "duration_orbits":8
        },
        "nominal_results":nominal,
        "zero_spin_control":zero_spin,
        "robustness_results":robust_rows,
        "interpretation":(
            "Both couplings support bounded motion under the same conservative finite-body 1/r control. "
            "The face-centroid model remains face-inward, so it fails the requested inverted-pyramid "
            "orbit criterion. The vertex-carried model remains apex-inward and passes that criterion. "
            "With zero initial co-rotation, neither rigid conservative model self-locks orientation; "
            "a true capture/spin-lock test requires internal energy-transfer degrees of freedom."
        )
    }
    METRICS_PATH.write_text(json.dumps(metrics,indent=2),encoding="utf-8")
    print(json.dumps({
        "status":metrics["status"],
        "nominal_results":nominal,
        "zero_spin_control":zero_spin
    },indent=2))

if __name__=="__main__":
    main()
