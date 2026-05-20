import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables

W, H = 1000, 1000
p = palette.INK
x0, y0 = 0, 0
x, y = 0, 0
travel = 20


def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((10))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.stroke_weight(5)
    py5.no_fill()
    
    
def draw():
    global x,y,x0,y0

    py5.translate(W/2,H/2)
    py5.stroke(*p['colors'][0],100)
    
    
    dx = py5.random(-1,1)
    dy = py5.random(-1,1)
    
    mag = py5.sqrt(dx*dx + dy*dy)
    
    dx /= mag
    dy /= mag
    
    x += dx * travel
    y += dy * travel
    
    
    py5.line(x0,y0,x,y)
    py5.circle(x,y, 5)
    
    x0, y0 = x,y


    if not inside_of_bounds():
        print("Out of bounds")
    
    

def inside_of_bounds():
    if -W/2 < x < W/2 and -H/2 < y < H/2:
        return True 

py5.run_sketch()