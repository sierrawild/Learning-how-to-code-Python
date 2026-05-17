import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables
W, H = 1000, 1000
p = palette.INK

cell_size = 50

camera_x, camera_y = 0, 0
camera_speed = 10

grid = {}




def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.stroke(*p['bg'])
    py5.stroke_weight(1)
    
    py5.rect_mode(py5.CORNER)
    
    # py5.no_fill()
    # py5.no_stroke()
    
def draw():
    global camera_x, camera_y
    
    py5.background(*p['bg'])
    
    # movement
    if py5.is_key_pressed:
        if py5.key == "w":
            camera_y -= camera_speed
        if py5.key == "s":
            camera_y += camera_speed
        if py5.key == "d":
            camera_x += camera_speed
        if py5.key == "a":
            camera_x -= camera_speed
            

        # visibility
        cols = W // cell_size + 2
        rows = H // cell_size + 2

        start_x = camera_x // cell_size
        start_y = camera_y // cell_size
  
        for y in range(rows):
            for x in range(cols):
                
                world_x = start_x + x
                world_y = start_y + y
                
            screen_x = world_x + cell_size - camera_x
            screen_y = world_y + cell_size - camera_y
            
            if (world_x, world_y) in grid:
                py5.fill(*p['colors'][1])
            else:
                py5.fill(*p['colors'][2])
                
            py5.square(screen_x,screen_y, cell_size)
            
def mouse_pressed():
    world_x = (py5.mouse_x + camera_x) // cell_size
    world_y = (py5.mouse_y + camera_y) // cell_size
    
    pos = (world_x, world_y)

    if pos in grid:
        del grid[pos]
    else:
        grid[pos] = 1
                

py5.run_sketch()