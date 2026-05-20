import py5, sys, random
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables

W, H = 1000, 1000
p = palette.INK
x_old, y_old = 0, 0
x, y = 0, 0
travel = 20
choices = ['right','up','left','down']
weights = [1,1,1,1]

gravity_x, gravity_y = 100, -100
gravity_strength = 100 # larger the weaker the gravity is

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
    # ghost_trails(p['bg'],7) 

    py5.translate(W/2,H/2)
    py5.scale(1,-1)
    
    py5.stroke(*p['colors'][0],10)
    
    if py5.frame_count == 10:
        gravity_draw(gravity_x, gravity_y)
    
    gravity(gravity_x, gravity_y, gravity_strength)
        
    next_move = random.choices(choices,weights, k=1)
    move(next_move[0])
    
    
    py5.circle(x,y, 10)
    py5.line(x_old,y_old,x,y)

    if not inside_of_bounds():
        print("Out of bounds")
    

    
def gravity(x2,y2, strength):
    global weights
    x_dist = x-x2
    y_dist = y-y2
    # left
    if x_dist > 0:
        weights[2] = (x_dist / strength) +1
    else:
        weights[2] = 1

    # right    
    if x_dist < 0:
        weights[0] = (abs(x_dist) / strength)+1 
    else:
        weights[0] = 1

    # down
    if y_dist > 0:
        weights[3] = (y_dist / strength) +1
    else:
        weights[3] = 1

    # up  
    if x_dist < 0:
        weights[1] = (abs(y_dist) / strength)+1 
    else:
        weights[1] = 1
    
    print(weights)
        
    
def gravity_draw(x1,y1):
    py5.push_style()
    
    py5.no_stroke()
    py5.fill(*p['bg'])
    circle_size = 150
    # py5.circle(x1,y1,circle_size + 5)
    for i in range(30):
        py5.fill("#FF2626",1*i)
        py5.circle(x1,y1,circle_size - i*5)

    py5.pop_style()


def stay_in_the_canvas():
    global choices
    margin = travel + 10
    if x < -W/2 + margin :
        choices.discard('left')
    elif x > -W/2 + margin :
        choices.add('left')

    if x > W/2 + margin:
        choices.discard('right')
    
    elif x < W/2 + margin:
        choices.add('right')

    if y < -H/2 + margin:
        choices.discard('up')
    if y > -H/2 + margin:
        choices.add('up')

    if y > H/2 + margin:
        choices.discard('down')
    if y < H/2 + margin:
        choices.add('down')

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

def inside_of_bounds():
    if x < W/2 and x > -W/2 and y < H/2 and y > -H/2:
        return True 

py5.run_sketch()