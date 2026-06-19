#!/usr/bin/env python3
"""MCIFT v0.58 3D real-data retest.
Reads v0.57 unified-field outputs and produces raw/transfer/calibrated comparison tables.
Speculative scaffold, not established physics.
"""
from pathlib import Path
import math
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
IN = ROOT / 'analysis' / 'results_v0.57'
OUT = ROOT / 'analysis' / 'results_v0.58'
OUT.mkdir(parents=True, exist_ok=True)

metrics = pd.read_csv(IN/'mcift_v0.57_unified_field_metrics.csv')
mdict = dict(zip(metrics.metric, metrics.value))
channels = pd.read_csv(IN/'mcift_v0.57_unified_field_channels.csv')
ch = dict(zip(channels.channel, channels.fraction))

SM = {
    'bb':0.582384276,
    'WW':0.213694230,
    'gg':0.0817977915,
    'tau':0.0626983071,
    'cc':0.028999217,
    'ZZ':0.0263992872,
    'gamma':0.00226993871,
    'Zgamma':0.00153995842,
    'mumu':0.000216994141,
}
raw = {k: float(ch.get(k, 0.0)) for k in SM}
rows = []
for k in SM:
    delta = (raw[k]-SM[k])/SM[k]*100
    k2 = raw[k]/SM[k]
    rows.append([k, SM[k], raw[k], delta, abs(delta), k2, math.sqrt(k2) if k2>=0 else np.nan, abs(delta)<=10])
cern = pd.DataFrame(rows, columns=['channel','BR_SM_ref','BR_raw_3d','delta_pct_raw_vs_SM','abs_delta_pct','kappa_eff_sq_raw','kappa_eff_raw','criterion_10pct'])
cern.to_csv(OUT/'mcift_v0.58_cern_channels.csv', index=False)

H0 = 67.4
Om_ref, Or_ref, Ol_ref = 0.315, 0.0, 0.685
def H(Om, Or, Ol, z):
    return H0 * math.sqrt(Om*(1+z)**3 + Or*(1+z)**4 + Ol)
visible = float(mdict['branch_visible_raw_fraction']); hidden = float(mdict['branch_hidden_raw_fraction'])
rot = float(mdict['branch_rotation_raw_fraction']); sound = float(mdict['branch_sound_raw_fraction']); rad = float(mdict['branch_radiation_raw_fraction'])
Om_raw = visible + hidden; Or_raw = rot + sound + rad; Ol_raw = 0.0
Om_t = float(mdict['Omega_m_like_today'])
Or_t = float(mdict['Omega_rotation_today']) + float(mdict['Omega_acoustic_today']) + float(mdict['Omega_radiation_today'])
Ol_t = float(mdict['Omega_smooth_lapse_reservoir_today'])
rows = []
for z in [0,0.25,0.5,0.75,1,1.5,2]:
    href = H(Om_ref, Or_ref, Ol_ref, z)
    hraw = H(Om_raw, Or_raw, Ol_raw, z)
    ht = H(Om_t, Or_t, Ol_t, z)
    rows.append([z, href, hraw, (hraw-href)/href*100, ht, (ht-href)/href*100])
pd.DataFrame(rows, columns=['z','H_planck_lcdm_ref','H_raw_3d_no_transfer','raw_delta_pct','H_3d_transfer','transfer_delta_pct']).to_csv(OUT/'mcift_v0.58_cosmology_Hz.csv', index=False)
print('wrote', OUT)
