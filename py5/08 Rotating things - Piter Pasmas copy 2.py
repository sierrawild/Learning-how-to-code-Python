# https://piterpasma.nl/articles/rotating

import py5, palette, image_save_for_py5

W, H = 540, 960
pallet = palette.INK
pallet = palette.random_palette()

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
    py5.fill(*pallet['bg'],10)
    # py5.rect_mode(py5.CENTER)
    py5.rect(0,0,W,H)
    
    py5.push_matrix()
    py5.translate(W/2,H/2)
    for i in range(1000):
        f = py5.frame_count / 600
        p = i / 1000
        a = 100
        s = 1+ i/1000

        
        pos1 = rotating_thing(f*3,p, a, s)
        pos2 = rotating_thing(f*2,p, a, s)

        pos = vec2_add(pos1,pos2)
        
        py5.circle(pos['x'], pos['y'], 5) 
        
    
    
    py5.pop_matrix()
    
    # IMAGE SAVING 
    # image_save_for_py5.save_img(0,10000, 1)

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