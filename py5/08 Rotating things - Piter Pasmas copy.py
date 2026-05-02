# https://piterpasma.nl/articles/rotating

import py5, palette

W, H = 1000, 1000
p = palette.INK

def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(5)
    
    py5.no_fill()
    # py5.no_stroke()
    
def draw():
    py5.background(*p['bg'])
    
    
def vec2(x,y):
    return{"x":x, "y":y}

def vec2_add(a,b):
    return vec2(a['x'] + b['x'], a['y'] + b['y'])
    
# Variables



py5.run_sketch()