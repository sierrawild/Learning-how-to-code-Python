import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables
W, H = 960, 960
p = palette.NEON_NIGHTS


def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.fill(*p['colors'][1])
    
    py5.no_fill()
    # py5.no_stroke()
    
    
def draw():
    
    ghost_trails(p['bg'],100) 
    center_coordinates()
    
    angle = 0.08 * py5.frame_count % 360
    r = 100
    
    
    # first pendulum
    py5.push_matrix()
    
    xy1 = 100
    speed = 0.15
    x1 = py5.cos(angle * speed) * xy1
    y1 = py5.sin(angle * speed) * xy1
    py5.translate(x1, y1)
    x = py5.cos(angle) * r
    y = py5.sin(angle) * r
    # Pendulum
    py5.stroke(*p['colors'][0])
    py5.stroke_weight(5)
    py5.line(0,0,x,y)
    py5.circle(0,0,10)
    # End of pendulum ball
    py5.stroke(*p['colors'][2])
    py5.circle(x,y,10)
    
    py5.pop_matrix()
    
    
    # second pendulum
    py5.push_matrix()
    xy2 = 80
    speed2 = 0.1
    x2 = py5.cos(angle * speed2) * xy2
    y2 = py5.sin(angle * speed2) * xy2
    py5.translate(x2,y2)
    
    
    # Pendulum 2
    py5.stroke(*p['colors'][3])
    py5.stroke_weight(5)
    py5.line(0,0,x2,y2)
    py5.circle(0,0,10)
    # End of pendulum ball 2
    py5.stroke(*p['colors'][3])
    py5.circle(x2,y2,10)
    py5.pop_matrix()
    
    
    # inside circle
    py5.stroke(*p['colors'][0])
    py5.stroke_weight(2)
    py5.circle(0,0,xy1*2)
    
    # Line
    line.append((float(x)+x1,float(y)+y1))
    py5.stroke(*p['colors'][2])
    py5.stroke_weight(3)
    py5.begin_shape()
    for i in range(len(line)):
        py5.vertex(*line[i])
    py5.end_shape()
    
    #remove from line
    if len(line) > 3000:
        line.pop(0)
    
    
    
    # END OF DRAW
line = []
line2 = [] # add another pendulum
    
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