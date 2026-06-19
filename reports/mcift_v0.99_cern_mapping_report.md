# MCIFT v0.99 CERN Mapping Test

**Status:** first CERN/collider mapping test from the v0.97 shared threefold reducer. This is not a full CERN validation.

## 1. Inputs from v0.97

```text
load_proxy = 0.009817928223
mean_shear_proxy = 0.063915576742
beta4_needed_for_balance = 0.170868625373
```

## 2. CERN anchors used

```text
SM Higgs width reference = 4.07 MeV
CMS H to ZZ signal strength = 0.94 +/- 0.114 combined
ATLAS top entanglement D = -0.537 +/- 0.0191 combined
CMS top entanglement D = -0.480 +/- 0.0275 approx symmetric
```

The top-entanglement values are direct ATLAS/CMS measurements. The Higgs width value is used here as a Standard Model reference, not as a direct experimental-width score.

## 3. Mapping rules

Higgs width proxy:

```text
Gamma_model = Gamma_SM * (1 + load_proxy)
```

Inclusive signal strength proxy:

```text
mu_inclusive_model = mean_A3 = 1
```

Top entanglement proxy:

```text
D_proxy = -(1/3 + beta4_needed_for_balance)
```

The `-1/3` term is the entanglement threshold used in the top-pair D observable. The v0.97 central-loop balance term supplies the excess entanglement depth.

## 4. Results

```text
Gamma_model = 4.109958967868 MeV
mu_inclusive_model = 1.000000000000
CMS HZZ residual = 0.526 sigma
D_proxy = -0.504201958707
ATLAS D residual = 1.717 sigma
CMS D residual = -0.880 sigma
```

## 5. Interpretation

The Higgs-width proxy is close to the SM reference but is not scored as an experimental pass.

The inclusive H to ZZ signal-strength proxy is compatible with the CMS value at this coarse level.

The top entanglement proxy lands between the ATLAS and CMS central values. It is closer to CMS than ATLAS in this first mapping.

## 6. What is not done

Detailed Higgs branching ratios are not scored.

Channel-by-channel signal strengths are not scored.

Detector-level event shapes are not scored.

This is a first collider mapping from the shared v0.97 reduced quantities, not a full CERN validation.

## 7. Next

Either build channel-specific Higgs rules from the same reduced quantities, or create the v1.00 joint scorecard that places v0.98 cosmology and v0.99 CERN side by side with clear labels.
