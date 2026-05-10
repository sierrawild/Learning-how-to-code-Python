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
    py5.stroke_weight(7)
    py5.no_stroke()
    
    
def draw():
    py5.background(*p['bg'])
    
    t = 1.0* (py5.frame_count ) / f
    t = t % 60
    
    for w in range(m):
        for h in range(m):
            x = py5.remap(w,0,m-1,0,W)
            y = py5.remap(h,0,m-1,0,H)
            radius =  periodic_function(t - offset(x,y))
            py5.circle(x,y,radius)
            
            
def periodic_function(p):
    return py5.remap(py5.sin(py5.TWO_PI*p),-1,1,2,8)


def offset(x,y):
    return 0.003 * py5.dist(x,y, W/2, H/2) + py5.atan2(y-W/2,x-W/2)/py5.TWO_PI
  
f = py5.get_frame_rate()  
m = 40  
p = palette.random_palette()
print(f"Palette in use: {p["name"]}")




py5.run_sketch()

    