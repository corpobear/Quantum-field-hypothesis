import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 900
BG = (7, 10, 17)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
CUBE = (120, 230, 255)
NODE = (255, 218, 126)
TIME = (255, 235, 122)
LIGHT = (150, 190, 255)
SCAFFOLD = (176, 142, 255)


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(28)
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
CENTER = np.array([SIZE / 2, SIZE / 2 + 40])
SCALE = 112


def project(point):
    p = ROT @ np.array(point, dtype=float)
    depth = 720 + p[2] * 58
    perspective = 720 / depth
    xy = CENTER + perspective * SCALE * np.array([p[0], -p[1]])
    return xy, p[2]


def base_image():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((30, 24), "15 - 3x3x3 Cubic Grid With Spacetime Scaffold", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (30, 60),
        "Static cubic lattice: 27 cells embedded in time, light-cone, and diagonal causal scaffold.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    for r in range(130, 390, 58):
        draw.ellipse((CENTER[0] - r, CENTER[1] - r, CENTER[0] + r, CENTER[1] + r), outline=(*GRID, 62), width=1)
    return img


def draw_axes(draw):
    axes = [
        (np.array([1.85, 0, 0]), "x", (255, 110, 110)),
        (np.array([0, 1.85, 0]), "y", (110, 255, 170)),
        (np.array([0, 0, 1.85]), "z", (120, 170, 255)),
    ]
    origin, _ = project(np.array([-1.35, -1.35, -1.35]))
    for vec, label, color in axes:
        end, _ = project(np.array([-1.35, -1.35, -1.35]) + vec)
        draw.line((*origin, *end), fill=(*color, 190), width=3)
        draw.text(tuple(end + np.array([6, -8])), label, fill=color, font=FONT_SMALL)

    # Time axis drawn as a separate scaffold through the center.
    p0, _ = project(np.array([0, 0, -1.75]))
    p1, _ = project(np.array([0, 0, 1.75]))
    draw.line((*p0, *p1), fill=(*TIME, 155), width=3)
    draw.text(tuple(p1 + np.array([8, -12])), "t", fill=TIME, font=FONT_SMALL)


def draw_spacetime_scaffold(draw):
    # Light-cone style nested surfaces centered on the middle event.
    for radius, alpha in [(0.65, 42), (1.05, 58), (1.45, 48)]:
        pts = []
        for i in range(96):
            a = 2 * math.pi * i / 96
            p = np.array([radius * math.cos(a), radius * math.sin(a), 0.0])
            xy, _ = project(p)
            pts.append(tuple(xy))
        for p1, p2 in zip(pts, pts[1:] + pts[:1]):
            draw.line((*p1, *p2), fill=(*LIGHT, alpha), width=1)

    # Body-diagonal causal rays.
    diagonals = [
        np.array([1, 1, 1]),
        np.array([1, -1, -1]),
        np.array([-1, 1, -1]),
        np.array([-1, -1, 1]),
    ]
    center, _ = project(np.array([0.0, 0.0, 0.0]))
    for d in diagonals:
        d = d / np.linalg.norm(d)
        p_plus, _ = project(1.72 * d)
        p_minus, _ = project(-1.72 * d)
        draw.line((*p_minus, *p_plus), fill=(*SCAFFOLD, 115), width=2)
        draw.ellipse((p_plus[0] - 4, p_plus[1] - 4, p_plus[0] + 4, p_plus[1] + 4), fill=(*SCAFFOLD, 160))
    draw.ellipse((center[0] - 6, center[1] - 6, center[0] + 6, center[1] + 6), fill=(*TIME, 210))


def draw_cubic_grid(draw):
    coords = [-1, 0, 1]
    points = [np.array([x, y, z], dtype=float) for x in coords for y in coords for z in coords]

    # Lines along each lattice direction.
    segments = []
    for fixed_a in coords:
        for fixed_b in coords:
            segments.extend(
                [
                    (np.array([-1, fixed_a, fixed_b]), np.array([1, fixed_a, fixed_b])),
                    (np.array([fixed_a, -1, fixed_b]), np.array([fixed_a, 1, fixed_b])),
                    (np.array([fixed_a, fixed_b, -1]), np.array([fixed_a, fixed_b, 1])),
                ]
            )

    depth_segments = []
    for a, b in segments:
        pa, za = project(a)
        pb, zb = project(b)
        depth_segments.append(((za + zb) / 2, pa, pb))
    depth_segments.sort(key=lambda item: item[0])
    for _, pa, pb in depth_segments:
        draw.line((*pa, *pb), fill=(*CUBE, 145), width=2)

    # Nodes.
    projected = []
    for p in points:
        xy, z = project(p)
        projected.append((z, xy, np.linalg.norm(p)))
    projected.sort(key=lambda item: item[0])
    for _, xy, dist in projected:
        radius = 5 if dist > 0 else 8
        alpha = 190 if dist > 0 else 245
        color = NODE if dist < 0.1 else CUBE
        draw.ellipse((xy[0] - radius, xy[1] - radius, xy[0] + radius, xy[1] + radius), fill=(*color, alpha))


def draw_labels(draw):
    draw.text((30, SIZE - 82), "static view: no animation, no shell motion", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text(
        (30, SIZE - 58),
        "cubic grid: 3 x 3 x 3 cell centers / scaffold: time axis, light-cone rings, body-diagonal causal rays",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )
    draw.text((30, SIZE - 34), "purpose: establish the cube geometry before deriving cell-resolved mechanics", fill=(180, 235, 245), font=FONT_SMALL)


def make_visual():
    img = base_image()
    draw = ImageDraw.Draw(img, "RGBA")
    draw_spacetime_scaffold(draw)
    draw_cubic_grid(draw)
    draw_axes(draw)
    draw_labels(draw)
    png = OUT_DIR / "15_3x3x3_cubic_grid_spacetime_scaffold.png"
    gif = OUT_DIR / "15_3x3x3_cubic_grid_spacetime_scaffold.gif"
    img.save(png)
    img.save(gif, save_all=True, append_images=[], duration=1200, loop=0)
    return png, gif


def main():
    png, gif = make_visual()
    print(png.name)
    print(gif.name)


if __name__ == "__main__":
    main()
