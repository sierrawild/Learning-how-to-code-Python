import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables
W, H = 1000, 1000
p = palette.INK

x,y = 0,0
x_old, y_old = x,y

DISTANCE_X = 1


def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(2)
    
    # py5.no_fill()
    # py5.no_stroke()
    
def draw():
    global x,y,x_old,y_old
    # ghost_trails(*p['bg'],10) 
    center_coordinates()
    
    # distance_y = py5.random_int(-10, 10)
    distance_y = py5.random_gaussian(0,10)
    y += distance_y
    print(distance_y)
    x += DISTANCE_X
    
    
    py5.line(x_old,y_old,x,y)
    py5.circle(x,y,3)
    
    x_old, y_old = x,y
    
    
    
    
    # END OF DRAW
    
def center_coordinates():
    py5.translate(0,py5.height/2)
    py5.scale(1,-1)
    
def ghost_trails(color, alpha):  
    py5.push_style()
    py5.fill(*color,alpha) 
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()
    py5.rect(0,0,py5.width,py5.height)
    py5.pop_style()

    
    

    

py5.run_sketch()