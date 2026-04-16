import py5

def settings():
    py5.size(1000,1000)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background('#000000')
    py5.fill('#ffffff')
    py5.stroke("#FF4D4D")
    py5.stroke_weight(5)
    
    # py5.no_fill()
    # py5.no_stroke()
    
    ernest = py5.create_font('py5\data\Ernest.ttf', 20)
    py5.text_font(ernest)
    
def draw():
    pass
    

    
# Variables
global swatches, brushcolor, brushshape, brushsize, painting, paintmode, palette
swatches = ['#FF0000', '#FF9900', '#FFFF00', 
            '#00FF00', '#0099FF', '#6633FF']
brushcolor = swatches[2]
brushshape = "ROUND"
brushsize = 3
painting = False
paintmode = 'free'
palette = 60

py5.run_sketch()