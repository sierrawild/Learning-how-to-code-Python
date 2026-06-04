import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables
W, H = 1000, 900
p = palette.random_palette()


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
    # py5.no_stroke()
    
def draw():
    ghost_trails(p['bg'],25) 
    # center_coordinates()
    
    spam = py5.frame_count * 0.01
    x = py5.noise(spam) * W
    y = py5.noise(spam + 1000) * H
    
    py5.circle(x,y, 5)
    
    spam = py5.frame_count * 0.01
    spam = spam * - 1
    x = py5.noise(spam) * W
    y = py5.noise(spam + 1000) * H
    py5.circle(x,y, 5)

    spam = py5.frame_count * 0.01
    spam = spam * - 1
    x = py5.noise(spam) * H
    y = py5.noise(spam + 1000) * W
    py5.circle(x,y, 5)
    
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