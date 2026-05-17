import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables
W, H = 1000, 1000
p = palette.NOIR

cell_size = 50

cols = W // cell_size
rows = H // cell_size

grid = []

for y in range(rows):
    row = []

    for x in range(cols):
        row.append(0)

    grid.append(row)
    
grid[5][5] = 1
grid[5][6] = 1
grid[5][7] = 1




speed = 10
is_paused = False

def settings():
    py5.size(W,H)
    
def setup():
    py5.frame_rate(speed)
    
    py5.background(*p['bg'])
    py5.stroke(*p['bg'])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(1)
    
    py5.rect_mode(py5.CORNER)
    
    # py5.no_fill()
    # py5.no_stroke()
    
def draw():
   
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:
                py5.fill(*p['colors'][1])
            else:
                py5.fill(*p['colors'][2])
            py5.square(x *cell_size,y * cell_size, cell_size)

        
    display_frame_count()

def display_frame_count():
    py5.push_style()
    py5.fill("#FFFFFF")
    py5.text_align(py5.CENTER)
    py5.text_size(18)
    py5.text(py5.frame_count, 20, 20)
    py5.pop_style()
    
def mouse_pressed():
    x = py5.mouse_x // cell_size
    y = py5.mouse_y // cell_size
    
    grid[x][y] = 1 - grid[x][y]
    
def key_pressed():
    global is_paused
    if py5.key == " ":
        is_paused = not is_paused
        # to get this work I will have to change how update grid work and display different counter 

py5.run_sketch()