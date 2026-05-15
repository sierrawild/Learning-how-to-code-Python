import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables
W, H = 1000, 1000
p = palette.INK

grid_size = 10

def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.stroke(*p['bg'])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(1)
    
    py5.rect_mode(py5.CENTER)
    
    # py5.no_fill()
    # py5.no_stroke()
    
def draw():
    # ghost_trails(p['bg'],10) 
    center_coordinates()
    

    
    for i in range(1000):
        x = py5.random_int(-20,20)
        y = py5.random_int(-20,20)
        
        py5.square(x *grid_size,y * grid_size, grid_size)
        
    py5.no_loop()
    
    # END OF DRAW
    
def center_coordinates():
    py5.translate(py5.width/2,py5.height/2)
    py5.scale(1,-1)

def ghost_trails(color, alpha):  
    py5.push_style()
    py5.fill(*color,alpha) 
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()
    py5.rect(0,0,py5.width,py5.height)
    py5.pop_style()

    
    

    

py5.run_sketch()