import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 720
CENTER = np.array([SIZE / 2, SIZE / 2], dtype=float)
FRAMES = 120
FPS_MS = 42
BG = (7, 10, 17)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (135, 151, 173)
CYAN = (74, 222, 255)
BLUE = (78, 144, 255)
VIOLET = (171, 120, 255)
AMBER = (255, 190, 82)
RED = (255, 86, 86)
RESERVOIR = (92, 180, 255)
SHELL = (120, 230, 255)


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
        draw.ellipse(box, outline=(*GRID, 115), width=1)
    draw.line((CENTER[0] - 310, CENTER[1], CENTER[0] + 310, CENTER[1]), fill=(*GRID, 95), width=1)
    draw.line((CENTER[0], CENTER[1] - 310, CENTER[0], CENTER[1] + 310), fill=(*GRID, 95), width=1)
    draw.text((28, 24), "Light Projection - Reservoir Shell", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 60),
        "Fourth mode fails outward; the outer reservoir fills the shell while stable mode 3 remains inside.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def glow_point(draw, xy, color, radius=8, alpha=255):
    x, y = xy
    for scale, frac in [(4.0, 0.08), (2.8, 0.13), (1.8, 0.22)]:
        rr = radius * scale
        draw.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(*color, int(alpha * frac)))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, alpha))


def ring(draw, radius, color, alpha, width=3):
    box = [CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius]
    draw.ellipse(box, outline=(*color, alpha), width=width)


def stable_threefold(draw, t):
    radius = 102
    colors = [CYAN, BLUE, VIOLET]
    points = []
    for k in range(3):
        angle = 2 * math.pi * t + 2 * math.pi * k / 3
        point = CENTER + radius * np.array([math.cos(angle), math.sin(angle)])
        points.append(point)
    draw.polygon([tuple(p) for p in points], outline=(*AMBER, 135))
    for k, point in enumerate(points):
        glow_point(draw, point, colors[k], radius=7)
    glow_point(draw, CENTER, (180, 196, 220), radius=3, alpha=155)


def reservoir_background(draw, t):
    fill = max(0.0, min(1.0, (t - 0.18) / 0.58))
    rng_phase = 0.17
    for idx in range(150):
        angle = 2 * math.pi * ((idx * 0.61803398875 + 0.035 * math.sin(4 * t)) % 1)
        outer_bias = (idx % 37) / 37
        radius = 260 + 95 * outer_bias + 16 * math.sin(idx + 5 * t)
        inward = 54 * fill * (1 - outer_bias)
        pos = CENTER + (radius - inward) * np.array([math.cos(angle), math.sin(angle)])
        alpha = int(8 + 68 * fill * (0.35 + 0.65 * outer_bias))
        draw.ellipse((pos[0] - 1.4, pos[1] - 1.4, pos[0] + 1.4, pos[1] + 1.4), fill=(*RESERVOIR, alpha))
    for idx in range(18):
        angle = 2 * math.pi * (idx / 18 + rng_phase * t)
        start = CENTER + 332 * np.array([math.cos(angle), math.sin(angle)])
        end = CENTER + (262 + 22 * math.sin(idx + 6 * t)) * np.array([math.cos(angle), math.sin(angle)])
        alpha = int(18 + 70 * fill)
        draw.line((*start, *end), fill=(*RESERVOIR, alpha), width=1)


def failed_fourth_to_shell(draw, t):
    fail = max(0.0, min(1.0, (t - 0.08) / 0.42))
    shell_fill = max(0.0, min(1.0, (t - 0.34) / 0.48))

    # Early fourth mode is visible only as an unstable attempted closure.
    square_radius = 132 + 65 * fail
    points = []
    for k in range(4):
        angle = math.pi / 4 + k * math.pi / 2 + 0.4 * t
        wobble = fail * 0.55 * math.sin(8 * t + k)
        point = CENTER + square_radius * np.array([math.cos(angle + wobble), math.sin(angle - wobble)])
        points.append(point)
    if fail < 0.95:
        alpha = int(150 * (1 - fail))
        draw.polygon([tuple(p) for p in points], outline=(*RED, alpha), width=2)
        for point in points:
            glow_point(draw, point, RED, radius=7, alpha=max(30, alpha))

    # Dissolution moves outward into the surrounding reservoir, not inward.
    for idx in range(80):
        angle = 2 * math.pi * (idx / 80 + 0.025 * t)
        distance = 145 + 155 * fail + 35 * math.sin(idx * 0.7 + 8 * t) * fail
        pos = CENTER + distance * np.array([math.cos(angle), math.sin(angle)])
        alpha = int(120 * fail * (1 - 0.45 * shell_fill))
        draw.ellipse((pos[0] - 1.7, pos[1] - 1.7, pos[0] + 1.7, pos[1] + 1.7), fill=(*RED, alpha))

    # The shell forms as a boundary fed by the outer reservoir.
    shell_radius = 236
    for width_idx, rad in enumerate([shell_radius - 7, shell_radius, shell_radius + 7]):
        alpha = int((50 + 80 * shell_fill) * (1 - 0.18 * width_idx))
        ring(draw, rad, SHELL, alpha, width=3)
    for idx in range(40):
        angle = 2 * math.pi * (idx / 40 - 0.05 * t)
        outer = CENTER + 310 * np.array([math.cos(angle), math.sin(angle)])
        inner = CENTER + (shell_radius + 10 * math.sin(idx + 4 * t)) * np.array(
            [math.cos(angle), math.sin(angle)]
        )
        alpha = int(105 * shell_fill)
        draw.line((*outer, *inner), fill=(*SHELL, alpha), width=2)

    # Keep a quiet gap: no fourth-mode streams from inside the stable triangle to shell.
    ring(draw, 154, (20, 26, 38), 190, width=5)
    ring(draw, 166, (20, 26, 38), 120, width=2)


def annotations(draw):
    draw.text((28, SIZE - 84), "inside: stable mode 3 remains coherent", fill=(190, 218, 245), font=FONT_SMALL)
    draw.text((28, SIZE - 58), "outside: dissolved fourth mode becomes reservoir/background", fill=(180, 205, 235), font=FONT_SMALL)
    draw.text((28, SIZE - 32), "shell: populated from outside reservoir, not emitted from the inner triangle", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        reservoir_background(draw, t)
        failed_fourth_to_shell(draw, t)
        stable_threefold(draw, t * 1.15)
        annotations(draw)
        frames.append(img)
    path = OUT_DIR / "02_light_projection_reservoir_shell.gif"
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    preview = frames[72].copy()
    preview.save(OUT_DIR / "02_light_projection_reservoir_shell_preview.png")
    return path


def main():
    path = make_animation()
    print(path.name)
    print("02_light_projection_reservoir_shell_preview.png")


if __name__ == "__main__":
    main()
