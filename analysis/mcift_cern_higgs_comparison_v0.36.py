#!/usr/bin/env python3
"""Regenerate MCIFT v0.36 CERN/LHC Higgs comparison tables.

Speculative scaffold. This is not a quantitative CERN/LHC pass.
"""
import math
from pathlib import Path
import pandas as pd

OUT = Path('analysis/results_v0.36')
OUT.mkdir(parents=True, exist_ok=True)

ideal_chi = 1.0
chi_c = 1 / math.sqrt(2)
sigma = 0.5 * (1 + math.tanh(6.0 * (ideal_chi - chi_c)))
ideal_mass_proxy = 6 * sigma
m_scale = 125.04 / ideal_mass_proxy

rows = [
    ['identity','scalar spin-parity Jp','0plus scalar alternatives disfavored','STRUCTURAL_PASS','balanced cube-center six-face vortex is scalar under cubic-average projection','no','structural only'],
    ['identity','neutral colorless excitation','Higgs is neutral and colorless in SM interpretation','STRUCTURAL_PASS','face-plane scalar response has no charge or color labels','no','needs gauge-channel implementation'],
    ['mass','Higgs boson mass','125.04 plusminus 0.12 GeV','CALIBRATION_REQUIRED',f'ideal proxy {ideal_mass_proxy:.6f}; calibrated m_scale {m_scale:.6f} GeV','calibrated','not independent prediction'],
    ['width','total width','3.0 plus2.0 minus1.5 MeV; SM about 4.1 MeV','NOT_IMPLEMENTED','no partial-width solver','no','major missing piece'],
    ['couplings','coupling hierarchy','W Z gluons photons top bottom tau observed; muon evidence emerging','WEAK_QUALITATIVE','mass-response idea can represent hierarchy but does not predict kappa values','no','needs Yukawa/gauge map'],
    ['rates','global signal strength','Run1 mu 1.09 plusminus 0.11; ATLAS Run2 mu 1.11 plus0.09 minus0.08','NOT_IMPLEMENTED','no production times branching likelihood','no','cannot claim rate agreement'],
    ['production','ggF VBF VH ttH','measured by LHC combinations','NOT_IMPLEMENTED','no QCD or VBF production solver','no','major missing bridge'],
    ['decay','ZZ WW gammagamma tautau bb mumu','included in LHC Higgs combinations','NOT_IMPLEMENTED','no branching fraction model','no','needs decay map'],
    ['beyond_SM','SM consistency','measurements broadly consistent with SM','CONSTRAINED','MCIFT collider limit must reduce to SM-like behavior','no','deviations must be small'],
]

pd.DataFrame(rows, columns=['sector','observable','cern_target','mcift_status','mcift_result','quantitative','notes']).to_csv(OUT/'mcift_v0.36_cern_higgs_comparison_metrics.csv', index=False)
pd.DataFrame([{
    'version':'v0.36',
    'name':'CERN LHC Higgs-sector comparison',
    'overall_verdict':'STRUCTURAL_ONLY_NOT_A_CERN_PASS',
    'structural_passes':2,
    'weak_qualitative':1,
    'calibration_required':1,
    'not_implemented':4,
    'constrained':1,
    'ideal_mass_proxy':ideal_mass_proxy,
    'm_scale_calibrated_GeV':m_scale,
}]).to_csv(OUT/'mcift_v0.36_cern_higgs_summary.csv', index=False)
print('v0.36 CERN/Higgs comparison regenerated')
