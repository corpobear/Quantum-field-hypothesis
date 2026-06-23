# Bubble Inflation Upscaler

**Status:** experimental image-processing application inspired by MCIFT reducer math.

Bubble Inflation Upscaler is a practical, tunable image enlargement script. It starts with ordinary high-quality interpolation, then applies a bubble-style radial inflation field, optional threefold modulation, local detail boosting, sharpening, and optional grain.

It does **not** claim to reconstruct lost ground-truth detail. It creates configurable enhancement layers that may be useful for visual upscaling experiments.

## Install

From the repository root:

```bash
python -m pip install -r applications/image_upscaling/requirements.txt
```

## Basic usage

```bash
python applications/image_upscaling/bubble_inflation_upscaler.py \
  input.png \
  output.png \
  --scale 4 \
  --preset applications/image_upscaling/presets/balanced.json \
  --compare \
  --save-debug debug/bubble_upscale
```

This writes:

```text
output.png                         final image
output_compare.png                 base interpolation beside final output
debug/bubble_upscale/*.png         intermediate layers
debug/bubble_upscale/config.json   merged run configuration
```

## Presets

```text
presets/gentle.json       mild inflation and sharpening
presets/balanced.json     default practical starting point
presets/aggressive.json   stronger bubble/detail/sharpening pass
```

A preset can be overridden from the command line:

```bash
python applications/image_upscaling/bubble_inflation_upscaler.py input.png output.png \
  --preset applications/image_upscaling/presets/balanced.json \
  --scale 3 \
  --bubble-strength 0.22 \
  --edge-boost 0.4 \
  --sharpen-amount 0.5
```

## Main parameters

```text
scale              final size multiplier, e.g. 2, 3, 4
resample           nearest, bilinear, bicubic, lanczos
bubble_strength    radial inflation strength; positive expands from center
bubble_radius      radius of the virtual bubble in normalized image units
bubble_falloff     how quickly the bubble fades toward its edge
center_x           bubble center x, 0.0 left to 1.0 right
center_y           bubble center y, 0.0 top to 1.0 bottom
threefold          enable/disable MCIFT-style threefold modulation
epsilon3           strength of the threefold modulation
psi3               phase offset of the threefold pattern
denoise_radius     optional blur before detail extraction
detail_strength    amount of local high-frequency detail added back
edge_boost         extra detail gain on detected edges
edge_threshold     edge mask threshold
sharpen_amount     final unsharp-mask-like gain
sharpen_radius     blur radius used by final sharpening
grain              optional fine texture amount
seed               random seed for reproducible grain
quality            JPEG quality, ignored for PNG
```

## MCIFT-inspired part

The optional threefold modulation uses a flat-image projection of the repository's compact activation form:

```text
A3 = 1 + epsilon3 * radial_band * cos(3 phi + psi3)
```

In the theoretical reducer this is related to:

```text
A_3(theta, phi) = 1 + epsilon_3 sin(theta)^2 cos(3 phi + psi_3)
```

The image application uses it as a controllable processing field only. It is not a claim that the image contains physical MCIFT structure.

## Debug outputs

With `--save-debug some_dir`, the script writes:

```text
01_base_interpolation.png
02_bubble_inflation.png
03_bubble_field.png
04_edge_mask.png
05_detail_enhanced.png
06_final_rgb.png
config.json
```

These files make it easier to see whether the bubble field, edge mask, and detail enhancement are helping or overcooking an image.

## Safe wording

Good:

```text
Bubble Inflation Upscaler is an experimental MCIFT-inspired image upscaler with tunable radial inflation, threefold modulation, detail boost, and sharpening.
```

Avoid:

```text
This recovers true hidden detail.
This proves MCIFT.
This is physically validated upscaling.
```

## License

Unless otherwise noted, this application follows the repository license: GNU Affero General Public License v3.0. See `LICENSE` and `COMMERCIAL-LICENSE.md` in the repository root.
