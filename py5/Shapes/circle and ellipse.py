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
    
    # text
    py5.text_align(py5.CENTER)
    py5.text_size(20)
    
def draw():
    
    py5.fill('#ffffff')
    py5.stroke("#FF4D4D")
    py5.stroke_weight(5)
    
    
    # standard circle
    py5.stroke_weight(5)
    py5.circle(100,100,100)
    py5.ellipse(100,350, 100,50)
    
    py5.text('Standard', 100, 200)
    
    # thick border
    py5.stroke_weight(25)
    py5.circle(250,100,100)
    py5.ellipse(250,350, 100,50)
    
    py5.text('Thick border', 250, 200)
    
    # no fill
    py5.no_fill()
    py5.stroke_weight(5)
    py5.circle(400,100,100)
    py5.ellipse(400,350, 100,50)
    
    py5.text('no_fill', 400, 200)
    
    # no border
    py5.fill('#ffffff')
    py5.no_stroke()
    py5.circle(550,100,100)
    py5.ellipse(550,350, 100,50)
    
    py5.text('no_stroke', 550, 200)
    
    
py5.run_sketch()