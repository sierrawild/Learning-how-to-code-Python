import py5, palette

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
    ghost_trails(p['bg'], 30)
    center_coordinates()
    
    angle = 0.1 * py5.frame_count
    r = 100
    
    py5.push_matrix()
    y1 = py5.sin(angle * 0.05) * 300
    py5.translate(0, y1)
    
    x = py5.cos(angle) * r
    y = py5.sin(angle) * r
    
    # Pendulum
    py5.stroke(*p['colors'][0])
    py5.stroke_weight(5)
    py5.line(0, 0, x, y)
    py5.circle(0, 0, 10)
    
    # End ball
    py5.stroke(*p['colors'][2])
    py5.circle(x, y, 10)
    
    py5.pop_matrix()
    
    # Add to trail
    spam.append((float(x), float(y) + y1))
    
    # Draw trail with gradient
    num_points = len(spam)
    for i in range(1, num_points):
        # Calculate alpha based on position (newer = brighter)
        alpha = py5.remap(i, 0, num_points, 50, 255)
        
        py5.stroke(*p['colors'][2], alpha)
        py5.stroke_weight(3)
        py5.line(spam[i-1][0], spam[i-1][1], spam[i][0], spam[i][1])

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
