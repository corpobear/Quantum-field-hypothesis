import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 760
FRAMES = 132
FPS_MS = 42
BG = (7, 10, 17)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
CORE = (255, 218, 126)
EDGE = (120, 230, 255)
FACE = (62, 143, 255)
CONNECTOR = (255, 235, 122)
KNOT = (255, 146, 96)
HEAT = (185, 128, 255)


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


def project(point, rot):
    p = rot @ point
    depth = 620 + p[2]
    perspective = 620 / depth
    xy = np.array([SIZE / 2, SIZE / 2 + 28]) + perspective * np.array([p[0], -p[1]])
    return xy, p[2]


VERTICES = [
    np.array([x, y, z], dtype=float)
    for x in (-1, 1)
    for y in (-1, 1)
    for z in (-1, 1)
]

EDGES = []
for i, a in enumerate(VERTICES):
    for j, b in enumerate(VERTICES):
        if j > i and np.sum(np.abs(a - b) > 0.1) == 1:
            EDGES.append((a, b))

FACES = [
    (np.array([1, 0, 0], dtype=float), [np.array([1, y, z], dtype=float) for y, z in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]),
    (np.array([-1, 0, 0], dtype=float), [np.array([-1, y, z], dtype=float) for y, z in [(-1, -1), (-1, 1), (1, 1), (1, -1)]]),
    (np.array([0, 1, 0], dtype=float), [np.array([x, 1, z], dtype=float) for x, z in [(-1, -1), (-1, 1), (1, 1), (1, -1)]]),
    (np.array([0, -1, 0], dtype=float), [np.array([x, -1, z], dtype=float) for x, z in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]),
    (np.array([0, 0, 1], dtype=float), [np.array([x, y, 1], dtype=float) for x, y in [(-1, -1), (1, -1), (1, 1), (-1, 1)]]),
    (np.array([0, 0, -1], dtype=float), [np.array([x, y, -1], dtype=float) for x, y in [(-1, -1), (-1, 1), (1, 1), (1, -1)]]),
]


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((26, 22), "14 - 3D Cubic Model", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (26, 56),
        "Center core, six face connectors, and projected activation inside a rotating cube.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    for r in range(120, 340, 54):
        draw.ellipse((SIZE / 2 - r, SIZE / 2 + 28 - r, SIZE / 2 + r, SIZE / 2 + 28 + r), outline=(*GRID, 55), width=1)
    return img


def scale_point(point):
    return 172 * point


def draw_faces(draw, rot, t):
    face_items = []
    for idx, (normal, corners) in enumerate(FACES):
        projected = []
        depths = []
        for c in corners:
            xy, z = project(scale_point(c), rot)
            projected.append(tuple(xy))
            depths.append(z)
        n_depth = float((rot @ normal)[2])
        pulse = 0.5 + 0.5 * math.sin(2 * math.pi * (0.55 * t + idx / 6))
        alpha = int(20 + 58 * pulse + 28 * max(0, n_depth))
        face_items.append((sum(depths) / len(depths), projected, alpha))
    face_items.sort(key=lambda item: item[0])
    for depth, poly, alpha in face_items:
        draw.polygon(poly, fill=(*FACE, alpha))


def draw_edges(draw, rot):
    for a, b in EDGES:
        p1, _ = project(scale_point(a), rot)
        p2, _ = project(scale_point(b), rot)
        draw.line((*p1, *p2), fill=(*EDGE, 205), width=3)


def draw_connectors(draw, rot, t):
    center, _ = project(np.array([0.0, 0.0, 0.0]), rot)
    for idx, (normal, corners) in enumerate(FACES):
        face_center_3d = scale_point(normal)
        p, depth = project(face_center_3d, rot)
        pulse = 0.5 + 0.5 * math.sin(2 * math.pi * (1.15 * t + idx / 6))
        draw.line((*center, *p), fill=(*CONNECTOR, int(76 + 98 * pulse)), width=2)
        radius = 4 + 5 * pulse
        draw.ellipse((p[0] - radius, p[1] - radius, p[0] + radius, p[1] + radius), fill=(*CONNECTOR, 200))


def draw_internal_three_knot(draw, rot, t):
    points = []
    for k in range(3):
        angle = 2 * math.pi * (k / 3 + 0.22 * t)
        z = 0.32 * math.sin(2 * math.pi * (t + k / 3))
        p3 = scale_point(np.array([0.52 * math.cos(angle), 0.52 * math.sin(angle), z]))
        p2, _ = project(p3, rot)
        points.append(p2)
    for p1, p2 in zip(points, points[1:] + points[:1]):
        draw.line((*p1, *p2), fill=(*KNOT, 180), width=2)
    for p in points:
        draw.ellipse((p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7), fill=(*KNOT, 220))


def draw_core(draw, rot, t):
    center, _ = project(np.array([0.0, 0.0, 0.0]), rot)
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 2.2 * t)
    radius = 24 + 5 * pulse
    for scale, alpha in [(3.8, 22), (2.4, 42), (1.5, 72)]:
        rr = radius * scale
        draw.ellipse((center[0] - rr, center[1] - rr, center[0] + rr, center[1] + rr), fill=(*CORE, alpha))
    draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=(*CORE, 235))
    inner = radius * 0.34
    draw.ellipse((center[0] - inner, center[1] - inner, center[0] + inner, center[1] + inner), fill=(255, 252, 220, 245))


def draw_activation_rays(draw, rot, t):
    for k in range(12):
        angle = 2 * math.pi * (k / 12 + 0.08 * t)
        p1 = scale_point(np.array([0.15 * math.cos(angle), 0.15 * math.sin(angle), 0.0]))
        p2 = scale_point(np.array([0.95 * math.cos(angle), 0.95 * math.sin(angle), 0.35 * math.sin(3 * angle + 2 * math.pi * t)]))
        a, _ = project(p1, rot)
        b, _ = project(p2, rot)
        draw.line((*a, *b), fill=(*HEAT, 45), width=1)


def annotations(draw):
    draw.text((26, SIZE - 58), "state: cubic model replaces the shell-only view", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text((26, SIZE - 34), "geometry: center core connects to six faces while the stable three-knot projection moves inside", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        rot = rotation_matrix([1, 0, 0], math.radians(62)) @ rotation_matrix([0, 1, 0], math.radians(25)) @ rotation_matrix(
            [0, 0, 1], 2 * math.pi * 0.32 * t
        )
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_faces(draw, rot, t)
        draw_activation_rays(draw, rot, t)
        draw_connectors(draw, rot, t)
        draw_internal_three_knot(draw, rot, t)
        draw_edges(draw, rot)
        draw_core(draw, rot, t)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "14_3d_cubic_model.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[86].save(OUT_DIR / "14_3d_cubic_model_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("14_3d_cubic_model_preview.png")


if __name__ == "__main__":
    main()
