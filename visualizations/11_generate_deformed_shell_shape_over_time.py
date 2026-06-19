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
TRACE = (110, 235, 255)


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(27)
FONT_SMALL = font(16)


def knot_angles(t):
    wobble = 0.16 * math.sin(2 * math.pi * 0.32 * t)
    return [math.radians(90) + wobble, math.radians(210) - 0.7 * wobble, math.radians(330) + 0.4 * wobble]


def shell_radius(angle, t, base=118):
    # Time-varying projected deformation from the stable 3-knot anchors.
    strength = 0.62 + 0.22 * math.sin(2 * math.pi * 0.42 * t)
    r = base
    for ka in knot_angles(t):
        delta = math.atan2(math.sin(angle - ka), math.cos(angle - ka))
        r -= base * 0.115 * strength * math.exp(-(delta * delta) / (2 * 0.23 * 0.23))
    r += base * 0.022 * math.sin(2 * angle - 1.1 + 2 * math.pi * 0.21 * t)
    r += base * 0.016 * math.sin(5 * angle + 2 * math.pi * 0.38 * t)
    return r


def base_frame():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((28, 22), "11 - Deformed Shell Shape Evolves Through Time", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 56),
        "The projected shell boundary is tracked as a moving shape, not only as color/frequency.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def draw_current_shell(draw, t):
    center = np.array([180.0, 306.0])
    for r in [72, 112, 152]:
        draw.ellipse((center[0] - r, center[1] - r, center[0] + r, center[1] + r), outline=(*GRID, 95), width=1)
    pts = []
    for j in range(240):
        a = 2 * math.pi * j / 240
        rr = shell_radius(a, t, base=136)
        pts.append(tuple(center + rr * np.array([math.cos(a), math.sin(a)])))
    for p1, p2 in zip(pts, pts[1:] + pts[:1]):
        draw.line((*p1, *p2), fill=(*SHELL, 230), width=4)

    # Perfect sphere reference.
    draw.ellipse((center[0] - 136, center[1] - 136, center[0] + 136, center[1] + 136), outline=(*SHELL, 55), width=1)

    for ka in knot_angles(t):
        p = center + 82 * np.array([math.cos(ka), math.sin(ka)])
        anchor = center + shell_radius(ka, t, base=136) * np.array([math.cos(ka), math.sin(ka)])
        draw.line((*p, *anchor), fill=(*KNOT, 160), width=2)
        draw.ellipse((p[0] - 6, p[1] - 6, p[0] + 6, p[1] + 6), fill=(*KNOT, 210))
    draw.ellipse((center[0] - 30, center[1] - 30, center[0] + 30, center[1] + 30), fill=(*CORE, 230))
    draw.text((42, 120), "current projected shell", fill=MUTED, font=FONT_SMALL)


def draw_time_shape_map(draw, t):
    left, top, right, bottom = 370, 106, 940, 472
    width = right - left
    height = bottom - top
    mid_y = (top + bottom) / 2
    draw.rectangle((left, top, right, bottom), outline=(*GRID, 170), width=1)
    for i in range(9):
        x = left + width * i / 8
        draw.line((x, top, x, bottom), fill=(*GRID, 95), width=1)
    for j in range(7):
        y = top + height * j / 6
        draw.line((left, y, right, y), fill=(*GRID, 70), width=1)

    samples = 68
    cursor_x = left + ((t * 0.72) % 1.0) * width
    angles = np.linspace(0, 2 * math.pi, 96, endpoint=False)
    for s in range(samples):
        age = s / (samples - 1)
        x = cursor_x - age * width * 0.82
        if x < left:
            x += width
        tt = (t - age * 0.52) % 1.0
        alpha = int(35 + 185 * (1 - age))
        # Unroll boundary shape: vertical displacement is radius deviation over angle.
        points = []
        for idx, a in enumerate(angles):
            rr = shell_radius(float(a), tt, base=118)
            y = mid_y + (idx / (len(angles) - 1) - 0.5) * height * 0.86
            dx = (rr - 118) * 2.2
            points.append((x + dx, y))
        for p1, p2 in zip(points, points[1:]):
            draw.line((*p1, *p2), fill=(*TRACE, alpha), width=2)

    draw.line((cursor_x, top, cursor_x, bottom), fill=(255, 245, 180, 210), width=2)
    draw.text((cursor_x - 16, top - 24), "now", fill=(255, 245, 180), font=FONT_SMALL)
    draw.text((left, bottom + 16), "time ->", fill=MUTED, font=FONT_SMALL)
    draw.text((left - 4, top - 24), "shell shape unrolled by angle", fill=MUTED, font=FONT_SMALL)


def annotations(draw):
    draw.text((28, H - 54), "state: the deformed shell boundary is sampled through time", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text((28, H - 30), "geometry: each trace is the shell radius as a function of angle, moving along the time axis", fill=(180, 235, 245), font=FONT_SMALL)


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_current_shell(draw, t)
        draw_time_shape_map(draw, t)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "11_deformed_shell_shape_over_time.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[96].save(OUT_DIR / "11_deformed_shell_shape_over_time_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("11_deformed_shell_shape_over_time_preview.png")


if __name__ == "__main__":
    main()
