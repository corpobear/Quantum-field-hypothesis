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
ARROW = (255, 245, 180)
KNOT = (255, 196, 96)


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
        draw.ellipse(box, outline=(*GRID, 92), width=1)
    draw.text((28, 24), "09 - Three-Knot Projection Deforms Shell", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (28, 60),
        "Stable 3-knot shapes inside the projection pull the shell away from perfect spherical form.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    return img


def rho_compression(radius):
    # Visual proxy for rho_0(r): stronger inward compression near the core.
    alpha = 0.055
    m0 = 2.0
    r_core = 44.0
    return alpha * m0 * 5400.0 / (radius * radius + r_core * r_core)


def deform_radius(base_radius, angle, strength):
    radial_pull = rho_compression(base_radius)
    deformation = strength * base_radius * radial_pull * 0.55
    for knot_angle in knot_angles():
        delta = math.atan2(math.sin(angle - knot_angle), math.cos(angle - knot_angle))
        # Three stable knot projections locally dent/pull the shell.
        deformation += strength * base_radius * radial_pull * 1.25 * math.exp(
            -(delta * delta) / (2 * 0.26 * 0.26)
        )
    deformation += strength * base_radius * radial_pull * 0.22 * math.sin(2 * angle - 0.7)
    return base_radius - deformation


def knot_angles():
    return [math.radians(90), math.radians(210), math.radians(330)]


def shell_point(radius, angle, strength):
    r = deform_radius(radius, angle, strength)
    return CENTER + r * np.array([math.cos(angle), math.sin(angle)])


def draw_core(draw, strength):
    radius = 42 + 8 * strength
    for scale, frac in [(5.0, 0.06), (3.3, 0.12), (2.0, 0.24)]:
        rr = radius * scale
        draw.ellipse(
            (CENTER[0] - rr, CENTER[1] - rr, CENTER[0] + rr, CENTER[1] + rr),
            fill=(*CORE, int(235 * frac)),
        )
    draw.ellipse(
        (CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius),
        fill=(*CORE, 238),
    )
    inner = radius * 0.34
    draw.ellipse(
        (CENTER[0] - inner, CENTER[1] - inner, CENTER[0] + inner, CENTER[1] + inner),
        fill=(255, 252, 220, 245),
    )


def draw_knot_projection(draw, strength):
    knot_radius = 116
    for idx, angle in enumerate(knot_angles()):
        center = CENTER + knot_radius * np.array([math.cos(angle), math.sin(angle)])
        tangent = np.array([-math.sin(angle), math.cos(angle)])
        normal = np.array([math.cos(angle), math.sin(angle)])

        pts = []
        for j in range(90):
            u = 2 * math.pi * j / 90
            r1 = 30 + 8 * math.sin(3 * u)
            point = center + tangent * (r1 * math.cos(u)) + normal * (16 * math.sin(u))
            pts.append(tuple(point))
        for p1, p2 in zip(pts, pts[1:] + pts[:1]):
            draw.line((*p1, *p2), fill=(*KNOT, int(80 + 95 * strength)), width=2)

        shell_anchor = shell_point(253, angle, strength)
        draw.line((*center, *shell_anchor), fill=(*KNOT, int(40 + 95 * strength)), width=2)
        draw.ellipse(
            (center[0] - 5, center[1] - 5, center[0] + 5, center[1] + 5),
            fill=(*KNOT, int(150 + 80 * strength)),
        )


def draw_gravity(draw, strength):
    for radius in [78, 116, 156, 198, 244, 292]:
        alpha = int(32 + 78 * strength * (1 - min(radius / 340, 0.8)))
        box = [CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius]
        draw.ellipse(box, outline=(*GRAVITY, alpha), width=2)


def draw_deformed_bands(draw, t, strength):
    band_count = 16
    for idx in range(band_count):
        u = idx / (band_count - 1)
        base_radius = 135 + 118 * u
        color = spectral_color(0.08 * idx + 0.11 * t)
        alpha = int(45 + 130 * u)
        pts = [tuple(shell_point(base_radius, 2 * math.pi * j / 220, strength)) for j in range(220)]
        for p1, p2 in zip(pts, pts[1:] + pts[:1]):
            draw.line((*p1, *p2), fill=(*color, alpha), width=2 if idx % 2 else 3)

    # Perfect sphere reference fades as deformation grows.
    ref_alpha = int(95 * (1 - strength))
    if ref_alpha > 4:
        for radius in [135, 180, 220, 253]:
            box = [CENTER[0] - radius, CENTER[1] - radius, CENTER[0] + radius, CENTER[1] + radius]
            draw.ellipse(box, outline=(*SHELL, ref_alpha), width=1)

    # Outer deformed boundary.
    pts = [tuple(shell_point(253, 2 * math.pi * j / 260, strength)) for j in range(260)]
    for p1, p2 in zip(pts, pts[1:] + pts[:1]):
        draw.line((*p1, *p2), fill=(*SHELL, 225), width=4)


def draw_inward_arrows(draw, strength):
    for idx in range(18):
        angle = 2 * math.pi * idx / 18
        outer = CENTER + 278 * np.array([math.cos(angle), math.sin(angle)])
        inner = shell_point(230, angle, strength)
        length_scale = rho_compression(140 + 110 * (idx % 3) / 2)
        tip = outer + (inner - outer) * (0.45 + 1.7 * strength * length_scale)
        draw.line((*outer, *tip), fill=(*ARROW, int(30 + 105 * strength)), width=2)
        # Arrow head.
        tangent = np.array([-math.sin(angle), math.cos(angle)])
        back = normalize(outer - tip)
        left = tip + 8 * back + 5 * tangent
        right = tip + 8 * back - 5 * tangent
        draw.polygon([tuple(tip), tuple(left), tuple(right)], fill=(*ARROW, int(40 + 120 * strength)))

    for angle in knot_angles():
        outer = CENTER + 285 * np.array([math.cos(angle), math.sin(angle)])
        inner = shell_point(253, angle, strength)
        draw.line((*outer, *inner), fill=(*KNOT, int(80 + 130 * strength)), width=4)


def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


def annotations(draw):
    draw.text(
        (28, SIZE - 58),
        "state: stable 3-knot projection dents the once-spherical outer shell",
        fill=(190, 220, 245),
        font=FONT_SMALL,
    )
    draw.text(
        (28, SIZE - 32),
        "geometry: shell deformation follows the three internal knot anchors",
        fill=(180, 235, 245),
        font=FONT_SMALL,
    )


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        strength = max(0.0, min(1.0, (t - 0.08) / 0.78))
        strength = strength * strength * (3 - 2 * strength)
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_gravity(draw, strength)
        draw_inward_arrows(draw, strength)
        draw_knot_projection(draw, strength)
        draw_deformed_bands(draw, t, strength)
        draw_core(draw, strength)
        annotations(draw)
        frames.append(img)

    gif_path = OUT_DIR / "09_outer_shell_pattern_deforms.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=FPS_MS,
        loop=0,
        optimize=True,
    )
    frames[108].save(OUT_DIR / "09_outer_shell_pattern_deforms_preview.png")
    return gif_path


def main():
    path = make_animation()
    print(path.name)
    print("09_outer_shell_pattern_deforms_preview.png")


if __name__ == "__main__":
    main()
