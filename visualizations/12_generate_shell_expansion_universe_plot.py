import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
W, H = 980, 580
FRAMES = 144
FPS_MS = 42
BG = (7, 10, 17)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
SHELL = (120, 230, 255)
CORE = (255, 218, 126)
KNOT = (255, 196, 96)
EXPAND = (128, 255, 185)
TIME = (255, 235, 122)


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(27)
FONT_SMALL = font(16)


def smoothstep(x):
    x = max(0.0, min(1.0, x))
    return x * x * (3 - 2 * x)


def expansion_scale(t):
    return 0.34 + 0.98 * smoothstep(t) + 0.025 * math.sin(2 * math.pi * 1.25 * t) * (1 - 0.35 * t)


def knot_angles(t):
    wobble = 0.12 * math.sin(2 * math.pi * 0.26 * t)
    return [math.radians(90) + wobble, math.radians(210) - 0.7 * wobble, math.radians(330) + 0.4 * wobble]


def shell_radius(angle, t, base=82):
    scale = expansion_scale(t)
    r = base * scale
    strength = 0.60 + 0.16 * math.sin(2 * math.pi * 0.34 * t)
    for ka in knot_angles(t):
        delta = math.atan2(math.sin(angle - ka), math.cos(angle - ka))
        r -= base * scale * 0.075 * strength * math.exp(-(delta * delta) / (2 * 0.24 * 0.24))
    r += base * scale * 0.012 * math.sin(2 * angle - 1.1 + 2 * math.pi * 0.18 * t)
    return r


def project(x, y, z):
    # Time axis runs left to right; y/z form each shell cross-section.
    px = 96 + x * 760
    perspective = 0.86 + 0.24 * x
    py = 308 - z * perspective + 42 * (x - 0.5)
    return np.array([px, py]) + np.array([0, y * 0.34 * perspective])


def base_frame():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((28, 22), "12 - 3D Shell Expansion Through Time", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 56),
        "The deformed shell grows along a time axis like a universe-shape expansion diagram.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def draw_time_axis(draw):
    start = project(0.02, 0, 0)
    end = project(0.98, 0, 0)
    draw.line((*start, *end), fill=(*TIME, 150), width=3)
    for i in range(9):
        x = 0.08 + i * 0.105
        p = project(x, 0, 0)
        draw.line((p[0], p[1] - 8, p[0], p[1] + 8), fill=(*TIME, 105), width=1)
    draw.text(tuple(start + np.array([-10, 22])), "early", fill=MUTED, font=FONT_SMALL)
    draw.text(tuple(end + np.array([-24, 22])), "later time", fill=MUTED, font=FONT_SMALL)


def draw_shell_slice(draw, t, current_t, alpha_boost=0):
    x = 0.08 + 0.86 * t
    pts = []
    for j in range(156):
        a = 2 * math.pi * j / 156
        r = shell_radius(a, t)
        y = r * math.cos(a)
        z = r * math.sin(a)
        pts.append(tuple(project(x, y, z)))

    alpha = int(45 + 135 * t + alpha_boost)
    color = SHELL if t < current_t else GRID
    width = 2 if alpha_boost < 20 else 4
    for p1, p2 in zip(pts, pts[1:] + pts[:1]):
        draw.line((*p1, *p2), fill=(*color, min(240, alpha)), width=width)

    # Three knot dents/anchors on each slice.
    if t <= current_t + 0.01:
        for ka in knot_angles(t):
            r = shell_radius(ka, t)
            anchor = project(x, r * math.cos(ka), r * math.sin(ka))
            inner = project(x, 0.58 * r * math.cos(ka), 0.58 * r * math.sin(ka))
            draw.line((*inner, *anchor), fill=(*KNOT, min(220, alpha + 40)), width=2)
            draw.ellipse((inner[0] - 3, inner[1] - 3, inner[0] + 3, inner[1] + 3), fill=(*KNOT, 190))


def draw_expansion_surface(draw, current_t):
    slices = 18
    for i in range(slices):
        t = i / (slices - 1)
        if t <= current_t:
            draw_shell_slice(draw, t, current_t)
        else:
            draw_shell_slice(draw, t, current_t, alpha_boost=-30)

    # Connect a few same-angle points to form a 3D tube/surface silhouette.
    for angle in np.linspace(0, 2 * math.pi, 12, endpoint=False):
        prev = None
        for i in range(slices):
            t = i / (slices - 1)
            if t > current_t:
                continue
            x = 0.08 + 0.86 * t
            r = shell_radius(float(angle), t)
            p = tuple(project(x, r * math.cos(angle), r * math.sin(angle)))
            if prev is not None:
                draw.line((*prev, *p), fill=(*SHELL, 62), width=1)
            prev = p

    # Current slice highlighted.
    draw_shell_slice(draw, current_t, current_t, alpha_boost=70)


def draw_core_worldline(draw, current_t):
    prev = None
    for i in range(80):
        t = current_t * i / 79
        x = 0.08 + 0.86 * t
        p = tuple(project(x, 0, 0))
        if prev is not None:
            draw.line((*prev, *p), fill=(*CORE, 120), width=2)
        prev = p
    current = project(0.08 + 0.86 * current_t, 0, 0)
    radius = 8 + 8 * expansion_scale(current_t)
    draw.ellipse((current[0] - radius, current[1] - radius, current[0] + radius, current[1] + radius), fill=(*CORE, 235))


def draw_outward_push(draw, current_t):
    x = 0.08 + 0.86 * current_t
    for angle in np.linspace(0, 2 * math.pi, 10, endpoint=False):
        r1 = shell_radius(float(angle), current_t) * 0.76
        r2 = shell_radius(float(angle), current_t) * 1.06
        p1 = project(x, r1 * math.cos(angle), r1 * math.sin(angle))
        p2 = project(x, r2 * math.cos(angle), r2 * math.sin(angle))
        draw.line((*p1, *p2), fill=(*EXPAND, 150), width=2)
        direction = p2 - p1
        norm = np.linalg.norm(direction)
        if norm > 0:
            direction = direction / norm
        tangent = np.array([-direction[1], direction[0]])
        left = p2 - 8 * direction + 5 * tangent
        right = p2 - 8 * direction - 5 * tangent
        draw.polygon([tuple(p2), tuple(left), tuple(right)], fill=(*EXPAND, 170))


def annotations(draw):
    draw.text((28, H - 54), "state: deformed shell is pushed outward and grows along the time axis", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text((28, H - 30), "geometry: each cross-section is a universe-shape slice; the expanding tube preserves the three-knot deformation", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / (FRAMES - 1)
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_time_axis(draw)
        draw_expansion_surface(draw, t)
        draw_core_worldline(draw, t)
        draw_outward_push(draw, t)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "12_shell_expansion_universe_plot.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[104].save(OUT_DIR / "12_shell_expansion_universe_plot_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("12_shell_expansion_universe_plot_preview.png")


if __name__ == "__main__":
    main()
