import csv
import math
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


OUT_DIR = Path(__file__).resolve().parent
SIZE = 980
FRAMES = 120
FPS_MS = 50
VISUAL_EARTH_ORBITS = 1.2
VISUAL_PERIOD_EXPONENT = 0.6
BG = (5, 8, 14)
GRID = (24, 31, 45)
TEXT = (224, 233, 245)
MUTED = (136, 152, 174)
FABRIC_A = (92, 255, 224)
FABRIC_B = (178, 132, 255)
SHELL = (120, 230, 255)
CORE = (255, 218, 126)
TENSION = (255, 150, 96)
ORBIT = (82, 100, 134)


PLANETS = [
    {"name": "Mercury", "a": 0.387, "period": 0.241, "mass_e": 0.055, "color": (180, 174, 160), "size": 3},
    {"name": "Venus", "a": 0.723, "period": 0.615, "mass_e": 0.815, "color": (234, 192, 122), "size": 5},
    {"name": "Earth", "a": 1.000, "period": 1.000, "mass_e": 1.000, "color": (98, 170, 255), "size": 5},
    {"name": "Mars", "a": 1.524, "period": 1.881, "mass_e": 0.107, "color": (225, 112, 78), "size": 4},
    {"name": "Jupiter", "a": 5.203, "period": 11.862, "mass_e": 317.8, "color": (220, 178, 132), "size": 11},
    {"name": "Saturn", "a": 9.537, "period": 29.457, "mass_e": 95.2, "color": (222, 199, 132), "size": 10},
    {"name": "Uranus", "a": 19.191, "period": 84.017, "mass_e": 14.5, "color": (137, 220, 220), "size": 8},
    {"name": "Neptune", "a": 30.069, "period": 164.8, "mass_e": 17.1, "color": (91, 128, 239), "size": 8},
]


def font(size=20):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except OSError:
        return ImageFont.load_default()


FONT_TITLE = font(27)
FONT_SMALL = font(15)
FONT_TINY = font(13)


def rotation_matrix(axis, angle):
    axis = np.array(axis, dtype=float)
    axis /= np.linalg.norm(axis)
    x, y, z = axis
    c = math.cos(angle)
    s = math.sin(angle)
    C = 1 - c
    return np.array(
        [
            [c + x * x * C, x * y * C - z * s, x * z * C + y * s],
            [y * x * C + z * s, c + y * y * C, y * z * C - x * s],
            [z * x * C - y * s, z * y * C + x * s, c + z * z * C],
        ]
    )


ROT = rotation_matrix([1, 0, 0], math.radians(61)) @ rotation_matrix([0, 0, 1], math.radians(-28))
CENTER = np.array([SIZE / 2, SIZE / 2 + 88])
SCALE = 168
R_MAX = math.log1p(30.069)


def map_radius(au):
    return 0.24 + 2.50 * math.log1p(au) / R_MAX


for p in PLANETS:
    p["r"] = map_radius(p["a"])
    p["coupling"] = math.sqrt(p["mass_e"]) / (p["r"] * p["r"] + 0.20)

MAX_COUPLING = max(p["coupling"] for p in PLANETS)
for p in PLANETS:
    p["coupling_norm"] = p["coupling"] / MAX_COUPLING
    p["visual_period"] = p["period"] ** VISUAL_PERIOD_EXPONENT

MEMORY_WEIGHTS = {
    "Mercury": 0.06,
    "Venus": 0.12,
    "Earth": 0.48,
    "Mars": 0.10,
    "Jupiter": 1.00,
    "Saturn": 0.86,
    "Uranus": 0.16,
    "Neptune": 0.13,
}


def project(point):
    p = ROT @ np.array(point, dtype=float)
    depth = 840 + p[2] * 72
    perspective = 840 / depth
    xy = CENTER + perspective * SCALE * np.array([p[0], -p[1]])
    return xy, p[2]


def planet_angle(planet, t):
    phase = {
        "Mercury": 0.06,
        "Venus": 0.31,
        "Earth": 0.58,
        "Mars": 0.80,
        "Jupiter": 0.15,
        "Saturn": 0.42,
        "Uranus": 0.68,
        "Neptune": 0.89,
    }[planet["name"]]
    visual_orbits = VISUAL_EARTH_ORBITS / planet["visual_period"]
    return 2 * math.pi * (phase + visual_orbits * t)


def planet_position(planet, t):
    a = planet_angle(planet, t)
    return np.array([planet["r"] * math.cos(a), planet["r"] * math.sin(a), 0.0])


def central_compression(x, y):
    r2 = x * x + y * y
    return math.exp(-r2 / 1.45)


def orbital_shear(x, y, t):
    point = np.array([x, y])
    value = 0.0
    for p in PLANETS:
        pp = planet_position(p, t)[:2]
        d2 = float(np.sum((point - pp) ** 2))
        orbital_band = math.exp(-((math.sqrt(x * x + y * y) - p["r"]) ** 2) / 0.018)
        local_pull = math.exp(-d2 / (0.018 + 0.015 * p["coupling_norm"]))
        value += 0.35 * p["coupling_norm"] * local_pull + 0.05 * p["coupling_norm"] * orbital_band
    return value


def threefold_shell_memory(x, y, t):
    a = math.atan2(y, x)
    r = math.sqrt(x * x + y * y)
    outer = 1 / (1 + math.exp(-(r - 1.10) * 4.0))
    phase = 0.35 * math.sin(2 * math.pi * t)
    return outer * (0.5 + 0.5 * math.cos(3 * a + phase))


def long_term_shell_memory(x, y):
    radius = math.sqrt(x * x + y * y)
    angle = math.atan2(y, x)
    value = 0.0
    for p in PLANETS:
        weight = MEMORY_WEIGHTS[p["name"]]
        width = 0.030 + 0.018 * p["coupling_norm"]
        groove = math.exp(-((radius - p["r"]) ** 2) / (2 * width * width))
        edge = math.exp(-((abs(radius - p["r"]) - width * 1.45) ** 2) / (2 * (width * 0.42) ** 2))
        corrugation = 0.72 + 0.28 * math.cos(24 * angle + 3 * p["r"])
        value += weight * (0.70 * groove + 0.30 * edge) * corrugation
    return value


def fabric_point(x, y, t):
    c = central_compression(x, y)
    s = orbital_shear(x, y, t)
    m = threefold_shell_memory(x, y, t)
    lm = long_term_shell_memory(x, y)
    z = 0.44 * c + 0.34 * s + 0.16 * m + 0.15 * lm + 0.04 * math.sin(3 * x - 2 * y + 2 * math.pi * t)
    inward = 0.10 * c + 0.045 * s + 0.012 * lm
    tx = x * (1 - inward)
    ty = y * (1 - inward)
    radial = math.sqrt(x * x + y * y) + 1e-6
    tx += 0.010 * lm * x / radial * math.sin(18 * radial)
    ty += 0.010 * lm * y / radial * math.sin(18 * radial)
    twist = 0.06 * m * math.sin(2 * math.pi * t) + 0.020 * lm
    ca, sa = math.cos(twist), math.sin(twist)
    return np.array([ca * tx - sa * ty, sa * tx + ca * ty, z])


def base_frame():
    img = Image.new("RGB", (SIZE, SIZE), BG)
    draw = ImageDraw.Draw(img, "RGBA")
    draw.text((30, 24), "20 - Solar System MCIFT Proxy Model", fill=TEXT, font=FONT_TITLE)
    draw.text(
        (30, 58),
        "Sun = central load; planets = orbit shell bands; fabric responds to compression, shear, and shell memory.",
        fill=MUTED,
        font=FONT_SMALL,
    )
    for r in np.linspace(0.5, 2.9, 6):
        pts = []
        for a in np.linspace(0, 2 * math.pi, 160):
            p, _ = project([r * math.cos(a), r * math.sin(a), -0.04])
            pts.append(tuple(p))
        for p1, p2 in zip(pts, pts[1:] + pts[:1]):
            draw.line((*p1, *p2), fill=(*GRID, 55), width=1)
    return img


def draw_orbits(draw):
    for planet in PLANETS:
        pts = []
        for a in np.linspace(0, 2 * math.pi, 200):
            p, _ = project([planet["r"] * math.cos(a), planet["r"] * math.sin(a), 0.02])
            pts.append(tuple(p))
        width = 1 if planet["name"] not in {"Jupiter", "Saturn"} else 2
        alpha = 70 + int(70 * planet["coupling_norm"])
        for p1, p2 in zip(pts, pts[1:] + pts[:1]):
            draw.line((*p1, *p2), fill=(*ORBIT, alpha), width=width)


def draw_fabric(draw, t):
    coords = np.linspace(-2.82, 2.82, 31)
    for idx, y in enumerate(coords):
        pts = [tuple(project(fabric_point(float(x), float(y), t))[0]) for x in coords]
        color = FABRIC_A if idx % 2 == 0 else (122, 232, 255)
        for p1, p2 in zip(pts, pts[1:]):
            draw.line((*p1, *p2), fill=(*color, 150), width=2)
    for idx, x in enumerate(coords):
        pts = [tuple(project(fabric_point(float(x), float(y), t))[0]) for y in coords]
        color = FABRIC_B if idx % 2 == 0 else (145, 155, 255)
        for p1, p2 in zip(pts, pts[1:]):
            draw.line((*p1, *p2), fill=(*color, 118), width=2)


def draw_memory_grooves(draw):
    for p in PLANETS:
        if p["name"] not in {"Earth", "Jupiter", "Saturn"}:
            continue
        weight = MEMORY_WEIGHTS[p["name"]]
        for offset, alpha_scale, width in [(-0.030, 0.24, 1), (0.0, 0.44, 2), (0.030, 0.24, 1)]:
            pts = []
            for a in np.linspace(0, 2 * math.pi, 220):
                ripple = 0.007 * weight * math.sin(18 * a + 2.0 * p["r"])
                r = p["r"] + offset + ripple
                groove_lift = 0.08 + 0.06 * weight
                pp, _ = project([r * math.cos(a), r * math.sin(a), groove_lift])
                pts.append(tuple(pp))
            alpha = int(82 * weight * alpha_scale + 18)
            for q1, q2 in zip(pts, pts[1:] + pts[:1]):
                draw.line((*q1, *q2), fill=(*FABRIC_A, alpha), width=width)
        pts = []
        for a in np.linspace(0, 2 * math.pi, 180):
            r = p["r"] + 0.052
            pp, _ = project([r * math.cos(a), r * math.sin(a), 0.09 + 0.05 * weight])
            pts.append(tuple(pp))
        for q1, q2 in zip(pts, pts[1:] + pts[:1]):
            draw.line((*q1, *q2), fill=(232, 255, 242, int(26 + 35 * weight)), width=1)


def draw_shell_bands(draw, t):
    for p in PLANETS:
        alpha = 34 + int(86 * p["coupling_norm"])
        for offset in [-0.018, 0.018]:
            pts = []
            for a in np.linspace(0, 2 * math.pi, 180):
                wave = 0.018 * math.sin(3 * a + 2 * math.pi * t)
                r = p["r"] + offset + wave * p["coupling_norm"]
                pp, _ = project([r * math.cos(a), r * math.sin(a), 0.15 * p["coupling_norm"]])
                pts.append(tuple(pp))
            for q1, q2 in zip(pts, pts[1:] + pts[:1]):
                draw.line((*q1, *q2), fill=(*SHELL, alpha), width=1)


def draw_planets(draw, t):
    depth_sorted = []
    for p in PLANETS:
        pos = planet_position(p, t)
        pos[2] = 0.18 + 0.15 * p["coupling_norm"]
        xy, depth = project(pos)
        depth_sorted.append((depth, p, xy))
    for _, p, xy in sorted(depth_sorted):
        radius = p["size"]
        glow = radius * (2.2 + 1.6 * p["coupling_norm"])
        draw.ellipse((xy[0] - glow, xy[1] - glow, xy[0] + glow, xy[1] + glow), fill=(*p["color"], 35))
        draw.ellipse((xy[0] - radius, xy[1] - radius, xy[0] + radius, xy[1] + radius), fill=(*p["color"], 235))
        if p["name"] in {"Earth", "Jupiter", "Saturn", "Neptune"}:
            draw.text((xy[0] + radius + 4, xy[1] - 7), p["name"], fill=(210, 222, 240), font=FONT_TINY)


def draw_sun(draw):
    xy, _ = project([0, 0, 0.60])
    for scale, alpha in [(4.8, 28), (3.0, 55), (1.8, 88)]:
        rr = 22 * scale
        draw.ellipse((xy[0] - rr, xy[1] - rr, xy[0] + rr, xy[1] + rr), fill=(*CORE, alpha))
    draw.ellipse((xy[0] - 23, xy[1] - 23, xy[0] + 23, xy[1] + 23), fill=(*CORE, 245))
    draw.text((xy[0] + 29, xy[1] - 10), "Sun/core load", fill=(250, 235, 178), font=FONT_TINY)


def draw_tension(draw, t):
    for p in PLANETS:
        if p["name"] not in {"Jupiter", "Saturn", "Earth", "Venus"}:
            continue
        start = project(planet_position(p, t) + np.array([0, 0, 0.12]))[0]
        end = project(0.74 * planet_position(p, t) + np.array([0, 0, 0.28]))[0]
        width = 1 + int(3 * p["coupling_norm"])
        draw.line((*start, *end), fill=(*TENSION, 120 + int(100 * p["coupling_norm"])), width=width)


def annotations(draw):
    draw.text((30, SIZE - 86), "method: rho0 central compression + orbital shell bands + local planetary shear", fill=(190, 220, 245), font=FONT_SMALL)
    draw.text((30, SIZE - 61), "scale: orbital radii and orbital speeds are compressed for readable visual cadence", fill=(180, 235, 245), font=FONT_SMALL)
    draw.text((30, SIZE - 36), "status: proxy visualization, not an ephemeris or GR/N-body replacement", fill=(245, 196, 145), font=FONT_SMALL)


def write_proxy_table():
    path = OUT_DIR / "20_solar_system_mcift_proxy_table.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "planet",
                "semi_major_axis_au",
                "period_years",
                "mass_earth",
                "mapped_radius",
                "coupling_norm",
                "visual_period",
                "visual_orbits_per_gif",
            ],
        )
        writer.writeheader()
        for p in PLANETS:
            writer.writerow(
                {
                    "planet": p["name"],
                    "semi_major_axis_au": p["a"],
                    "period_years": p["period"],
                    "mass_earth": p["mass_e"],
                    "mapped_radius": f"{p['r']:.6f}",
                    "coupling_norm": f"{p['coupling_norm']:.6f}",
                    "visual_period": f"{p['visual_period']:.6f}",
                    "visual_orbits_per_gif": f"{VISUAL_EARTH_ORBITS / p['visual_period']:.6f}",
                }
            )
    return path


def make_animation():
    frames = []
    for i in range(FRAMES):
        t = i / FRAMES
        img = base_frame()
        draw = ImageDraw.Draw(img, "RGBA")
        draw_fabric(draw, t)
        draw_memory_grooves(draw)
        draw_orbits(draw)
        draw_shell_bands(draw, t)
        draw_tension(draw, t)
        draw_planets(draw, t)
        draw_sun(draw)
        annotations(draw)
        frames.append(img)
    gif_path = OUT_DIR / "20_solar_system_mcift_proxy.gif"
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=FPS_MS, loop=0, optimize=True)
    frames[72].save(OUT_DIR / "20_solar_system_mcift_proxy_preview.png")
    return gif_path


def main():
    table = write_proxy_table()
    gif_path = make_animation()
    print(gif_path.name)
    print("20_solar_system_mcift_proxy_preview.png")
    print(table.name)


if __name__ == "__main__":
    main()
