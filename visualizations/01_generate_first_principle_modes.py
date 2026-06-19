import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 640
CENTER = np.array([SIZE / 2, SIZE / 2], dtype=float)
FRAMES = 96
FPS_MS = 42
BG = (8, 11, 18)
GRID = (24, 31, 45)
TEXT = (222, 232, 245)
MUTED = (132, 148, 170)
CYAN = (74, 222, 255)
BLUE = (78, 144, 255)
AMBER = (255, 184, 77)
RED = (255, 86, 86)
VIOLET = (171, 120, 255)


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(26)
FONT_SMALL = font(16)


def base_frame(title, subtitle):
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    for r in range(80, 300, 44):
        bbox = [CENTER[0] - r, CENTER[1] - r, CENTER[0] + r, CENTER[1] + r]
        draw.ellipse(bbox, outline=(*GRID, 130), width=1)
    draw.line((CENTER[0] - 270, CENTER[1], CENTER[0] + 270, CENTER[1]), fill=(*GRID, 110), width=1)
    draw.line((CENTER[0], CENTER[1] - 270, CENTER[0], CENTER[1] + 270), fill=(*GRID, 110), width=1)
    draw.text((28, 24), title, fill=TEXT, font=FONT_TITLE)
    draw.text((28, 58), subtitle, fill=MUTED, font=FONT_SMALL)
    return img


def glow_point(draw, xy, color, radius=8, alpha=255):
    x, y = xy
    for i, scale in enumerate([4.2, 3.0, 2.0]):
        a = int(alpha * [0.08, 0.13, 0.2][i])
        rr = radius * scale
        draw.ellipse((x - rr, y - rr, x + rr, y + rr), fill=(*color, a))
    draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=(*color, alpha))
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill=(255, 255, 255, alpha))


def draw_trail(draw, points, color):
    if len(points) < 2:
        return
    for idx in range(1, len(points)):
        alpha = int(190 * idx / len(points))
        draw.line((*points[idx - 1], *points[idx]), fill=(*color, alpha), width=2)


def save_gif(name, frames):
    path = OUT_DIR / name
    frames[0].save(
        path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    return path


def mode1_point():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame(
            "Mode 1 - Point",
            "One stable center: no orbit, no surface loop, only retained position.",
        )
        draw = ImageDraw.Draw(img, "RGBA")
        pulse = 1.0 + 0.18 * math.sin(2 * math.pi * t)
        glow_point(draw, CENTER, CYAN, radius=10 * pulse)
        draw.text((28, SIZE - 48), "state: stable point seed", fill=MUTED, font=FONT_SMALL)
        frames.append(img)
    return save_gif("01a_first_principle_mode_1_point.gif", frames)


def mode2_binary():
    frames = []
    trail_a = []
    trail_b = []
    radius = 115
    for i in range(FRAMES):
        t = i / FRAMES
        angle = 2 * math.pi * t
        p1 = CENTER + radius * np.array([math.cos(angle), math.sin(angle)])
        p2 = CENTER - radius * np.array([math.cos(angle), math.sin(angle)])
        trail_a.append(tuple(p1))
        trail_b.append(tuple(p2))
        trail_a = trail_a[-38:]
        trail_b = trail_b[-38:]

        img = base_frame(
            "Mode 2 - Stable Pair",
            "Two points circle one shared center: binary stability and balanced exchange.",
        )
        draw = ImageDraw.Draw(img, "RGBA")
        draw.ellipse(
            (CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius),
            outline=(*BLUE, 90),
            width=2,
        )
        draw.line((*p1, *p2), fill=(*MUTED, 75), width=1)
        draw_trail(draw, trail_a, CYAN)
        draw_trail(draw, trail_b, BLUE)
        glow_point(draw, p1, CYAN, radius=8)
        glow_point(draw, p2, BLUE, radius=8)
        glow_point(draw, CENTER, MUTED, radius=3, alpha=160)
        draw.text((28, SIZE - 48), "state: stable two-body loop", fill=MUTED, font=FONT_SMALL)
        frames.append(img)
    return save_gif("01b_first_principle_mode_2_stable_pair.gif", frames)


def mode3_lagrange_triangle():
    frames = []
    trails = [[], [], []]
    radius = 128
    colors = [CYAN, BLUE, VIOLET]
    for i in range(FRAMES):
        t = i / FRAMES
        base_angle = 2 * math.pi * t
        points = []
        for k in range(3):
            angle = base_angle + 2 * math.pi * k / 3
            point = CENTER + radius * np.array([math.cos(angle), math.sin(angle)])
            points.append(point)
            trails[k].append(tuple(point))
            trails[k] = trails[k][-42:]

        img = base_frame(
            "Mode 3 - Stable Threefold Loop",
            "Three-body Lagrange-style choreography: equal spacing preserves the loop.",
        )
        draw = ImageDraw.Draw(img, "RGBA")
        poly = [tuple(p) for p in points]
        draw.polygon(poly, outline=(*AMBER, 135))
        for k, point in enumerate(points):
            draw_trail(draw, trails[k], colors[k])
            glow_point(draw, point, colors[k], radius=8)
        glow_point(draw, CENTER, MUTED, radius=3, alpha=150)
        draw.text((28, SIZE - 48), "state: stable three-loop surface activation", fill=MUTED, font=FONT_SMALL)
        frames.append(img)
    return save_gif("01c_first_principle_mode_3_stable_threefold.gif", frames)


def mode4_dissolve():
    frames = []
    trails = [[], [], [], []]
    colors = [CYAN, BLUE, VIOLET, AMBER]
    rng = np.random.default_rng(4)
    phase_offsets = rng.uniform(-0.25, 0.25, size=4)
    for i in range(FRAMES):
        t = i / (FRAMES - 1)
        angle = 2 * math.pi * (1.05 * t)
        instability = max(0.0, (t - 0.28) / 0.72)
        spread = 95 + 230 * instability**1.55
        fade = int(255 * (1.0 - 0.72 * instability))
        points = []
        for k in range(4):
            square_angle = angle + math.pi / 4 + k * math.pi / 2
            wobble = 0.5 * math.sin(10 * t + k) * instability
            drift = np.array(
                [
                    math.cos(square_angle + phase_offsets[k] + wobble),
                    math.sin(square_angle + phase_offsets[k] - wobble),
                ]
            )
            turbulent = instability * np.array(
                [
                    38 * math.sin(13 * t + 1.7 * k),
                    38 * math.cos(11 * t + 1.3 * k),
                ]
            )
            point = CENTER + spread * drift + turbulent
            points.append(point)
            trails[k].append(tuple(point))
            trails[k] = trails[k][-34:]

        img = base_frame(
            "Mode 4 - Failed Stability",
            "Fourth mode cannot close: square symmetry breaks, load dissolves outward.",
        )
        draw = ImageDraw.Draw(img, "RGBA")
        if t < 0.32:
            draw.polygon([tuple(p) for p in points], outline=(*AMBER, 130), width=2)
        else:
            for a, b in zip(points, points[1:] + points[:1]):
                draw.line((*a, *b), fill=(*RED, int(95 * (1 - instability))), width=2)
        for k, point in enumerate(points):
            draw_trail(draw, trails[k], RED if instability > 0.45 else colors[k])
            glow_point(draw, point, RED if instability > 0.45 else colors[k], radius=8, alpha=max(35, fade))
        # Dissolving particles.
        for dust_idx in range(46):
            dust_angle = 2 * math.pi * ((dust_idx / 46) + 0.31 * t)
            dust_r = 70 + 285 * instability + 28 * math.sin(dust_idx + 8 * t)
            dust = CENTER + dust_r * np.array([math.cos(dust_angle), math.sin(dust_angle)])
            alpha = int(150 * instability * (1 - 0.45 * t))
            draw.ellipse((dust[0] - 1.8, dust[1] - 1.8, dust[0] + 1.8, dust[1] + 1.8), fill=(*RED, alpha))
        glow_point(draw, CENTER, RED, radius=4 + 8 * instability, alpha=210)
        draw.text((28, SIZE - 48), "state: failed fourth mode -> central residue and outward dissolution", fill=MUTED, font=FONT_SMALL)
        frames.append(img)
    return save_gif("01d_first_principle_mode_4_failed_dissolve.gif", frames)


def contact_sheet(paths):
    labels = [
        "Mode 1",
        "Mode 2",
        "Mode 3",
        "Mode 4",
    ]
    thumbs = []
    for path in paths:
        with Image.open(path) as img:
            img.seek(FRAMES // 3)
            thumb = img.convert("RGB").resize((260, 260))
            thumbs.append(thumb)
    sheet = Image.new("RGB", (1120, 340), BG)
    draw = ImageDraw.Draw(sheet, "RGBA")
    for idx, thumb in enumerate(thumbs):
        x = 24 + idx * 274
        sheet.paste(thumb, (x, 50))
        draw.text((x, 18), labels[idx], fill=TEXT, font=FONT_TITLE)
    sheet.save(OUT_DIR / "01_first_principle_modes_contact_sheet.png")


def main():
    paths = [
        mode1_point(),
        mode2_binary(),
        mode3_lagrange_triangle(),
        mode4_dissolve(),
    ]
    contact_sheet(paths)
    for path in paths:
        print(path.name)
    print("01_first_principle_modes_contact_sheet.png")


if __name__ == "__main__":
    main()
