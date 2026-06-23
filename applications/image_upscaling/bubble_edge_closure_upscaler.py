#!/usr/bin/env python3
"""
Bubble Edge Closure Upscaler

Experimental MCIFT-inspired restoration workflow that recalculates edges before
high-resolution reconstruction. This is intended for low-quality inputs where a
plain edge mask reinforces blocky or smeared source edges.

It does not recover true lost ground-truth detail. It builds a tunable edge
closure field, smooths along edge tangents, preserves across-edge contrast, and
uses that field to guide residual reconstruction.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict, fields
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

import numpy as np
from PIL import Image, ImageFilter

from bubble_reconstruction_upscaler import (
    ReconstructionConfig,
    RESAMPLE_MODES,
    artifact_sink,
    bilinear_sample,
    bubble_inflation_remap,
    edge_mask,
    float_to_image,
    gaussian_blur_array,
    image_to_float,
    luminance,
    make_compare,
    save_gray,
    save_rgb,
    sharpen,
)


@dataclass
class EdgeClosureConfig(ReconstructionConfig):
    edge_recalculate: bool = True
    edge_closure_strength: float = 0.70
    edge_closure_iterations: int = 2
    edge_tangent_smoothing: float = 1.35
    edge_normal_preserve: float = 0.70
    edge_prune_threshold: float = 0.055


def clamp_config(cfg: EdgeClosureConfig) -> EdgeClosureConfig:
    # Use the parent clamp logic for all shared reconstruction parameters.
    cfg = EdgeClosureConfig(**asdict(ReconstructionConfig(**{k: v for k, v in asdict(cfg).items() if k in asdict(ReconstructionConfig())})), **{
        k: v for k, v in asdict(cfg).items() if k not in asdict(ReconstructionConfig())
    })

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

    cfg.edge_recalculate = bool(cfg.edge_recalculate)
    cfg.edge_closure_strength = float(np.clip(float(cfg.edge_closure_strength), 0.0, 1.0))
    cfg.edge_closure_iterations = int(max(0, cfg.edge_closure_iterations))
    cfg.edge_tangent_smoothing = max(0.0, float(cfg.edge_tangent_smoothing))
    cfg.edge_normal_preserve = float(np.clip(float(cfg.edge_normal_preserve), 0.0, 1.0))
    cfg.edge_prune_threshold = float(np.clip(float(cfg.edge_prune_threshold), 0.0, 1.0))

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


def load_config(preset_path: Optional[Path], cli_values: Dict[str, Any]) -> EdgeClosureConfig:
    values = asdict(EdgeClosureConfig())
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
    return clamp_config(EdgeClosureConfig(**values))


def resize_float(arr: np.ndarray, size: Tuple[int, int], resample: Image.Resampling = Image.Resampling.BICUBIC) -> np.ndarray:
    if arr.ndim == 2:
        return image_to_float(float_to_image(arr, mode="L").resize(size, resample))
    if arr.shape[-1] == 1:
        plane = image_to_float(float_to_image(arr[..., 0], mode="L").resize(size, resample))
        return plane[..., None]
    return image_to_float(float_to_image(arr, mode="RGB").resize(size, resample))


def gradient_field(rgb: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    lum = luminance(rgb)
    gx = np.zeros_like(lum)
    gy = np.zeros_like(lum)
    gx[:, 1:-1] = 0.5 * (lum[:, 2:] - lum[:, :-2])
    gy[1:-1, :] = 0.5 * (lum[2:, :] - lum[:-2, :])
    mag = np.sqrt(gx * gx + gy * gy).astype(np.float32)
    return gx.astype(np.float32), gy.astype(np.float32), mag


def normalize_vectors(vx: np.ndarray, vy: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    norm = np.sqrt(vx * vx + vy * vy)
    norm = np.maximum(norm, 1e-6)
    return (vx / norm).astype(np.float32), (vy / norm).astype(np.float32)


def directional_sample_average(arr: np.ndarray, vx: np.ndarray, vy: np.ndarray, radius: float) -> np.ndarray:
    if radius <= 0:
        return arr.copy()
    h, w = arr.shape[:2]
    yy, xx = np.meshgrid(np.arange(h, dtype=np.float32), np.arange(w, dtype=np.float32), indexing="ij")
    samples = [arr]
    for step in (0.5, 1.0):
        off = radius * step
        samples.append(bilinear_sample(arr, xx + vx * off, yy + vy * off))
        samples.append(bilinear_sample(arr, xx - vx * off, yy - vy * off))
    return np.mean(samples, axis=0).astype(np.float32)


def recalculate_edge_closure_field(rgb: np.ndarray, cfg: EdgeClosureConfig) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    gx, gy, mag = gradient_field(rgb)
    max_mag = float(np.max(mag))
    if max_mag <= 1e-8:
        h, w = rgb.shape[:2]
        zeros = np.zeros((h, w), dtype=np.float32)
        ones = np.ones((h, w), dtype=np.float32)
        return zeros, zeros, ones, zeros, np.stack([zeros, ones], axis=-1)

    raw = mag / max_mag
    raw = np.clip((raw - cfg.edge_threshold) / max(1e-6, 1.0 - cfg.edge_threshold), 0.0, 1.0).astype(np.float32)

    # Normal = brightness gradient. Tangent = boundary direction.
    nx, ny = normalize_vectors(gx, gy)
    tx, ty = normalize_vectors(-ny, nx)

    closed = raw.copy()
    for _ in range(cfg.edge_closure_iterations):
        along = directional_sample_average(closed[..., None], tx, ty, cfg.edge_tangent_smoothing)[..., 0]
        across = directional_sample_average(closed[..., None], nx, ny, max(0.25, cfg.edge_tangent_smoothing * 0.55))[..., 0]
        continuity = np.clip(along - across * cfg.edge_normal_preserve, 0.0, 1.0)
        closed = np.clip(
            closed * (1.0 - cfg.edge_closure_strength)
            + np.maximum(raw, continuity) * cfg.edge_closure_strength,
            0.0,
            1.0,
        )
        closed = np.where(closed >= cfg.edge_prune_threshold, closed, 0.0).astype(np.float32)

    closed = gaussian_blur_array(closed, 0.45)
    closed = np.clip(np.maximum(raw * 0.35, closed), 0.0, 1.0).astype(np.float32)
    return raw, closed, tx, ty, np.stack([nx, ny], axis=-1).astype(np.float32)


def remap_edge_field(cleaned_rgb: np.ndarray, out_size: Tuple[int, int], cfg: EdgeClosureConfig) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    raw, closed, tx, ty, _ = recalculate_edge_closure_field(cleaned_rgb, cfg)
    raw_hi = resize_float(raw, out_size, Image.Resampling.BICUBIC)
    closed_hi = resize_float(closed, out_size, Image.Resampling.BICUBIC)
    tx_hi = resize_float(tx, out_size, Image.Resampling.BICUBIC)
    ty_hi = resize_float(ty, out_size, Image.Resampling.BICUBIC)
    stack = np.stack([raw_hi, closed_hi, tx_hi, ty_hi], axis=-1).astype(np.float32)
    remapped, _, _ = bubble_inflation_remap(stack, cfg)
    raw_r = np.clip(remapped[..., 0], 0.0, 1.0)
    closed_r = np.clip(remapped[..., 1], 0.0, 1.0)
    tx_r, ty_r = normalize_vectors(remapped[..., 2], remapped[..., 3])
    nx_r, ny_r = normalize_vectors(-ty_r, tx_r)
    normal = np.stack([nx_r, ny_r], axis=-1).astype(np.float32)
    return raw_r, closed_r, tx_r, ty_r, normal


def reconstruct_with_edges(
    bubble_rgb: np.ndarray,
    a3: np.ndarray,
    edge_closed: np.ndarray,
    tangent_x: np.ndarray,
    tangent_y: np.ndarray,
    cfg: EdgeClosureConfig,
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    local_edges = edge_mask(bubble_rgb, cfg.edge_threshold)[..., 0]
    if cfg.edge_recalculate:
        edges = np.clip(edge_closed * 0.78 + local_edges * 0.22, 0.0, 1.0)
    else:
        edges = local_edges

    blur = gaussian_blur_array(bubble_rgb, cfg.detail_radius)
    residual = bubble_rgb - blur
    edge3 = edges[..., None]

    structure = np.clip(bubble_rgb + residual * (cfg.structure_strength * edge3), 0.0, 1.0)
    tangent_smoothed = directional_sample_average(structure, tangent_x, tangent_y, cfg.edge_tangent_smoothing)
    structure = np.clip(
        structure * (1.0 - edge3 * cfg.edge_closure_strength)
        + tangent_smoothed * (edge3 * cfg.edge_closure_strength),
        0.0,
        1.0,
    )

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
    texture_layer = texture * cfg.texture_strength * (0.35 + 0.65 * edge3) * a3_norm

    candidate = structure + residual * cfg.residual_gain * (0.35 + edge3 * cfg.edge_confidence) + texture_layer
    return np.clip(candidate, 0.0, 1.0), edges, residual, texture_layer


def normal_sample_coords(shape: Tuple[int, int], nx: np.ndarray, ny: np.ndarray, radius: float) -> Tuple[np.ndarray, np.ndarray]:
    h, w = shape
    yy, xx = np.meshgrid(np.arange(h, dtype=np.float32), np.arange(w, dtype=np.float32), indexing="ij")
    return xx + nx * radius, yy + ny * radius


def edge_guided_closure_guard(base_rgb: np.ndarray, candidate: np.ndarray, edges: np.ndarray, normal: np.ndarray, cfg: EdgeClosureConfig) -> np.ndarray:
    if cfg.closure_strength <= 0:
        return candidate
    if cfg.anti_ringing_radius > 0:
        anti_ring_base = gaussian_blur_array(candidate, cfg.anti_ringing_radius)
        candidate = candidate * 0.82 + anti_ring_base * 0.18

    edge3 = edges[..., None]
    nx = normal[..., 0]
    ny = normal[..., 1]
    normal_forward = bilinear_sample(candidate, *normal_sample_coords(candidate.shape[:2], nx, ny, 0.75))
    normal_back = bilinear_sample(candidate, *normal_sample_coords(candidate.shape[:2], nx, ny, -0.75))
    cross_delta = np.mean(np.abs(normal_forward - normal_back), axis=-1, keepdims=True)
    normal_penalty = np.clip(cross_delta / max(1e-6, cfg.halo_limit * 2.0), 0.0, 1.0)

    limit = cfg.halo_limit * (0.45 + edge3 * (1.0 - cfg.edge_normal_preserve * 0.35))
    limit = limit * (1.0 - normal_penalty * cfg.edge_normal_preserve * 0.45)
    clipped = base_rgb + np.clip(candidate - base_rgb, -limit, limit)
    return np.clip(candidate * (1.0 - cfg.closure_strength) + clipped * cfg.closure_strength, 0.0, 1.0)


def save_tangent_debug(path: Path, tx: np.ndarray, ty: np.ndarray, edges: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rgb = np.stack([
        np.clip(tx * 0.5 + 0.5, 0.0, 1.0),
        np.clip(ty * 0.5 + 0.5, 0.0, 1.0),
        np.clip(edges, 0.0, 1.0),
    ], axis=-1)
    float_to_image(rgb, mode="RGB").save(path)


def upscale_image(input_path: Path, output_path: Path, cfg: EdgeClosureConfig, debug_dir: Optional[Path] = None, compare_path: Optional[Path] = None) -> None:
    source = Image.open(input_path).convert("RGB")
    source_rgb = image_to_float(source)
    cleaned = artifact_sink(source_rgb, cfg)

    src_w, src_h = source.size
    out_w = max(1, int(round(src_w * cfg.scale)))
    out_h = max(1, int(round(src_h * cfg.scale)))
    out_size = (out_w, out_h)

    if cfg.edge_recalculate:
        edge_raw, edge_closed, tangent_x, tangent_y, normal = remap_edge_field(cleaned, out_size, cfg)
    else:
        edge_raw = np.zeros((out_h, out_w), dtype=np.float32)
        edge_closed = np.zeros((out_h, out_w), dtype=np.float32)
        tangent_x = np.ones((out_h, out_w), dtype=np.float32)
        tangent_y = np.zeros((out_h, out_w), dtype=np.float32)
        normal = np.stack([np.zeros((out_h, out_w), dtype=np.float32), np.ones((out_h, out_w), dtype=np.float32)], axis=-1)

    base_img = float_to_image(cleaned, mode="RGB").resize(out_size, RESAMPLE_MODES[cfg.resample])
    base_rgb = image_to_float(base_img)
    bubble_rgb, inflation, a3 = bubble_inflation_remap(base_rgb, cfg)
    candidate, edges, residual, texture_layer = reconstruct_with_edges(bubble_rgb, a3, edge_closed, tangent_x, tangent_y, cfg)
    guarded = edge_guided_closure_guard(bubble_rgb, candidate, edges, normal, cfg)
    final_rgb = sharpen(guarded, cfg)

    save_rgb(output_path, final_rgb, quality=cfg.quality)

    if debug_dir:
        debug_dir.mkdir(parents=True, exist_ok=True)
        save_rgb(debug_dir / "01_source.png", source_rgb, quality=cfg.quality)
        save_rgb(debug_dir / "02_artifact_sink.png", cleaned, quality=cfg.quality)
        save_gray(debug_dir / "03_edge_raw_low_to_high.png", edge_raw)
        save_gray(debug_dir / "04_edge_closed_recalculated.png", edge_closed)
        save_tangent_debug(debug_dir / "05_edge_tangent_field.png", tangent_x, tangent_y, edge_closed)
        save_rgb(debug_dir / "06_base_upscale.png", base_rgb, quality=cfg.quality)
        save_rgb(debug_dir / "07_bubble_inflation.png", bubble_rgb, quality=cfg.quality)
        save_gray(debug_dir / "08_bubble_field.png", inflation)
        save_gray(debug_dir / "09_a3_field.png", a3)
        save_gray(debug_dir / "10_edge_confidence_used.png", edges)
        save_rgb(debug_dir / "11_candidate_reconstruction.png", candidate, quality=cfg.quality)
        save_rgb(debug_dir / "12_texture_layer_visual.png", np.clip(texture_layer * 12.0 + 0.5, 0.0, 1.0), quality=cfg.quality)
        save_rgb(debug_dir / "13_final.png", final_rgb, quality=cfg.quality)
        with (debug_dir / "config.json").open("w", encoding="utf-8") as f:
            json.dump(asdict(cfg), f, indent=2)

    if compare_path:
        make_compare(source_rgb, final_rgb, compare_path, quality=cfg.quality)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="MCIFT-inspired Bubble Edge Closure Upscaler")
    parser.add_argument("input", type=Path, help="Input image path")
    parser.add_argument("output", type=Path, help="Output image path")
    parser.add_argument("--preset", type=Path, default=None, help="JSON preset to load before CLI overrides")

    for field in fields(EdgeClosureConfig):
        name = field.name
        if name in {"threefold", "texture_seed", "edge_recalculate"}:
            continue
        parser.add_argument("--" + name.replace("_", "-"), dest=name, default=None)

    parser.add_argument("--texture-seed", type=int, default=None, help="Random seed for synthetic residual texture")
    threefold_group = parser.add_mutually_exclusive_group()
    threefold_group.add_argument("--threefold", dest="threefold", action="store_true", default=None, help="Enable threefold modulation")
    threefold_group.add_argument("--no-threefold", dest="threefold", action="store_false", help="Disable threefold modulation")
    edge_group = parser.add_mutually_exclusive_group()
    edge_group.add_argument("--edge-recalculate", dest="edge_recalculate", action="store_true", default=None, help="Enable edge closure recalculation")
    edge_group.add_argument("--no-edge-recalculate", dest="edge_recalculate", action="store_false", help="Disable edge closure recalculation")

    parser.add_argument("--save-debug", type=Path, default=None, help="Directory for intermediate outputs")
    parser.add_argument("--compare", nargs="?", const="auto", default=None, help="Save source/final comparison. Optionally provide a path.")
    parser.add_argument("--print-config", action="store_true", help="Print final merged configuration")
    return parser.parse_args()


def cli_values_from_args(args: argparse.Namespace) -> Dict[str, Any]:
    cfg_keys = {f.name for f in fields(EdgeClosureConfig)}
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
