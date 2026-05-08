import py5, palette

W, H = 540, 960
p = palette.INK

def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((120))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(5)
    
    py5.no_fill()
    # py5.no_stroke()
    
def draw():
    # flip y axis and center the origin
    py5.scale(1,-1)
    py5.push_matrix()
    py5.translate(W/2,H/2-H)
    py5.rotate(py5.frame_count * 0.001)
    
    # py5.background(*p['bg'])
    # semi transparent bg for trails
    py5.fill(*p['bg'],40)
    py5.rect(-W,-H, 2*W,2*H)
    py5.no_fill()
    
    
    
    a = py5.sin(py5.frame_count * 0.0002) * 2 + 3
    b = py5.cos(py5.frame_count * 0.00015) * 2 + 5
    
    
    py5.begin_shape()
    
    for i in range(period):
        theta = py5.TAU * (i/period)
        ham = 0.2
        # A = (W*ham)+80 * py5.sin(theta * 0.5)
        # B = (H*ham)+80 * py5.cos(theta * 0.4 + 1.4)
        
        
        x, y = lissajousPoint(theta,W*ham, H*ham, a, b)
        py5.vertex(x,y)
        
        
        
    py5.end_shape()
    py5.pop_matrix()
    
    
    
    
def lissajousPoint(t,A,B,a,b):
    x = py5.cos(t * a) * A    
    y = py5.sin(t * b) * B    
    return x,y
    

    
# Variables

period = 1000

py5.run_sketch()