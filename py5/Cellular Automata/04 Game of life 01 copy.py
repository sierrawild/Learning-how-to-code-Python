import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables
W, H = 1000, 1000
p = palette.NOIR

cell_size = 50

cols = W // cell_size
rows = H // cell_size

alive = [(10, 9), (10, 10), (10, 11)]

speed = 10
is_paused = False
generation = 0


def settings():
    py5.size(W, H)


def setup():
    py5.frame_rate(speed)

    py5.stroke(*p['bg'])
    py5.stroke_weight(1)
    py5.rect_mode(py5.CORNER)


def draw():
    global alive, generation

    py5.background(*p['bg'])

    if not is_paused:
        alive = next_generation(alive)
        generation += 1

    draw_grid()
    display_cycle_count()


###############################
# GAME LOGIC
###############################

def next_generation(alive_cells):

    # Count neighbors for every relevant cell
    neighbor_counts = {}

    for cell in alive_cells:
        x, y = cell

        neighbors = [
            (x - 1, y - 1),
            (x,     y - 1),
            (x + 1, y - 1),

            (x - 1, y),
            (x + 1, y),

            (x - 1, y + 1),
            (x,     y + 1),
            (x + 1, y + 1),
        ]

        for n in neighbors:
            if n not in neighbor_counts:
                neighbor_counts[n] = 0

            neighbor_counts[n] += 1

    new_alive = []

    for cell, count in neighbor_counts.items():

        # Survival
        if cell in alive_cells and (count == 2 or count == 3):
            new_alive.append(cell)

        # Reproduction
        elif cell not in alive_cells and count == 3:
            new_alive.append(cell)

    return new_alive


###############################
# DRAWING
###############################

def draw_grid():

    for x in range(cols):
        for y in range(rows):

            if (x, y) in alive:
                py5.fill(*p['colors'][2])
            else:
                py5.fill(*p['colors'][1])

            py5.square(
                x * cell_size,
                y * cell_size,
                cell_size
            )


def display_cycle_count():
    py5.push_style()

    py5.fill("#FFFFFF")
    py5.text_size(18)

    py5.text(f"Generation: {generation}", 20, 30)

    py5.pop_style()


###############################
# INPUT
###############################

def mouse_pressed():
    global alive

    x = py5.mouse_x // cell_size
    y = py5.mouse_y // cell_size

    cell = (x, y)

    if cell in alive:
        alive.remove(cell)
    else:
        alive.append(cell)


def key_pressed():
    global is_paused

    if py5.key == " ":
        is_paused = not is_paused


py5.run_sketch()