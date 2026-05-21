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
alive = ((10,9),(10,10), (10,11))

    

# for y in range(rows):
#     row = []

#     for x in range(cols):
#         row.append(0)

#     grid.append(row)



speed = 10
is_paused = False

generation = 0

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
    global alive, grid
    
    
    if not is_paused:
        for y in range(rows):
            row = []

            for x in range(cols):
                row.append(0)

            grid.append(row)
        
        new_alive = []
        checked_cells = []
        if len(alive)>0:
            new_alive, checked_cells = check_alive_neighbors()
            
            # turn on alive cells in the grid
            for i in alive:
                grid[i[0]][i[1]] = 1 
        
        # check dead cells if they reproduce
        reproduce = []
        if len(checked_cells) > 0:
            for i in checked_cells:
                if i in alive:
                    continue
                x = check_if_reproduce(checked_cells)
                print(x)
            
        alive = new_alive + reproduce
    
    draw_the_grid()
    display_cycle_count()
    

############################### END of draw() ###############################

def draw_the_grid():
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 0:
                py5.fill(*p['colors'][1])
            else:
                py5.fill(*p['colors'][2])
            py5.square(x *cell_size,y * cell_size, cell_size)

def check_if_reproduce(cells):
    reproduce = []
    
    for i in cells:
        count_alive_neighbors = 0
        neighbors = [
            (i[0] - 1, i[1] -1), 
            (i[0], i[1] -1), 
            (i[0] + 1, i[1] -1),
            
            (i[0] -1 , i[1] ), 
            (i[0] +1, i[1] ), 
            
            (i[0] - 1, i[1] +1), 
            (i[0], i[1] +1), 
            (i[0] + 1, i[1] +1),
            ]
        for j in neighbors:
            if j in alive:
                count_alive_neighbors +=1
        if count_alive_neighbors == 3:
            reproduce.append(i)
    return reproduce

def check_alive_neighbors():
    checked_cells = []
    new_alive = []
    
    for i in alive:
        count_alive_neighbors = 0
        checked_cells.append(i)
        neighbors = [
            (i[0] - 1, i[1] -1), 
            (i[0], i[1] -1), 
            (i[0] + 1, i[1] -1),
            
            (i[0] -1 , i[1] ), 
            (i[0] +1, i[1] ), 
            
            (i[0] - 1, i[1] +1), 
            (i[0], i[1] +1), 
            (i[0] + 1, i[1] +1),
            ]
        for j in neighbors:
            checked_cells.append(j)
            if j in alive:
                count_alive_neighbors +=1
        if count_alive_neighbors == 2 or count_alive_neighbors == 3:
            new_alive.append(i)
    return new_alive, checked_cells

def display_cycle_count():
    py5.push_style()
    py5.fill("#FFFFFF")
    py5.text_align(py5.CENTER)
    py5.text_size(18)
    py5.text(generation, 20, 20)
    py5.pop_style()
    
def mouse_pressed():
    x = py5.mouse_x // cell_size
    y = py5.mouse_y // cell_size
    
    grid[x][y] = 1 - grid[x][y]
    if grid[x][y] == 1:
        alive.append((x,y))
    else:
        alive.remove((x,y))
    
def key_pressed():
    global is_paused
    if py5.key == " ":
        is_paused = not is_paused
        # to get this work I will have to change how update grid work and display different counter 

py5.run_sketch()