# MCIFT Image Upscaling Applications

**Status:** experimental image-processing applications inspired by MCIFT reducer math.

This folder contains three related workflows:

```text
bubble_inflation_upscaler.py          enlargement-first workflow
bubble_reconstruction_upscaler.py     restoration-first workflow for low-quality inputs
bubble_edge_closure_upscaler.py       edge-recalculation workflow for bad/blocky boundaries
```

None of these workflows claim to reconstruct lost ground-truth detail. They create configurable enhancement and reconstruction layers for practical image upscaling experiments.

## Install

From the repository root:

```bash
python -m pip install -r applications/image_upscaling/requirements.txt
```

---

## 1. Bubble Inflation Upscaler

Use this when the source image is already decent and you mostly want enlargement plus tunable detail/sharpening.

```bash
python applications/image_upscaling/bubble_inflation_upscaler.py \
  input.png \
  output.png \
  --scale 4 \
  --preset applications/image_upscaling/presets/balanced.json \
  --compare \
  --save-debug debug/bubble_upscale
```

Presets:

```text
presets/gentle.json       mild inflation and sharpening
presets/balanced.json     default practical starting point
presets/aggressive.json   stronger bubble/detail/sharpening pass
```

---

## 2. Bubble Reconstruction Upscaler

Use this when the source is low-quality, blocky, smeared, or visibly compressed.

This workflow adds a restoration-first stage before enlargement:

```text
source image
-> artifact sink / preclean
-> structure field extraction
-> bubble inflation remap
-> threefold residual reconstruction
-> closure guard / anti-ringing
-> final sharpening
```

```bash
python applications/image_upscaling/bubble_reconstruction_upscaler.py \
  low_quality_input.png \
  restored_4x.png \
  --preset applications/image_upscaling/presets/restoration_balanced.json \
  --compare \
  --save-debug debug/bubble_reconstruction
```

Restoration presets:

```text
presets/restoration_gentle.json       safer cleanup, low synthetic texture
presets/restoration_balanced.json     default low-quality input workflow
presets/restoration_strong.json       stronger deblock/detail/texture pass
```

---

## 3. Bubble Edge Closure Upscaler

Use this when the reconstruction output still has bad edges: blocky contours, doubled halos, crunchy outlines, or smeared boundaries.

This workflow does not merely detect edges after upscaling. It recalculates a separate edge closure field before reconstruction:

```text
source image
-> artifact sink / preclean
-> raw low-res edge estimate
-> edge tangent + normal field
-> tangent-direction closure smoothing
-> isolated edge pruning
-> high-res edge re-projection through bubble remap
-> edge-guided residual reconstruction
-> normal-preserving closure guard
-> final sharpening
```

```bash
python applications/image_upscaling/bubble_edge_closure_upscaler.py \
  low_quality_input.png \
  edge_closed_4x.png \
  --preset applications/image_upscaling/presets/edge_closure_balanced.json \
  --compare \
  --save-debug debug/edge_closure
```

Edge-closure preset:

```text
presets/edge_closure_balanced.json    default edge-recalculation workflow
```

The edge-closure workflow writes these debug files when `--save-debug` is used:

```text
01_source.png
02_artifact_sink.png
03_edge_raw_low_to_high.png
04_edge_closed_recalculated.png
05_edge_tangent_field.png
06_base_upscale.png
07_bubble_inflation.png
08_bubble_field.png
09_a3_field.png
10_edge_confidence_used.png
11_candidate_reconstruction.png
12_texture_layer_visual.png
13_final.png
config.json
```

---

## Main inflation parameters

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
quality            JPEG quality, ignored for PNG
```

## Main reconstruction parameters

```text
artifact_suppression   global strength of the pre-upscale artifact sink
deblock_strength       strength of JPEG/block-boundary smoothing
jpeg_grid_size         expected compression block grid, usually 8
chroma_smooth_radius   color-smear cleanup radius
luma_smooth_radius     mild luminance cleanup radius
structure_strength     edge/shape reinforcement strength
edge_confidence        how strongly edge confidence controls reconstruction
residual_gain          how much controlled residual detail is added back
texture_strength       synthetic fine texture amount
texture_scale          synthetic texture grain scale
closure_strength       strength of residual limiting / anti-halo guard
halo_limit             maximum allowed residual swing around the bubble base
anti_ringing_radius    softening radius before closure guard
sharpen_amount         final unsharp-mask-like gain
sharpen_radius         blur radius used by final sharpening
```

## Edge recalculation parameters

```text
edge_recalculate          enables separate edge closure field calculation
edge_closure_strength     how strongly the closed edge field replaces raw edge confidence
edge_closure_iterations   number of tangent-closure passes
edge_tangent_smoothing    smoothing distance along the recalculated edge tangent
edge_normal_preserve      how strongly reconstruction avoids smearing across the edge normal
edge_prune_threshold      removes isolated weak edge fragments before upscaling
```

## MCIFT-inspired part

All workflows use a flat-image projection of the repository's compact threefold activation form:

```text
A3 = 1 + epsilon3 * radial_band * cos(3 phi + psi3)
```

In the theoretical reducer this is related to:

```text
A_3(theta, phi) = 1 + epsilon_3 sin(theta)^2 cos(3 phi + psi_3)
```

The image applications use this as a controllable processing field only. They do not claim that the image contains physical MCIFT structure.

## Safe wording

Good:

```text
Bubble Edge Closure Upscaler is an experimental MCIFT-inspired restoration workflow that recalculates a boundary field before reconstruction, then uses tangent-guided smoothing and normal-preserving closure to reduce blocky or smeared edges.
```

Avoid:

```text
This recovers true hidden detail.
This proves MCIFT.
This is physically validated upscaling.
```

## License

Unless otherwise noted, this application follows the repository license: GNU Affero General Public License v3.0. See `LICENSE` and `COMMERCIAL-LICENSE.md` in the repository root.
