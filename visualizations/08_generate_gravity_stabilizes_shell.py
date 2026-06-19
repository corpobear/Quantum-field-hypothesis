import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 720
CENTER = np.array([SIZE / 2, SIZE / 2], dtype=float)
FRAMES = 144
FPS_MS = 42
BG = (7, 10, 17)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
SHELL = (120, 230, 255)
CORE = (255, 218, 126)
GRAVITY = (176, 142, 255)
SLOW = (255, 245, 180)


SPECTRUM = [
    (92, 190, 255),
    (114, 245, 255),
    (128, 255, 174),
    (255, 235, 122),
    (255, 166, 94),
    (255, 104, 152),
    (185, 128, 255),
]


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(28)
FONT_SMALL = font(16)


def lerp_color(a, b, u):
    return tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))


def spectral_color(x):
    x = x % 1.0
    pos = x * len(SPECTRUM)
    i = int(pos) % len(SPECTRUM)
    j = (i + 1) % len(SPECTRUM)
    return lerp_color(SPECTRUM[i], SPECTRUM[j], pos - int(pos))


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for r in range(90, 350, 48):
        box = [CENTER[0] - r, CENTER[1] - r, CENTER[0] + r, CENTER[1] + r]
        draw.ellipse(box, outline=(*GRID, 105), width=1)
    draw.text((28, 24), "08 - Core Gravity Stabilizes Shell Pattern", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 60),
        "Core densifies from shell mass; gravity stabilizes patterns and slows updates outward.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def ring(draw, radius, color, alpha, width=2):
    box = [CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius]
    draw.ellipse(box, outline=(*color, alpha), width=width)


def glow(draw, xy, color, radius, alpha=255):
    x, y = xy
    for scale, frac in [(5.0, 0.07), (3.2, 0.13), (2.0, 0.24)]:
        rr = radius * scale
        draw.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(*color, int(alpha * frac)))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))


def draw_mass_feed(draw, t):
    density = max(0.0, min(1.0, (t - 0.06) / 0.72))
    for idx in range(36):
        a = 2 * math.pi * (idx / 36 + 0.015 * math.sin(2 * math.pi * t))
        phase = (t * 0.9 + idx / 36) % 1.0
        shell_r = 244
        core_r = 44 - 14 * density
        r = shell_r - (shell_r - core_r) * phase
        p = CENTER + r * np.array([math.cos(a), math.sin(a)])
        start = CENTER + shell_r * np.array([math.cos(a), math.sin(a)])
        alpha = int(28 + 90 * density * (1 - phase))
        draw.line((*start, *p), fill=(*SHELL, int(alpha * 0.4)), width=1)
        draw.ellipse((p[0] - 1.7, p[1] - 1.7, p[0] + 1.7, p[1] + 1.7), fill=(*SHELL, alpha))
    return density


def draw_core(draw, t, density):
    radius = 28 + 23 * density
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * (4.0 - 2.2 * density) * t)
    compressed = radius + 4 * pulse * (1 - 0.45 * density)
    glow(draw, CENTER, CORE, compressed, 238)
    inner = compressed * (0.28 + 0.06 * pulse)
    draw.ellipse(
        (CENTER[0] - inner, CENTER[1] - inner, CENTER[0] + inner, CENTER[1] + inner),
        fill=(255, 252, 220, 245),
    )


def draw_gravity_field(draw, t, density):
    for idx, radius in enumerate([78, 112, 150, 192, 238, 286]):
        phase_speed = 1.2 / (1 + idx * 0.55)
        phase = 0.5 + 0.5 * math.sin(2 * math.pi * (phase_speed * t + idx * 0.13))
        alpha = int((24 + 88 * density) * (0.55 + 0.45 * phase))
        ring(draw, radius, GRAVITY, alpha, width=2)
    for idx in range(24):
        a = 2 * math.pi * idx / 24
        curve = []
        for j in range(54):
            u = j / 53
            r = 52 + 236 * u
            bend = 0.08 * density * math.sin(4 * u + idx)
            p = CENTER + r * np.array([math.cos(a + bend), math.sin(a - bend)])
            curve.append(tuple(p))
        for p1, p2 in zip(curve, curve[1:]):
            draw.line((*p1, *p2), fill=(*GRAVITY, int(24 + 42 * density)), width=1)


def draw_stabilized_shell(draw, t, density):
    outer_radius = 248
    band_count = 16
    # Inner bands still shimmer quickly; outer bands update slowly as density rises.
    for idx in range(band_count):
        u = idx / (band_count - 1)
        radius = 140 + (outer_radius - 140) * u
        slow_factor = 1.0 / (1.0 + 5.0 * density * u * u)
        color = spectral_color(0.22 * idx + t * slow_factor)
        alpha = int(44 + 115 * u + 45 * density)
        ring(draw, radius, color, alpha, width=2 if idx % 2 else 3)

        # Threefold pattern locks into place as gravity strengthens.
        lock = density
        wobble_amp = 0.16 * (1 - lock)
        for k in range(3):
            center_angle = 2 * math.pi * k / 3 + wobble_amp * math.sin(2 * math.pi * t + idx)
            arc = []
            for j in range(20):
                a = center_angle - 0.13 + 0.26 * j / 19
                p = CENTER + radius * np.array([math.cos(a), math.sin(a)])
                arc.append(tuple(p))
            for p1, p2 in zip(arc, arc[1:]):
                draw.line((*p1, *p2), fill=(*color, min(245, alpha + 78)), width=3)
    ring(draw, outer_radius, SHELL, 225, width=4)


def draw_update_frequency_markers(draw, t, density):
    labels = [
        (92, "fast"),
        (164, "slower"),
        (246, "slow"),
    ]
    for idx, (radius, label) in enumerate(labels):
        speed = 2.6 / (1 + density * idx * 2.2)
        for dot in range(6):
            a = 2 * math.pi * ((dot / 6) + speed * t)
            p = CENTER + radius * np.array([math.cos(a), math.sin(a)])
            draw.ellipse((p[0] - 2.4, p[1] - 2.4, p[0] + 2.4, p[1] + 2.4), fill=(*SLOW, 160))
        text_pos = CENTER + np.array([radius + 12, -10 - idx * 4])
        draw.text(tuple(text_pos), label, fill=(*SLOW, 150), font=FONT_SMALL)


def annotations(draw):
    draw.text(
        (28, SIZE - 58),
        "state: densifying core creates gravity that locks the shell pattern",
        fill=(190, 220, 245),
        font=FONT_SMALL,
    )
    draw.text(
        (28, SIZE - 32),
        "geometry: update frequency slows with radius, so outer spectral bands change more slowly",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        density = draw_mass_feed(draw, t)
        draw_stabilized_shell(draw, t, density)
        draw_gravity_field(draw, t, density)
        draw_update_frequency_markers(draw, t, density)
        draw_core(draw, t, density)
        annotations(draw)
        frames.append(img)

    gif_path = OUT_DIR / "08_gravity_stabilizes_shell_pattern.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    frames[104].save(OUT_DIR / "08_gravity_stabilizes_shell_pattern_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("08_gravity_stabilizes_shell_pattern_preview.png")


if __name__ == "__main__":
    main()
