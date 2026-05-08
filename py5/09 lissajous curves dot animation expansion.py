import py5, palette
from image_save_for_py5 import save_img

W, H = 540, 960
p = palette.INK



def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate(60)
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(3)
    
    # py5.no_fill()
    # py5.no_stroke()
    
def draw():
    global theta, prev_x, prev_y, noise_offset_x, noise_offset_y

    a = 3 + 0.2* py5.sin(theta*0.2)
    b = 3 + 0.2* py5.cos(theta*0.15)

    ham = 0.45
    # A = (W*ham)+80 * py5.sin(theta * 0.5)
    # B = (H*ham)+80 * py5.cos(theta * 0.4 + 1.4)
    A = W * ham
    B = H * ham
    
    
    # flip y axis and center the origin
    py5.scale(1,-1)
    py5.translate(W/2,H/2-H)
    
    # py5.background(*p['bg'])
    # transparent bg for traces
    py5.fill(*p['bg'],20)
    py5.rect(-W,-H, 2*W,2*H)
    py5.no_fill()
    
    theta += py5.TAU / (120 * period)
    
    x, y = lissajousPoint(theta,A, B, 5, 1)
    # perlin drift
    drift = 20
    x += py5.remap(py5.noise(noise_offset_x), 0, 1, -drift, drift)
    y += py5.remap(py5.noise(noise_offset_y), 0, 1, -drift, drift)
    noise_offset_x += 0.1
    noise_offset_y += 0.1
    
    # vary stroke weight
    weight = py5.remap(py5.noise(theta*2), 0,1, 1, 10)
    py5.stroke_weight(weight)
    
    py5.circle(x,y,3)
    # spam = 10
    # py5.circle(x+spam,y+spam,4)
    # py5.circle(x+spam*2,y+spam*2,4)
    # draw lines
    if prev_x != None:
        py5.line(prev_x,prev_y,x,y)
        # py5.line(prev_x+spam,prev_y+spam,x+spam,y+spam)
        # py5.line(prev_x+spam*2,prev_y+spam*2,x+spam,y+spam)
        # py5.line(prev_x+spam*2,prev_y+spam*2,x+spam*2,y+spam*2)
    prev_x, prev_y = x,y
    
    # image save
    save_img(1)
    if theta >= py5.TAU * period:
        py5.no_loop()
    
    if py5.frame_count % 60*3 == 0:
        print(f'FPS: {py5.get_frame_rate():.1f}')
        
    
    # color
    idx = int((py5.sin(theta)* 0.5 + 0.5) * (len(c)-1))
    py5.stroke(*c[idx])
    
    
def lissajousPoint(t,A,B,a,b):
    x = py5.cos(t * a) * A    
    y = py5.sin(t * b) * B    
    return x,y
    
# Variables
global theta, period
theta = 0
period = 3
prev_x, prev_y = None, None

# color
c = p['colors']

noise_offset_x, noise_offset_y = 0, 1000

py5.run_sketch()