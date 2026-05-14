import py5, palette

# Variables
W, H = 1000, 1000
p = palette.INK


def settings():
    py5.size(W,H, py5.P2D)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(5)
    
    # py5.no_fill()
    py5.no_stroke()
    
def draw():
    # ghost_trails(*p['bg'],10) 
    center_coordinates()
    
    py5.begin_shape()
    py5.fill(*p['colors'][0],0) # transparent
    # py5.fill(*p['bg'],0) # transparent
    py5.vertex(0,0)
    
    py5.fill(*p['colors'][0],10) # not transparent
    py5.vertex(100,100)
    
    py5.fill(*p['colors'][0],100) # not transparent
    py5.vertex(100,50)
    
    py5.end_shape(py5.CLOSE)
    
    # END OF DRAW
    
def center_coordinates():
    py5.translate(py5.width/2,py5.height/2)
    py5.scale(1,-1)

def ghost_trails(color, alpha):  
    py5.push_style()
    py5.fill(*color,alpha) 
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()
    py5.rect(0,0,py5.width,py5.height)
    py5.pop_style()

    
    

    

py5.run_sketch()