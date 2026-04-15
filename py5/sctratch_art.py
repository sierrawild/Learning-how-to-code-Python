import py5

def settings():
    py5.size(800,400)
    
def setup():
    py5.frame_rate(20)
    py5.background('#000000')
    py5.stroke('#ffffff')
    py5.fill('#ffffff')

def draw():
    py5.stroke_weight(15)
    py5.line(py5.mouse_x, py5.mouse_y, py5.pmouse_x, py5.pmouse_y)
    # py5.circle(py5.mouse_x, py5.mouse_y, 15)
    
py5.run_sketch()