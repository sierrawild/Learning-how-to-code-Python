import py5, palette
from image_save_for_py5 import save_img

W, H = 1080, 1920
p = palette.INK

def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate(120)
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(5)
    
    # py5.no_fill()
    # py5.no_stroke()
    
def draw():
    global theta
    # flip y axis and center the origin
    py5.scale(1,-1)
    py5.translate(W/2,H/2-H)
    
    
    # py5.background(*p['bg'])
    # transparent bg for traces
    py5.fill(*p['bg'],4)
    py5.rect(-W,-H, 2*W,2*H)
    py5.no_fill()
    
    
    
    
    theta += py5.TAU / (120 * period)
    
    
    x, y = lissajousPoint(theta,400, 300, 3, 5)
    
    py5.circle(x,y,10)
    
    save_img(1,60*10)
    
    if py5.frame_count % 60 == 0:
        print(f'FPS: {py5.get_frame_rate():.1f}')
    
    
def lissajousPoint(t,A,B,a,b):
    x = py5.cos(t * a) * A    
    y = py5.sin(t * b) * B    
    return x,y
    

    
# Variables
global theta, period
theta = 0
period = 3

py5.run_sketch()