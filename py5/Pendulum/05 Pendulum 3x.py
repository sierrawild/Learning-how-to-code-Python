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
    
    py5.no_fill()
    # py5.no_stroke()
    
    
def draw():
    
    ghost_trails(p['bg'],100) 
    center_coordinates()
    
    angle = 0.05 * py5.frame_count 
    r = 100
    
    # layer 1
    py5.fill(*p['colors'][1])
    py5.stroke(*p['colors'][1])
    py5.stroke_weight(3)
    x1 = py5.cos(angle) * r
    y1 = py5.sin(angle) * r
    py5.line(0,0,x1,y1)
    py5.circle(x1,y1,10)
    
    # layer 2
    py5.fill(*p['colors'][2])
    py5.stroke(*p['colors'][2])
    py5.stroke_weight(3)
    angle = angle * 1.5 
    r = r * 0.8
    x2 = (py5.cos(angle) * r) + x1
    y2 = (py5.sin(angle) * r) + y1
    py5.line(x1,y1, x2, y2)
    py5.circle(x2,y2,10)
    
    # layer 3
    py5.fill(*p['colors'][3])
    py5.stroke(*p['colors'][3])
    py5.stroke_weight(3)
    angle = angle * 1.5 * -1
    r = r * 0.8
    x3 = (py5.cos(angle) * r) + x2
    y3 = (py5.sin(angle) * r) + y2
    py5.line(x2, y2, x3, y3)
    py5.circle(x3,y3,10)
    
    # line 3 setup
    line_3_point = (x3,y3)
    if line_3_point not in line_3:
        line_3.append(line_3_point)
        
    # line 3 draw
    py5.no_fill()
    py5.begin_shape()
    py5.stroke_weight(1)
    for i in line_3:
        py5.vertex(i)
    py5.end_shape()
    
line_3 = []

    
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