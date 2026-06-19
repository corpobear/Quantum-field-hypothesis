import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 900
FRAMES = 132
FPS_MS = 42
BG = (6, 9, 16)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
CUBE = (94, 214, 255)
NODE = (255, 218, 126)
FABRIC_A = (92, 255, 224)
FABRIC_B = (170, 130, 255)
PULL = (255, 235, 122)


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
CENTER = np.array([SIZE / 2, SIZE / 2 + 52])
SCALE = 112


def project(point):
    p = ROT @ np.array(point, dtype=float)
    depth = 740 + p[2] * 60
    perspective = 740 / depth
    xy = CENTER + perspective * SCALE * np.array([p[0], -p[1]])
    return xy, p[2]


def fabric_z(x, y, t):
    twist = 0.42 * math.sin(1.35 * x - 1.15 * y + 2 * math.pi * t)
    saddle = 0.20 * x * y
    cube_pulls = 0.0
    for cx in [-1, 0, 1]:
        for cy in [-1, 0, 1]:
            d2 = (x - cx) ** 2 + (y - cy) ** 2
            phase = 2 * math.pi * t + 0.7 * cx - 0.45 * cy
            cube_pulls += 0.16 * math.exp(-d2 / 0.18) * math.sin(phase)
    return twist + saddle + cube_pulls


def fabric_point(x, y, t):
    z = fabric_z(x, y, t)
    # A gentle in-plane twist, so the fabric looks woven through the lattice.
    angle = 0.18 * math.sin(2 * math.pi * t + 0.8 * x) + 0.10 * y
    ca, sa = math.cos(angle), math.sin(angle)
    tx = ca * x - sa * y
    ty = sa * x + ca * y
    return np.array([tx, ty, z])


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((30, 24), "16 - Spacetime Fabric Twists Through Cubes", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (30, 60),
        "A visible fabric scaffold twists and turns where cube-to-cube connections pull on it.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    for r in range(130, 390, 58):
        draw.ellipse((CENTER[0] - r, CENTER[1] - r, CENTER[0] + r, CENTER[1] + r), outline=(*GRID, 55), width=1)
    return img


def draw_fabric(draw, t):
    coords = np.linspace(-1.55, 1.55, 23)
    # Draw back-to-front-ish by one direction first, then crossing threads.
    for idx, y in enumerate(coords):
        pts = [tuple(project(fabric_point(x, y, t))[0]) for x in coords]
        color = FABRIC_A if idx % 2 == 0 else (125, 240, 255)
        for p1, p2 in zip(pts, pts[1:]):
            draw.line((*p1, *p2), fill=(*color, 210), width=3)
            draw.line((*p1, *p2), fill=(255, 255, 255, 42), width=1)

    for idx, x in enumerate(coords):
        pts = [tuple(project(fabric_point(x, y, t))[0]) for y in coords]
        color = FABRIC_B if idx % 2 == 0 else (145, 155, 255)
        for p1, p2 in zip(pts, pts[1:]):
            draw.line((*p1, *p2), fill=(*color, 185), width=2)

    # Highlight local pulls at the 3x3 cube-cell centers.
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            p = project(fabric_point(x, y, t))[0]
            pulse = 0.5 + 0.5 * math.sin(2 * math.pi * t + x - y)
            rr = 5 + 5 * pulse
            draw.ellipse((p[0] - rr, p[1] - rr, p[0] + rr, p[1] + rr), fill=(*PULL, 150))


def draw_cubic_grid(draw):
    coords = [-1, 0, 1]
    points = [np.array([x, y, z], dtype=float) for x in coords for y in coords for z in coords]
    segments = []
    for a in coords:
        for b in coords:
            segments.extend(
                [
                    (np.array([-1, a, b]), np.array([1, a, b])),
                    (np.array([a, -1, b]), np.array([a, 1, b])),
                    (np.array([a, b, -1]), np.array([a, b, 1])),
                ]
            )
    for a, b in segments:
        pa, _ = project(a)
        pb, _ = project(b)
        draw.line((*pa, *pb), fill=(*CUBE, 82), width=2)
    for p3 in points:
        p, _ = project(p3)
        color = NODE if np.linalg.norm(p3) < 0.1 else CUBE
        radius = 7 if np.linalg.norm(p3) < 0.1 else 4
        draw.ellipse((p[0] - radius, p[1] - radius, p[0] + radius, p[1] + radius), fill=(*color, 205))


def draw_connection_pulls(draw, t):
    # Show cube-to-cube connection forces tugging the fabric.
    pairs = [
        (np.array([-1, -1, 0]), np.array([0, 0, 0])),
        (np.array([1, -1, 0]), np.array([0, 0, 0])),
        (np.array([-1, 1, 0]), np.array([0, 0, 0])),
        (np.array([1, 1, 0]), np.array([0, 0, 0])),
        (np.array([0, 0, -1]), np.array([0, 0, 1])),
    ]
    for idx, (a, b) in enumerate(pairs):
        pa = project(a)[0]
        pb = project(b)[0]
        alpha = int(90 + 80 * (0.5 + 0.5 * math.sin(2 * math.pi * t + idx)))
        draw.line((*pa, *pb), fill=(*PULL, alpha), width=2)


def annotations(draw):
    draw.text((30, SIZE - 82), "fabric: woven spacetime scaffold, not just guide lines", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text(
        (30, SIZE - 58),
        "twist: cube-to-cube connections tug the fabric and change local curvature",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )
    draw.text((30, SIZE - 34), "grid: the 3x3x3 cubic cells remain visible underneath the fabric", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_fabric(draw, t)
        draw_cubic_grid(draw)
        draw_connection_pulls(draw, t)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "16_spacetime_fabric_twist.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[86].save(OUT_DIR / "16_spacetime_fabric_twist_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("16_spacetime_fabric_twist_preview.png")


if __name__ == "__main__":
    main()
