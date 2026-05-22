import py5, sys
sys.path.append(r'C:\Users\Pawel\Desktop\Learning how to code Python\py5')
import palette

# Variables
W, H = 540, 960
p = palette.INK

# Store trails for multiple pendulums
trails = [[] for _ in range(3)]

def settings():
    py5.size(W,H)
    
def setup():
    py5.frame_rate(60)
    py5.background(*p['bg'])
    py5.no_fill()
    
def draw():
    ghost_trails(p['bg'], 90)  # Lower alpha = longer trails
    center_coordinates()
    
    angle = 0.1 * py5.frame_count
    
    # Draw 3 pendulums with different frequencies
    frequencies = [1.0, 1.5, 2.0]
    radii = [80, 100, 120]
    colors = p['colors'][:3]
    
    for i, (freq, r, color) in enumerate(zip(frequencies, radii, colors)):
        py5.push_matrix()
        
        # Vertical oscillation
        y1 = py5.sin(angle * 0.05) * 300
        py5.translate(0, y1)
        
        # Circular motion
        x = py5.cos(angle * freq) * r
        y = py5.sin(angle * freq) * r
        
        # Pendulum arm
        py5.stroke(*colors[0], 100)
        py5.stroke_weight(2)
        py5.line(0, 0, x, y)
        
        # Pendulum ball
        py5.stroke(*color)
        py5.stroke_weight(8)
        py5.point(x, y)
        
        py5.pop_matrix()
        
        # Store trail
        trails[i].append((float(x), float(y) + y1))
        
        # Draw trail
        py5.stroke(*color)
        py5.stroke_weight(2)
        py5.begin_shape()
        for pos in trails[i]:
            py5.vertex(*pos)
        py5.end_shape()


def center_coordinates():
    py5.translate(py5.width/2, py5.height/2)
    py5.scale(1, -1)

def ghost_trails(color, alpha):  
    py5.push_style()
    py5.fill(*color, alpha) 
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()
    py5.rect(0, 0, py5.width, py5.height)
    py5.pop_style()

py5.run_sketch()
