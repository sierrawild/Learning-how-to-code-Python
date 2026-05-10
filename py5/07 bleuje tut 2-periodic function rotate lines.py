import py5, palette
#https://bleuje.com/tutorial2/

W = 540 
H = 960



def settings():
    py5.size(W,H)

def setup():
    py5.frame_rate(60)
    py5.fill(*p['colors'][0])
    py5.stroke(*p['colors'][2])
    py5.stroke_weight(1)
    # py5.no_stroke()
    
    
def draw():
    py5.background(*p['bg'])
    
    t = 1.0* (py5.frame_count ) / f
    t = t % 60
    
    for w in range(m):
        for h in range(m):
            x = py5.remap(w,0,m-1,0,W)
            y = py5.remap(h,0,m-1,0,H)
            radius =  periodic_function(t - offset(x,y))
            # py5.circle(x,y,radius)
            py5.push_matrix()
            py5.translate(x,y)
            py5.rotate(radius)
            py5.line(-5,0,5,0)

            
            py5.pop_matrix()
            
            
def periodic_function(p):
    return 1.0 * py5.sin(py5.TWO_PI*p)


def offset(x,y):
    # return 0.01 * py5.dist(x,y, W/2, H/2) # ripple like in stone in a water
    return 0.005 * (x+2 - y) # traveling lines
  
f = py5.get_frame_rate()  
m = 40  
p = palette.random_palette()
print(f"Palette in use: {p["name"]}")




py5.run_sketch()

    