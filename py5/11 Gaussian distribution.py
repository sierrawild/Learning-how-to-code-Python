import py5, palette, random

# Variables
W, H = 1000, 800
p = palette.INK

samples = 500


gaussian_py5 = []
gaussian_random = []

mu = 100
sigma = 200

for i in range(samples):
    gaussian_py5.append(py5.random_gaussian(mu, sigma))
    gaussian_random.append(random.gauss(mu, sigma))
    
# gaussian_py5.sort()
# gaussian_random.sort()
    
    
def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.fill(*p['colors'][1])
    
    # py5.no_fill()
    # py5.no_stroke()
    
def draw():
    ghost_trails(p['bg'],10) 
    center_coordinates()
    
    # lines
    py5.stroke(*p['colors'][4])
    py5.stroke_weight(1)
    
    py5.push_matrix()
    py5.scale(1,-1)
    py5.text_size(18)
    
    # horizontal lines
    for i in range(int(H/50)):
        y = i*50-H/2
        py5.line(-W,y,W,y)
        py5.text(int(y*-1),-W/2 +20, y)
        py5.text("py5_gaussian",-50, 0)
        py5.text("random_gaussian",-50, 250)
    # py5.pop_matrix()

    # vertical lines
    for i in range(int(W/50)):
        x = i*50-W/2
        py5.line(x,-H,x,H)
        py5.text(int(x),x + 5, -H/2 + 20)
    py5.pop_matrix()
    
    py5.stroke_weight(4)
    # py5 bell curve
    py5.stroke(*p['colors'][0])
    for i in gaussian_py5:
        height = 150 * py5.exp(-0.5 * (i/50)**2)
        py5.point(i, height)
    
    # py5 random curve
    py5.stroke(*p['colors'][1])
    for i in gaussian_random:
        height = 150 * py5.exp(-0.5 * (i/50)**2)
        py5.point(i, height - 250)
        
    
    
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