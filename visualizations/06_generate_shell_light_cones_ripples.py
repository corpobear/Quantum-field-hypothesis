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
LIGHT = (255, 245, 180)
RIPPLE = (166, 245, 255)


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
    draw.text((28, 24), "06 - Shell Receives Light as Cones and Ripples", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 60),
        "Core light reaches the shell in cones; the shell responds with water-like ripples.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def ring(draw, radius, color, alpha, width=2):
    box = [CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius]
    draw.ellipse(box, outline=(*color, alpha), width=width)


def glow_point(draw, xy, color, radius=8, alpha=255):
    x, y = xy
    for scale, frac in [(4.2, 0.07), (2.9, 0.13), (1.8, 0.24)]:
        rr = radius * scale
        draw.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(*color, int(alpha * frac)))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, alpha))


def shell_point(angle, radius=238):
    return CENTER + radius * np.array([math.cos(angle), math.sin(angle)])


def draw_shell(draw, t, activation):
    for radius, alpha in [(232, 130), (239, 180), (246, 95)]:
        ring(draw, radius, SHELL, alpha + int(60 * activation), width=3)

    # Water surface texture around the shell.
    for idx in range(144):
        a = 2 * math.pi * idx / 144
        wave = math.sin(9 * a - 2 * math.pi * 2.2 * t)
        r = 239 + 2.8 * wave * activation
        p = shell_point(a, r)
        alpha = int(70 + 90 * activation * (0.5 + 0.5 * wave))
        draw.ellipse((p[0] - 1.2, p[1] - 1.2, p[0] + 1.2, p[1] + 1.2), fill=(*SHELL, alpha))


def draw_core(draw, t):
    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 4.0 * t)
    radius = 27 + 7 * pulse
    for scale, frac in [(5.0, 0.07), (3.2, 0.13), (2.0, 0.23)]:
        rr = radius * scale
        draw.ellipse(
            (CENTER[0] - rr, CENTER[1] - rr, CENTER[0] + rr, CENTER[1] + rr),
            fill=(*AMBER, int(230 * frac)),
        )
    draw.ellipse(
        (CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius),
        fill=(*AMBER, 235),
    )
    inner = radius * (0.32 + 0.12 * pulse)
    draw.ellipse(
        (CENTER[0] - inner, CENTER[1] - inner, CENTER[0] + inner, CENTER[1] + inner),
        fill=(255, 252, 220, 245),
    )


def draw_threefold_markers(draw, t):
    colors = [CYAN, BLUE, VIOLET]
    radius = 104
    rot = 2 * math.pi * 0.45 * t
    pts = []
    for k in range(3):
        a = rot + 2 * math.pi * k / 3
        p = CENTER + radius * np.array([math.cos(a), 0.72 * math.sin(a)])
        pts.append(p)
    draw.polygon([tuple(p) for p in pts], outline=(*AMBER, 85))
    for k, p in enumerate(pts):
        glow_point(draw, p, colors[k], radius=6, alpha=205)


def draw_light_cones(draw, t):
    activation = 0.0
    cone_width = math.radians(20)
    base_rot = 2 * math.pi * 0.18 * t
    for k in range(3):
        a = base_rot + 2 * math.pi * k / 3
        pulse = (t * 1.45 + k / 3) % 1.0
        cone_alpha = int(58 + 80 * (1 - abs(pulse - 0.62)))
        tip = CENTER + 36 * np.array([math.cos(a), math.sin(a)])
        left = shell_point(a - cone_width)
        right = shell_point(a + cone_width)
        draw.polygon([tuple(tip), tuple(left), tuple(right)], fill=(*LIGHT, max(20, cone_alpha)))

        # Traveling bright ridge inside the cone.
        ridge_r = 52 + 184 * pulse
        ridge_center = CENTER + ridge_r * np.array([math.cos(a), math.sin(a)])
        ridge_span = 18 + 25 * pulse
        tangent = np.array([-math.sin(a), math.cos(a)])
        p1 = ridge_center - ridge_span * tangent
        p2 = ridge_center + ridge_span * tangent
        draw.line((*p1, *p2), fill=(*LIGHT, int(190 * (1 - pulse * 0.6))), width=3)

        if 0.82 < pulse < 0.99:
            activation = max(activation, (pulse - 0.82) / 0.17)
        impact = shell_point(a)
        glow_point(draw, impact, LIGHT, radius=5 + 5 * activation, alpha=170)
    return activation


def draw_water_ripples(draw, t):
    base_rot = 2 * math.pi * 0.18 * t
    for k in range(3):
        a = base_rot + 2 * math.pi * k / 3
        impact = shell_point(a)
        normal = np.array([math.cos(a), math.sin(a)])
        tangent = np.array([-math.sin(a), math.cos(a)])
        for ripple_idx in range(5):
            phase = (t * 2.2 - ripple_idx * 0.17 + k / 3) % 1.0
            width = 16 + 58 * phase
            height = 4 + 11 * phase
            alpha = int(150 * (1 - phase))
            points = []
            for j in range(42):
                u = -1.0 + 2.0 * j / 41
                offset = tangent * (u * width)
                wave = normal * (math.sin(u * math.pi * 2.0) * height)
                points.append(tuple(impact + offset + wave))
            for p1, p2 in zip(points, points[1:]):
                draw.line((*p1, *p2), fill=(*RIPPLE, alpha), width=2)


def annotations(draw):
    draw.text(
        (28, SIZE - 58),
        "state: light arrives in three cones and activates the shell locally",
        fill=(190, 220, 245),
        font=FONT_SMALL,
    )
    draw.text(
        (28, SIZE - 32),
        "geometry: shell response ripples like water, organizing into the A3 surface pattern",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        activation = draw_light_cones(draw, t)
        draw_shell(draw, t, activation)
        draw_water_ripples(draw, t)
        draw_threefold_markers(draw, t)
        draw_core(draw, t)
        annotations(draw)
        frames.append(img)

    gif_path = OUT_DIR / "06_shell_light_cones_ripples.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    frames[88].save(OUT_DIR / "06_shell_light_cones_ripples_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("06_shell_light_cones_ripples_preview.png")


if __name__ == "__main__":
    main()
