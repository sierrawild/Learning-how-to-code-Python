import py5

def settings():
    py5.size(1000,1000, py5.P3D)
    # py5.full_screen()
    
def setup():
    py5.background('#ffffff')
    py5.frame_rate((60))
    
    
    
def draw():
    py5.translate(py5.width/2, py5.height/2)
    py5.rotate_y(20)
    py5.rotate_x(45)
    py5.box(50,40,100)
    
    
py5.run_sketch()