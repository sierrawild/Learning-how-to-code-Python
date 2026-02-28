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
