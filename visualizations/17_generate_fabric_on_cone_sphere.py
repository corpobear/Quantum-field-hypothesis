import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 900
FRAMES = 84
FPS_MS = 42
BG = (6, 9, 16)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
SPHERE = (72, 148, 255)
FABRIC_A = (92, 255, 224)
FABRIC_B = (178, 132, 255)
CORE = (255, 218, 126)
CONE = (255, 235, 122)
TUG = (255, 150, 96)


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


def heat_color(value):
    value = max(0.0, min(1.0, value))
    cold = np.array([28, 54, 118])
    mid = np.array([90, 240, 255])
    hot = np.array([255, 226, 118])
    if value < 0.55:
        u = value / 0.55
        c = cold + (mid - cold) * u
    else:
        u = (value - 0.55) / 0.45
        c = mid + (hot - mid) * u
    return tuple(int(x) for x in c)


def knot_dirs(t):
    dirs = []
    wobble = 0.18 * math.sin(2 * math.pi * 0.23 * t)
    for k in range(3):
        phi = 2 * math.pi * k / 3 + wobble
        theta = math.pi / 2 + 0.22 * math.sin(2 * math.pi * (0.31 * t + k / 3))
        dirs.append(np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)]))
    return dirs


def cone_sphere_point(theta, phi, t):
    n = np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)])
    radius = 170
    # Three cone-projection lobes make the sphere visibly born from cone expansion.
    lift = 0.0
    dent = 0.0
    for kd in knot_dirs(t):
        dot = max(-1.0, min(1.0, float(np.dot(n, kd))))
        angular = math.acos(dot)
        lift += 0.10 * math.exp(-(angular * angular) / (2 * 0.30 * 0.30))
        dent += 0.055 * math.exp(-(angular * angular) / (2 * 0.18 * 0.18))
    ripple = 0.026 * math.sin(3 * phi + 2.2 * math.cos(theta) + 2 * math.pi * t)
    return radius * (1 + lift - dent + ripple) * n


def fabric_displacement(theta, phi, t):
    wave = 0.035 * math.sin(6 * phi + 4 * math.cos(theta) + 2 * math.pi * t)
    pull = 0.0
    n = np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)])
    for kd in knot_dirs(t):
        dot = max(-1.0, min(1.0, float(np.dot(n, kd))))
        angular = math.acos(dot)
        pull += 0.050 * math.exp(-(angular * angular) / (2 * 0.24 * 0.24)) * math.sin(2 * math.pi * t + 2 * dot)
    return wave + pull


def surface_heat(theta, phi, t):
    n = np.array([math.sin(theta) * math.cos(phi), math.sin(theta) * math.sin(phi), math.cos(theta)])
    cone = 0.0
    for kd in knot_dirs(t):
        dot = max(-1.0, min(1.0, float(np.dot(n, kd))))
        cone = max(cone, math.exp(-((math.acos(dot)) ** 2) / (2 * 0.27 * 0.27)))
    fabric = 0.5 + 0.5 * math.sin(5 * phi - 3.5 * math.cos(theta) + 2 * math.pi * 1.3 * t)
    return max(0.0, min(1.0, 0.24 + 0.62 * cone + 0.20 * fabric))


def project(point, rot):
    p = rot @ point
    depth = 640 + p[2]
    perspective = 640 / depth
    xy = np.array([SIZE / 2, SIZE / 2 + 30]) + perspective * np.array([p[0], -p[1]])
    return xy, p[2]


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((30, 24), "17 - Spacetime Fabric Mapped Onto Cone-Sphere", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (30, 60),
        "A cone-expanded sphere carries the moving fabric scaffold over its full surface.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    for r in range(130, 390, 58):
        draw.ellipse((SIZE / 2 - r, SIZE / 2 + 30 - r, SIZE / 2 + r, SIZE / 2 + 30 + r), outline=(*GRID, 54), width=1)
    return img


def draw_sphere_heat(draw, rot, t):
    lat_steps = 13
    lon_steps = 30
    cells = []
    for i in range(lat_steps):
        theta1 = 0.10 + (math.pi - 0.20) * i / lat_steps
        theta2 = 0.10 + (math.pi - 0.20) * (i + 1) / lat_steps
        for j in range(lon_steps):
            phi1 = 2 * math.pi * j / lon_steps
            phi2 = 2 * math.pi * (j + 1) / lon_steps
            corners = [
                cone_sphere_point(theta1, phi1, t),
                cone_sphere_point(theta1, phi2, t),
                cone_sphere_point(theta2, phi2, t),
                cone_sphere_point(theta2, phi1, t),
            ]
            projected = []
            depths = []
            for point in corners:
                xy, z = project(point, rot)
                projected.append(tuple(xy))
                depths.append(z)
            h = surface_heat((theta1 + theta2) / 2, (phi1 + phi2) / 2, t)
            cells.append((sum(depths) / 4, projected, h))
    cells.sort(key=lambda item: item[0])
    for depth, poly, h in cells:
        color = heat_color(h)
        shade = 0.70 + 0.30 * max(0.0, min(1.0, (depth + 180) / 360))
        color = tuple(int(c * shade) for c in color)
        draw.polygon(poly, fill=(*color, int(62 + 125 * h)))


def fabric_surface_point(theta, phi, t):
    base = cone_sphere_point(theta, phi, t)
    n = base / np.linalg.norm(base)
    return base + n * (18 * fabric_displacement(theta, phi, t))


def draw_fabric(draw, rot, t):
    # Latitude threads.
    for idx, theta in enumerate(np.linspace(0.26, math.pi - 0.26, 11)):
        pts = []
        for phi in np.linspace(0, 2 * math.pi, 78):
            xy, z = project(fabric_surface_point(float(theta), float(phi), t), rot)
            pts.append((tuple(xy), z))
        visible = [(p, z) for p, z in pts if z > -180]
        color = FABRIC_A if idx % 2 == 0 else (130, 250, 255)
        for (p1, z1), (p2, z2) in zip(visible, visible[1:]):
            alpha = int(135 + 75 * max(0.0, min(1.0, (z1 + 180) / 360)))
            draw.line((*p1, *p2), fill=(*color, alpha), width=3)

    # Longitude threads.
    for idx, phi in enumerate(np.linspace(0, 2 * math.pi, 13, endpoint=False)):
        pts = []
        for theta in np.linspace(0.18, math.pi - 0.18, 62):
            xy, z = project(fabric_surface_point(float(theta), float(phi), t), rot)
            pts.append((tuple(xy), z))
        color = FABRIC_B if idx % 2 == 0 else (145, 155, 255)
        for (p1, z1), (p2, z2) in zip(pts, pts[1:]):
            alpha = int(90 + 70 * max(0.0, min(1.0, (z1 + 180) / 360)))
            draw.line((*p1, *p2), fill=(*color, alpha), width=2)


def draw_cone_sources(draw, rot, t):
    center, _ = project(np.array([0.0, 0.0, 0.0]), rot)
    for kd in knot_dirs(t):
        anchor, _ = project(cone_sphere_point(math.acos(kd[2]), math.atan2(kd[1], kd[0]), t), rot)
        inner, _ = project(66 * kd, rot)
        draw.polygon([tuple(center), tuple(inner), tuple(anchor)], fill=(*CONE, 36))
        draw.line((*center, *anchor), fill=(*CONE, 130), width=2)
        draw.ellipse((anchor[0] - 5, anchor[1] - 5, anchor[0] + 5, anchor[1] + 5), fill=(*TUG, 190))
    draw.ellipse((center[0] - 26, center[1] - 26, center[0] + 26, center[1] + 26), fill=(*CORE, 230))
    draw.ellipse((center[0] - 9, center[1] - 9, center[0] + 9, center[1] + 9), fill=(255, 252, 220, 245))


def annotations(draw):
    draw.text((30, SIZE - 82), "sphere: cone projection exploded into full 3D surface", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text((30, SIZE - 58), "fabric: spacetime weave is mapped onto the sphere and moves with connection tugs", fill=(180, 235, 245), font=FONT_SMALL)
    draw.text((30, SIZE - 34), "heat: cone/ripple intensity remains visible underneath the fabric", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        rot = rotation_matrix([1, 0, 0], math.radians(64)) @ rotation_matrix([0, 1, 0], math.radians(18)) @ rotation_matrix(
            [0, 0, 1], 2 * math.pi * 0.25 * t
        )
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_sphere_heat(draw, rot, t)
        draw_fabric(draw, rot, t)
        draw_cone_sources(draw, rot, t)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "17_fabric_on_cone_sphere.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[54].save(OUT_DIR / "17_fabric_on_cone_sphere_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("17_fabric_on_cone_sphere_preview.png")


if __name__ == "__main__":
    main()
