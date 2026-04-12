import py5

def settings():
    py5.size(500,500)
    
def setup():
    py5.rect_mode(py5.CENTER)

def draw():
    py5.fill('#ff0000')
    py5.rect(py5.width/2,py5.height/2, 200,300)

py5.run_sketch()