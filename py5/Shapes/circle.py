import py5

# https://py5coding.org/reference/sketch_circle.html

def settings():
    py5.size(1000,1000)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    py5.background('#000000')
    py5.fill('#ffffff')
    # py5.no_fill()
    py5.stroke("#FF4D4D")
    py5.stroke_weight(5)
    # py5.no_stroke()
    
def draw():
    
    # standard circle
    py5.stroke_weight(5)
    py5.circle(100,100,100)
    
    # thick border
    py5.stroke_weight(25)
    py5.circle(250,100,100)
    
py5.run_sketch()