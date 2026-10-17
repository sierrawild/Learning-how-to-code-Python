"""TIDELIGHT: a tiny, dependency-free isometric crystal run.\n\nRun with `python wew.py`. Use WASD or the arrow keys to move, P to pause,\nand R to restart. The island's faceted textures are drawn procedurally.\n"""

from __future__ import annotations

import json
import math
import os
import random
import sys
import time
import tkinter as tk

try:
	import winsound
except ImportError:  # pragma: no cover - only used on Windows
	winsound = None


MAP_SIZE = 9
PLAYER_SPEED = 4.2

LEVELS = [
	{
		"crystals": ((2, 1), (4, 1), (6, 2), (1, 4), (4, 4), (7, 5), (2, 7)),
		"rocks": ((2, 2), (3, 5), (5, 4), (6, 6), (1, 6), (7, 2)),
		"trees": ((3, 0), (6, 1), (0, 4), (8, 4), (4, 7), (6, 8)),
		"start": (0.0, 0.0),
		"enemies": (( (4.4, 5.7), (7.0, 5.7), 1.05), ((7.3, 1.1), (7.3, 4.0), 0.82)),
	},
	{
		"crystals": ((1, 1), (3, 2), (5, 1), (6, 4), (2, 6), (7, 6), (4, 7)),
		"rocks": ((2, 3), (5, 3), (3, 5), (6, 2), (1, 7), (7, 4)),
		"trees": ((0, 2), (4, 0), (6, 0), (8, 3), (2, 8), (7, 8)),
		"start": (0.0, 0.0),
		"enemies": (((3.5, 1.5), (6.5, 1.5), 1.2), ((7.2, 5.0), (7.2, 7.5), 0.9)),
	},
	{
		"crystals": ((1, 2), (2, 5), (4, 2), (5, 5), (7, 1), (7, 7), (3, 7)),
		"rocks": ((1, 5), (3, 3), (5, 2), (6, 6), (2, 7), (8, 5)),
		"trees": ((0, 6), (4, 8), (7, 0), (8, 2), (5, 7), (3, 0)),
		"start": (0.0, 0.0),
		"enemies": (((2.4, 6.1), (6.2, 6.1), 1.1), ((5.6, 2.3), (5.6, 4.6), 1.0)),
	},
	{
		"crystals": ((2, 2), (4, 1), (6, 3), (1, 5), (4, 5), (6, 6), (2, 7)),
		"rocks": ((1, 1), (3, 4), (5, 4), (7, 5), (2, 6), (6, 7)),
		"trees": ((0, 3), (2, 0), (5, 0), (8, 1), (6, 8), (4, 6)),
		"start": (0.0, 0.0),
		"enemies": (((4.1, 3.4), (7.1, 3.4), 1.35), ((6.8, 5.8), (6.8, 8.0), 1.05)),
	},
	{
		"crystals": ((1, 3), (3, 1), (5, 3), (7, 2), (2, 6), (4, 6), (6, 7)),
		"rocks": ((2, 1), (4, 3), (6, 1), (1, 6), (5, 6), (7, 6)),
		"trees": ((0, 5), (3, 8), (8, 4), (6, 0), (2, 8), (4, 0)),
		"start": (0.0, 0.0),
		"enemies": (((2.6, 2.7), (6.2, 2.7), 1.2), ((5.5, 5.4), (5.5, 7.9), 1.1)),
	},
	{
		"crystals": ((2, 1), (3, 4), (5, 2), (6, 5), (1, 7), (7, 7), (4, 8)),
		"rocks": ((1, 2), (4, 2), (3, 6), (5, 5), (7, 4), (8, 7)),
		"trees": ((0, 1), (2, 8), (5, 0), (7, 1), (6, 8), (4, 4)),
		"start": (0.0, 0.0),
		"enemies": (((3.7, 1.9), (7.1, 1.9), 1.3), ((7.0, 5.0), (7.0, 8.0), 0.95)),
	},
	{
		"crystals": ((1, 1), (3, 3), (5, 1), (6, 4), (2, 6), (4, 7), (7, 6)),
		"rocks": ((2, 2), (5, 3), (1, 5), (3, 6), (6, 6), (7, 2)),
		"trees": ((0, 4), (3, 0), (6, 0), (8, 3), (2, 8), (6, 8)),
		"start": (0.0, 0.0),
		"enemies": (((3.2, 5.4), (6.9, 5.4), 1.15), ((5.7, 1.5), (5.7, 4.2), 1.1)),
	},
	{
		"crystals": ((2, 3), (4, 2), (6, 1), (1, 5), (4, 5), (6, 6), (3, 8)),
		"rocks": ((1, 1), (3, 2), (5, 4), (7, 3), (2, 6), (6, 7)),
		"trees": ((0, 7), (3, 0), (5, 8), (8, 2), (7, 0), (4, 6)),
		"start": (0.0, 0.0),
		"enemies": (((2.5, 3.8), (6.5, 3.8), 1.25), ((6.8, 6.0), (6.8, 8.2), 1.0)),
	},
	{
		"crystals": ((1, 2), (3, 1), (5, 4), (7, 1), (2, 5), (4, 7), (6, 8)),
		"rocks": ((2, 1), (4, 3), (6, 3), (1, 6), (5, 6), (7, 6)),
		"trees": ((0, 3), (2, 8), (5, 0), (8, 1), (7, 8), (4, 4)),
		"start": (0.0, 0.0),
		"enemies": (((2.8, 2.0), (7.0, 2.0), 1.4), ((5.9, 5.2), (5.9, 7.6), 1.2)),
	},
	{
		"crystals": ((2, 2), (4, 1), (6, 2), (1, 4), (3, 6), (5, 6), (7, 7)),
		"rocks": ((1, 1), (3, 3), (5, 3), (2, 5), (6, 5), (7, 4)),
		"trees": ((0, 6), (3, 8), (6, 0), (8, 5), (5, 8), (2, 0)),
		"start": (0.0, 0.0),
		"enemies": (((3.3, 1.4), (7.0, 1.4), 1.35), ((6.9, 5.8), (6.9, 7.9), 1.05)),
	},
]

LEVEL_COUNT = len(LEVELS)
DEFAULT_CRYSTALS = LEVELS[0]["crystals"]
DEFAULT_ROCKS = LEVELS[0]["rocks"]
DEFAULT_TREES = LEVELS[0]["trees"]
DEFAULT_BLOCKERS = DEFAULT_ROCKS + DEFAULT_TREES


SAVE_PATH = os.path.join(os.path.expanduser("~"), ".tidelight-save.json")


def clamp(value: float, low: float, high: float) -> float:
	return max(low, min(value, high))


class Leaderboard:
	def __init__(self, path: str = SAVE_PATH):
		self.path = path
		self.data = self.load()

	def load(self) -> dict:
		default = {"last_username": "PLAYER", "last_level": 1, "leaderboard": []}
		try:
			with open(self.path, "r", encoding="utf-8") as handle:
				data = json.load(handle)
			if isinstance(data, dict):
				default.update(data)
		except (FileNotFoundError, json.JSONDecodeError, OSError):
			pass
		return default

	def save(self) -> None:
		with open(self.path, "w", encoding="utf-8") as handle:
			json.dump(self.data, handle, indent=2)

	def remember_user(self, username: str) -> None:
		clean = self.clean_name(username)
		if clean:
			self.data["last_username"] = clean
			self.save()

	@staticmethod
	def clean_name(username: str) -> str:
		name = (username or "PLAYER").strip()[:12]
		return name or "PLAYER"

	def record_run(self, username: str, elapsed: float, completed_level: int) -> None:
		name = self.clean_name(username)
		entry = {
			"username": name,
			"time": int(max(0.0, elapsed)),
			"level": max(1, completed_level),
			"date": time.strftime("%Y-%m-%d"),
		}
		self.data.setdefault("leaderboard", []).append(entry)
		self.data["leaderboard"] = sorted(
			self.data["leaderboard"],
			key=lambda item: (-int(item.get("level", 1)), int(item.get("time", 999999))),
		)
		self.data["leaderboard"] = self.data["leaderboard"][:10]
		self.data["last_username"] = name
		self.data["last_level"] = max(self.data.get("last_level", 1), completed_level)
		self.save()

	def top_entries(self, limit: int = 6) -> list[dict]:
		entries = self.data.get("leaderboard", [])
		return entries[:limit]


class SoundManager:
	def __init__(self):
		self.enabled = True
		self._winsound = winsound

	def play(self, sound: str) -> None:
		if not self.enabled or self._winsound is None:
			return
		if sound == "collect":
			self._winsound.Beep(880, 70)
		elif sound == "hit":
			self._winsound.Beep(220, 120)
		elif sound == "start":
			self._winsound.Beep(660, 110)
		elif sound == "win":
			self._winsound.Beep(440, 80)
			self._winsound.Beep(660, 90)
			self._winsound.Beep(880, 120)


class Patrol:
	def __init__(self, start: tuple[float, float], end: tuple[float, float], speed: float):
		self.start = start
		self.end = end
		self.speed = speed
		self.distance = 0.0
		self.direction = 1.0
		self.length = math.dist(start, end)
		self.x, self.y = start

	def update(self, dt: float) -> None:
		self.distance += self.speed * dt * self.direction
		if self.distance > self.length:
			self.distance = self.length
			self.direction = -1.0
		elif self.distance < 0:
			self.distance = 0.0
			self.direction = 1.0
		ratio = self.distance / self.length if self.length else 0.0
		self.x = self.start[0] + (self.end[0] - self.start[0]) * ratio
		self.y = self.start[1] + (self.end[1] - self.start[1]) * ratio


class GameModel:
	def __init__(self):
		self.level_index = 0
		self.levels = LEVELS
		self.level_rocks = ()
		self.level_trees = ()
		self.level_name = ""
		self.reset()

	def reset(self) -> None:
		self.level_index = 0
		self.load_level(0)
		self.lives = 3
		self.state = "playing"
		self.invulnerable = 0.0
		self.elapsed = 0.0

	def load_level(self, index: int) -> None:
		level_index = max(0, min(index, LEVEL_COUNT - 1))
		self.level_index = level_index
		level = self.levels[level_index]
		self.level_rocks = tuple(level["rocks"])
		self.level_trees = tuple(level["trees"])
		self.level_name = f"LEVEL {level_index + 1}"
		self.x, self.y = level["start"]
		self.crystals = list(level["crystals"])
		self.blockers = self.level_rocks + self.level_trees
		self.enemies = [Patrol(start, end, speed) for start, end, speed in level["enemies"]]

	@property
	def collected(self) -> int:
		return len(self.levels[self.level_index]["crystals"]) - len(self.crystals)

	def _blocked(self, x: float, y: float) -> bool:
		if x < -0.25 or y < -0.25 or x > MAP_SIZE - 0.75 or y > MAP_SIZE - 0.75:
			return True
		return any(abs(x - bx) < 0.58 and abs(y - by) < 0.58 for bx, by in self.blockers)

	def _attempt_move(self, dx: float, dy: float, dt: float) -> None:
		if not (dx or dy):
			return
		distance = PLAYER_SPEED * dt / math.hypot(dx, dy)
		next_x = clamp(self.x + dx * distance, -0.25, MAP_SIZE - 0.75)
		if not self._blocked(next_x, self.y):
			self.x = next_x
		next_y = clamp(self.y + dy * distance, -0.25, MAP_SIZE - 0.75)
		if not self._blocked(self.x, next_y):
			self.y = next_y

	def step(self, dt: float, keys: set[str]) -> None:
		if self.state != "playing":
			return
		dt = min(max(dt, 0.0), 0.05)
		self.elapsed += dt
		self.invulnerable = max(0.0, self.invulnerable - dt)

		dx = float(bool(keys & {"d", "right"})) - float(bool(keys & {"a", "left"}))
		dy = float(bool(keys & {"s", "down"})) - float(bool(keys & {"w", "up"}))
		self._attempt_move(dx, dy, dt)

		self.crystals = [
			crystal for crystal in self.crystals
			if math.dist((self.x, self.y), crystal) >= 0.48
		]
		for enemy in self.enemies:
			enemy.update(dt)
			if self.invulnerable <= 0 and math.dist((self.x, self.y), (enemy.x, enemy.y)) < 0.48:
				self.lives -= 1
				self.x, self.y = 0.0, 0.0
				self.invulnerable = 1.5
				if self.lives <= 0:
					self.state = "lost"
				break

		if not self.crystals and math.dist((self.x, self.y), (8.0, 8.0)) < 0.72:
			if self.level_index == LEVEL_COUNT - 1:
				self.state = "won"
			else:
				self.level_index += 1
				self.load_level(self.level_index)
				self.state = "playing"


class GameApp:
	def __init__(self, root: tk.Tk):
		self.root = root
		self.leaderboard = Leaderboard()
		self.sound = SoundManager()
		self.username = self.leaderboard.data.get("last_username", "PLAYER")
		self.current_screen = "menu"
		self.run_logged = False
		root.title("TIDELIGHT | Shard Run")
		root.geometry("1040x760")
		root.minsize(760, 600)
		root.configure(bg="#102a3b")
		self.canvas = tk.Canvas(root, bg="#102a3b", highlightthickness=0)
		self.canvas.pack(fill="both", expand=True)
		self.username_entry = tk.Entry(root, width=18, font=("Segoe UI", 16), justify="center")
		self.username_entry.insert(0, self.username)
		self.username_entry.bind("<Return>", self.start_game)
		self.username_entry.place_forget()
		self.model = GameModel()
		self.keys: set[str] = set()
		self.width, self.height = 1040, 760
		self.tile_w, self.tile_h = 76.0, 42.0
		self.board_y = 360.0
		self.started = time.perf_counter()
		self.last_time = self.started
		root.bind("<KeyPress>", self.on_key_down)
		root.bind("<KeyRelease>", self.on_key_up)
		root.bind("<Escape>", lambda _event: root.destroy())
		self.canvas.bind("<Configure>", self.on_resize)
		self.draw()
		self.loop()

	def on_resize(self, event: tk.Event) -> None:
		self.width, self.height = max(event.width, 1), max(event.height, 1)
		self.tile_w = min(76.0, (self.width - 110.0) / (MAP_SIZE - 1))
		self.tile_h = self.tile_w * 0.56
		self.board_y = self.height * 0.49

	def format_time(self, seconds: float) -> str:
		minutes, secs = divmod(int(seconds), 60)
		return f"{minutes:02d}:{secs:02d}"

	def start_game(self, _event: tk.Event | None = None) -> None:
		self.username = Leaderboard.clean_name(self.username_entry.get())
		self.leaderboard.remember_user(self.username)
		start_level = max(0, min(int(self.leaderboard.data.get("last_level", 1)) - 1, LEVEL_COUNT - 1))
		self.model.load_level(start_level)
		self.model.state = "playing"
		self.model.elapsed = 0.0
		self.current_screen = "game"
		self.run_logged = False
		self.keys.clear()
		self.username_entry.place_forget()
		self.sound.play("start")

	def on_key_down(self, event: tk.Event) -> None:
		if self.current_screen == "menu":
			if event.keysym == "Return":
				self.start_game()
			return
		key = event.keysym.lower()
		if key == "r":
			self.model.reset()
			self.run_logged = False
			self.current_screen = "game"
			self.username_entry.place_forget()
		elif key in {"p", "space"} and key not in self.keys:
			if self.model.state == "playing":
				self.model.state = "paused"
			elif self.model.state == "paused":
				self.model.state = "playing"
		self.keys.add(key)

	def on_key_up(self, event: tk.Event) -> None:
		self.keys.discard(event.keysym.lower())

	def project(self, x: float, y: float) -> tuple[float, float]:
		return (
			self.width / 2 + (x - y) * self.tile_w / 2,
			self.board_y + (x + y - (MAP_SIZE - 1)) * self.tile_h / 2,
		)

	def diamond(self, x: float, y: float) -> tuple[tuple[float, float], ...]:
		sx, sy = self.project(x, y)
		return (
			(sx, sy - self.tile_h / 2),
			(sx + self.tile_w / 2, sy),
			(sx, sy + self.tile_h / 2),
			(sx - self.tile_w / 2, sy),
		)

	def draw(self) -> None:
		if self.current_screen == "menu":
			self.draw_menu()
			return
		c = self.canvas
		c.delete("all")
		self.draw_water()
		self.draw_island()
		objects: list[tuple[float, int, str, object]] = []
		for x, y in self.model.level_trees:
			objects.append((x + y, 0, "tree", (x, y)))
		for x, y in self.model.level_rocks:
			objects.append((x + y, 0, "rock", (x, y)))
		objects.append((16.0, 1, "gate", None))
		for index, (x, y) in enumerate(self.model.crystals):
			objects.append((x + y, 2, "crystal", (index, x, y)))
		for index, enemy in enumerate(self.model.enemies):
			objects.append((enemy.x + enemy.y, 3, "slime", (index, enemy.x, enemy.y)))
		objects.append((self.model.x + self.model.y, 4, "player", None))
		for _depth, _order, kind, data in sorted(objects, key=lambda item: (item[0], item[1])):
			if kind == "tree":
				self.draw_tree(*data)
			elif kind == "rock":
				self.draw_rock(*data)
			elif kind == "gate":
				self.draw_gate()
			elif kind == "crystal":
				self.draw_crystal(*data)
			elif kind == "slime":
				self.draw_slime(*data)
			else:
				self.draw_player()
		self.draw_hud()
		if self.model.state in ("paused", "won", "lost"):
			self.draw_overlay()

	def draw_menu(self) -> None:
		c = self.canvas
		c.delete("all")
		self.draw_water()
		self.draw_island()
		c.create_rectangle(0, 0, self.width, self.height, fill="#0d1d2b", stipple="gray25", outline="")
		c.create_text(self.width / 2, 140, text="TIDELIGHT", fill="#dff5d8", font=("Segoe UI", 36, "bold"))
		c.create_text(self.width / 2, 190, text="SHARD RUN", fill="#8ad8c8", font=("Segoe UI", 16, "bold"))
		c.create_text(self.width / 2, 240, text="Enter username and press Enter", fill="#d9e9df", font=("Segoe UI", 12))
		self.username_entry.place(x=self.width / 2 - 120, y=270, width=240, height=36)
		self.username_entry.focus_set()
		c.create_rectangle(self.width / 2 - 200, 330, self.width / 2 + 200, 520, fill="#132835", outline="#7AC7B7", width=2)
		c.create_text(self.width / 2, 350, text="LEADERBOARD", fill="#e9f8cb", font=("Segoe UI", 14, "bold"))
		entries = self.leaderboard.top_entries(6)
		for index, entry in enumerate(entries):
			label = f"{index + 1}. {entry.get('username', 'PLAYER'):<12}  {self.format_time(entry.get('time', 0))}"
			c.create_text(self.width / 2, 390 + index * 26, text=label, fill="#dfead3", font=("Segoe UI", 11))
		if not entries:
			c.create_text(self.width / 2, 390, text="No runs recorded yet.", fill="#b6d0c0", font=("Segoe UI", 11))
		c.create_text(self.width / 2, self.height - 80, text="Press Enter to begin the run", fill="#bfe9d2", font=("Segoe UI", 11, "bold"))

	def draw_water(self) -> None:
		c = self.canvas
		c.create_rectangle(0, 0, self.width, self.height, fill="#123449", outline="")
		for index in range(17):
			y = (index * 73 + 34) % max(self.height, 1)
			points = []
			for x in range(-20, self.width + 30, 18):
				points.extend((x, y + math.sin(x * 0.018 + index * 1.7) * 5))
			c.create_line(*points, fill="#1b4a5b", width=1, smooth=True)
		for index in range(8):
			x = (index * 157 + 63) % max(self.width, 1)
			y = (index * 109 + 87) % max(self.height, 1)
			c.create_oval(x, y, x + 3, y + 3, fill="#72bcb0", outline="")

	def draw_island(self) -> None:
		c = self.canvas
		depth = self.tile_h * 0.66
		for y in range(MAP_SIZE):
			for x in range(MAP_SIZE):
				points = self.diamond(x, y)
				top, right, bottom, left = points
				if x == MAP_SIZE - 1:
					c.create_polygon(
						right, bottom, (bottom[0], bottom[1] + depth),
						(right[0], right[1] + depth),
						fill="#315b48", outline="#254a40", width=1,
					)
				if y == MAP_SIZE - 1:
					c.create_polygon(
						left, bottom, (bottom[0], bottom[1] + depth),
						(left[0], left[1] + depth),
						fill="#24483f", outline="#1c3d39", width=1,
					)
		greens = ("#72a65d", "#7cad62", "#699b58", "#83b36b", "#6f9f60")
		facets = ("#94bd70", "#639254", "#80ad65", "#5e8b55", "#a2c77b")
		for y in range(MAP_SIZE):
			for x in range(MAP_SIZE):
				top, right, bottom, left = self.diamond(x, y)
				center = self.project(x, y)
				rng = random.Random(x * 91 + y * 137 + 21)
				base = rng.randrange(len(greens))
				c.create_polygon(*sum(([p[0], p[1]] for p in (top, right, bottom, left)), []),
								 fill=greens[base], outline="#466f50", width=1)
				corners = (top, right, bottom, left)
				for side in range(4):
					first, second = corners[side], corners[(side + 1) % 4]
					shade = facets[(base + side + rng.randrange(1, 4)) % len(facets)]
					c.create_polygon(first, second, center, fill=shade, outline="")
				for _ in range(2):
					px = center[0] + rng.uniform(-self.tile_w * 0.19, self.tile_w * 0.19)
					py = center[1] + rng.uniform(-self.tile_h * 0.18, self.tile_h * 0.18)
					c.create_line(px, py, px + 2, py - 3, fill="#b7c97c", width=1)

	def draw_tree(self, x: float, y: float) -> None:
		c = self.canvas
		sx, sy = self.project(x, y)
		c.create_oval(sx - 13, sy - 3, sx + 13, sy + 5, fill="#41604b", outline="")
		c.create_polygon(sx - 4, sy - 7, sx - 2, sy - 23, sx + 3, sy - 23,
						 sx + 6, sy - 5, fill="#8a6847", outline="#604d3d")
		c.create_polygon(sx, sy - 54, sx - 19, sy - 22, sx + 17, sy - 21,
						 fill="#276b54", outline="#1b5448")
		c.create_polygon(sx, sy - 46, sx + 2, sy - 21, sx + 17, sy - 21,
						 fill="#429064", outline="")
		c.create_polygon(sx, sy - 39, sx - 13, sy - 20, sx + 12, sy - 19,
						 fill="#68a96d", outline="")
		c.create_oval(sx - 3, sy - 40, sx + 2, sy - 35, fill="#d5dc91", outline="")

	def draw_rock(self, x: float, y: float) -> None:
		c = self.canvas
		sx, sy = self.project(x, y)
		c.create_oval(sx - 17, sy - 4, sx + 17, sy + 6, fill="#53664e", outline="")
		c.create_polygon(sx - 15, sy - 3, sx - 13, sy - 17, sx - 4, sy - 26,
						 sx + 9, sy - 24, sx + 16, sy - 11, sx + 15, sy - 3,
						 fill="#748071", outline="#485d58", width=2)
		c.create_polygon(sx - 13, sy - 16, sx - 4, sy - 25, sx + 1, sy - 12,
						 sx - 7, sy - 7, fill="#a6ae94", outline="")
		c.create_polygon(sx + 1, sy - 12, sx - 4, sy - 25, sx + 9, sy - 23,
						 sx + 15, sy - 11, fill="#65756d", outline="")

	def draw_crystal(self, index: int, x: float, y: float) -> None:
		c = self.canvas
		sx, sy = self.project(x, y)
		pulse = math.sin(time.perf_counter() * 3.0 + index) * 3
		top_y = sy - 30 - pulse
		palette = (("#71f0df", "#2daaa9", "#c1fff0"),
				   ("#ff947d", "#d94f63", "#ffd0a9"),
				   ("#ffe67d", "#df9d43", "#fff6c4"))
		light, dark, glint = palette[index % len(palette)]
		c.create_oval(sx - 12, sy - 4, sx + 12, sy + 4, fill="#4f795a", outline="")
		c.create_polygon(sx, top_y, sx + 10, sy - 9, sx + 5, sy - 2,
						 sx - 7, sy - 2, sx - 10, sy - 11,
						 fill=light, outline="#dbf4ca", width=1)
		c.create_polygon(sx, top_y, sx + 10, sy - 9, sx + 5, sy - 2,
						 fill=dark, outline="")
		c.create_polygon(sx, top_y, sx - 10, sy - 11, sx - 4, sy - 8,
						 fill=glint, outline="")
		c.create_line(sx - 16, sy - 28 - pulse, sx - 13, sy - 28 - pulse,
					  fill="#fff2bd", width=2)
		c.create_line(sx - 14, sy - 30 - pulse, sx - 14, sy - 26 - pulse,
					  fill="#fff2bd", width=2)

	def draw_gate(self) -> None:
		c = self.canvas
		sx, sy = self.project(8, 8)
		unlocked = not self.model.crystals
		glow = "#91f2db" if unlocked else "#769c9c"
		c.create_oval(sx - 22, sy - 7, sx + 22, sy + 7,
					  fill="#446f63", outline="#81b9a0", width=2)
		c.create_polygon(sx, sy - 46, sx + 18, sy - 23, sx + 14, sy - 4,
						 sx - 14, sy - 4, sx - 18, sy - 23,
						 fill="#254f5a", outline=glow, width=3)
		c.create_polygon(sx, sy - 39, sx + 10, sy - 22, sx + 7, sy - 8,
						 sx - 7, sy - 8, sx - 10, sy - 22,
						 fill="#277c83" if unlocked else "#385b65", outline="")
		c.create_line(sx, sy - 37, sx, sy - 11, fill="#d2fff0" if unlocked else "#78999b", width=2)

	def draw_slime(self, index: int, x: float, y: float) -> None:
		c = self.canvas
		sx, sy = self.project(x, y)
		wobble = math.sin(time.perf_counter() * 7 + index) * 2
		c.create_oval(sx - 16, sy - 3, sx + 16, sy + 5, fill="#51634b", outline="")
		c.create_polygon(sx - 14, sy - 4, sx - 15, sy - 11 - wobble,
						 sx - 8, sy - 22 - wobble, sx + 5, sy - 24 - wobble,
						 sx + 14, sy - 15 - wobble, sx + 15, sy - 4,
						 fill="#eb756d" if index == 0 else "#e9a64f",
						 outline="#784e4c", width=2)
		c.create_polygon(sx - 7, sy - 20 - wobble, sx + 4, sy - 22 - wobble,
						 sx + 3, sy - 8, sx - 9, sy - 7,
						 fill="#f6a28b" if index == 0 else "#ffd276", outline="")
		c.create_oval(sx - 6, sy - 13 - wobble, sx - 2, sy - 8 - wobble,
					  fill="#263c43", outline="")
		c.create_oval(sx + 4, sy - 13 - wobble, sx + 8, sy - 8 - wobble,
					  fill="#263c43", outline="")

	def draw_player(self) -> None:
		c = self.canvas
		sx, sy = self.project(self.model.x, self.model.y)
		if self.model.invulnerable > 0 and int(time.perf_counter() * 12) % 2:
			return
		c.create_oval(sx - 13, sy - 4, sx + 13, sy + 5, fill="#40594b", outline="")
		c.create_polygon(sx - 9, sy - 8, sx - 8, sy - 20, sx + 7, sy - 20,
						 sx + 9, sy - 7, sx + 5, sy - 2, sx - 6, sy - 2,
						 fill="#287f83", outline="#1b525b", width=2)
		c.create_polygon(sx - 8, sy - 18, sx + 6, sy - 18, sx + 5, sy - 12,
						 sx - 7, sy - 11, fill="#e6a86d", outline="")
		c.create_polygon(sx - 7, sy - 25, sx - 2, sy - 32, sx + 7, sy - 27,
						 sx + 9, sy - 20, sx + 1, sy - 18, sx - 8, sy - 20,
						 fill="#efc78d", outline="#8a6754", width=1)
		c.create_polygon(sx - 9, sy - 23, sx - 7, sy - 33, sx + 8, sy - 31,
						 sx + 11, sy - 24, sx + 2, sy - 27,
						 fill="#db765f", outline="#8d5049", width=2)
		c.create_polygon(sx - 5, sy - 6, sx + 2, sy - 6, sx + 7, sy + 1,
						 sx + 1, sy + 2, sx - 6, sy - 1,
						 fill="#e2b56f", outline="")
		c.create_oval(sx + 2, sy - 24, sx + 4, sy - 22, fill="#263e45", outline="")

	def draw_hud(self) -> None:
		c = self.canvas
		c.create_text(28, 23, text="TIDELIGHT", anchor="nw", fill="#e6f0d2",
					  font=("Segoe UI", 19, "bold"))
		c.create_text(30, 51, text=f"{self.model.level_name}  /  ISLE OF MOSS", anchor="nw",
					  fill="#83bcb0", font=("Segoe UI", 9, "bold"))
		right = self.width - 28
		time_text = self._clock_text(self.model.elapsed)
		level_crystals = len(self.model.levels[self.model.level_index]["crystals"])
		c.create_text(right, 27, text=f"SHARDS   {self.model.collected:02d} / {level_crystals:02d}",
					  anchor="ne", fill="#f0df9d", font=("Segoe UI", 13, "bold"))
		c.create_text(right, 53, text=f"TIME  {time_text}", anchor="ne",
					  fill="#f0df9d", font=("Segoe UI", 11, "bold"))
		c.create_text(right - 200, 53, text="LIVES  " + "  ".join("◆" for _ in range(self.model.lives)),
					  anchor="ne", fill="#f28a73", font=("Segoe UI", 11, "bold"))
		c.create_text(self.width / 2, 27, text="COLLECT THE SHARDS. FIND THE GATE.",
					  anchor="n", fill="#d2e3d3", font=("Segoe UI", 10, "bold"))
		c.create_text(self.width / 2, self.height - 22,
					  text="WASD / ARROWS  MOVE     P OR SPACE  PAUSE     R  RESTART     ESC  QUIT",
					  anchor="s", fill="#a5c8bd", font=("Segoe UI", 9, "bold"))
		if self.model.crystals:
			sx, sy = self.project(8, 8)
			c.create_text(sx, sy + 18, text="LOCKED", fill="#c3d7c5",
						  font=("Segoe UI", 8, "bold"))
		else:
			sx, sy = self.project(8, 8)
			c.create_text(sx, sy + 18, text="ENTER GATE", fill="#d7f4cb",
						  font=("Segoe UI", 8, "bold"))

	@staticmethod
	def _clock_text(seconds: float) -> str:
		minutes, secs = divmod(int(seconds), 60)
		return f"{minutes:02d}:{secs:02d}"

	def draw_overlay(self) -> None:
		c = self.canvas
		c.create_rectangle(0, 0, self.width, self.height, fill="#0c202c", stipple="gray50", outline="")
		if self.model.state == "won":
			title, detail = "ALL 10 LEVELS CLEARED", f"Final time: {self._clock_text(self.model.elapsed)}. Press R to play again."
			color = "#b7f0c6"
		elif self.model.state == "lost":
			title, detail = "LOST TO THE TIDE", "Three lives gone. Press R to try again."
			color = "#ffb39a"
		else:
			title, detail = "PAUSED", "Press P or Space to return to the island."
			color = "#e9dda8"
		c.create_text(self.width / 2, self.height / 2 - 20, text=title,
					  fill=color, font=("Segoe UI", 26, "bold"))
		c.create_text(self.width / 2, self.height / 2 + 20, text=detail,
					  fill="#d7e5db", font=("Segoe UI", 12))

	def loop(self) -> None:
		now = time.perf_counter()
		dt = min(now - self.last_time, 0.05)
		self.last_time = now
		if self.current_screen == "game":
			collected_before = self.model.collected
			self.model.step(dt, self.keys)
			if self.model.collected > collected_before:
				self.sound.play("collect")
			if not self.run_logged and self.model.state in ("won", "lost"):
				self.run_logged = True
				if self.model.state == "won":
					self.sound.play("win")
					self.leaderboard.record_run(self.username, self.model.elapsed, self.model.level_index + 1)
				else:
					self.sound.play("hit")
		self.draw()
		self.root.after(16, self.loop)


def run_self_test() -> None:
	model = GameModel()
	model.step(0.05, {"right"})
	assert model.x > 0, "Player should move with arrow-key input"
	model.x, model.y = 1.0, 2.0
	model.step(0.05, {"d"})
	assert model.x < 1.5, "Player should not pass through a blocking rock"
	model.x, model.y = 2.0, 1.0
	model.step(0.0, set())
	assert model.collected == 1, "Touching a shard should collect it"
	model.crystals.clear()
	model.x, model.y = 8.0, 8.0
	model.step(0.0, set())
	assert model.level_index == 1, "Clearing a stage should advance to the next one"
	model.reset()
	model.x, model.y = model.enemies[0].x, model.enemies[0].y
	model.step(0.0, set())
	assert model.lives == 2, "A patrolling hazard should cost one life"
	model.load_level(LEVEL_COUNT - 1)
	model.crystals.clear()
	model.x, model.y = 8.0, 8.0
	model.step(0.0, set())
	assert model.state == "won", "The final gate should finish the full run"
	print("Self-test passed: movement, collision, shards, gate, and hazard.")


def main() -> None:
	if "--self-test" in sys.argv:
		run_self_test()
		return
	root = tk.Tk()
	GameApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()











