import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 900
FRAMES = 96
FPS_MS = 42
BG = (6, 9, 16)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
FABRIC_A = (92, 255, 224)
FABRIC_B = (178, 132, 255)
CORE = (255, 218, 126)
GRAVITY = (176, 142, 255)
SHELL = (120, 230, 255)
BAND = (255, 235, 122)
TENSION = (255, 150, 96)


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(27)
FONT_SMALL = font(16)


def rotation_matrix(axis, angle):
    axis = np.array(axis, dtype=float)
    axis = axis / np.linalg.norm(axis)
    x, y, z = axis
    c = math.cos(angle)
    s = math.sin(angle)
    C = 1 - c
    return np.array(
        [
            [c + x * x * C, x * y * C - z * s, x * z * C + y * s],
            [y * x * C + z * s, c + y * y * C, y * z * C - x * s],
            [z * x * C - y * s, z * y * C + x * s, c + z * z * C],
        ]
    )


ROT = rotation_matrix([1, 0, 0], math.radians(62)) @ rotation_matrix([0, 0, 1], math.radians(-35))
CENTER = np.array([SIZE / 2, SIZE / 2 + 54])
SCALE = 116


def project(point):
    p = ROT @ np.array(point, dtype=float)
    depth = 760 + p[2] * 62
    perspective = 760 / depth
    xy = CENTER + perspective * SCALE * np.array([p[0], -p[1]])
    return xy, p[2]


def gravity_strength(x, y, t):
    r2 = x * x + y * y
    base = math.exp(-r2 / 1.15)
    ring = 0.5 + 0.5 * math.sin(9.0 * math.sqrt(r2 + 0.02) - 2 * math.pi * 1.4 * t)
    return base * (0.55 + 0.45 * ring)


def shell_band_strength(x, y, t):
    angle = math.atan2(y, x)
    radius = math.sqrt(x * x + y * y)
    threefold = 0.5 + 0.5 * math.cos(3 * angle + 0.35)
    band = math.exp(-((radius - 1.18) ** 2) / (2 * 0.13 * 0.13))
    lock = 0.5 + 0.5 * math.sin(2 * math.pi * 0.6 * t + 3 * angle)
    return band * (0.45 + 0.45 * threefold + 0.10 * lock)


def fabric_point(x, y, t):
    g = gravity_strength(x, y, t)
    s = shell_band_strength(x, y, t)
    z = 0.16 * x * y
    z += 0.48 * g
    z += 0.28 * s
    z += 0.08 * math.sin(2 * math.pi * t + 3 * x - 2 * y)
    inward = 0.10 * g
    tx = x * (1 - inward)
    ty = y * (1 - inward)
    twist = 0.10 * s * math.sin(2 * math.pi * t)
    ca, sa = math.cos(twist), math.sin(twist)
    return np.array([ca * tx - sa * ty, sa * tx + ca * ty, z])


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((30, 24), "19 - Step 8 Gravity Overlay on Spacetime Fabric", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (30, 58),
        "Gravity-stabilized shell bands from step 8 tension and warp the fabric scaffold.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    for r in range(130, 390, 58):
        draw.ellipse((CENTER[0] - r, CENTER[1] - r, CENTER[0] + r, CENTER[1] + r), outline=(*GRID, 52), width=1)
    return img


def draw_step8_overlay(draw, t):
    # Gravity field rings.
    for idx, radius in enumerate(np.linspace(0.34, 1.62, 7)):
        alpha = int(30 + 72 * (0.5 + 0.5 * math.sin(8 * radius - 2 * math.pi * t)))
        pts = []
        for a in np.linspace(0, 2 * math.pi, 120):
            p, _ = project(np.array([radius * math.cos(a), radius * math.sin(a), 0.52 * math.exp(-radius)]))
            pts.append(tuple(p))
        for p1, p2 in zip(pts, pts[1:] + pts[:1]):
            draw.line((*p1, *p2), fill=(*GRAVITY, alpha), width=2)

    # Stabilized threefold shell bands.
    for k in range(3):
        angle = 2 * math.pi * k / 3 + 0.12 * math.sin(2 * math.pi * 0.4 * t)
        pts = []
        for u in np.linspace(-0.32, 0.32, 60):
            a = angle + u
            radius = 1.25 + 0.04 * math.sin(9 * u + 2 * math.pi * t)
            p, _ = project(np.array([radius * math.cos(a), radius * math.sin(a), 0.23]))
            pts.append(tuple(p))
        for p1, p2 in zip(pts, pts[1:]):
            draw.line((*p1, *p2), fill=(*BAND, 205), width=5)


def draw_fabric(draw, t):
    coords = np.linspace(-1.55, 1.55, 23)
    for idx, y in enumerate(coords):
        pts = [tuple(project(fabric_point(float(x), float(y), t))[0]) for x in coords]
        color = FABRIC_A if idx % 2 == 0 else (130, 250, 255)
        for p1, p2 in zip(pts, pts[1:]):
            draw.line((*p1, *p2), fill=(*color, 205), width=3)
            draw.line((*p1, *p2), fill=(255, 255, 255, 35), width=1)

    for idx, x in enumerate(coords):
        pts = [tuple(project(fabric_point(float(x), float(y), t))[0]) for y in coords]
        color = FABRIC_B if idx % 2 == 0 else (145, 155, 255)
        for p1, p2 in zip(pts, pts[1:]):
            draw.line((*p1, *p2), fill=(*color, 165), width=2)


def draw_tension_vectors(draw, t):
    for x, y in [(-1, -1), (1, -1), (-1, 1), (1, 1), (0, 1), (1, 0), (-1, 0), (0, -1)]:
        start = project(fabric_point(x, y, t))[0]
        end = project(fabric_point(x * 0.72, y * 0.72, t))[0]
        draw.line((*start, *end), fill=(*TENSION, 160), width=3)
        draw.ellipse((start[0] - 4, start[1] - 4, start[0] + 4, start[1] + 4), fill=(*TENSION, 190))


def draw_core(draw):
    center, _ = project(np.array([0.0, 0.0, 0.58]))
    for scale, alpha in [(4.0, 22), (2.5, 42), (1.6, 72)]:
        rr = 24 * scale
        draw.ellipse((center[0] - rr, center[1] - rr, center[0] + rr, center[1] + rr), fill=(*CORE, alpha))
    draw.ellipse((center[0] - 25, center[1] - 25, center[0] + 25, center[1] + 25), fill=(*CORE, 235))


def annotations(draw):
    draw.text((30, SIZE - 82), "overlay: step 8 gravity rings + stabilized shell bands", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text((30, SIZE - 58), "fabric response: inward tension near core, lifted bands where shell pattern locks", fill=(180, 235, 245), font=FONT_SMALL)
    draw.text((30, SIZE - 34), "interpretation: gravity and shell memory influence spacetime fabric curvature", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_step8_overlay(draw, t)
        draw_fabric(draw, t)
        draw_tension_vectors(draw, t)
        draw_core(draw)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "19_step8_fabric_influence_overlay.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[62].save(OUT_DIR / "19_step8_fabric_influence_overlay_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("19_step8_fabric_influence_overlay_preview.png")


if __name__ == "__main__":
    main()
