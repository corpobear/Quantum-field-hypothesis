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
LIGHT = (255, 245, 180)


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
    draw.text((28, 24), "05 - Core Vibrates and Lights the Shell", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 60),
        "Shell-fed core vibration sends light outward until the shell responds.",
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


def draw_shell(draw, t, impact):
    for radius, alpha in [(232, 170), (239, 120), (246, 76)]:
        ring(draw, radius, SHELL, alpha + int(55 * impact), width=3)
    for idx in range(72):
        a = 2 * math.pi * (idx / 72 + 0.025 * t)
        r = 236 + 8 * math.sin(idx + 5 * t)
        p = CENTER + r * np.array([math.cos(a), math.sin(a)])
        alpha = 105 + int(90 * impact * (0.5 + 0.5 * math.sin(idx + 12 * t)))
        draw.ellipse((p[0] - 1.6, p[1] - 1.6, p[0] + 1.6, p[1] + 1.6), fill=(*SHELL, alpha))


def draw_inflow(draw, t):
    # Keep a subtler version of operation 04 so the core is visibly still fed by shell mass.
    for idx in range(32):
        a = 2 * math.pi * (idx / 32 + 0.02 * math.sin(2 * math.pi * t))
        phase = (t * 1.1 + idx / 32) % 1.0
        shell_r = 232
        core_r = 34
        r = shell_r - (shell_r - core_r) * phase
        p = CENTER + r * np.array([math.cos(a), math.sin(a)])
        alpha = int(45 + 60 * (1 - phase))
        start = CENTER + shell_r * np.array([math.cos(a), math.sin(a)])
        draw.line((*start, *p), fill=(*SHELL, 32), width=1)
        draw.ellipse((p[0] - 1.8, p[1] - 1.8, p[0] + 1.8, p[1] + 1.8), fill=(*SHELL, alpha))


def draw_threefold(draw, t):
    radius = 105
    points = []
    colors = [CYAN, BLUE, VIOLET]
    wobble_y = 0.62 + 0.18 * math.sin(2 * math.pi * 0.85 * t)
    rot = 2 * math.pi * 0.9 * t
    for k in range(3):
        a = rot + 2 * math.pi * k / 3
        p = CENTER + radius * np.array([math.cos(a), wobble_y * math.sin(a)])
        points.append(p)
    draw.polygon([tuple(p) for p in points], outline=(*AMBER, 125))
    for k, p in enumerate(points):
        glow_point(draw, p, colors[k], radius=7, alpha=235)


def draw_light_emission(draw, t):
    impact = 0.0
    for pulse_idx in range(4):
        phase = (t * 1.65 - pulse_idx * 0.25) % 1.0
        radius = 36 + phase * 202
        alpha = int(185 * (1.0 - phase))
        if radius > 210:
            impact = max(impact, 1.0 - abs(radius - 232) / 28)
        ring(draw, radius, LIGHT, alpha, width=3)
        ring(draw, radius + 6, LIGHT, int(alpha * 0.28), width=2)
    for idx in range(18):
        a = 2 * math.pi * (idx / 18 + 0.04 * math.sin(4 * t))
        flicker = 0.55 + 0.45 * math.sin(2 * math.pi * 3.3 * t + idx)
        end = CENTER + 222 * np.array([math.cos(a), math.sin(a)])
        draw.line((*CENTER, *end), fill=(*LIGHT, int(22 * flicker)), width=1)
    return max(0.0, min(1.0, impact))


def draw_core(draw, t):
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 4.0 * t)
    jitter = np.array(
        [
            2.2 * math.sin(2 * math.pi * 7.0 * t),
            2.2 * math.cos(2 * math.pi * 5.5 * t),
        ]
    )
    core_center = CENTER + jitter
    radius = 28 + 8 * pulse
    alpha = 230
    for scale, frac in [(5.2, 0.07), (3.5, 0.12), (2.1, 0.22)]:
        rr = radius * scale
        draw.ellipse(
            (core_center[0] - rr, core_center[1] - rr, core_center[0] + rr, core_center[1] + rr),
            fill=(*CORE, int(alpha * frac)),
        )
    draw.ellipse(
        (core_center[0] - radius, core_center[1] - radius, core_center[0] + radius, core_center[1] + radius),
        fill=(*CORE, alpha),
    )
    inner = radius * (0.3 + 0.16 * pulse)
    draw.ellipse(
        (core_center[0] - inner, core_center[1] - inner, core_center[0] + inner, core_center[1] + inner),
        fill=(255, 250, 214, 245),
    )


def annotations(draw, t):
    state = "state: shell-fed core vibrates; vibration emits light back to the shell"
    draw.text((28, SIZE - 58), state, fill=(190, 220, 245), font=FONT_SMALL)
    draw.text(
        (28, SIZE - 32),
        "geometry: inward mass feed and outward light response form the first core-shell feedback",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        impact = draw_light_emission(draw, t)
        draw_shell(draw, t, impact)
        draw_inflow(draw, t)
        draw_threefold(draw, t)
        draw_core(draw, t)
        annotations(draw, t)
        frames.append(img)

    gif_path = OUT_DIR / "05_core_vibration_light_to_shell.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    frames[86].save(OUT_DIR / "05_core_vibration_light_to_shell_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("05_core_vibration_light_to_shell_preview.png")


if __name__ == "__main__":
    main()
