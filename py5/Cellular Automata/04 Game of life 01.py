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





def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
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

        
    

    
    

    

py5.run_sketch()