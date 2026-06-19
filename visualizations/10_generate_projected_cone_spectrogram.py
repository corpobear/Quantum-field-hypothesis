import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
W, H = 960, 560
FRAMES = 144
FPS_MS = 42
BG = (7, 10, 17)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
SHELL = (120, 230, 255)
CORE = (255, 210, 112)
LIGHT = (255, 245, 180)


SPECTRUM = [
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


def lerp_color(a, b, u):
    return tuple(int(a[i] + (b[i] - a[i]) * u) for i in range(3))


def heat_color(value):
    value = max(0.0, min(1.0, value))
    pos = value * (len(SPECTRUM) - 1)
    i = int(pos)
    j = min(i + 1, len(SPECTRUM) - 1)
    return lerp_color(SPECTRUM[i], SPECTRUM[j], pos - i)


def base_frame():
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((28, 22), "10 - Projected Cone Spectrogram", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 56),
        "One cone is projected into a time-frequency map: color preserves changing shell response.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def signal_intensity(time_value, freq_value, frame_t):
    # One selected cone with drifting core frequency, harmonics, and ripple sidebands.
    carrier = 0.34 + 0.26 * math.sin(2 * math.pi * (0.42 * time_value + 0.16 * math.sin(2 * math.pi * frame_t)))
    harmonic = min(0.95, carrier * 1.72)
    low_sideband = max(0.05, carrier - 0.16 - 0.05 * math.sin(2 * math.pi * time_value))
    high_sideband = min(0.98, carrier + 0.18 + 0.04 * math.cos(2 * math.pi * time_value))

    def ridge(center, width, gain):
        return gain * math.exp(-((freq_value - center) ** 2) / (2 * width * width))

    cone_gate = 0.45 + 0.55 * max(0.0, math.sin(2 * math.pi * (1.2 * time_value - 0.18)))
    ripple_mod = 0.5 + 0.5 * math.sin(2 * math.pi * (8.0 * time_value - 3.5 * freq_value))
    intensity = ridge(carrier, 0.028, 1.0)
    intensity += ridge(harmonic, 0.022, 0.46)
    intensity += ridge(low_sideband, 0.018, 0.34 * ripple_mod)
    intensity += ridge(high_sideband, 0.018, 0.30 * (1 - ripple_mod))
    intensity *= cone_gate
    return max(0.0, min(1.0, intensity))


def draw_spectrogram(draw, frame_t):
    left, top, right, bottom = 286, 96, 922, 456
    width = right - left
    height = bottom - top

    # Draw heatmap at a practical resolution, then scale via rectangles.
    cols = 160
    rows = 92
    cursor = int((frame_t * 0.82 % 1.0) * cols)
    for x_idx in range(cols):
        for y_idx in range(rows):
            # Scroll time so the current slice advances left-to-right.
            time_value = ((x_idx - cursor) % cols) / cols
            freq_value = 1.0 - y_idx / (rows - 1)
            intensity = signal_intensity(time_value, freq_value, frame_t)
            # Keep old history dimmer than the most recent region.
            age = ((cursor - x_idx) % cols) / cols
            recency = 0.45 + 0.55 * (1 - age)
            color = heat_color(intensity * recency)
            alpha = int(35 + 220 * intensity * recency)
            x0 = left + x_idx * width / cols
            x1 = left + (x_idx + 1) * width / cols + 1
            y0 = top + y_idx * height / rows
            y1 = top + (y_idx + 1) * height / rows + 1
            draw.rectangle((x0, y0, x1, y1), fill=(*color, alpha))

    # Grid and cursor.
    draw.rectangle((left, top, right, bottom), outline=(*GRID, 180), width=1)
    for i in range(9):
        x = left + i * width / 8
        draw.line((x, top, x, bottom), fill=(*GRID, 105), width=1)
    for j in range(7):
        y = top + j * height / 6
        draw.line((left, y, right, y), fill=(*GRID, 105), width=1)
    cursor_x = left + cursor * width / cols
    draw.line((cursor_x, top, cursor_x, bottom), fill=(*LIGHT, 210), width=2)
    draw.text((cursor_x - 16, top - 24), "now", fill=LIGHT, font=FONT_SMALL)
    draw.text((left, bottom + 16), "time ->", fill=MUTED, font=FONT_SMALL)
    draw.text((left - 14, top - 24), "frequency / projected ripple mode", fill=MUTED, font=FONT_SMALL)
    draw.text((right - 132, bottom + 16), "cone history", fill=MUTED, font=FONT_SMALL)


def draw_cone_panel(draw, frame_t):
    center = np.array([142.0, 288.0])
    shell_r = 105
    angle = -0.45 + 0.16 * math.sin(2 * math.pi * frame_t)
    width = math.radians(17)
    for r, alpha in [(shell_r - 5, 90), (shell_r, 180), (shell_r + 5, 90)]:
        draw.ellipse((center[0] - r, center[1] - r, center[0] + r, center[1] + r), outline=(*SHELL, alpha), width=2)

    for rr, alpha in [(42, 35), (27, 85), (17, 230)]:
        draw.ellipse((center[0] - rr, center[1] - rr, center[0] + rr, center[1] + rr), fill=(*CORE, alpha))

    tip = center + 24 * np.array([math.cos(angle), math.sin(angle)])
    left = center + shell_r * np.array([math.cos(angle - width), math.sin(angle - width)])
    right = center + shell_r * np.array([math.cos(angle + width), math.sin(angle + width)])
    impact = center + shell_r * np.array([math.cos(angle), math.sin(angle)])
    draw.polygon([tuple(tip), tuple(left), tuple(right)], fill=(*LIGHT, 72))
    draw.line((*tip, *impact), fill=(*LIGHT, 190), width=3)

    pulse = 0.5 + 0.5 * math.sin(2 * math.pi * 4 * frame_t)
    tangent = np.array([-math.sin(angle), math.cos(angle)])
    normal = np.array([math.cos(angle), math.sin(angle)])
    for k in range(5):
        phase = (frame_t * 2.4 - k * 0.15) % 1.0
        span = 12 + 46 * phase
        height = 5 + 13 * phase
        alpha = int(170 * (1 - phase))
        pts = []
        for i in range(36):
            u = -1 + 2 * i / 35
            pts.append(tuple(impact + tangent * (u * span) + normal * (math.sin(u * math.pi * 2) * height)))
        for p1, p2 in zip(pts, pts[1:]):
            draw.line((*p1, *p2), fill=(120, 235, 255, alpha), width=2)
    draw.text((34, 112), "selected cone", fill=MUTED, font=FONT_SMALL)
    draw.text((34, 444), "impact signal -> spectrogram", fill=MUTED, font=FONT_SMALL)


def annotations(draw):
    draw.text(
        (28, H - 54),
        "state: one cone's projected shell impact becomes a spectrogram over time",
        fill=(190, 220, 245),
        font=FONT_SMALL,
    )
    draw.text(
        (28, H - 30),
        "geometry: changing core frequency, ripple harmonics, and sidebands are preserved as color intensity",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_cone_panel(draw, t)
        draw_spectrogram(draw, t)
        annotations(draw)
        frames.append(img)

    gif_path = OUT_DIR / "10_projected_cone_spectrogram.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    frames[96].save(OUT_DIR / "10_projected_cone_spectrogram_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("10_projected_cone_spectrogram_preview.png")


if __name__ == "__main__":
    main()
