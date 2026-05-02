import py5, palette
W = 1000
H = 1000



def settings():
    py5.size(W,H)

def setup():
    py5.frame_rate(60)
    py5.fill(*p['colors'][0])
    py5.stroke(*p['colors'][2])
    py5.stroke_weight(7)
    
    
def draw():
    # circle
    t = 1 * ((py5.frame_count-1) / 300)
    py5.background(*p['bg'])
    
    x = W/2 + r * py5.cos(py5.TWO_PI * t)
    y = H/2 + r * py5.sin(py5.TWO_PI * t)
    
    py5.circle(x,y, 10)
    
    # palette squares
    
    palette.draw_sample_squares(p)
    
    
p = palette.INK
    
r = 400



py5.run_sketch()

    