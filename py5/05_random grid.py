import py5

bg = '#000000'
def settings():
    py5.size(1000,1000)
    # py5.full_screen()
    
def setup():
    py5.rect_mode(py5.CENTER)
    py5.background(bg)
    py5.frame_rate((3))
    # py5.no_stroke()
    
def draw():
    py5.translate(50,50)
    py5.background(bg)
    
    for i in range(10):
        for j in range(10):
            rect_size = py5.random_int(85,120)
            py5.rect(j*100,i*100,rect_size,rect_size)
    
    
py5.run_sketch()