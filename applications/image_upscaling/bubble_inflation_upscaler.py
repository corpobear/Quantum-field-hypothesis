#!/usr/bin/env python3
"""
Bubble Inflation Upscaler

Experimental MCIFT-inspired image upscaling utility.

The script performs ordinary high-quality interpolation first, then applies a
parameterized bubble inflation field, optional threefold modulation, local detail
boosting, and sharpening. It does not reconstruct lost ground-truth detail; it
creates tunable enhancement layers for practical image enlargement experiments.

Dependencies:
    pip install -r applications/image_upscaling/requirements.txt

Example:
    python applications/image_upscaling/bubble_inflation_upscaler.py input.png output.png \
        --scale 4 --preset applications/image_upscaling/presets/balanced.json
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
class UpscaleConfig:
    scale: float = 2.0
    resample: str = "lanczos"

    bubble_strength: float = 0.14
    bubble_radius: float = 1.15
    bubble_falloff: float = 2.0
    center_x: float = 0.5
    center_y: float = 0.5

    threefold: bool = True
    epsilon3: float = 0.125
    psi3: float = 0.0

    denoise_radius: float = 0.0
    detail_strength: float = 0.22
    detail_radius: float = 1.25
    edge_boost: float = 0.25
    edge_threshold: float = 0.035

    sharpen_amount: float = 0.35
    sharpen_radius: float = 0.85

    grain: float = 0.0
    seed: Optional[int] = None

    quality: int = 95


RESAMPLE_MODES = {
    "nearest": Image.Resampling.NEAREST,
    "bilinear": Image.Resampling.BILINEAR,
    "bicubic": Image.Resampling.BICUBIC,
    "lanczos": Image.Resampling.LANCZOS,
}


def clamp_config(cfg: UpscaleConfig) -> UpscaleConfig:
    """Clamp numerically sensitive options to safe ranges."""
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

    cfg.denoise_radius = max(0.0, float(cfg.denoise_radius))
    cfg.detail_strength = float(cfg.detail_strength)
    cfg.detail_radius = max(0.0, float(cfg.detail_radius))
    cfg.edge_boost = float(cfg.edge_boost)
    cfg.edge_threshold = float(np.clip(float(cfg.edge_threshold), 0.0, 1.0))

    cfg.sharpen_amount = float(cfg.sharpen_amount)
    cfg.sharpen_radius = max(0.0, float(cfg.sharpen_radius))

    cfg.grain = max(0.0, float(cfg.grain))
    if cfg.seed is not None:
        cfg.seed = int(cfg.seed)
    cfg.quality = int(np.clip(int(cfg.quality), 1, 100))

    if cfg.resample not in RESAMPLE_MODES:
        raise ValueError(f"Unknown resample mode: {cfg.resample}")
    return cfg


def load_config(preset_path: Optional[Path], cli_values: Dict[str, Any]) -> UpscaleConfig:
    values = asdict(UpscaleConfig())

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

    return clamp_config(UpscaleConfig(**values))


def image_to_float(img: Image.Image) -> np.ndarray:
    return np.asarray(img).astype(np.float32) / 255.0


def float_to_image(arr: np.ndarray, mode: str = "RGB") -> Image.Image:
    arr8 = np.clip(arr * 255.0 + 0.5, 0, 255).astype(np.uint8)
    return Image.fromarray(arr8, mode=mode)


def gaussian_blur_array(arr: np.ndarray, radius: float) -> np.ndarray:
    if radius <= 0:
        return arr.copy()
    mode = "RGBA" if arr.shape[-1] == 4 else "RGB"
    return image_to_float(float_to_image(arr, mode=mode).filter(ImageFilter.GaussianBlur(radius=radius)))


def bilinear_sample(arr: np.ndarray, src_x: np.ndarray, src_y: np.ndarray) -> np.ndarray:
    """Sample arr at floating source coordinates using bilinear interpolation."""
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


def bubble_inflation_remap(arr: np.ndarray, cfg: UpscaleConfig) -> Tuple[np.ndarray, np.ndarray]:
    """
    Apply inverse radial bubble inflation.

    Positive bubble_strength expands content outward from the chosen center by
    sampling from a slightly smaller source radius. Optional threefold modulation
    follows the same compact activation pattern used in the MCIFT reducer:

        A3 = 1 + epsilon3 * radial_band * cos(3 phi + psi3)

    On a flat image this is a practical projection, not a physical claim.
    """
    h, w = arr.shape[:2]
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
        a3 = 1.0

    inflation = cfg.bubble_strength * envelope * a3
    denom = np.maximum(0.05, 1.0 + inflation)

    src_x = cx + (dx / denom) * norm
    src_y = cy + (dy / denom) * norm

    remapped = bilinear_sample(arr, src_x, src_y)
    field = inflation.astype(np.float32)
    return remapped, field


def edge_mask(rgb: np.ndarray, threshold: float) -> np.ndarray:
    lum = 0.2126 * rgb[..., 0] + 0.7152 * rgb[..., 1] + 0.0722 * rgb[..., 2]

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


def enhance_detail(rgb: np.ndarray, cfg: UpscaleConfig) -> Tuple[np.ndarray, np.ndarray]:
    working = rgb
    if cfg.denoise_radius > 0:
        working = gaussian_blur_array(working, cfg.denoise_radius)

    blur = gaussian_blur_array(working, cfg.detail_radius)
    detail = working - blur
    edges = edge_mask(working, cfg.edge_threshold)

    detail_gain = cfg.detail_strength + cfg.edge_boost * edges
    enhanced = working + detail * detail_gain
    return np.clip(enhanced, 0.0, 1.0), edges[..., 0]


def sharpen(rgb: np.ndarray, cfg: UpscaleConfig) -> np.ndarray:
    if cfg.sharpen_amount == 0 or cfg.sharpen_radius <= 0:
        return rgb
    blur = gaussian_blur_array(rgb, cfg.sharpen_radius)
    out = rgb + cfg.sharpen_amount * (rgb - blur)
    return np.clip(out, 0.0, 1.0)


def add_grain(rgb: np.ndarray, cfg: UpscaleConfig) -> np.ndarray:
    if cfg.grain <= 0:
        return rgb
    rng = np.random.default_rng(cfg.seed)
    noise = rng.normal(0.0, cfg.grain, size=rgb.shape).astype(np.float32)
    return np.clip(rgb + noise, 0.0, 1.0)


def save_rgb(path: Path, rgb: np.ndarray, quality: int = 95) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = float_to_image(rgb, mode="RGB")
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        img.save(path, quality=quality, optimize=True)
    else:
        img.save(path)


def save_rgba(path: Path, rgba: np.ndarray, quality: int = 95) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = float_to_image(rgba, mode="RGBA")
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        img.convert("RGB").save(path, quality=quality, optimize=True)
    else:
        img.save(path)


def save_gray(path: Path, arr: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    arr8 = np.clip(arr * 255.0 + 0.5, 0, 255).astype(np.uint8)
    Image.fromarray(arr8, mode="L").save(path)


def make_compare(base_rgb: np.ndarray, final_rgb: np.ndarray, output_path: Path, quality: int) -> None:
    h, w = final_rgb.shape[:2]
    base_img = float_to_image(base_rgb, mode="RGB")
    final_img = float_to_image(final_rgb, mode="RGB")

    canvas = Image.new("RGB", (w * 2, h))
    canvas.paste(base_img, (0, 0))
    canvas.paste(final_img, (w, 0))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    if output_path.suffix.lower() in {".jpg", ".jpeg"}:
        canvas.save(output_path, quality=quality, optimize=True)
    else:
        canvas.save(output_path)


def upscale_image(input_path: Path, output_path: Path, cfg: UpscaleConfig, debug_dir: Optional[Path] = None, compare_path: Optional[Path] = None) -> None:
    source = Image.open(input_path)
    has_alpha = source.mode in {"RGBA", "LA"} or "transparency" in source.info
    working_mode = "RGBA" if has_alpha else "RGB"
    source = source.convert(working_mode)

    src_w, src_h = source.size
    out_w = max(1, int(round(src_w * cfg.scale)))
    out_h = max(1, int(round(src_h * cfg.scale)))

    base_img = source.resize((out_w, out_h), RESAMPLE_MODES[cfg.resample])
    base_arr = image_to_float(base_img)

    if has_alpha:
        base_rgb = base_arr[..., :3]
        base_alpha = base_arr[..., 3:4]
    else:
        base_rgb = base_arr
        base_alpha = None

    bubble_rgb, bubble_field = bubble_inflation_remap(base_rgb, cfg)
    if base_alpha is not None:
        bubble_alpha, _ = bubble_inflation_remap(base_alpha, cfg)
    else:
        bubble_alpha = None

    detailed_rgb, edges = enhance_detail(bubble_rgb, cfg)
    sharp_rgb = sharpen(detailed_rgb, cfg)
    final_rgb = add_grain(sharp_rgb, cfg)

    if bubble_alpha is not None:
        final = np.concatenate([final_rgb, np.clip(bubble_alpha, 0.0, 1.0)], axis=-1)
        save_rgba(output_path, final, quality=cfg.quality)
    else:
        save_rgb(output_path, final_rgb, quality=cfg.quality)

    if debug_dir:
        debug_dir.mkdir(parents=True, exist_ok=True)
        save_rgb(debug_dir / "01_base_interpolation.png", base_rgb, quality=cfg.quality)
        save_rgb(debug_dir / "02_bubble_inflation.png", bubble_rgb, quality=cfg.quality)
        save_gray(debug_dir / "03_bubble_field.png", normalize_for_debug(bubble_field))
        save_gray(debug_dir / "04_edge_mask.png", edges)
        save_rgb(debug_dir / "05_detail_enhanced.png", detailed_rgb, quality=cfg.quality)
        save_rgb(debug_dir / "06_final_rgb.png", final_rgb, quality=cfg.quality)
        with (debug_dir / "config.json").open("w", encoding="utf-8") as f:
            json.dump(asdict(cfg), f, indent=2)

    if compare_path:
        make_compare(base_rgb, final_rgb, compare_path, quality=cfg.quality)


def normalize_for_debug(arr: np.ndarray) -> np.ndarray:
    mn = float(np.min(arr))
    mx = float(np.max(arr))
    if mx - mn <= 1e-8:
        return np.zeros_like(arr, dtype=np.float32)
    return ((arr - mn) / (mx - mn)).astype(np.float32)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="MCIFT-inspired Bubble Inflation Upscaler")
    parser.add_argument("input", type=Path, help="Input image path")
    parser.add_argument("output", type=Path, help="Output image path")
    parser.add_argument("--preset", type=Path, default=None, help="JSON preset to load before CLI overrides")

    for field in fields(UpscaleConfig):
        name = field.name
        if name in {"threefold", "seed"}:
            continue
        arg = "--" + name.replace("_", "-")
        parser.add_argument(arg, dest=name, default=None)

    parser.add_argument("--seed", type=int, default=None, help="Random seed for grain")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--threefold", dest="threefold", action="store_true", default=None, help="Enable threefold modulation")
    group.add_argument("--no-threefold", dest="threefold", action="store_false", help="Disable threefold modulation")

    parser.add_argument("--save-debug", type=Path, default=None, help="Directory for intermediate outputs")
    parser.add_argument("--compare", nargs="?", const="auto", default=None, help="Save side-by-side base/final comparison. Optionally provide a path.")
    parser.add_argument("--print-config", action="store_true", help="Print final merged configuration")
    return parser.parse_args()


def cli_values_from_args(args: argparse.Namespace) -> Dict[str, Any]:
    cfg_keys = {f.name for f in fields(UpscaleConfig)}
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
