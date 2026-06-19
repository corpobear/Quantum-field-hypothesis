import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
W, H = 980, 600
FRAMES = 144
FPS_MS = 42
BG = (7, 10, 17)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
SHELL = (120, 230, 255)
CORE = (255, 218, 126)
TIME = (255, 235, 122)


HEAT = [
    (20, 34, 72),
    (42, 102, 210),
    (55, 215, 255),
    (110, 255, 185),
    (255, 235, 118),
    (255, 148, 82),
    (255, 82, 122),
    (204, 118, 255),
]


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


def lerp_color(a, b, u):
    return tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))


def heat_color(value):
    value = max(0.0, min(1.0, value))
    pos = value * (len(HEAT) - 1)
    i = int(pos)
    j = min(i + 1, len(HEAT) - 1)
    return lerp_color(HEAT[i], HEAT[j], pos - i)


def expansion_scale(t):
    return 0.34 + 0.98 * smoothstep(t) + 0.025 * math.sin(2 * math.pi * 1.25 * t) * (1 - 0.35 * t)


def knot_angles(t):
    wobble = 0.12 * math.sin(2 * math.pi * 0.26 * t)
    return [math.radians(90) + wobble, math.radians(210) - 0.7 * wobble, math.radians(330) + 0.4 * wobble]


def shell_radius(angle, t, base=82):
    scale = expansion_scale(t)
    r = base * scale
    for ka in knot_angles(t):
        delta = math.atan2(math.sin(angle - ka), math.cos(angle - ka))
        r -= base * scale * 0.075 * math.exp(-(delta * delta) / (2 * 0.24 * 0.24))
    r += base * scale * 0.012 * math.sin(2 * angle - 1.1 + 2 * math.pi * 0.18 * t)
    return r


def spectrogram_intensity(t, angle, frame_t):
    # Cone-projection heat on the expanding shell: three angular cone ridges,
    # core-frequency drift over time, and ripple sidebands.
    cone = 0.0
    for ka in knot_angles(t):
        delta = math.atan2(math.sin(angle - ka), math.cos(angle - ka))
        cone = max(cone, math.exp(-(delta * delta) / (2 * 0.19 * 0.19)))
    carrier = 0.48 + 0.28 * math.sin(2 * math.pi * (0.58 * t + 0.13 * math.sin(2 * math.pi * frame_t)))
    angular_mode = 0.5 + 0.5 * math.sin(3 * angle - 5.4 * t)
    sideband = 0.5 + 0.5 * math.sin(8.0 * t - 2.8 * math.cos(angle))
    return max(0.0, min(1.0, cone * (0.42 + 0.46 * carrier + 0.18 * angular_mode + 0.15 * sideband)))


def project(x, y, z):
    px = 96 + x * 760
    perspective = 0.86 + 0.24 * x
    py = 322 - z * perspective + 42 * (x - 0.5)
    return np.array([px, py]) + np.array([0, y * 0.34 * perspective])


def base_frame():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((28, 22), "13 - Expansion Spectrogram Heatmap", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 56),
        "The projected cone spectrogram is overlaid onto the 3D shell expansion history.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def draw_time_axis(draw):
    start = project(0.02, 0, 0)
    end = project(0.98, 0, 0)
    draw.line((*start, *end), fill=(*TIME, 135), width=3)
    draw.text(tuple(start + np.array([-10, 22])), "early", fill=MUTED, font=FONT_SMALL)
    draw.text(tuple(end + np.array([-24, 22])), "later time", fill=MUTED, font=FONT_SMALL)


def draw_heat_slice(draw, t, current_t, highlight=False):
    x = 0.08 + 0.86 * t
    samples = 132
    pts = []
    heats = []
    for j in range(samples):
        angle = 2 * math.pi * j / samples
        r = shell_radius(angle, t)
        p = tuple(project(x, r * math.cos(angle), r * math.sin(angle)))
        pts.append(p)
        heats.append(spectrogram_intensity(t, angle, current_t))

    center = project(x, 0, 0)
    for j in range(samples):
        p1 = pts[j]
        p2 = pts[(j + 1) % samples]
        h = (heats[j] + heats[(j + 1) % samples]) / 2
        color = heat_color(h)
        alpha = int((55 + 185 * h) * (1.0 if t <= current_t else 0.22))
        draw.line((*center, *p1), fill=(*color, int(alpha * 0.18)), width=1)
        draw.line((*p1, *p2), fill=(*color, alpha), width=7 if highlight else 5)


def draw_heat_surface(draw, current_t):
    slices = 20
    # Future ghost grid first.
    for i in range(slices):
        t = i / (slices - 1)
        draw_heat_slice(draw, t, current_t, highlight=abs(t - current_t) < 0.03)

    for angle in np.linspace(0, 2 * math.pi, 15, endpoint=False):
        prev = None
        for i in range(slices):
            t = i / (slices - 1)
            if t > current_t:
                continue
            x = 0.08 + 0.86 * t
            r = shell_radius(float(angle), t)
            p = tuple(project(x, r * math.cos(angle), r * math.sin(angle)))
            if prev is not None:
                intensity = spectrogram_intensity(t, float(angle), current_t)
                draw.line((*prev, *p), fill=(*heat_color(intensity), 80), width=1)
            prev = p


def draw_core_worldline(draw, current_t):
    prev = None
    for i in range(80):
        t = current_t * i / 79
        p = tuple(project(0.08 + 0.86 * t, 0, 0))
        if prev is not None:
            draw.line((*prev, *p), fill=(*CORE, 110), width=2)
        prev = p
    current = project(0.08 + 0.86 * current_t, 0, 0)
    radius = 8 + 8 * expansion_scale(current_t)
    draw.ellipse((current[0] - radius, current[1] - radius, current[0] + radius, current[1] + radius), fill=(*CORE, 235))


def draw_heat_legend(draw):
    x0, y0 = 742, 86
    draw.text((x0, y0 - 24), "spectrogram heat", fill=MUTED, font=FONT_SMALL)
    for i in range(120):
        v = i / 119
        color = heat_color(v)
        draw.rectangle((x0 + i, y0, x0 + i + 1, y0 + 12), fill=color)
    draw.text((x0, y0 + 18), "low", fill=MUTED, font=FONT_SMALL)
    draw.text((x0 + 88, y0 + 18), "high", fill=MUTED, font=FONT_SMALL)


def annotations(draw):
    draw.text((28, H - 54), "state: expansion history and projected-cone spectrogram become one heatmap", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text((28, H - 30), "geometry: each shell slice is colored by cone frequency/ripple intensity at that time", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / (FRAMES - 1)
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_time_axis(draw)
        draw_heat_surface(draw, t)
        draw_core_worldline(draw, t)
        draw_heat_legend(draw)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "13_expansion_spectrogram_heatmap.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[104].save(OUT_DIR / "13_expansion_spectrogram_heatmap_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("13_expansion_spectrogram_heatmap_preview.png")


if __name__ == "__main__":
    main()
