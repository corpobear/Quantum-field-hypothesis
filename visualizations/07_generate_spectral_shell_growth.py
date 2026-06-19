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
CORE = (255, 220, 130)


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


def spectral_color(t):
    x = (t * 2.7) % 1.0
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
    draw.text((28, 24), "07 - Spectral Shell Growth", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 60),
        "The shell grows outward while changing core frequencies preserve color bands.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def ring(draw, radius, color, alpha, width=2):
    box = [CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius]
    draw.ellipse(box, outline=(*color, alpha), width=width)


def glow(draw, xy, color, radius, alpha=255):
    x, y = xy
    for scale, frac in [(4.4, 0.07), (3.0, 0.13), (1.9, 0.24)]:
        rr = radius * scale
        draw.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(*color, int(alpha * frac)))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))


def draw_core(draw, t):
    color = spectral_color(t)
    frequency = 2.0 + 5.0 * (0.5 + 0.5 * math.sin(2 * math.pi * 0.55 * t))
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * frequency * t)
    radius = 26 + 9 * pulse
    glow(draw, CENTER, color, radius, 235)
    inner = radius * 0.35
    draw.ellipse(
        (CENTER[0] - inner, CENTER[1] - inner, CENTER[0] + inner, CENTER[1] + inner),
        fill=(255, 252, 224, 245),
    )
    return color


def draw_threefold_guides(draw, t, radius):
    for k in range(3):
        a = 2 * math.pi * (k / 3 + 0.05 * math.sin(2 * math.pi * t))
        p = CENTER + radius * np.array([math.cos(a), math.sin(a)])
        draw.line((*CENTER, *p), fill=(255, 220, 120, 34), width=1)
        glow(draw, p, (255, 235, 160), 4, 155)


def draw_growth_bands(draw, t):
    growth = max(0.0, min(1.0, (t - 0.06) / 0.9))
    inner_radius = 138
    outer_radius = 138 + 150 * growth
    band_count = 18

    for idx in range(band_count):
        u = idx / (band_count - 1)
        birth_t = max(0.0, t - (1 - u) * 0.36)
        color = spectral_color(birth_t)
        radius = inner_radius + (outer_radius - inner_radius) * u
        alpha = int(42 + 120 * u)
        width = 2 if idx % 2 else 3
        ring(draw, radius, color, alpha, width=width)

        # Preserve cone imprint as three brighter arcs on each growth layer.
        for k in range(3):
            center_angle = 2 * math.pi * (k / 3 + 0.04 * math.sin(2 * math.pi * birth_t))
            arc = []
            for j in range(18):
                a = center_angle - 0.14 + 0.28 * j / 17
                wobble = 2.2 * math.sin(9 * a + 8 * t + idx)
                p = CENTER + (radius + wobble) * np.array([math.cos(a), math.sin(a)])
                arc.append(tuple(p))
            for p1, p2 in zip(arc, arc[1:]):
                draw.line((*p1, *p2), fill=(*color, min(230, alpha + 75)), width=3)

    # Current outer edge.
    ring(draw, outer_radius, SHELL, 220, width=4)
    return outer_radius


def draw_outgoing_colored_light(draw, t, color):
    for pulse_idx in range(5):
        phase = (t * 1.35 - pulse_idx * 0.21) % 1.0
        radius = 38 + phase * 260
        alpha = int(160 * (1 - phase))
        ring(draw, radius, color, alpha, width=2)
    for k in range(3):
        a = 2 * math.pi * (k / 3 + 0.035 * math.sin(2 * math.pi * t))
        left = CENTER + 46 * np.array([math.cos(a - 0.08), math.sin(a - 0.08)])
        right = CENTER + 46 * np.array([math.cos(a + 0.08), math.sin(a + 0.08)])
        tip = CENTER + 285 * np.array([math.cos(a), math.sin(a)])
        draw.polygon([tuple(left), tuple(right), tuple(tip)], fill=(*color, 36))


def annotations(draw):
    draw.text(
        (28, SIZE - 58),
        "state: shell grows outward while each core frequency leaves a color layer",
        fill=(190, 220, 245),
        font=FONT_SMALL,
    )
    draw.text(
        (28, SIZE - 32),
        "geometry: growth preserves spectral history as bands and threefold cone imprints",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        outer_radius = draw_growth_bands(draw, t)
        color = draw_core(draw, t)
        draw_outgoing_colored_light(draw, t, color)
        draw_threefold_guides(draw, t, outer_radius)
        annotations(draw)
        frames.append(img)

    gif_path = OUT_DIR / "07_spectral_shell_growth.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    frames[104].save(OUT_DIR / "07_spectral_shell_growth_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("07_spectral_shell_growth_preview.png")


if __name__ == "__main__":
    main()
