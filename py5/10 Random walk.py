import py5, palette

# Variables

W, H = 1000, 1000
p = palette.INK
x = 0
choices = ['right','up','left','down']

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
    
    
def draw():
    global x
    ghost_trails(p['bg'],5) 

    x += 1
    py5.translate(W/2,H/2)
    py5.stroke(*p['colors'][0])
    py5.circle(x,0, 50)
    
def ghost_trails(color, alpha):  
    py5.push_style()
    py5.fill(*color,alpha) 
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()
    py5.rect(0,0,py5.width,py5.height)
    py5.pop_style()

    

py5.run_sketch()