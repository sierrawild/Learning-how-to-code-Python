import py5, palette

# Variables
W, H = 1000, 1000
p = palette.INK


a = (0,0)
b = (0,300)
c = (300,300)
d = (300,0)

r0 = 0.8
c = py5.lerp(a[0],c[0], r0), py5.lerp(a[1],c[1], r0)

def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(5)
    
    # py5.no_fill()
    # py5.no_stroke()
    
def draw():
    ghost_trails(p['bg'],10) 
    center_coordinates()
    
    rotate = 4
    py5.push_matrix()
    for i in range(rotate):
        box(a,b,c,d, size=1, dots=False)
        py5.rotate(py5.TAU / rotate)
        # py5.line(a[0],a[1],b[0],b[1])
    py5.pop_matrix()
    
    # END OF DRAW

def box(a,b,c,d,size, dots=True):
    if dots:
        py5.circle(a[0], a[1], size)
        py5.circle(b[0], b[1], size)
        py5.circle(c[0], c[1], size)
        py5.circle(d[0], d[1], size)
    
    for i in range(1,20):
        r = 0.05
        
        x1, y1 = points_x_to_y(a, b, size, dots, i, r)
        x2, y2 = points_x_to_y(b, c, size, dots, i, r)
        x3, y3 = points_x_to_y(c, d, size, dots, i, r)
        x4, y4 = points_x_to_y(d, a, size, dots, i, r)
        
        py5.line(x1,y1,x2,y2)
        py5.line(x3,y3,x4,y4)

def points_x_to_y(a, b, size, dots, i, r):
    x= py5.lerp(a[0], b[0], i * r)
    y= py5.lerp(a[1], b[1], i * r)
        
    if dots:
        py5.circle(x,y, size * 2)
    return x,y
        
    
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