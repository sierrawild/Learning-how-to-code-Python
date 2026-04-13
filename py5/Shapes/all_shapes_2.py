import py5

def settings():
    py5.size(1000,1000)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    py5.background('#000000')
    
    py5.rect_mode(py5.CENTER)


def shapes(x,y,size):
    magnifier = 150
    py5.quad(x-50,y-50, x+50,y-60, x+30,y+45,x-40,y+55)  
    py5.rect(x,y+magnifier, size,size)
    py5.square(x,y+magnifier*2, size)
    
    py5.line(x-50,y+magnifier*3, x+50, y+magnifier*2.8)
    
    py5.triangle(x, y+magnifier*4-50, x+50, y+magnifier*4+50, x-90, y+magnifier*4+50,)

def draw():
    
    py5.text_align(py5.CENTER)

    py5.fill('#ffffff')
    py5.stroke("#FF4D4D")
    py5.stroke_weight(5)
    
    shapes(py5.width* 0.25,100,100)
    
    
    py5.no_fill()
    shapes(py5.width* 0.50,100,100)
    
    
    py5.fill('#ffffff')
    py5.no_stroke()
    shapes(py5.width* 0.75,100,100)
    
py5.run_sketch()