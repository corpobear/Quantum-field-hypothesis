H_proxy = 0.977215138494
shear = 0.063915576742

H0_planck = 67.36
sig_H0_planck = 0.54
H0_shoes = 73.04
sig_H0_shoes = 1.04

S8_planck = 0.832
S8_des = 0.776
sig_S8_des = 0.017

H0_norm = H0_planck / H_proxy
H0_early_model = H0_norm * H_proxy
H0_local_model = H0_early_model * (1.0 + shear)
H0_local_resid = (H0_local_model - H0_shoes) / sig_H0_shoes

S8_late_model = S8_planck * (1.0 - shear)
S8_late_resid = (S8_late_model - S8_des) / sig_S8_des

print("H0_norm", H0_norm)
print("H0_early_model", H0_early_model)
print("H0_local_model", H0_local_model)
print("H0_local_resid_sigma", H0_local_resid)
print("S8_late_model", S8_late_model)
print("S8_late_resid_sigma", S8_late_resid)
