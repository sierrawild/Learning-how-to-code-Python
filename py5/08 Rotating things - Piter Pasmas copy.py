# https://piterpasma.nl/articles/rotating

import py5, palette

W, H = 1000, 1000
pallet = palette.INK

def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*pallet['bg'])
    py5.stroke(*pallet['colors'][0])
    py5.fill(*pallet['colors'][1])
    py5.stroke_weight(5)
    
    py5.no_fill()
    # py5.no_stroke()
    
def draw():
    py5.background(*pallet['bg'])
    
    py5.push_matrix()
    py5.translate(W/2,H/2)
    for i in range(100):
        f = py5.frame_count / 60
        p = i / 100
        
        pos = rotating_thing(f,p, 100, 1)
        
        py5.circle(pos['x'], pos['y'], 5) 
    
    
    py5.pop_matrix()

def rotating_circle(phi, r):
    return vec2(r * py5.cos(phi), r * py5.sin(phi))


def rotating_thing(f,p,a,s):
    return rotating_circle((s * f + p) * py5.TAU, a)

  
def vec2(x,y):
    return{"x":x, "y":y}

def vec2_add(a,b):
    return vec2(a['x'] + b['x'], a['y'] + b['y'])
    
# Variables



py5.run_sketch()