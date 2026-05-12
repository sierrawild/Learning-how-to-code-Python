import py5, palette

# Variables

W, H = 1000, 1000
p = palette.INK
x_old, y_old = 0, 0
x, y = 0, 0
travel = 20
choices = ['right','up','left','down']

def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((10))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.stroke_weight(5)
    py5.no_fill()
    
    
def draw():
    global x,y,x_old,y_old
    ghost_trails(p['bg'],10) 

    py5.translate(W/2,H/2)
    py5.stroke(*p['colors'][0])
    
    # TODO pop a choice if near edge  
    # TODO travel by adding 1 until it == travel
    # TODO turn this into a function
    next = py5.random_choice(choices)
    if next == 'right':
        x_old = x
        y_old = y
        x += travel
    elif next == 'left':
        x_old = x
        y_old = y
        x -= travel
    elif next == 'up':
        x_old = x
        y_old = y
        y += travel
    elif next == 'down':
        x_old = x
        y_old = y
        y -= travel
    
    py5.circle(x,y, 10)
    py5.line(x_old,y_old,x,y)
    
def ghost_trails(color, alpha):  
    py5.push_style()
    py5.fill(*color,alpha) 
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()
    py5.rect(0,0,py5.width,py5.height)
    py5.pop_style()

    

py5.run_sketch()