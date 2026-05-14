import py5
import sys

sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')

import palette


# ----------------------------------------
# VARIABLES
# ----------------------------------------

W, H = 300, 300

p = palette.INK

x = 0
y = 0

x_old = 0
y_old = 0

travel = 20


# ----------------------------------------
# PY5
# ----------------------------------------

def settings():
    py5.size(W, H)
    # py5.full_screen()


def setup():
    py5.frame_rate(60)

    py5.background(*p['bg'])

    py5.stroke_weight(5)
    py5.no_fill()


def draw():
    global x, y

    # ghost_trails(p['bg'], 7)

    py5.translate(W / 2, H / 2)

    available_moves = get_available_moves()

    next_move = py5.random_choice(available_moves)

    color_change(next_move)

    move(next_move)

    py5.circle(x, y, 10)
    py5.line(x_old, y_old, x, y)

    print(available_moves)
    print(next_move)


# ----------------------------------------
# MOVEMENT
# ----------------------------------------

def get_available_moves():

    moves = ['right', 'left', 'up', 'down']

    margin = travel + 10

    # LEFT EDGE
    if x <= -W / 2 + margin:
        moves.remove('left')

    # RIGHT EDGE
    if x >= W / 2 - margin:
        moves.remove('right')

    # TOP EDGE
    if y <= -H / 2 + margin:
        moves.remove('up')

    # BOTTOM EDGE
    if y >= H / 2 - margin:
        moves.remove('down')

    return moves


def move(direction):
    global x, y, x_old, y_old

    x_old = x
    y_old = y

    if direction == 'right':
        x += travel

    elif direction == 'left':
        x -= travel

    elif direction == 'up':
        y -= travel

    elif direction == 'down':
        y += travel


# ----------------------------------------
# COLORS
# ----------------------------------------

def color_change(direction):

    if direction == 'right':
        py5.stroke(*p['colors'][0])

    elif direction == 'left':
        py5.stroke(*p['colors'][1])

    elif direction == 'up':
        py5.stroke(*p['colors'][2])

    elif direction == 'down':
        py5.stroke(*p['colors'][3])


# ----------------------------------------
# EFFECTS
# ----------------------------------------

def ghost_trails(color, alpha):

    py5.push_style()

    py5.fill(*color, alpha)

    py5.rect_mode(py5.CORNER)

    py5.no_stroke()

    py5.rect(0, 0, py5.width, py5.height)

    py5.pop_style()


# ----------------------------------------
# RUN
# ----------------------------------------

py5.run_sketch()