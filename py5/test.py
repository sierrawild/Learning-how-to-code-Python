import py5

def settings():
    py5.size(1000,1000)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    # py5.no_fill()
    # py5.no_stroke()
    
    py5.background('#000000')
    py5.fill('#ffffff')
    py5.stroke("#FF4D4D")
    py5.stroke_weight(5)
    
    
def draw():
    py5.background('#FF0000')  # red
    
    py5.background('#0000FF')  # blue
    

    
# Variables
global x, y, size
x = 1
y = 2
size = 100

py5.run_sketch()