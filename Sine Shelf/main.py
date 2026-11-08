#!/usr/bin/env python3
"""Sine Shelf — watch a sine or cosine motion, edit it, copy the code.

    python sine_shelf.py

Needs only the Python standard library (tkinter, which ships with python.org
and Windows installs). Your copies are saved in your home folder.
"""

from __future__ import annotations

import json
import math
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path

SAVE_PATH = Path.home() / ".sine-shelf.json"
RANGE = 1.2
TRAIL_SECONDS = 8.0
SCOPE_SECONDS = 4.0

BG = "#0e1114"
SURFACE = "#161b1f"
SURFACE_2 = "#1e252b"
FG = "#e7e4dc"
MUTED = "#b7c0bb"
SUBTLE = "#8d9994"
LINE = "#2c3532"
ACCENT = "#d5e4dc"
INK = "#13201b"
WAVE = "#9dcebc"
DANGER = "#e0a097"


class FormulaError(Exception):
    pass


FUNCTIONS = {
    "sin": 1, "cos": 1, "tan": 1, "asin": 1, "acos": 1, "atan": 1, "atan2": 2,
    "abs": 1, "sqrt": 1, "exp": 1, "log": 1, "sign": 1, "floor": 1, "ceil": 1,
    "round": 1, "min": 2, "max": 2, "pow": 2, "mod": 2, "clamp": 3, "lerp": 3,
    "smooth": 1, "hypot": 2,
}
CONSTANTS = {"pi", "tau", "e"}
VARS = {"t", "s"}
HELPERS = ("mod", "sign", "clamp", "lerp", "smooth")


@dataclass(frozen=True)
class Num:
    value: float


@dataclass(frozen=True)
class Name:
    name: str


@dataclass(frozen=True)
class Unary:
    op: str
    expr: "Expr"


@dataclass(frozen=True)
class Binary:
    op: str
    left: "Expr"
    right: "Expr"


@dataclass(frozen=True)
class Call:
    name: str
    args: tuple["Expr", ...]


Expr = Num | Name | Unary | Binary | Call


class Parser:
    def __init__(self, src: str) -> None:
        self.src = src
        self.i = 0

    def parse(self) -> Expr:
        expr = self.parse_sum()
        self.skip()
        if self.i < len(self.src):
            raise FormulaError(f"Unexpected “{self.src[self.i]}”")
        return expr

    def skip(self) -> None:
        while self.i < len(self.src) and self.src[self.i].isspace():
            self.i += 1

    def parse_sum(self) -> Expr:
        left = self.parse_mul()
        while True:
            self.skip()
            op = self.src[self.i] if self.i < len(self.src) else ""
            if op not in ("+", "-"):
                break
            self.i += 1
            right = self.parse_mul()
            left = Binary(op, left, right)
        return left

    def parse_mul(self) -> Expr:
        left = self.parse_pow()
        while True:
            self.skip()
            op = self.src[self.i] if self.i < len(self.src) else ""
            if op not in ("*", "/", "%"):
                break
            if op == "*" and self.src.startswith("**", self.i):
                break
            self.i += 1
            right = self.parse_pow()
            left = Binary(op, left, right)
        return left

    def parse_pow(self) -> Expr:
        left = self.parse_unary()
        self.skip()
        if self.src.startswith("**", self.i):
            self.i += 2
            return Binary("^", left, self.parse_pow())
        if self.i < len(self.src) and self.src[self.i] == "^":
            self.i += 1
            return Binary("^", left, self.parse_pow())
        return left

    def parse_unary(self) -> Expr:
        self.skip()
        op = self.src[self.i] if self.i < len(self.src) else ""
        if op in ("+", "-"):
            self.i += 1
            return Unary(op, self.parse_unary())
        return self.parse_implicit()

    def parse_implicit(self) -> Expr:
        left = self.parse_primary()
        while True:
            self.skip()
            c = self.src[self.i] if self.i < len(self.src) else ""
            if c == "(" or (c and (c.isalnum() or c == ".")):
                left = Binary("*", left, self.parse_primary())
                continue
            break
        return left

    def parse_primary(self) -> Expr:
        self.skip()
        if self.i >= len(self.src):
            raise FormulaError("Formula ended early")
        c = self.src[self.i]
        if c == "(":
            self.i += 1
            inner = self.parse_sum()
            self.skip()
            if self.i >= len(self.src) or self.src[self.i] != ")":
                raise FormulaError("Missing )")
            self.i += 1
            return inner
        if c.isdigit() or c == ".":
            return self.parse_number()
        if c.isalpha():
            return self.parse_ident()
        raise FormulaError(f"Unexpected “{c}”")

    def parse_number(self) -> Expr:
        start = self.i
        while self.i < len(self.src) and (self.src[self.i].isdigit() or self.src[self.i] == "."):
            self.i += 1
        raw = self.src[start:self.i]
        if raw.count(".") > 1 or raw == ".":
            raise FormulaError(f"Bad number “{raw}”")
        try:
            value = float(raw)
        except ValueError as exc:
            raise FormulaError(f"Bad number “{raw}”") from exc
        if not math.isfinite(value):
            raise FormulaError(f"Bad number “{raw}”")
        return Num(value)

    def parse_ident(self) -> Expr:
        start = self.i
        while self.i < len(self.src) and self.src[self.i].isalpha():
            self.i += 1
        name = self.src[start:self.i].lower()
        self.skip()
        if self.i < len(self.src) and self.src[self.i] == "(":
            arity = FUNCTIONS.get(name)
            if arity is None:
                raise FormulaError(f"Unknown function “{name}”")
            self.i += 1
            args: list[Expr] = []
            self.skip()
            if self.i >= len(self.src) or self.src[self.i] != ")":
                while True:
                    args.append(self.parse_sum())
                    self.skip()
                    if self.i < len(self.src) and self.src[self.i] == ",":
                        self.i += 1
                        continue
                    break
            self.skip()
            if self.i >= len(self.src) or self.src[self.i] != ")":
                raise FormulaError(f"Missing ) after {name}")
            self.i += 1
            if len(args) != arity:
                noun = "argument" if arity == 1 else "arguments"
                raise FormulaError(f"{name} takes {arity} {noun}")
            return Call(name, tuple(args))
        if name in FUNCTIONS:
            raise FormulaError(f"{name} needs parentheses, like {name}(t)")
        if name not in CONSTANTS and name not in VARS:
            raise FormulaError(f"Unknown name “{name}”")
        return Name(name)


def parse_formula(source: str) -> Expr:
    trimmed = source.strip()
    if not trimmed:
        raise FormulaError("Enter a formula")
    return Parser(trimmed).parse()


def uses_name(expr: Expr, name: str) -> bool:
    if isinstance(expr, Num):
        return False
    if isinstance(expr, Name):
        return expr.name == name
    if isinstance(expr, Unary):
        return uses_name(expr.expr, name)
    if isinstance(expr, Binary):
        return uses_name(expr.left, name) or uses_name(expr.right, name)
    return any(uses_name(arg, name) for arg in expr.args)


def _mod(a: float, b: float) -> float:
    if b == 0:
        return float("nan")
    return a % b


def _call(name: str, args: list[float]) -> float:
    if name == "sin":
        return math.sin(args[0])
    if name == "cos":
        return math.cos(args[0])
    if name == "tan":
        return math.tan(args[0])
    if name == "asin":
        return math.asin(args[0])
    if name == "acos":
        return math.acos(args[0])
    if name == "atan":
        return math.atan(args[0])
    if name == "atan2":
        return math.atan2(args[0], args[1])
    if name == "abs":
        return abs(args[0])
    if name == "sqrt":
        return math.sqrt(args[0])
    if name == "exp":
        return math.exp(args[0])
    if name == "log":
        return math.log(args[0])
    if name == "sign":
        x = args[0]
        return float((x > 0) - (x < 0))
    if name == "floor":
        return math.floor(args[0])
    if name == "ceil":
        return math.ceil(args[0])
    if name == "round":
        return float(round(args[0]))
    if name == "min":
        return min(args[0], args[1])
    if name == "max":
        return max(args[0], args[1])
    if name == "pow":
        return args[0] ** args[1]
    if name == "mod":
        return _mod(args[0], args[1])
    if name == "clamp":
        return min(args[2], max(args[1], args[0]))
    if name == "lerp":
        return args[0] + (args[1] - args[0]) * args[2]
    if name == "smooth":
        x = min(1.0, max(0.0, args[0]))
        return x * x * (3.0 - 2.0 * x)
    if name == "hypot":
        return math.hypot(args[0], args[1])
    raise FormulaError(f"Unknown function “{name}”")


def evaluate(expr: Expr, t: float, s: float) -> float:
    try:
        return float(_eval(expr, t, s))
    except (ValueError, OverflowError, ZeroDivisionError, FormulaError):
        return float("nan")


def _eval(expr: Expr, t: float, s: float) -> float:
    if isinstance(expr, Num):
        return expr.value
    if isinstance(expr, Name):
        if expr.name == "t":
            return t
        if expr.name == "s":
            return s
        if expr.name == "pi":
            return math.pi
        if expr.name == "tau":
            return math.tau
        if expr.name == "e":
            return math.e
        raise FormulaError(expr.name)
    if isinstance(expr, Unary):
        value = _eval(expr.expr, t, s)
        return value if expr.op == "+" else -value
    if isinstance(expr, Binary):
        left = _eval(expr.left, t, s)
        right = _eval(expr.right, t, s)
        if expr.op == "+":
            return left + right
        if expr.op == "-":
            return left - right
        if expr.op == "*":
            return left * right
        if expr.op == "/":
            return left / right
        if expr.op == "%":
            return _mod(left, right)
        if expr.op == "^":
            return left ** right
        raise FormulaError(expr.op)
    return _call(expr.name, [_eval(arg, t, s) for arg in expr.args])


def compile_formula(source: str) -> tuple[Expr, bool]:
    expr = parse_formula(source)
    probe = evaluate(expr, 0.35, 0.2)
    if isinstance(probe, complex) or probe is None:
        raise FormulaError("Formula did not return a number")
    return expr, uses_name(expr, "s")


def format_num(value: float) -> str:
    if value == 0:
        return "0"
    if value == int(value) and abs(value) < 1e15:
        return str(int(value))
    return str(value)


def js_atom(expr: Expr) -> str:
    if isinstance(expr, Num):
        return format_num(expr.value)
    if isinstance(expr, Name):
        if expr.name == "pi":
            return "Math.PI"
        if expr.name == "tau":
            return "(Math.PI * 2)"
        if expr.name == "e":
            return "Math.E"
        return expr.name
    if isinstance(expr, Unary):
        return f"({expr.op}{js_atom(expr.expr)})"
    if isinstance(expr, Binary):
        if expr.op == "%":
            return f"mod({js_atom(expr.left)}, {js_atom(expr.right)})"
        if expr.op == "^":
            return f"({js_atom(expr.left)} ** {js_atom(expr.right)})"
        return f"({js_atom(expr.left)} {expr.op} {js_atom(expr.right)})"
    if expr.name in HELPERS:
        return f"{expr.name}({', '.join(js_atom(arg) for arg in expr.args)})"
    return f"Math.{expr.name}({', '.join(js_atom(arg) for arg in expr.args)})"


PY_FUNC = {
    "sin": "math.sin", "cos": "math.cos", "tan": "math.tan", "asin": "math.asin",
    "acos": "math.acos", "atan": "math.atan", "atan2": "math.atan2",
    "sqrt": "math.sqrt", "exp": "math.exp", "log": "math.log",
    "floor": "math.floor", "ceil": "math.ceil", "hypot": "math.hypot", "pow": "math.pow",
    "abs": "abs", "round": "round", "min": "min", "max": "max",
    "mod": "mod", "clamp": "clamp", "lerp": "lerp", "smooth": "smooth", "sign": "sign",
}


def py_atom(expr: Expr) -> str:
    if isinstance(expr, Num):
        return format_num(expr.value)
    if isinstance(expr, Name):
        if expr.name == "pi":
            return "math.pi"
        if expr.name == "tau":
            return "math.tau"
        if expr.name == "e":
            return "math.e"
        return expr.name
    if isinstance(expr, Unary):
        return f"({expr.op}{py_atom(expr.expr)})"
    if isinstance(expr, Binary):
        if expr.op == "%":
            return f"({py_atom(expr.left)} % {py_atom(expr.right)})"
        if expr.op == "^":
            return f"({py_atom(expr.left)} ** {py_atom(expr.right)})"
        return f"({py_atom(expr.left)} {expr.op} {py_atom(expr.right)})"
    return f"{PY_FUNC[expr.name]}({', '.join(py_atom(arg) for arg in expr.args)})"


def collect_helpers(expr: Expr, acc: set[str], lang: str) -> None:
    if isinstance(expr, (Num, Name)):
        return
    if isinstance(expr, Unary):
        collect_helpers(expr.expr, acc, lang)
        return
    if isinstance(expr, Binary):
        if expr.op == "%" and lang == "javascript":
            acc.add("mod")
        collect_helpers(expr.left, acc, lang)
        collect_helpers(expr.right, acc, lang)
        return
    if expr.name in HELPERS:
        acc.add(expr.name)
    for arg in expr.args:
        collect_helpers(arg, acc, lang)


PY_HELPERS = {
    "mod": "def mod(a, b):\n    return a % b",
    "sign": "def sign(x):\n    return (x > 0) - (x < 0)",
    "clamp": "def clamp(v, lo, hi):\n    return max(lo, min(hi, v))",
    "lerp": "def lerp(a, b, u):\n    return a + (b - a) * u",
    "smooth": "def smooth(u):\n    x = max(0.0, min(1.0, u))\n    return x * x * (3.0 - 2.0 * x)",
}
JS_HELPERS = {
    "mod": "function mod(a, b) {\n  return ((a % b) + b) % b;\n}",
    "sign": "function sign(x) {\n  return Math.sign(x);\n}",
    "clamp": "function clamp(v, lo, hi) {\n  return Math.min(hi, Math.max(lo, v));\n}",
    "lerp": "function lerp(a, b, u) {\n  return a + (b - a) * u;\n}",
    "smooth": "function smooth(u) {\n  const x = Math.min(1, Math.max(0, u));\n  return x * x * (3 - 2 * x);\n}",
}


def safe_name(name: str) -> str:
    cleaned = name.replace('"""', "").replace("*/", "").strip()
    return cleaned or "Motion"


def build_snippet(name: str, x: Expr, y: Expr, lang: str) -> str:
    title = safe_name(name)
    helpers: set[str] = set()
    collect_helpers(x, helpers, lang)
    collect_helpers(y, helpers, lang)
    ordered = [h for h in HELPERS if h in helpers]
    curve = uses_name(x, "s") or uses_name(y, "s")
    curve_note = " s runs from 0 to 1 along the shape." if curve else ""
    if lang == "javascript":
        head = "\n\n".join(JS_HELPERS[h] for h in ordered)
        body = (
            "export function motion(t, s = 0) {\n"
            f"  // {title} — about -1 to 1. Multiply by your pixel scale.{curve_note}\n"
            f"  const x = {js_atom(x)};\n"
            f"  const y = {js_atom(y)};\n"
            "  return { x, y };\n"
            "}"
        )
        return f"{head}\n\n{body}" if head else body
    pygame = (
        " Pygame y points down, so screen_y = origin_y - y * scale."
        if lang == "pygame"
        else ""
    )
    head = "\n\n".join(PY_HELPERS[h] for h in ordered)
    body = (
        "def motion(t, s=0.0):\n"
        f'    """{title} — about -1 to 1. Multiply by your pixel scale.{curve_note}{pygame}"""\n'
        f"    x = {py_atom(x)}\n"
        f"    y = {py_atom(y)}\n"
        "    return x, y\n"
    )
    parts = [part for part in ("import math", head, body) if part]
    return "\n\n".join(parts)


PRESETS = [
    {"id": "circle", "name": "Circle", "group": "Paths", "note": "Orbit, radar sweep, a loading dot.", "x": "cos(t)", "y": "sin(t)"},
    {"id": "ellipse", "name": "Ellipse", "group": "Paths", "note": "Same orbit, squeezed on y.", "x": "cos(t)", "y": "sin(t) * 0.55"},
    {"id": "lissajous", "name": "Lissajous", "group": "Paths", "note": "A knot from two frequencies.", "x": "sin(3 * t)", "y": "sin(2 * t + 0.6)"},
    {"id": "rose", "name": "Rose", "group": "Paths", "note": "Three petals from one cosine.", "x": "cos(3 * t) * cos(t)", "y": "cos(3 * t) * sin(t)"},
    {"id": "eight", "name": "Figure eight", "group": "Paths", "note": "A patrol path that crosses itself.", "x": "sin(t)", "y": "sin(2 * t) * 0.5"},
    {"id": "spiro", "name": "Spiro", "group": "Paths", "note": "A circle with a faster hitch on it.", "x": "(cos(t) + 0.32 * cos(-6 * t)) * 0.72", "y": "(sin(t) + 0.32 * sin(-6 * t)) * 0.72"},
    {"id": "cardioid", "name": "Cardioid", "group": "Paths", "note": "Heart-shaped roll of one circle on another.", "x": "(1 - cos(t)) * cos(t) * 0.42", "y": "(1 - cos(t)) * sin(t) * 0.42"},
    {"id": "travel", "name": "Traveling sine", "group": "Waves", "note": "Move a row of points. s is position along the row.", "x": "s * 2 - 1", "y": "sin(s * tau * 2 + t * 2) * 0.62"},
    {"id": "standing", "name": "Standing wave", "group": "Waves", "note": "The whole string swelling in place.", "x": "s * 2 - 1", "y": "sin(s * tau * 3) * cos(t * 1.5) * 0.7"},
    {"id": "beats", "name": "Two sines", "group": "Waves", "note": "Two frequencies adding into beats.", "x": "s * 2 - 1", "y": "(sin(s * tau * 2 + t) + 0.45 * sin(s * tau * 5 - t * 1.7)) * 0.42"},
    {"id": "square", "name": "Square-ish", "group": "Waves", "note": "Odd harmonics stacking toward a square.", "x": "s * 2 - 1", "y": "(sin(s * tau + t * 0.35) + sin(3 * (s * tau + t * 0.35)) / 3 + sin(5 * (s * tau + t * 0.35)) / 5 + sin(7 * (s * tau + t * 0.35)) / 7) * 0.78"},
    {"id": "packet", "name": "Wave packet", "group": "Waves", "note": "A short burst sliding along the line.", "x": "s * 2 - 1", "y": "sin(s * tau * 6 - t * 3) * exp(-(((s - mod(t * 0.18, 1)) * 4) ^ 2))"},
    {"id": "float", "name": "Float", "group": "Motion", "note": "Idle bob. Add it to a sprite's y.", "x": "0", "y": "sin(t * 2) * 0.55"},
    {"id": "sway", "name": "Sway", "group": "Motion", "note": "Slow lean for a plant, sign, or lantern.", "x": "sin(t * 1.1) * 0.7", "y": "cos(t * 0.55) * 0.18"},
    {"id": "pendulum", "name": "Pendulum", "group": "Motion", "note": "Hang a bob. The angle is itself a sine.", "x": "sin(sin(t * 1.5) * 1.15) * 0.95", "y": "0.35 - cos(sin(t * 1.5) * 1.15) * 0.95"},
    {"id": "bounce", "name": "Bounce", "group": "Motion", "note": "Runs across. The hop is abs(sin).", "x": "mod(t * 0.55, 2) - 1", "y": "abs(sin(t * pi * 0.55)) * 0.85"},
    {"id": "shake", "name": "Shake", "group": "Motion", "note": "Hit or camera shake that is not a circle.", "x": "sin(t * 41) * 0.55 + sin(t * 27) * 0.28", "y": "cos(t * 36) * 0.48 + sin(t * 19) * 0.22"},
    {"id": "wobble", "name": "Wobbly orbit", "group": "Motion", "note": "Radius breathes while it circles.", "x": "cos(t) * (0.72 + 0.22 * sin(5 * t))", "y": "sin(t) * (0.72 + 0.22 * sin(5 * t))"},
    {"id": "ease", "name": "Ease across", "group": "Motion", "note": "Smoothstep shuttle, the usual UI ease.", "x": "lerp(-0.82, 0.82, smooth(1 - abs(mod(t * 0.7, 2) - 1)))", "y": "0"},
    {"id": "settle", "name": "Settle", "group": "Motion", "note": "A spin that damps out, then repeats.", "x": "cos(t * 7) * exp(-mod(t, 4) * 0.7)", "y": "sin(t * 7) * exp(-mod(t, 4) * 0.7)"},
    {"id": "pulse", "name": "Pulse", "group": "Motion", "note": "A double bump, like a heartbeat on y.", "x": "0", "y": "pow(max(sin(t * 3), 0), 8) * 0.75 + pow(max(sin(t * 3 - 0.7), 0), 14) * 0.4"},
]
GROUPS = ("Paths", "Waves", "Motion")
PRESET_BY_ID = {item["id"]: item for item in PRESETS}


def run_checks() -> None:
    x, _ = compile_formula("cos(t)")
    y, _ = compile_formula("sin(t)")
    assert abs(evaluate(x, 0, 0) - 1) < 1e-9
    assert abs(evaluate(y, 0, 0)) < 1e-9
    doubled, _ = compile_formula("2sin(pi / 2)")
    assert abs(evaluate(doubled, 0, 0) - 2) < 1e-9
    for item in PRESETS:
        xe, xs = compile_formula(item["x"])
        ye, ys = compile_formula(item["y"])
        for t in (0.0, 0.35, 1.7):
            px = evaluate(xe, t, 0.2)
            py = evaluate(ye, t, 0.2)
            assert math.isfinite(px) and math.isfinite(py), item["id"]
        snippet = build_snippet(item["name"], xe, ye, "python")
        assert snippet.startswith("import math")
        assert "def motion" in snippet
        if xs or ys:
            assert "s runs from 0 to 1" in snippet
    pygame = build_snippet("Circle", x, y, "pygame")
    assert "screen_y" in pygame
    javascript = build_snippet("Circle", x, y, "javascript")
    assert "Math.cos" in javascript and "export function motion" in javascript
    try:
        parse_formula("sin(")
        raise AssertionError("expected a parse error")
    except FormulaError:
        pass
    print(f"ok — {len(PRESETS)} motions")


def launch() -> None:
    import time
    import tkinter as tk
    from tkinter import font as tkfont

    def family(mono: bool) -> str:
        names = set(tkfont.families())
        options = (
            ("IBM Plex Mono", "DejaVu Sans Mono", "Consolas", "Menlo")
            if mono
            else ("IBM Plex Sans", "Segoe UI", "DejaVu Sans", "Ubuntu")
        )
        for name in options:
            if name in names:
                return name
        return "TkFixedFont" if mono else "TkDefaultFont"

    class App:
        def __init__(self, root: tk.Tk) -> None:
            self.root = root
            self.sans = family(False)
            self.mono = family(True)
            self.t = 0.0
            self.speed = 1.0
            self.playing = True
            self.scrubbing = False
            self.last = time.perf_counter()
            self.trail: list[tuple[float, float, float]] = []
            self.hist: list[tuple[float, float, float]] = []
            self.lang = "python"
            self.query = ""
            self.selected_id = "circle"
            self.customs: list[dict[str, str]] = []
            self.drafts: dict[str, dict[str, str]] = {}
            self.x_expr: Expr | None = None
            self.y_expr: Expr | None = None
            self.x_err = ""
            self.y_err = ""
            self.good_key = ""
            self.copied_after: str | None = None
            self.armed_delete = ""
            self.suspend = False
            self._load()
            self._build()
            self._apply_selection(reset=False)
            self._tick()

        def _load(self) -> None:
            try:
                data = json.loads(SAVE_PATH.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                return
            customs = data.get("customs")
            if isinstance(customs, list):
                self.customs = [
                    item for item in customs
                    if isinstance(item, dict) and all(isinstance(item.get(k), str) for k in ("id", "name", "x", "y"))
                ]
            drafts = data.get("drafts")
            if isinstance(drafts, dict):
                self.drafts = {
                    key: value for key, value in drafts.items()
                    if isinstance(key, str) and isinstance(value, dict)
                }
            if isinstance(data.get("selectedId"), str):
                self.selected_id = data["selectedId"]
            if data.get("lang") in ("python", "pygame", "javascript"):
                self.lang = data["lang"]
            if data.get("speed") in (0.25, 0.5, 1, 2):
                self.speed = data["speed"]

        def _save(self) -> None:
            payload = {
                "selectedId": self.selected_id,
                "lang": self.lang,
                "speed": self.speed,
                "customs": self.customs,
                "drafts": self.drafts,
            }
            try:
                SAVE_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
            except OSError:
                pass

        def _base(self) -> dict[str, str] | None:
            for item in self.customs:
                if item["id"] == self.selected_id:
                    return item
            return PRESET_BY_ID.get(self.selected_id) or PRESETS[0]

        def _shown(self) -> tuple[str, str, str]:
            base = self._base() or PRESETS[0]
            draft = self.drafts.get(base["id"], {})
            return (
                str(draft.get("name", base["name"])),
                str(draft.get("x", base["x"])),
                str(draft.get("y", base["y"])),
            )

        def _patch_draft(self, **patch: str) -> None:
            base = self._base()
            if not base:
                return
            current = dict(self.drafts.get(base["id"], {}))
            current.update(patch)
            self.drafts[base["id"]] = current
            self._save()

        def _build(self) -> None:
            root = self.root
            root.title("Sine Shelf")
            root.configure(bg=BG)
            root.geometry("1180x760")
            root.minsize(880, 640)
            root.grid_columnconfigure(0, weight=1)
            root.grid_columnconfigure(1, weight=0, minsize=320)
            root.grid_rowconfigure(1, weight=1)

            header = tk.Frame(root, bg=BG)
            header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=16, pady=(14, 8))
            tk.Label(header, text="Sine Shelf", bg=BG, fg=FG, font=(self.sans, 18)).pack(anchor="w")
            tk.Label(
                header,
                text="Sine and cosine motions you can see, edit, and paste into a project.",
                bg=BG, fg=MUTED, font=(self.sans, 11),
            ).pack(anchor="w")

            left = tk.Frame(root, bg=BG)
            left.grid(row=1, column=0, sticky="nsew", padx=(12, 6), pady=(0, 12))
            left.grid_columnconfigure(0, weight=1)
            left.grid_rowconfigure(0, weight=1)

            self.plot = tk.Canvas(left, bg=BG, highlightthickness=0, height=360)
            self.plot.grid(row=0, column=0, sticky="nsew")
            self.plot.bind("<Configure>", lambda _e: self._draw())

            self.scope = tk.Canvas(left, bg=BG, highlightthickness=0, height=72)
            self.scope.grid(row=1, column=0, sticky="ew", pady=(4, 0))

            controls = tk.Frame(left, bg=BG)
            controls.grid(row=2, column=0, sticky="ew", pady=(8, 0))
            self.play_btn = self._button(controls, "Pause", self._toggle_play, fill=True)
            self.play_btn.pack(side="left")
            self._button(controls, "Reset", self._reset).pack(side="left", padx=(8, 0))
            speeds = tk.Frame(controls, bg=LINE)
            speeds.pack(side="left", padx=(8, 0))
            self.speed_btns: dict[float, tk.Button] = {}
            for value in (0.25, 0.5, 1, 2):
                label = f"{value:g}×"
                btn = tk.Button(
                    speeds, text=label, command=lambda v=value: self._set_speed(v),
                    bg=SURFACE_2 if value == self.speed else BG, fg=FG if value == self.speed else MUTED,
                    activebackground=SURFACE_2, activeforeground=FG, relief="flat",
                    font=(self.mono, 11), padx=10, pady=6, highlightthickness=0, bd=0,
                )
                btn.pack(side="left")
                self.speed_btns[value] = btn
            self.time_label = tk.Label(controls, text="0.00s", bg=BG, fg=MUTED, font=(self.mono, 11))
            self.time_label.pack(side="left", padx=(10, 0))
            self.value_label = tk.Label(controls, text="x 0.00   y 0.00", bg=BG, fg=MUTED, font=(self.mono, 11))
            self.value_label.pack(side="right")

            self.scale = tk.Scale(
                left, from_=0, to=8, resolution=0.01, orient="horizontal", showvalue=False,
                bg=BG, fg=MUTED, troughcolor=LINE, activebackground=WAVE, highlightthickness=0,
                bd=0, sliderrelief="flat", length=400,
            )
            self.scale.grid(row=3, column=0, sticky="ew", pady=(4, 0))
            self.scale.bind("<ButtonPress-1>", lambda _e: self._set_scrubbing(True))
            self.scale.bind("<ButtonRelease-1>", lambda _e: self._set_scrubbing(False))
            self.scale.configure(command=self._on_scrub)

            tk.Label(
                left, text="Grid is −1 to 1, y up. Multiply the copied formula by your pixel scale.",
                bg=BG, fg=MUTED, font=(self.sans, 10),
            ).grid(row=4, column=0, sticky="w", pady=(2, 8))

            editor = tk.Frame(left, bg=BG)
            editor.grid(row=5, column=0, sticky="ew")
            editor.grid_columnconfigure(0, weight=1)

            name_row = tk.Frame(editor, bg=BG)
            name_row.grid(row=0, column=0, sticky="ew")
            tk.Label(name_row, text="Name", bg=BG, fg=MUTED, font=(self.sans, 10)).pack(anchor="w")
            name_line = tk.Frame(name_row, bg=BG)
            name_line.pack(fill="x", pady=(2, 6))
            self.name_var = tk.StringVar()
            self.name_entry = tk.Entry(
                name_line, textvariable=self.name_var, bg=BG, fg=FG, insertbackground=FG,
                relief="flat", highlightthickness=1, highlightbackground=LINE, highlightcolor=WAVE,
                font=(self.sans, 12),
            )
            self.name_entry.pack(side="left", fill="x", expand=True, ipady=6)
            self.name_var.trace_add("write", lambda *_: self._on_name())
            self._button(name_line, "Save a copy", self._save_copy).pack(side="left", padx=(8, 0))
            self.revert_btn = self._button(name_line, "Revert", self._revert)
            self.delete_btn = self._button(name_line, "Delete", self._delete, danger=True)

            self.x_box, self.x_err_label = self._formula_row(editor, 1, "x")
            self.y_box, self.y_err_label = self._formula_row(editor, 2, "y")
            self.mode_label = tk.Label(editor, text="", bg=BG, fg=MUTED, font=(self.sans, 10), wraplength=640, justify="left")
            self.mode_label.grid(row=5, column=0, sticky="w", pady=(4, 6))

            lang_row = tk.Frame(editor, bg=BG)
            lang_row.grid(row=6, column=0, sticky="w")
            langs = tk.Frame(lang_row, bg=LINE)
            langs.pack(side="left")
            self.lang_btns: dict[str, tk.Button] = {}
            for key, label in (("python", "Python"), ("pygame", "Pygame"), ("javascript", "JavaScript")):
                btn = tk.Button(
                    langs, text=label, command=lambda k=key: self._set_lang(k),
                    bg=BG, fg=MUTED, activebackground=SURFACE_2, activeforeground=FG,
                    relief="flat", font=(self.sans, 11), padx=12, pady=6, highlightthickness=0, bd=0,
                )
                btn.pack(side="left")
                self.lang_btns[key] = btn
            self.copy_btn = self._button(lang_row, "Copy", self._copy, fill=True)
            self.copy_btn.pack(side="left", padx=(8, 0))

            self.snippet = tk.Text(
                editor, height=8, bg=SURFACE, fg=FG, insertbackground=FG, relief="flat",
                highlightthickness=1, highlightbackground=LINE, highlightcolor=WAVE,
                font=(self.mono, 10), wrap="none", padx=8, pady=8,
            )
            self.snippet.grid(row=7, column=0, sticky="ew", pady=(8, 0))
            self.snippet.configure(state="disabled")

            right = tk.Frame(root, bg=BG, highlightthickness=1, highlightbackground=LINE)
            right.grid(row=1, column=1, sticky="nsew", padx=(6, 12), pady=(0, 12))
            right.grid_rowconfigure(1, weight=1)
            right.grid_columnconfigure(0, weight=1)
            tools = tk.Frame(right, bg=BG)
            tools.grid(row=0, column=0, sticky="ew", padx=8, pady=8)
            tools.grid_columnconfigure(0, weight=1)
            self.query_var = tk.StringVar()
            query = tk.Entry(
                tools, textvariable=self.query_var, bg=SURFACE, fg=FG, insertbackground=FG,
                relief="flat", highlightthickness=1, highlightbackground=LINE, highlightcolor=WAVE,
                font=(self.sans, 12),
            )
            query.grid(row=0, column=0, sticky="ew", ipady=6)
            self.query_var.trace_add("write", lambda *_: self._on_query())
            self._button(tools, "New", self._blank).grid(row=0, column=1, padx=(8, 0))
            self.shelf_canvas = tk.Canvas(right, bg=BG, highlightthickness=0)
            self.shelf_canvas.grid(row=1, column=0, sticky="nsew")
            self.shelf_scroll = tk.Scrollbar(right, orient="vertical", command=self.shelf_canvas.yview)
            self.shelf_scroll.grid(row=1, column=1, sticky="ns")
            self.shelf_canvas.configure(yscrollcommand=self.shelf_scroll.set)
            self.shelf_inner = tk.Frame(self.shelf_canvas, bg=BG)
            self.shelf_window = self.shelf_canvas.create_window((0, 0), window=self.shelf_inner, anchor="nw")
            self.shelf_inner.bind("<Configure>", self._shelf_region)
            self.shelf_canvas.bind("<Configure>", self._shelf_width)
            right.bind("<Enter>", lambda _e: self._bind_wheel(True))
            right.bind("<Leave>", lambda _e: self._bind_wheel(False))
            tk.Label(
                right, text="Your copies are saved on this computer.",
                bg=BG, fg=SUBTLE, font=(self.sans, 9),
            ).grid(row=2, column=0, sticky="w", padx=10, pady=(4, 8))
            root.protocol("WM_DELETE_WINDOW", self._close)

        def _button(self, parent: tk.Widget, text: str, command, fill: bool = False, danger: bool = False) -> tk.Button:
            bg = ACCENT if fill else BG
            fg = INK if fill else (DANGER if danger else FG)
            return tk.Button(
                parent, text=text, command=command, bg=bg, fg=fg,
                activebackground=WAVE if fill else SURFACE_2, activeforeground=INK if fill else FG,
                relief="flat", font=(self.sans, 11), padx=12, pady=6,
                highlightthickness=1, highlightbackground=LINE, highlightcolor=WAVE, bd=0,
            )

        def _formula_row(self, parent: tk.Widget, row: int, label: str) -> tuple[tk.Text, tk.Label]:
            tk.Label(parent, text=label, bg=BG, fg=MUTED, font=(self.sans, 10)).grid(
                row=row * 2 - 1, column=0, sticky="w"
            )
            holder = tk.Frame(parent, bg=BG)
            holder.grid(row=row * 2, column=0, sticky="ew", pady=(2, 2))
            holder.grid_columnconfigure(0, weight=1)
            box = tk.Text(
                holder, height=2, bg=BG, fg=FG, insertbackground=FG, relief="flat",
                highlightthickness=1, highlightbackground=LINE, highlightcolor=WAVE,
                font=(self.mono, 12), wrap="word", padx=8, pady=6, undo=True,
            )
            box.grid(row=0, column=0, sticky="ew")
            box.bind("<KeyRelease>", lambda _e: self._on_formula())
            err = tk.Label(holder, text="", bg=BG, fg=DANGER, font=(self.sans, 10), anchor="w")
            err.grid(row=1, column=0, sticky="w")
            return box, err

        def _set_text(self, box: tk.Text, value: str) -> None:
            box.delete("1.0", "end")
            box.insert("1.0", value)

        def _read(self, box: tk.Text) -> str:
            return box.get("1.0", "end-1c")

        def _apply_selection(self, reset: bool) -> None:
            name, x, y = self._shown()
            self.suspend = True
            self.name_var.set(name)
            self._set_text(self.x_box, x)
            self._set_text(self.y_box, y)
            self.suspend = False
            self._compile(reset=reset)
            self._refresh_actions()
            self._rebuild_shelf()
            self._paint_langs()

        def _compile(self, reset: bool) -> None:
            x_src = self._read(self.x_box).strip()
            y_src = self._read(self.y_box).strip()
            self.x_err = ""
            self.y_err = ""
            x_expr = self.x_expr
            y_expr = self.y_expr
            try:
                x_expr, _ = compile_formula(x_src)
            except FormulaError as exc:
                self.x_err = str(exc)
            try:
                y_expr, _ = compile_formula(y_src)
            except FormulaError as exc:
                self.y_err = str(exc)
            self.x_err_label.configure(text=self.x_err)
            self.y_err_label.configure(text=self.y_err)
            if self.x_err or self.y_err or x_expr is None or y_expr is None:
                self._set_snippet("")
                return
            key = f"{x_src}||{y_src}"
            if reset or key != self.good_key:
                self.t = 0.0
                self.trail.clear()
                self.hist.clear()
                if not self.scrubbing:
                    self.scale.set(0)
            self.x_expr = x_expr
            self.y_expr = y_expr
            self.good_key = key
            curve = uses_name(x_expr, "s") or uses_name(y_expr, "s")
            self.mode_label.configure(
                text="This one uses s, so the preview draws the whole curve. s runs from 0 to 1."
                if curve
                else "One moving point. The trail is the path it has taken."
            )
            self._set_snippet(build_snippet(self.name_var.get(), x_expr, y_expr, self.lang))

        def _set_snippet(self, text: str) -> None:
            self.snippet.configure(state="normal")
            self.snippet.delete("1.0", "end")
            self.snippet.insert("1.0", text or "Fix the formula to copy it.")
            self.snippet.configure(state="disabled")

        def _on_formula(self) -> None:
            if self.suspend:
                return
            base = self._base()
            if not base:
                return
            self._patch_draft(x=self._read(self.x_box), y=self._read(self.y_box))
            self._compile(reset=True)
            self._refresh_actions()

        def _on_name(self) -> None:
            if self.suspend or not hasattr(self, "x_box"):
                return
            self._patch_draft(name=self.name_var.get())
            if self.x_expr and self.y_expr and not self.x_err and not self.y_err:
                self._set_snippet(build_snippet(self.name_var.get(), self.x_expr, self.y_expr, self.lang))
            self._refresh_actions()

        def _refresh_actions(self) -> None:
            preset = PRESET_BY_ID.get(self.selected_id)
            draft = self.drafts.get(self.selected_id, {})
            dirty = bool(preset and any(k in draft for k in ("x", "y", "name")))
            if dirty:
                self.revert_btn.pack(side="left", padx=(8, 0))
            else:
                self.revert_btn.pack_forget()
            custom = next((item for item in self.customs if item["id"] == self.selected_id), None)
            if custom:
                label = "Confirm delete" if self.armed_delete == custom["id"] else "Delete"
                self.delete_btn.configure(text=label)
                self.delete_btn.pack(side="left", padx=(8, 0))
            else:
                self.delete_btn.pack_forget()

        def _toggle_play(self) -> None:
            self.playing = not self.playing
            self.play_btn.configure(text="Pause" if self.playing else "Play")

        def _reset(self) -> None:
            self.t = 0.0
            self.trail.clear()
            self.hist.clear()
            self.scale.set(0)

        def _set_speed(self, value: float) -> None:
            self.speed = value
            for speed, btn in self.speed_btns.items():
                on = speed == value
                btn.configure(bg=SURFACE_2 if on else BG, fg=FG if on else MUTED)
            self._save()

        def _set_scrubbing(self, active: bool) -> None:
            self.scrubbing = active

        def _on_scrub(self, value: str) -> None:
            if not self.scrubbing:
                return
            v = float(value)
            base = math.floor(self.t / 8) * 8
            nxt = base + v
            if nxt < self.t - 0.02:
                self.trail.clear()
                self.hist.clear()
            self.t = nxt

        def _set_lang(self, lang: str) -> None:
            self.lang = lang
            self._paint_langs()
            if self.x_expr and self.y_expr and not self.x_err and not self.y_err:
                self._set_snippet(build_snippet(self.name_var.get(), self.x_expr, self.y_expr, lang))
            self._save()

        def _paint_langs(self) -> None:
            for key, btn in self.lang_btns.items():
                on = key == self.lang
                btn.configure(bg=SURFACE_2 if on else BG, fg=FG if on else MUTED)

        def _copy(self) -> None:
            text = self.snippet.get("1.0", "end-1c")
            if not text or text.startswith("Fix the formula"):
                return
            self.root.clipboard_clear()
            self.root.clipboard_append(text)
            self.copy_btn.configure(text="Copied")
            if self.copied_after:
                self.root.after_cancel(self.copied_after)
            self.copied_after = self.root.after(1400, lambda: self.copy_btn.configure(text="Copy"))

        def _save_copy(self) -> None:
            item = {
                "id": f"c_{uuid.uuid4().hex}",
                "name": self.name_var.get().strip() or "Untitled",
                "x": self._read(self.x_box),
                "y": self._read(self.y_box),
            }
            self.customs.insert(0, item)
            self.selected_id = item["id"]
            self.query_var.set("")
            self.armed_delete = ""
            self._save()
            self._apply_selection(reset=False)

        def _blank(self) -> None:
            item = {"id": f"c_{uuid.uuid4().hex}", "name": "Untitled", "x": "cos(t)", "y": "sin(t)"}
            self.customs.insert(0, item)
            self.selected_id = item["id"]
            self.query_var.set("")
            self.armed_delete = ""
            self._save()
            self._apply_selection(reset=True)

        def _revert(self) -> None:
            self.drafts.pop(self.selected_id, None)
            self._save()
            self._apply_selection(reset=True)

        def _delete(self) -> None:
            if self.armed_delete != self.selected_id:
                self.armed_delete = self.selected_id
                self._refresh_actions()
                return
            self.customs = [item for item in self.customs if item["id"] != self.selected_id]
            self.drafts.pop(self.selected_id, None)
            self.selected_id = PRESETS[0]["id"]
            self.armed_delete = ""
            self._save()
            self._apply_selection(reset=True)

        def _on_query(self) -> None:
            self.query = self.query_var.get().strip().lower()
            self._rebuild_shelf()

        def _select(self, item_id: str) -> None:
            self.selected_id = item_id
            self.armed_delete = ""
            self._save()
            self._apply_selection(reset=True)

        def _matches(self, item: dict[str, str]) -> bool:
            if not self.query:
                return True
            blob = " ".join((item.get("name", ""), item.get("note", ""), item.get("x", ""), item.get("y", ""))).lower()
            return self.query in blob

        def _rebuild_shelf(self) -> None:
            for child in self.shelf_inner.winfo_children():
                child.destroy()
            shown = [item for item in self.customs if self._matches(item)]
            if shown:
                self._group("Mine")
                for item in shown:
                    draft = self.drafts.get(item["id"], {})
                    self._row(item["id"], str(draft.get("name", item["name"])), "Saved on this computer", item["x"], item["y"])
            for group in GROUPS:
                items = [item for item in PRESETS if item["group"] == group and self._matches(item)]
                if not items:
                    continue
                self._group(group)
                for item in items:
                    draft = self.drafts.get(item["id"], {})
                    self._row(
                        item["id"],
                        str(draft.get("name", item["name"])),
                        item["note"],
                        str(draft.get("x", item["x"])),
                        str(draft.get("y", item["y"])),
                    )

        def _group(self, title: str) -> None:
            tk.Label(self.shelf_inner, text=title, bg=BG, fg=SUBTLE, font=(self.sans, 10)).pack(anchor="w", padx=8, pady=(10, 2))

        def _row(self, item_id: str, name: str, note: str, x: str, y: str) -> None:
            selected = item_id == self.selected_id
            row = tk.Frame(self.shelf_inner, bg=SURFACE_2 if selected else BG, cursor="hand2")
            row.pack(fill="x", padx=6, pady=2)
            spark = tk.Canvas(row, width=72, height=44, bg=SURFACE_2 if selected else SURFACE, highlightthickness=0)
            spark.pack(side="left", padx=6, pady=6)
            self._draw_spark(spark, x, y)
            text = tk.Frame(row, bg=SURFACE_2 if selected else BG)
            text.pack(side="left", fill="x", expand=True, pady=6)
            tk.Label(text, text=name, bg=SURFACE_2 if selected else BG, fg=FG, font=(self.sans, 11), anchor="w").pack(fill="x")
            tk.Label(text, text=note, bg=SURFACE_2 if selected else BG, fg=MUTED, font=(self.sans, 9), anchor="w", wraplength=200, justify="left").pack(fill="x")
            for widget in (row, spark, text, *text.winfo_children()):
                widget.bind("<Button-1>", lambda _e, i=item_id: self._select(i))

        def _draw_spark(self, canvas: tk.Canvas, x_src: str, y_src: str) -> None:
            try:
                x_expr, xs = compile_formula(x_src)
                y_expr, ys = compile_formula(y_src)
            except FormulaError:
                return
            curve = xs or ys
            n = 72 if curve else 100
            pad, w, h, span = 4, 72, 44, 1.25
            prev = None
            for i in range(n + 1):
                s = i / n if curve else 0
                t = 0.65 if curve else (i / n) * math.pi * 4
                px = evaluate(x_expr, t, s)
                py = evaluate(y_expr, t, s)
                if not math.isfinite(px) or not math.isfinite(py):
                    prev = None
                    continue
                cx = max(-span, min(span, px))
                cy = max(-span, min(span, py))
                sx = pad + ((cx + span) / (span * 2)) * (w - pad * 2)
                sy = pad + ((span - cy) / (span * 2)) * (h - pad * 2)
                if prev and (px - prev[0]) ** 2 + (py - prev[1]) ** 2 <= 0.75:
                    canvas.create_line(prev[2], prev[3], sx, sy, fill=WAVE, width=1.5)
                prev = (px, py, sx, sy)

        def _shelf_region(self, _event: object) -> None:
            self.shelf_canvas.configure(scrollregion=self.shelf_canvas.bbox("all"))

        def _shelf_width(self, event: tk.Event) -> None:
            self.shelf_canvas.itemconfigure(self.shelf_window, width=event.width)

        def _bind_wheel(self, active: bool) -> None:
            if active:
                self.root.bind_all("<MouseWheel>", self._wheel)
                self.root.bind_all("<Button-4>", self._wheel)
                self.root.bind_all("<Button-5>", self._wheel)
            else:
                self.root.unbind_all("<MouseWheel>")
                self.root.unbind_all("<Button-4>")
                self.root.unbind_all("<Button-5>")

        def _wheel(self, event: tk.Event) -> None:
            if getattr(event, "num", None) == 4 or getattr(event, "delta", 0) > 0:
                self.shelf_canvas.yview_scroll(-3, "units")
            else:
                self.shelf_canvas.yview_scroll(3, "units")

        def _sample(self, t: float, s: float) -> tuple[float, float]:
            if self.x_expr is None or self.y_expr is None:
                return float("nan"), float("nan")
            return evaluate(self.x_expr, t, s), evaluate(self.y_expr, t, s)

        def _to_px(self, x: float, y: float, w: int, h: int, pad: int = 28) -> tuple[float, float]:
            span = max(1, min(w, h) - pad * 2)
            ox = (w - span) / 2
            oy = (h - span) / 2
            px = ox + ((x + RANGE) / (RANGE * 2)) * span
            py = oy + ((RANGE - y) / (RANGE * 2)) * span
            return px, py

        def _draw(self) -> None:
            plot = self.plot
            w = max(plot.winfo_width(), 2)
            h = max(plot.winfo_height(), 2)
            plot.delete("all")
            for tick in (-1, 0, 1):
                x0, y0 = self._to_px(tick, -RANGE, w, h)
                x1, y1 = self._to_px(tick, RANGE, w, h)
                plot.create_line(x0, y0, x1, y1, fill=LINE)
                x0, y0 = self._to_px(-RANGE, tick, w, h)
                x1, y1 = self._to_px(RANGE, tick, w, h)
                plot.create_line(x0, y0, x1, y1, fill=LINE)
            if self.x_expr is None or self.y_expr is None:
                return
            curve = uses_name(self.x_expr, "s") or uses_name(self.y_expr, "s")
            if curve:
                prev = None
                n = 180
                for i in range(n + 1):
                    s = i / n
                    px, py = self._sample(self.t, s)
                    if not math.isfinite(px) or not math.isfinite(py):
                        prev = None
                        continue
                    sx, sy = self._to_px(px, py, w, h)
                    if prev and (px - prev[0]) ** 2 + (py - prev[1]) ** 2 <= 1.4:
                        plot.create_line(prev[2], prev[3], sx, sy, fill=WAVE, width=2)
                    prev = (px, py, sx, sy)
                mx, my = self._sample(self.t, 0.5)
            else:
                prev = None
                for _tt, px, py in self.trail:
                    if prev and (px - prev[0]) ** 2 + (py - prev[1]) ** 2 <= 0.75:
                        a, b = self._to_px(prev[0], prev[1], w, h)
                        c, d = self._to_px(px, py, w, h)
                        plot.create_line(a, b, c, d, fill=WAVE, width=2)
                    prev = (px, py)
                mx, my = self._sample(self.t, 0)
            if math.isfinite(mx) and math.isfinite(my):
                sx, sy = self._to_px(mx, my, w, h)
                plot.create_oval(sx - 5, sy - 5, sx + 5, sy + 5, fill=ACCENT, outline="")
            self._draw_scope()

        def _draw_scope(self) -> None:
            scope = self.scope
            w = max(scope.winfo_width(), 2)
            h = max(scope.winfo_height(), 2)
            scope.delete("all")
            mid = h / 2
            scope.create_line(0, mid, w, mid, fill=LINE)
            if len(self.hist) < 2:
                return
            t0 = self.t - SCOPE_SECONDS

            def poly(index: int, color: str, dash: tuple[int, ...] | None) -> None:
                pts: list[float] = []
                for tt, x, y in self.hist:
                    if tt < t0:
                        continue
                    value = x if index == 0 else y
                    if not math.isfinite(value):
                        if len(pts) >= 4:
                            scope.create_line(*pts, fill=color, width=1.5, dash=dash)
                        pts = []
                        continue
                    sx = ((tt - t0) / SCOPE_SECONDS) * w
                    sy = mid - max(-1.2, min(1.2, value)) * (h * 0.38)
                    pts.extend((sx, sy))
                if len(pts) >= 4:
                    scope.create_line(*pts, fill=color, width=1.5, dash=dash)

            poly(0, WAVE, None)
            poly(1, MUTED, (3, 3))

        def _tick(self) -> None:
            now = time.perf_counter()
            dt = min(0.05, now - self.last)
            self.last = now
            prev = self.t
            if self.playing:
                self.t += dt * self.speed
            if self.t < prev:
                self.trail.clear()
                self.hist.clear()
            curve = bool(self.x_expr and self.y_expr and (uses_name(self.x_expr, "s") or uses_name(self.y_expr, "s")))
            px, py = self._sample(self.t, 0.5 if curve else 0)
            if math.isfinite(px) and math.isfinite(py):
                if not self.trail or self.t - self.trail[-1][0] > 0.012:
                    self.trail.append((self.t, px, py))
                    self.hist.append((self.t, px, py))
                while self.trail and self.t - self.trail[0][0] > TRAIL_SECONDS:
                    self.trail.pop(0)
                while self.hist and self.t - self.hist[0][0] > SCOPE_SECONDS:
                    self.hist.pop(0)
                self.value_label.configure(text=f"x {px:.2f}   y {py:.2f}")
            else:
                self.value_label.configure(text="x —   y —")
            self.time_label.configure(text=f"{self.t:.2f}s")
            if not self.scrubbing:
                self.scale.set(self.t % 8)
            self._draw()
            self.root.after(16, self._tick)

        def _close(self) -> None:
            self._save()
            self.root.destroy()

    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    if "--check" in sys.argv:
        run_checks()
    else:
        launch()
