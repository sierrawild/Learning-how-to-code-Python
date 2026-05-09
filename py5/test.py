import py5

def setup():
    py5.size(400, 400)

def draw():
    py5.background(20)
    
    # Oscillate between 50 and 350
    x = py5.remap(py5.sin(py5.frame_count * 0.05), -1, 1, 50, 350)
    
    py5.circle(x, 200, 30)

py5.run_sketch()