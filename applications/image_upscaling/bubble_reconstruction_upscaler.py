#!/usr/bin/env python3
"""
Bubble Reconstruction Upscaler

Restoration-first MCIFT-inspired image upscaling utility.

This script is meant for low-quality inputs where plain enlargement mostly makes
compression blocks, smear, and weak edges bigger. It separates the input into a
cleaned structure layer, an artifact-suppressed base, and a controlled residual
texture layer before applying bubble inflation and closure-guarded sharpening.

It does not recover true lost ground-truth detail. It creates a tunable
restoration/enhancement reconstruction for practical experiments.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict, fields
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import numpy as np
from PIL import Image, ImageFilter


@dataclass
class ReconstructionConfig:
    scale: float = 4.0
    resample: str = "lanczos"

    # Bubble field, matching the first upscaler's practical projection.
    bubble_strength: float = 0.10
    bubble_radius: float = 1.18
    bubble_falloff: float = 2.0
    center_x: float = 0.5
    center_y: float = 0.5
    threefold: bool = True
    epsilon3: float = 0.10
    psi3: float = 0.0

    # Restoration / artifact sink.
    median_preclean_size: int = 3
    artifact_suppression: float = 0.45
    deblock_strength: float = 0.55
    jpeg_grid_size: int = 8
    chroma_smooth_radius: float = 1.25
    luma_smooth_radius: float = 0.20

    # Reconstruction channels.
    structure_strength: float = 0.42
    edge_confidence: float = 0.55
    edge_threshold: float = 0.030
    detail_radius: float = 1.15
    residual_gain: float = 0.20

    # Controlled synthetic residual. Keep low for honest restoration.
    texture_strength: float = 0.012
    texture_scale: float = 0.85
    texture_seed: Optional[int] = 0

    # Closure guard and final finish.
    closure_strength: float = 0.70
    halo_limit: float = 0.080
    anti_ringing_radius: float = 0.80
    sharpen_amount: float = 0.20
    sharpen_radius: float = 0.85
    quality: int = 95


RESAMPLE_MODES = {
    "nearest": Image.Resampling.NEAREST,
    "bilinear": Image.Resampling.BILINEAR,
    "bicubic": Image.Resampling.BICUBIC,
    "lanczos": Image.Resampling.LANCZOS,
}


def clamp_config(cfg: ReconstructionConfig) -> ReconstructionConfig:
    cfg.scale = max(1.0, float(cfg.scale))
    cfg.resample = str(cfg.resample).lower()

    cfg.bubble_strength = float(cfg.bubble_strength)
    cfg.bubble_radius = max(0.05, float(cfg.bubble_radius))
    cfg.bubble_falloff = max(0.05, float(cfg.bubble_falloff))
    cfg.center_x = float(np.clip(float(cfg.center_x), 0.0, 1.0))
    cfg.center_y = float(np.clip(float(cfg.center_y), 0.0, 1.0))
    cfg.threefold = bool(cfg.threefold)
    cfg.epsilon3 = float(np.clip(float(cfg.epsilon3), -0.95, 0.95))
    cfg.psi3 = float(cfg.psi3)

    cfg.median_preclean_size = int(max(0, cfg.median_preclean_size))
    if cfg.median_preclean_size > 0 and cfg.median_preclean_size % 2 == 0:
        cfg.median_preclean_size += 1
    cfg.artifact_suppression = float(np.clip(float(cfg.artifact_suppression), 0.0, 1.0))
    cfg.deblock_strength = float(np.clip(float(cfg.deblock_strength), 0.0, 1.0))
    cfg.jpeg_grid_size = int(max(2, cfg.jpeg_grid_size))
    cfg.chroma_smooth_radius = max(0.0, float(cfg.chroma_smooth_radius))
    cfg.luma_smooth_radius = max(0.0, float(cfg.luma_smooth_radius))

    cfg.structure_strength = float(cfg.structure_strength)
    cfg.edge_confidence = float(np.clip(float(cfg.edge_confidence), 0.0, 1.0))
    cfg.edge_threshold = float(np.clip(float(cfg.edge_threshold), 0.0, 1.0))
    cfg.detail_radius = max(0.0, float(cfg.detail_radius))
    cfg.residual_gain = float(cfg.residual_gain)

    cfg.texture_strength = max(0.0, float(cfg.texture_strength))
    cfg.texture_scale = max(0.05, float(cfg.texture_scale))
    if cfg.texture_seed is not None:
        cfg.texture_seed = int(cfg.texture_seed)

    cfg.closure_strength = float(np.clip(float(cfg.closure_strength), 0.0, 1.0))
    cfg.halo_limit = max(0.0, float(cfg.halo_limit))
    cfg.anti_ringing_radius = max(0.0, float(cfg.anti_ringing_radius))
    cfg.sharpen_amount = float(cfg.sharpen_amount)
    cfg.sharpen_radius = max(0.0, float(cfg.sharpen_radius))
    cfg.quality = int(np.clip(int(cfg.quality), 1, 100))

    if cfg.resample not in RESAMPLE_MODES:
        raise ValueError(f"Unknown resample mode: {cfg.resample}")
    return cfg


def load_config(preset_path: Optional[Path], cli_values: Dict[str, Any]) -> ReconstructionConfig:
    values = asdict(ReconstructionConfig())
    if preset_path:
        with preset_path.open("r", encoding="utf-8") as f:
            preset_values = json.load(f)
        unknown = sorted(set(preset_values) - set(values))
        if unknown:
            raise ValueError(f"Unknown preset key(s): {', '.join(unknown)}")
        values.update(preset_values)

    for key, value in cli_values.items():
        if value is not None and key in values:
            values[key] = value

    return clamp_config(ReconstructionConfig(**values))


def image_to_float(img: Image.Image) -> np.ndarray:
    return np.asarray(img).astype(np.float32) / 255.0


def float_to_image(arr: np.ndarray, mode: str = "RGB") -> Image.Image:
    arr8 = np.clip(arr * 255.0 + 0.5, 0, 255).astype(np.uint8)
    return Image.fromarray(arr8, mode=mode)


def gaussian_blur_array(arr: np.ndarray, radius: float) -> np.ndarray:
    if radius <= 0:
        return arr.copy()
    mode = "L" if arr.ndim == 2 else "RGB"
    return image_to_float(float_to_image(arr, mode=mode).filter(ImageFilter.GaussianBlur(radius=radius)))


def median_filter_array(arr: np.ndarray, size: int) -> np.ndarray:
    if size <= 1:
        return arr.copy()
    return image_to_float(float_to_image(arr, mode="RGB").filter(ImageFilter.MedianFilter(size=size)))


def rgb_to_ycbcr(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    y = 0.299 * r + 0.587 * g + 0.114 * b
    cb = -0.168736 * r - 0.331264 * g + 0.5 * b + 0.5
    cr = 0.5 * r - 0.418688 * g - 0.081312 * b + 0.5
    return np.stack([y, cb, cr], axis=-1).astype(np.float32)


def ycbcr_to_rgb(ycbcr: np.ndarray) -> np.ndarray:
    y = ycbcr[..., 0]
    cb = ycbcr[..., 1] - 0.5
    cr = ycbcr[..., 2] - 0.5
    r = y + 1.402 * cr
    g = y - 0.344136 * cb - 0.714136 * cr
    b = y + 1.772 * cb
    return np.clip(np.stack([r, g, b], axis=-1), 0.0, 1.0).astype(np.float32)


def chroma_smooth(rgb: np.ndarray, chroma_radius: float, luma_radius: float) -> np.ndarray:
    ycc = rgb_to_ycbcr(rgb)
    if luma_radius > 0:
        ycc[..., 0] = gaussian_blur_array(ycc[..., 0], luma_radius)
    if chroma_radius > 0:
        ycc[..., 1] = gaussian_blur_array(ycc[..., 1], chroma_radius)
        ycc[..., 2] = gaussian_blur_array(ycc[..., 2], chroma_radius)
    return ycbcr_to_rgb(ycc)


def deblock(rgb: np.ndarray, grid_size: int, strength: float) -> np.ndarray:
    if strength <= 0:
        return rgb.copy()
    h, w = rgb.shape[:2]
    blurred = gaussian_blur_array(rgb, 0.85)
    mask = np.zeros((h, w, 1), dtype=np.float32)
    strip = max(1, grid_size // 8)
    for x in range(grid_size, w, grid_size):
        lo = max(0, x - strip)
        hi = min(w, x + strip + 1)
        mask[:, lo:hi, :] = 1.0
    for y in range(grid_size, h, grid_size):
        lo = max(0, y - strip)
        hi = min(h, y + strip + 1)
        mask[lo:hi, :, :] = 1.0
    mask = gaussian_blur_array(mask[..., 0], max(0.5, strip * 0.8))[..., None]
    return np.clip(rgb * (1.0 - mask * strength) + blurred * (mask * strength), 0.0, 1.0)


def artifact_sink(rgb: np.ndarray, cfg: ReconstructionConfig) -> np.ndarray:
    """Suppress unstable artifact load before enlargement."""
    cleaned = rgb.copy()
    if cfg.median_preclean_size > 1:
        medianed = median_filter_array(cleaned, cfg.median_preclean_size)
        cleaned = cleaned * (1.0 - cfg.artifact_suppression * 0.45) + medianed * (cfg.artifact_suppression * 0.45)

    cleaned = deblock(cleaned, cfg.jpeg_grid_size, cfg.deblock_strength * cfg.artifact_suppression)

    chroma = chroma_smooth(cleaned, cfg.chroma_smooth_radius, cfg.luma_smooth_radius)
    cleaned = cleaned * (1.0 - cfg.artifact_suppression) + chroma * cfg.artifact_suppression
    return np.clip(cleaned, 0.0, 1.0).astype(np.float32)


def bilinear_sample(arr: np.ndarray, src_x: np.ndarray, src_y: np.ndarray) -> np.ndarray:
    h, w = arr.shape[:2]
    src_x = np.clip(src_x, 0.0, w - 1.0)
    src_y = np.clip(src_y, 0.0, h - 1.0)

    x0 = np.floor(src_x).astype(np.int32)
    y0 = np.floor(src_y).astype(np.int32)
    x1 = np.clip(x0 + 1, 0, w - 1)
    y1 = np.clip(y0 + 1, 0, h - 1)

    wx = (src_x - x0)[..., None]
    wy = (src_y - y0)[..., None]

    top = arr[y0, x0] * (1.0 - wx) + arr[y0, x1] * wx
    bottom = arr[y1, x0] * (1.0 - wx) + arr[y1, x1] * wx
    return top * (1.0 - wy) + bottom * wy


def bubble_field(shape: Tuple[int, int], cfg: ReconstructionConfig) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    h, w = shape
    yy, xx = np.meshgrid(np.arange(h, dtype=np.float32), np.arange(w, dtype=np.float32), indexing="ij")
    cx = cfg.center_x * (w - 1)
    cy = cfg.center_y * (h - 1)
    norm = max(1.0, min(w, h) * 0.5)
    dx = (xx - cx) / norm
    dy = (yy - cy) / norm
    r = np.sqrt(dx * dx + dy * dy)
    phi = np.arctan2(dy, dx)
    radius_ratio = r / cfg.bubble_radius
    envelope = np.clip(1.0 - np.power(radius_ratio, cfg.bubble_falloff), 0.0, 1.0)
    if cfg.threefold:
        radial_band = np.clip(1.0 - radius_ratio * radius_ratio, 0.0, 1.0)
        a3 = 1.0 + cfg.epsilon3 * radial_band * np.cos(3.0 * phi + cfg.psi3)
    else:
        a3 = np.ones_like(envelope)
    inflation = (cfg.bubble_strength * envelope * a3).astype(np.float32)
    return inflation, a3.astype(np.float32), envelope.astype(np.float32)


def bubble_inflation_remap(arr: np.ndarray, cfg: ReconstructionConfig) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    h, w = arr.shape[:2]
    yy, xx = np.meshgrid(np.arange(h, dtype=np.float32), np.arange(w, dtype=np.float32), indexing="ij")
    cx = cfg.center_x * (w - 1)
    cy = cfg.center_y * (h - 1)
    norm = max(1.0, min(w, h) * 0.5)
    dx = (xx - cx) / norm
    dy = (yy - cy) / norm
    inflation, a3, _ = bubble_field((h, w), cfg)
    denom = np.maximum(0.05, 1.0 + inflation)
    src_x = cx + (dx / denom) * norm
    src_y = cy + (dy / denom) * norm
    return bilinear_sample(arr, src_x, src_y), inflation, a3


def luminance(rgb: np.ndarray) -> np.ndarray:
    return (0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]).astype(np.float32)


def edge_mask(rgb: np.ndarray, threshold: float) -> np.ndarray:
    lum = luminance(rgb)
    gx = np.zeros_like(lum)
    gy = np.zeros_like(lum)
    gx[:, 1:-1] = 0.5 * (lum[:, 2:] - lum[:, :-2])
    gy[1:-1, :] = 0.5 * (lum[2:, :] - lum[:-2, :])
    mag = np.sqrt(gx * gx + gy * gy)
    max_mag = float(np.max(mag))
    if max_mag <= 1e-8:
        return np.zeros((*rgb.shape[:2], 1), dtype=np.float32)
    mask = mag / max_mag
    mask = np.clip((mask - threshold) / max(1e-6, 1.0 - threshold), 0.0, 1.0)
    return mask[..., None].astype(np.float32)


def reconstruct_channels(bubble_rgb: np.ndarray, a3: np.ndarray, cfg: ReconstructionConfig) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    edges = edge_mask(bubble_rgb, cfg.edge_threshold)
    blur = gaussian_blur_array(bubble_rgb, cfg.detail_radius)
    residual = bubble_rgb - blur

    structure = np.clip(bubble_rgb + residual * (cfg.structure_strength * edges), 0.0, 1.0)

    rng = np.random.default_rng(cfg.texture_seed)
    noise = rng.normal(0.0, 1.0, size=bubble_rgb.shape[:2]).astype(np.float32)
    noise_img = np.repeat(noise[..., None], 3, axis=-1)
    fine = gaussian_blur_array(noise_img, cfg.texture_scale)
    coarse = gaussian_blur_array(noise_img, cfg.texture_scale * 3.0)
    texture = fine - coarse
    texture_std = float(np.std(texture))
    if texture_std > 1e-8:
        texture = texture / texture_std
    a3_norm = a3[..., None]
    a3_norm = a3_norm / max(1e-6, float(np.mean(a3_norm)))
    texture_layer = texture * cfg.texture_strength * (0.35 + 0.65 * edges) * a3_norm

    candidate = structure + residual * cfg.residual_gain * (0.35 + edges * cfg.edge_confidence) + texture_layer
    return np.clip(candidate, 0.0, 1.0), edges[..., 0], residual, texture_layer


def closure_guard(base_rgb: np.ndarray, candidate: np.ndarray, edges: np.ndarray, cfg: ReconstructionConfig) -> np.ndarray:
    """Limit residuals that do not agree with the stabilized bubble base."""
    if cfg.closure_strength <= 0:
        return candidate
    if cfg.anti_ringing_radius > 0:
        anti_ring_base = gaussian_blur_array(candidate, cfg.anti_ringing_radius)
        candidate = candidate * 0.82 + anti_ring_base * 0.18
    edge3 = edges[..., None]
    limit = cfg.halo_limit * (0.55 + edge3)
    clipped = base_rgb + np.clip(candidate - base_rgb, -limit, limit)
    return np.clip(candidate * (1.0 - cfg.closure_strength) + clipped * cfg.closure_strength, 0.0, 1.0)


def sharpen(rgb: np.ndarray, cfg: ReconstructionConfig) -> np.ndarray:
    if cfg.sharpen_amount == 0 or cfg.sharpen_radius <= 0:
        return rgb
    blur = gaussian_blur_array(rgb, cfg.sharpen_radius)
    return np.clip(rgb + cfg.sharpen_amount * (rgb - blur), 0.0, 1.0)


def save_rgb(path: Path, rgb: np.ndarray, quality: int = 95) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = float_to_image(rgb, mode="RGB")
    if path.suffix.lower() in {".jpg", ".jpeg"}:
        img.save(path, quality=quality, optimize=True)
    else:
        img.save(path)


def save_gray(path: Path, arr: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    arr = np.asarray(arr, dtype=np.float32)
    mn, mx = float(np.min(arr)), float(np.max(arr))
    if mx - mn > 1e-8:
        arr = (arr - mn) / (mx - mn)
    else:
        arr = np.zeros_like(arr)
    Image.fromarray(np.clip(arr * 255.0 + 0.5, 0, 255).astype(np.uint8), mode="L").save(path)


def make_compare(left_rgb: np.ndarray, right_rgb: np.ndarray, output_path: Path, quality: int) -> None:
    h, w = right_rgb.shape[:2]
    left = float_to_image(left_rgb, mode="RGB").resize((w, h), Image.Resampling.NEAREST)
    right = float_to_image(right_rgb, mode="RGB")
    canvas = Image.new("RGB", (w * 2, h))
    canvas.paste(left, (0, 0))
    canvas.paste(right, (w, 0))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() in {".jpg", ".jpeg"}:
        canvas.save(output_path, quality=quality, optimize=True)
    else:
        canvas.save(output_path)


def upscale_image(input_path: Path, output_path: Path, cfg: ReconstructionConfig, debug_dir: Optional[Path] = None, compare_path: Optional[Path] = None) -> None:
    source = Image.open(input_path).convert("RGB")
    source_rgb = image_to_float(source)

    cleaned = artifact_sink(source_rgb, cfg)

    src_w, src_h = source.size
    out_w = max(1, int(round(src_w * cfg.scale)))
    out_h = max(1, int(round(src_h * cfg.scale)))
    base_img = float_to_image(cleaned, mode="RGB").resize((out_w, out_h), RESAMPLE_MODES[cfg.resample])
    base_rgb = image_to_float(base_img)

    bubble_rgb, inflation, a3 = bubble_inflation_remap(base_rgb, cfg)
    candidate, edges, residual, texture_layer = reconstruct_channels(bubble_rgb, a3, cfg)
    guarded = closure_guard(bubble_rgb, candidate, edges, cfg)
    final_rgb = sharpen(guarded, cfg)

    save_rgb(output_path, final_rgb, quality=cfg.quality)

    if debug_dir:
        debug_dir.mkdir(parents=True, exist_ok=True)
        save_rgb(debug_dir / "01_source.png", source_rgb, quality=cfg.quality)
        save_rgb(debug_dir / "02_artifact_sink.png", cleaned, quality=cfg.quality)
        save_rgb(debug_dir / "03_base_upscale.png", base_rgb, quality=cfg.quality)
        save_rgb(debug_dir / "04_bubble_inflation.png", bubble_rgb, quality=cfg.quality)
        save_gray(debug_dir / "05_bubble_field.png", inflation)
        save_gray(debug_dir / "06_a3_field.png", a3)
        save_gray(debug_dir / "07_edge_confidence.png", edges)
        save_rgb(debug_dir / "08_candidate_reconstruction.png", candidate, quality=cfg.quality)
        save_rgb(debug_dir / "09_texture_layer_visual.png", np.clip(texture_layer * 12.0 + 0.5, 0.0, 1.0), quality=cfg.quality)
        save_rgb(debug_dir / "10_final.png", final_rgb, quality=cfg.quality)
        with (debug_dir / "config.json").open("w", encoding="utf-8") as f:
            json.dump(asdict(cfg), f, indent=2)

    if compare_path:
        make_compare(source_rgb, final_rgb, compare_path, quality=cfg.quality)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="MCIFT-inspired Bubble Reconstruction Upscaler")
    parser.add_argument("input", type=Path, help="Input image path")
    parser.add_argument("output", type=Path, help="Output image path")
    parser.add_argument("--preset", type=Path, default=None, help="JSON preset to load before CLI overrides")

    for field in fields(ReconstructionConfig):
        name = field.name
        if name in {"threefold", "texture_seed"}:
            continue
        parser.add_argument("--" + name.replace("_", "-"), dest=name, default=None)

    parser.add_argument("--texture-seed", type=int, default=None, help="Random seed for synthetic residual texture")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--threefold", dest="threefold", action="store_true", default=None, help="Enable threefold modulation")
    group.add_argument("--no-threefold", dest="threefold", action="store_false", help="Disable threefold modulation")

    parser.add_argument("--save-debug", type=Path, default=None, help="Directory for intermediate outputs")
    parser.add_argument("--compare", nargs="?", const="auto", default=None, help="Save source/final comparison. Optionally provide a path.")
    parser.add_argument("--print-config", action="store_true", help="Print final merged configuration")
    return parser.parse_args()


def cli_values_from_args(args: argparse.Namespace) -> Dict[str, Any]:
    cfg_keys = {f.name for f in fields(ReconstructionConfig)}
    return {key: getattr(args, key) for key in cfg_keys if hasattr(args, key)}


def resolve_compare_path(compare_arg: Optional[str], output_path: Path) -> Optional[Path]:
    if compare_arg is None:
        return None
    if compare_arg == "auto":
        return output_path.with_name(output_path.stem + "_compare" + output_path.suffix)
    return Path(compare_arg)


def main() -> None:
    args = parse_args()
    cfg = load_config(args.preset, cli_values_from_args(args))
    if args.print_config:
        print(json.dumps(asdict(cfg), indent=2))
    compare_path = resolve_compare_path(args.compare, args.output)
    upscale_image(args.input, args.output, cfg, debug_dir=args.save_debug, compare_path=compare_path)


if __name__ == "__main__":
    main()
