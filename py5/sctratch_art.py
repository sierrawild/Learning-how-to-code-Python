import py5

def settings():
    py5.size(800,400)
    
def setup():
    py5.frame_rate(120)
    py5.background('#000000')
    py5.stroke('#ffffff')
    py5.fill('#ffffff')

def draw():
    py5.stroke_weight(15)
    py5.color_mode(py5.HSB, 360,100,100)
    h = py5.mouse_x * 360.0 / py5.width
    s = py5.mouse_y * 100.0 / py5.height
    b = 100
    py5.stroke(h,s,b)
    if py5.is_mouse_pressed and py5.mouse_button == py5.LEFT:
        py5.line(py5.mouse_x, py5.mouse_y, py5.pmouse_x, py5.pmouse_y)
    # py5.circle(py5.mouse_x, py5.mouse_y, 15)
    
py5.run_sketch()