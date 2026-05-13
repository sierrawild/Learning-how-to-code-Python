import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

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
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.stroke_weight(5)
    py5.no_fill()
    
    
def draw():
    global x,y,x_old,y_old
    ghost_trails(p['bg'],7) 

    py5.translate(W/2,H/2)
    py5.stroke(*p['colors'][0])
    
    
    # TODO pop a choice if near edge  
    # TODO travel by adding 1 until it == travel to make it travel
    stay_in_the_canvas()
    next_move = py5.random_choice(choices)
    move(next_move)
    # color_change(next)
    print(choices)
    print(next_move)
    
    py5.circle(x,y, 10)
    py5.line(x_old,y_old,x,y)

def stay_in_the_canvas():
    global choices
    margin = travel + 10
    if x < -W/2 + margin :
        choices = ['right','up','down']
    elif x > W/2 + margin:
        choices = ['up','left','down']
    elif y < -H/2 + margin:
        choices = ['right','left','down']
    elif y > H/2 + margin:
        choices = ['right','up','left']
    else:
        choices = ['right','up','left','down']
    

def color_change(next):
    if next == 'right':
        py5.fill(*p['colors'][0])
        py5.stroke(*p['colors'][0])
    elif next == 'left':
        py5.fill(*p['colors'][1])
        py5.stroke(*p['colors'][1])
    elif next == 'up':
        py5.fill(*p['colors'][2])
        py5.stroke(*p['colors'][2])
    elif next == 'down':
        py5.fill(*p['colors'][3])
        py5.stroke(*p['colors'][3])
        
        
def move(next):
    global x,y,x_old,y_old
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
    
def ghost_trails(color, alpha):  
    py5.push_style()
    py5.fill(*color,alpha) 
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()
    py5.rect(0,0,py5.width,py5.height)
    py5.pop_style()

    

py5.run_sketch()