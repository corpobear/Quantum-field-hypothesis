import math

load = 0.009817928223
shear = 0.063915576742
beta4 = 0.170868625373

Gamma_SM = 4.07
mu_ZZ_CMS = 0.94
mu_ZZ_sigma = math.sqrt(0.07**2 + 0.09**2)
D_ATLAS = -0.537
D_ATLAS_sigma = math.sqrt(0.002**2 + 0.019**2)
D_CMS = -0.480
D_CMS_sigma = 0.0275

Gamma_model = Gamma_SM * (1.0 + load)
mu_inclusive_model = 1.0
mu_ZZ_resid = (mu_inclusive_model - mu_ZZ_CMS) / mu_ZZ_sigma

D_proxy = -(1.0 / 3.0 + beta4)
D_ATLAS_resid = (D_proxy - D_ATLAS) / D_ATLAS_sigma
D_CMS_resid = (D_proxy - D_CMS) / D_CMS_sigma

print("Gamma_model", Gamma_model)
print("mu_inclusive_model", mu_inclusive_model)
print("mu_ZZ_resid_sigma", mu_ZZ_resid)
print("D_proxy", D_proxy)
print("D_ATLAS_resid_sigma", D_ATLAS_resid)
print("D_CMS_resid_sigma", D_CMS_resid)
