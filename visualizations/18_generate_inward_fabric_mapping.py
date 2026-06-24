import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 720
FRAMES = 48
FPS_MS = 42
BG = (6, 9, 16)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
FABRIC_A = (92, 255, 224)
FABRIC_B = (178, 132, 255)
CORE = (255, 218, 126)
SHELL = (72, 148, 255)
INFLOW = (255, 235, 122)
ANCHOR = (255, 150, 96)


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


def knot_dirs(t):
    wobble = 0.16 * math.sin(2 * math.pi * 0.21 * t)
    dirs = []
    for k in range(3):
        phi = 2 * math.pi * k / 3 + wobble
        theta = math.pi / 2 + 0.24 * math.sin(2 * math.pi * (0.27 * t + k / 3))
        dirs.append(np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)]))
    return dirs


def shell_radius(theta, phi, t):
    n = np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)])
    radius = 174
    dent = 0.0
    for kd in knot_dirs(t):
        dot = max(-1.0, min(1.0, float(np.dot(n, kd))))
        angular = math.acos(dot)
        dent += 0.075 * math.exp(-(angular * angular) / (2 * 0.25 * 0.25))
    ripple = 0.020 * math.sin(3 * phi + 2.0 * math.cos(theta) + 2 * math.pi * t)
    return radius * (1 - dent + ripple)


def surface_point(theta, phi, t):
    r = shell_radius(theta, phi, t)
    return r * np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)])


def project(point, rot):
    p = rot @ point
    depth = 640 + p[2]
    perspective = 640 / depth
    xy = np.array([SIZE / 2, SIZE / 2 + 30]) + perspective * np.array([p[0], -p[1]])
    return xy, p[2]


def fabric_inward_point(theta, phi, t, u):
    # u = 0 at shell, u = 1 toward core. Inference: fabric follows radial
    # geodesic-like pull paths, with twisting from the projected three-knot anchors.
    outer = surface_point(theta, phi, t)
    n = outer / np.linalg.norm(outer)
    twist_axis = np.array([0.0, 0.0, 1.0])
    twist = 0.35 * u * math.sin(2 * math.pi * t + 3 * phi)
    rot = rotation_matrix(twist_axis, twist)
    radius_scale = (1 - u) ** 1.35
    inward = rot @ (outer * radius_scale)
    wave = n * (8 * math.sin(6 * u + 2 * math.pi * t + 2 * phi) * (1 - u))
    return inward + wave


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((30, 24), "18 - Inward Mapping of Spacetime Fabric", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (30, 60),
        "Inferred map: fabric on the cone-sphere is pulled inward along radial connection paths.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    for r in range(100, 310, 52):
        draw.ellipse((SIZE / 2 - r, SIZE / 2 + 30 - r, SIZE / 2 + r, SIZE / 2 + 30 + r), outline=(*GRID, 54), width=1)
    return img


def draw_outer_shell(draw, rot, t):
    for theta in np.linspace(0.28, math.pi - 0.28, 5):
        pts = []
        for phi in np.linspace(0, 2 * math.pi, 38):
            xy, z = project(surface_point(float(theta), float(phi), t), rot)
            pts.append((tuple(xy), z))
        for (p1, z1), (p2, z2) in zip(pts, pts[1:]):
            alpha = int(70 + 60 * max(0, min(1, (z1 + 180) / 360)))
            draw.line((*p1, *p2), fill=(*SHELL, alpha), width=2)


def draw_inward_fabric(draw, rot, t):
    # A few latitude and longitude fabric strands are continued inward.
    latitudes = np.linspace(0.40, math.pi - 0.40, 4)
    longitudes = np.linspace(0, 2 * math.pi, 6, endpoint=False)

    for idx, theta in enumerate(latitudes):
        color = FABRIC_A if idx % 2 == 0 else (130, 250, 255)
        for phi in np.linspace(0, 2 * math.pi, 7, endpoint=False):
            pts = []
            for u in np.linspace(0, 0.86, 18):
                xy, z = project(fabric_inward_point(float(theta), float(phi), t, float(u)), rot)
                pts.append((tuple(xy), z, u))
            for (p1, z1, u1), (p2, z2, u2) in zip(pts, pts[1:]):
                alpha = int(175 * (1 - 0.62 * u1))
                width = 3 if u1 < 0.35 else 2
                draw.line((*p1, *p2), fill=(*color, alpha), width=width)

    for idx, phi in enumerate(longitudes):
        color = FABRIC_B if idx % 2 == 0 else (145, 155, 255)
        for theta in np.linspace(0.48, math.pi - 0.48, 4):
            pts = []
            for u in np.linspace(0, 0.82, 16):
                xy, z = project(fabric_inward_point(float(theta), float(phi), t, float(u)), rot)
                pts.append((tuple(xy), z, u))
            for (p1, z1, u1), (p2, z2, u2) in zip(pts, pts[1:]):
                alpha = int(135 * (1 - 0.58 * u1))
                draw.line((*p1, *p2), fill=(*color, alpha), width=2)


def draw_anchor_paths(draw, rot, t):
    center, _ = project(np.array([0.0, 0.0, 0.0]), rot)
    for kd in knot_dirs(t):
        theta = math.acos(kd[2])
        phi = math.atan2(kd[1], kd[0])
        outer = surface_point(theta, phi, t)
        anchor, _ = project(outer, rot)
        mid, _ = project(outer * 0.48, rot)
        draw.line((*anchor, *mid), fill=(*ANCHOR, 185), width=4)
        draw.line((*mid, *center), fill=(*INFLOW, 120), width=2)
        draw.ellipse((anchor[0] - 6, anchor[1] - 6, anchor[0] + 6, anchor[1] + 6), fill=(*ANCHOR, 210))


def draw_core(draw, rot, t):
    center, _ = project(np.array([0.0, 0.0, 0.0]), rot)
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 1.7 * t)
    radius = 30 + 8 * pulse
    for scale, alpha in [(4.2, 22), (2.7, 42), (1.7, 76)]:
        rr = radius * scale
        draw.ellipse((center[0] - rr, center[1] - rr, center[0] + rr, center[1] + rr), fill=(*CORE, alpha))
    draw.ellipse((center[0] - radius, center[1] - radius, center[0] + radius, center[1] + radius), fill=(*CORE, 235))
    inner = radius * 0.34
    draw.ellipse((center[0] - inner, center[1] - inner, center[0] + inner, center[1] + inner), fill=(255, 252, 220, 245))


def annotations(draw):
    draw.text((30, SIZE - 82), "inference: shell fabric maps inward by radial connection paths", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text((30, SIZE - 58), "outer weave: remains on cone-sphere / inner weave: compresses and twists toward core", fill=(180, 235, 245), font=FONT_SMALL)
    draw.text((30, SIZE - 34), "anchors: three projected cone/knot paths guide the inward fabric flow", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        rot = rotation_matrix([1, 0, 0], math.radians(64)) @ rotation_matrix([0, 1, 0], math.radians(18)) @ rotation_matrix(
            [0, 0, 1], 2 * math.pi * 0.22 * t
        )
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_outer_shell(draw, rot, t)
        draw_inward_fabric(draw, rot, t)
        draw_anchor_paths(draw, rot, t)
        draw_core(draw, rot, t)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "18_inward_fabric_mapping.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[30].save(OUT_DIR / "18_inward_fabric_mapping_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("18_inward_fabric_mapping_preview.png")


if __name__ == "__main__":
    main()
