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
SHELL = (120, 230, 255)
CORE = (255, 210, 112)


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(28)
FONT_SMALL = font(16)


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for r in range(90, 350, 48):
        box = [CENTER[0] - r, CENTER[1] - r, CENTER[0] + r, CENTER[1] + r]
        draw.ellipse(box, outline=(*GRID, 110), width=1)
    draw.text((28, 24), "04 - Outer Shell Feeds Core", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 60),
        "Reservoir mass flows inward from the shell; the center condenses into a core.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def glow_point(draw, xy, color, radius=8, alpha=255):
    x, y = xy
    for scale, frac in [(4.2, 0.07), (2.9, 0.13), (1.8, 0.24)]:
        rr = radius * scale
        draw.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(*color, int(alpha * frac)))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, alpha))


def ring(draw, radius, color, alpha, width=2):
    box = [CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius]
    draw.ellipse(box, outline=(*color, alpha), width=width)


def draw_sphere_and_shell(draw, t):
    for lat in np.linspace(-60, 60, 7):
        rr = 156 * math.cos(math.radians(lat))
        y_scale = 0.56
        box = [
            CENTER[0] - rr,
            CENTER[1] - rr * y_scale,
            CENTER[0] + rr,
            CENTER[1] + rr * y_scale,
        ]
        draw.ellipse(box, outline=(*SHELL, 58), width=1)
    for radius, alpha in [(232, 180), (239, 120), (246, 80)]:
        ring(draw, radius, SHELL, alpha, width=3)
    for idx in range(60):
        a = 2 * math.pi * (idx / 60 + 0.035 * t)
        r = 236 + 8 * math.sin(idx + 5 * t)
        p = CENTER + r * np.array([math.cos(a), math.sin(a)])
        draw.ellipse((p[0] - 1.5, p[1] - 1.5, p[0] + 1.5, p[1] + 1.5), fill=(*SHELL, 120))


def draw_threefold(draw, t):
    radius = 105
    points = []
    colors = [CYAN, BLUE, VIOLET]
    wobble_y = 0.62 + 0.22 * math.sin(2 * math.pi * 0.9 * t)
    rot = 2 * math.pi * 1.1 * t
    for k in range(3):
        a = rot + 2 * math.pi * k / 3
        p = CENTER + radius * np.array([math.cos(a), wobble_y * math.sin(a)])
        points.append(p)
    draw.polygon([tuple(p) for p in points], outline=(*AMBER, 145))
    for k, p in enumerate(points):
        glow_point(draw, p, colors[k], radius=7)


def draw_inflow(draw, t):
    fill = max(0.0, min(1.0, (t - 0.12) / 0.76))
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 3.0 * t)
    for idx in range(48):
        a = 2 * math.pi * (idx / 48 + 0.02 * math.sin(2 * math.pi * t))
        phase = (t * 1.8 + idx / 48) % 1.0
        shell_r = 232
        core_r = 24 + 18 * (1 - fill)
        r = shell_r - (shell_r - core_r) * phase * fill
        p = CENTER + r * np.array([math.cos(a), math.sin(a)])
        alpha = int((35 + 145 * fill) * (0.55 + 0.45 * pulse))
        start = CENTER + shell_r * np.array([math.cos(a), math.sin(a)])
        draw.line((*start, *p), fill=(*SHELL, int(alpha * 0.22)), width=1)
        draw.ellipse((p[0] - 2.2, p[1] - 2.2, p[0] + 2.2, p[1] + 2.2), fill=(*SHELL, alpha))


def draw_core(draw, t):
    fill = max(0.0, min(1.0, (t - 0.2) / 0.72))
    radius = 6 + 30 * fill
    alpha = int(130 + 125 * fill)
    for scale, frac in [(4.5, 0.08), (3.0, 0.14), (1.9, 0.23)]:
        rr = radius * scale
        draw.ellipse(
            (CENTER[0] - rr, CENTER[1] - rr, CENTER[0] + rr, CENTER[1] + rr),
            fill=(*CORE, int(alpha * frac)),
        )
    draw.ellipse(
        (CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius),
        fill=(*CORE, alpha),
    )
    draw.ellipse(
        (CENTER[0] - radius * 0.34, CENTER[1] - radius * 0.34, CENTER[0] + radius * 0.34, CENTER[1] + radius * 0.34),
        fill=(255, 247, 204, alpha),
    )


def annotations(draw, t):
    if t < 0.32:
        state = "state: reservoir shell is formed around the wobbling third mode"
    elif t < 0.72:
        state = "state: mass flows inward from the shell toward the center"
    else:
        state = "state: center condenses into a core while the third mode remains stable"
    draw.text((28, SIZE - 58), state, fill=(190, 220, 245), font=FONT_SMALL)
    draw.text(
        (28, SIZE - 32),
        "geometry: core is fed by the outer reservoir shell, not by consuming the threefold loop",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_sphere_and_shell(draw, t)
        draw_inflow(draw, t)
        draw_threefold(draw, t)
        draw_core(draw, t)
        annotations(draw, t)
        frames.append(img)

    gif_path = OUT_DIR / "04_outer_shell_feeds_core.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    frames[94].save(OUT_DIR / "04_outer_shell_feeds_core_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("04_outer_shell_feeds_core_preview.png")


if __name__ == "__main__":
    main()
