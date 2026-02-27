"""
Geometric Loop Visuals Generator for YouTube Shorts
Generates 3 looping animations as MP4 (1080x1920 vertical format)
"""

import numpy as np
import cv2
import math
import os

WIDTH, HEIGHT = 1080, 1920
FPS = 60
DURATION = 6  # seconds — seamless loop
TOTAL_FRAMES = FPS * DURATION
OUT_DIR = "/mnt/user-data/outputs"
os.makedirs(OUT_DIR, exist_ok=True)


def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))


# ─────────────────────────────────────────────
# VISUAL 1: Rotating Sacred Geometry / Mandala
# ─────────────────────────────────────────────
def draw_visual_1(frame_idx):
    t = frame_idx / TOTAL_FRAMES  # 0..1
    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

    bg = np.full((HEIGHT, WIDTH, 3), (8, 6, 14), dtype=np.uint8)
    img[:] = bg

    cx, cy = WIDTH // 2, HEIGHT // 2
    angle_offset = t * 2 * math.pi

    # Draw nested rotating polygons
    palette = [
        (220, 200, 255),
        (180, 140, 255),
        (120, 80, 220),
        (80, 50, 160),
        (50, 30, 100),
    ]

    for layer in range(12):
        n_sides = 3 + (layer % 5)  # 3 to 7 sides
        radius = 60 + layer * 68
        direction = 1 if layer % 2 == 0 else -1
        speed = 0.5 + layer * 0.08
        angle = angle_offset * speed * direction + layer * 0.3

        pts = []
        for i in range(n_sides):
            a = angle + i * 2 * math.pi / n_sides
            x = int(cx + radius * math.cos(a))
            y = int(cy + radius * math.sin(a))
            pts.append([x, y])

        pts = np.array(pts, dtype=np.int32)
        color_idx = layer % len(palette)
        alpha = max(0.15, 1.0 - layer * 0.07)
        c = tuple(int(v * alpha) for v in palette[color_idx])
        thickness = max(1, 3 - layer // 4)
        cv2.polylines(img, [pts], True, c, thickness, cv2.LINE_AA)

    # Central pulsing dot
    pulse = 0.5 + 0.5 * math.sin(t * 4 * math.pi)
    core_r = int(8 + pulse * 12)
    cv2.circle(img, (cx, cy), core_r, (240, 230, 255), -1, cv2.LINE_AA)
    cv2.circle(img, (cx, cy), core_r + 6, (180, 160, 240), 2, cv2.LINE_AA)

    return img


# ─────────────────────────────────────────────
# VISUAL 2: Flowing Grid Warp
# ─────────────────────────────────────────────
def draw_visual_2(frame_idx):
    t = frame_idx / TOTAL_FRAMES
    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    img[:] = (4, 10, 12)

    spacing = 80
    phase = t * 2 * math.pi

    for gx in range(-spacing, WIDTH + spacing, spacing):
        pts = []
        for gy in range(0, HEIGHT + 10, 10):
            wave = math.sin(gy / 180.0 + phase * 2) * 30
            wave += math.sin(gy / 90.0 + phase * 3.5) * 12
            x = int(gx + wave)
            pts.append((x, gy))
        for i in range(len(pts) - 1):
            blend = pts[i][1] / HEIGHT
            r = int(20 + blend * 80)
            g = int(180 + blend * 60)
            b = int(200 + blend * 55)
            cv2.line(img, pts[i], pts[i + 1], (r, g, b), 1, cv2.LINE_AA)

    for gy in range(-spacing, HEIGHT + spacing, spacing):
        pts = []
        for gx in range(0, WIDTH + 10, 10):
            wave = math.sin(gx / 180.0 + phase * 1.5) * 30
            wave += math.sin(gx / 90.0 - phase * 2.5) * 12
            y = int(gy + wave)
            pts.append((gx, y))
        for i in range(len(pts) - 1):
            blend = pts[i][0] / WIDTH
            r = int(20 + blend * 60)
            g = int(160 + blend * 80)
            b = int(200 + blend * 55)
            cv2.line(img, pts[i], pts[i + 1], (r, g, b), 1, cv2.LINE_AA)

    # Vignette
    for r_step in range(10):
        r_val = int(WIDTH * 0.4 + r_step * 60)
        alpha = int(6 - r_step * 0.4)
        cv2.circle(img, (WIDTH // 2, HEIGHT // 2), r_val, (0, 0, 0), alpha * 6)

    return img


# ─────────────────────────────────────────────
# VISUAL 3: Orbiting Particles + Trails
# ─────────────────────────────────────────────
def draw_visual_3(frame_idx):
    t = frame_idx / TOTAL_FRAMES
    img = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
    img[:] = (6, 4, 8)

    cx, cy = WIDTH // 2, HEIGHT // 2
    phase = t * 2 * math.pi

    # Draw orbital rings
    for ring in range(6):
        r = 120 + ring * 120
        cv2.circle(img, (cx, cy), r, (30 + ring * 5, 20 + ring * 5, 50 + ring * 5), 1, cv2.LINE_AA)

    # Orbiting particles with trails
    particles = [
        {"ring": 0, "speed": 1.2, "size": 8,  "color": (255, 220, 180)},
        {"ring": 1, "speed": -0.9, "size": 6, "color": (180, 255, 220)},
        {"ring": 2, "speed": 0.7, "size": 10, "color": (220, 180, 255)},
        {"ring": 3, "speed": -1.4, "size": 5, "color": (255, 255, 200)},
        {"ring": 4, "speed": 1.1, "size": 7,  "color": (200, 220, 255)},
        {"ring": 5, "speed": -0.6, "size": 9, "color": (255, 200, 210)},
        # Second particles on some rings
        {"ring": 1, "speed": -0.9, "size": 4, "color": (100, 255, 200), "offset": math.pi},
        {"ring": 3, "speed": -1.4, "size": 4, "color": (255, 200, 100), "offset": math.pi},
    ]

    trail_len = 30
    for p in particles:
        ring_r = 120 + p["ring"] * 120
        speed = p["speed"]
        offset = p.get("offset", 0)

        # Draw trail
        for ti in range(trail_len):
            trail_t = (frame_idx - ti) / TOTAL_FRAMES
            trail_angle = trail_t * 2 * math.pi * speed + offset
            tx = int(cx + ring_r * math.cos(trail_angle))
            ty = int(cy + ring_r * math.sin(trail_angle))
            alpha = (1 - ti / trail_len) ** 2
            tc = tuple(int(c * alpha * 0.7) for c in p["color"])
            size = max(1, int(p["size"] * alpha * 0.6))
            if 0 <= tx < WIDTH and 0 <= ty < HEIGHT:
                cv2.circle(img, (tx, ty), size, tc, -1, cv2.LINE_AA)

        # Draw particle
        angle = phase * speed + offset
        px = int(cx + ring_r * math.cos(angle))
        py = int(cy + ring_r * math.sin(angle))
        if 0 <= px < WIDTH and 0 <= py < HEIGHT:
            cv2.circle(img, (px, py), p["size"], p["color"], -1, cv2.LINE_AA)
            # Glow
            glow_c = tuple(min(255, int(c * 0.5)) for c in p["color"])
            cv2.circle(img, (px, py), p["size"] + 5, glow_c, 1, cv2.LINE_AA)

    # Central star
    pulse = 0.5 + 0.5 * math.sin(phase * 2)
    cv2.circle(img, (cx, cy), int(10 + pulse * 6), (255, 255, 255), -1, cv2.LINE_AA)
    cv2.circle(img, (cx, cy), int(20 + pulse * 8), (180, 160, 220), 1, cv2.LINE_AA)

    return img


# ─────────────────────────────────────────────
# RENDER ALL THREE
# ─────────────────────────────────────────────
visuals = [
    ("visual_1_sacred_geometry.mp4", draw_visual_1),
    ("visual_2_grid_warp.mp4",       draw_visual_2),
    ("visual_3_orbital_particles.mp4", draw_visual_3),
]

for filename, draw_fn in visuals:
    out_path = os.path.join(OUT_DIR, filename)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(out_path, fourcc, FPS, (WIDTH, HEIGHT))

    print(f"Rendering {filename}...")
    for i in range(TOTAL_FRAMES):
        frame_rgb = draw_fn(i)
        frame_bgr = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)
        writer.write(frame_bgr)
        if i % 60 == 0:
            print(f"  Frame {i}/{TOTAL_FRAMES}")

    writer.release()
    print(f"  ✓ Saved to {out_path}")

print("\nAll done! 3 loop visuals generated.")
