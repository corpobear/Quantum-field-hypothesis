import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 720
CENTER = np.array([SIZE / 2, SIZE / 2], dtype=float)
FRAMES = 132
FPS_MS = 42
BG = (7, 10, 17)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
CYAN = (74, 222, 255)
BLUE = (78, 144, 255)
VIOLET = (171, 120, 255)
AMBER = (255, 190, 82)
SPHERE = (118, 224, 255)
AXIS_X = (255, 105, 105)
AXIS_Y = (105, 255, 168)
AXIS_Z = (112, 164, 255)


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(28)
FONT_SMALL = font(16)


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def rotation_matrix(axis, angle):
    axis = normalize(np.array(axis, dtype=float))
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


def basis_from_normal(normal):
    normal = normalize(normal)
    helper = np.array([0.0, 0.0, 1.0])
    if abs(float(np.dot(normal, helper))) > 0.92:
        helper = np.array([0.0, 1.0, 0.0])
    u = normalize(np.cross(helper, normal))
    v = normalize(np.cross(normal, u))
    return u, v


CAMERA_ROT = rotation_matrix([1, 0, 0], math.radians(64)) @ rotation_matrix(
    [0, 0, 1], math.radians(-28)
)


def project(point, scale=1.0):
    p = CAMERA_ROT @ np.array(point, dtype=float)
    depth = 4.2 + p[2] / 170.0
    perspective = 4.2 / depth
    xy = CENTER + scale * perspective * np.array([p[0], -p[1]])
    return xy, p[2]


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for r in range(90, 350, 48):
        box = [CENTER[0] - r, CENTER[1] - r, CENTER[0] + r, CENTER[1] + r]
        draw.ellipse(box, outline=(*GRID, 110), width=1)
    draw.text((28, 24), "03 - Threefold Wobble Creates Sphere", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 60),
        "The stable third mode wobbles axis by axis; its spin sweep fills a sphere, not only a flat bubble.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def glow_point(draw, xy, color, radius=8, alpha=255):
    x, y = xy
    for scale, frac in [(4.0, 0.07), (2.8, 0.12), (1.8, 0.22)]:
        rr = radius * scale
        draw.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(*color, int(alpha * frac)))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, alpha))


def axis_for_time(t):
    # Starts as a clean z-axis spin, then wobbles through x, y, and mixed axes.
    ramp = max(0.0, min(1.0, (t - 0.12) / 0.62))
    x = ramp * math.sin(2 * math.pi * (1.45 * t + 0.03))
    y = ramp * math.sin(2 * math.pi * (1.13 * t + 0.31))
    z = 1.0 - 0.64 * ramp + 0.22 * math.sin(2 * math.pi * 0.73 * t) * ramp
    return normalize(np.array([x, y, z]))


def draw_axes(draw, t):
    axes = [
        (np.array([1.0, 0.0, 0.0]), AXIS_X, "x"),
        (np.array([0.0, 1.0, 0.0]), AXIS_Y, "y"),
        (np.array([0.0, 0.0, 1.0]), AXIS_Z, "z"),
    ]
    for vec, color, label in axes:
        p0, _ = project(-170 * vec)
        p1, _ = project(170 * vec)
        draw.line((*p0, *p1), fill=(*color, 78), width=2)
        text_pos, _ = project(188 * vec)
        draw.text(tuple(text_pos), label, fill=(*color, 185), font=FONT_SMALL)
    axis = axis_for_time(t)
    p0, _ = project(-190 * axis)
    p1, _ = project(190 * axis)
    draw.line((*p0, *p1), fill=(*AMBER, 210), width=4)


def sphere_points():
    pts = []
    for lat in np.linspace(-70, 70, 9):
        z = math.sin(math.radians(lat))
        rr = math.cos(math.radians(lat))
        ring = []
        for lon in np.linspace(0, 360, 120, endpoint=False):
            ring.append(150 * np.array([rr * math.cos(math.radians(lon)), rr * math.sin(math.radians(lon)), z]))
        pts.append(ring)
    meridians = []
    for lon in np.linspace(0, 360, 12, endpoint=False):
        meridian = []
        for lat in np.linspace(-85, 85, 80):
            meridian.append(
                150
                * np.array(
                    [
                        math.cos(math.radians(lat)) * math.cos(math.radians(lon)),
                        math.cos(math.radians(lat)) * math.sin(math.radians(lon)),
                        math.sin(math.radians(lat)),
                    ]
                )
            )
        meridians.append(meridian)
    return pts, meridians


LAT_RINGS, MERIDIANS = sphere_points()


def draw_sphere_ghost(draw, fill):
    alpha = int(20 + 95 * fill)
    for ring_points in LAT_RINGS:
        projected = [project(p)[0] for p in ring_points]
        for i in range(1, len(projected)):
            draw.line((*projected[i - 1], *projected[i]), fill=(*SPHERE, alpha), width=1)
        draw.line((*projected[-1], *projected[0]), fill=(*SPHERE, alpha), width=1)
    for meridian in MERIDIANS:
        projected = [project(p)[0] for p in meridian]
        for i in range(1, len(projected)):
            draw.line((*projected[i - 1], *projected[i]), fill=(*SPHERE, int(alpha * 0.72)), width=1)


def draw_threefold_loop(draw, t, surface_memory):
    spin = 2 * math.pi * 1.7 * t
    axis = axis_for_time(t)
    u, v = basis_from_normal(axis)
    loop_radius = 118
    colors = [CYAN, BLUE, VIOLET]
    current = []
    for k in range(3):
        phase = spin + 2 * math.pi * k / 3
        point = loop_radius * (math.cos(phase) * u + math.sin(phase) * v)
        current.append(point)
        surface_memory.append(point.copy())

    if len(surface_memory) > 820:
        del surface_memory[: len(surface_memory) - 820]

    for idx, point in enumerate(surface_memory):
        xy, depth = project(point)
        age = idx / max(1, len(surface_memory))
        alpha = int(18 + 120 * age)
        radius = 1.2 + 1.8 * age
        draw.ellipse((xy[0] - radius, xy[1] - radius, xy[0] + radius, xy[1] + radius), fill=(*SPHERE, alpha))

    projected = [project(p)[0] for p in current]
    for a, b in zip(projected, projected[1:] + projected[:1]):
        draw.line((*a, *b), fill=(*AMBER, 145), width=2)
    for k, point in enumerate(current):
        xy, depth = project(point)
        glow_point(draw, xy, colors[k], radius=8)


def annotations(draw, t):
    if t < 0.28:
        state = "state: stable third mode begins as one flat spin plane"
    elif t < 0.62:
        state = "state: spin axis wobbles through x, y, and z"
    else:
        state = "state: accumulated spin sweep closes as spherical coverage"
    draw.text((28, SIZE - 58), state, fill=(190, 220, 245), font=FONT_SMALL)
    draw.text(
        (28, SIZE - 32),
        "geometry: the sphere is made by axis-wobble sweep, not by a static bubble outline",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )


def make_animation():
    frames = []
    surface_memory = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        fill = max(0.0, min(1.0, (t - 0.28) / 0.58))
        draw_sphere_ghost(draw, fill)
        draw_axes(draw, t)
        draw_threefold_loop(draw, t, surface_memory)
        annotations(draw, t)
        frames.append(img)

    gif_path = OUT_DIR / "03_threefold_wobble_creates_sphere.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    frames[96].save(OUT_DIR / "03_threefold_wobble_creates_sphere_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("03_threefold_wobble_creates_sphere_preview.png")


if __name__ == "__main__":
    main()
