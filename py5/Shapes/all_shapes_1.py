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
    py5.rect(x,y, size,size)
    py5.circle(x, y + magnifier, size)
    py5.ellipse(x,y + magnifier*2, size,size/2)
    py5.arc(x,y + magnifier * 3, size, size*0.7, 0,py5.PI+1, py5.PIE)    
    py5.arc(x,y + magnifier * 4, size, size*0.7, 0,py5.PI+1, py5.OPEN) # default   
    py5.arc(x,y + magnifier * 5, size, size*0.7, 0,py5.PI+1, py5.CHORD)    

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