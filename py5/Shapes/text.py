import py5

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
    
    ### Print a list of fonts ### 
    fonts = py5.Py5Font.list()
    for font in fonts:
        print(font)
        
    # print all fonts in one block
    # print(py5.Py5Font.list())
    
    global my_font
    my_font = py5.create_font('Comic Sans MS', 35) 
    
    
def draw():
    
    py5.fill("#50FFB0") # set color with fill
    py5.text_align(py5.CENTER) # LEFT   CENTER   RIGHT
    py5.text_size(55) # set size. Works only if I dont specify the size in create_font 
    py5.text_font(my_font)
    
    py5.text('Hello World!', py5.width/2, py5.height/2)
    
    
        
    
py5.run_sketch()

# Common fonts
'''
Arial
Courier New
Times New Roman
Verdana
Georgia
Comic Sans MS
'''
