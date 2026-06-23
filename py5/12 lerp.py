import py5

x = 100.0
y = 100.0
target_x = 0.0
target_y = 0.0

def setup():
    py5.size(400, 400)
    py5.no_stroke()

def draw():
    global x, y, target_x, target_y
    py5.background(30)
    
    # Update target coordinates to current mouse position
    target_x = py5.mouse_x
    target_y = py5.mouse_y
    
    # Linearly interpolate between current position and target
    x = py5.lerp(x, target_x, 0.05)
    y = py5.lerp(y, target_y, 0.05)
    
    # Draw the smoothly moving ellipse
    py5.fill(255, 100, 150)
    py5.ellipse(x, y, 40, 40)

py5.run_sketch()