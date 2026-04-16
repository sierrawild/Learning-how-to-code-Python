import py5

# Variables (define at module level, no 'global' keyword here)
swatches = ['#FF0000', '#FF9900', '#FFFF00', 
            '#00FF00', '#0099FF', '#6633FF']
brushcolor = swatches[2]
brushshape = py5.ROUND
brushsize = 3
painting = False
paintmode = 'free'
palette = 60

def settings():
    py5.size(1000, 1000)
    # py5.full_screen()
    
def setup():
    py5.frame_rate(60)
    
    py5.background('#000000')
    py5.fill('#ffffff')
    py5.stroke("#FF4D4D")
    py5.stroke_weight(5)
    
    # py5.no_fill()
    # py5.no_stroke()
    
    ernest = py5.create_font('py5/data/Ernest.ttf', 20)  # Use forward slashes
    py5.text_font(ernest)
    py5.no_loop()
    
def draw():
    global painting  # Declare global only when modifying
    
    print(py5.frame_count)
    
    if paintmode == "free":
        if painting:
            py5.stroke(brushcolor)
            py5.stroke_cap(brushshape)
            py5.stroke_weight(brushsize)
            py5.line(py5.mouse_x, py5.mouse_y, py5.pmouse_x, py5.pmouse_y)
        
def mouse_pressed():
    global painting  # Declare when modifying
    if py5.mouse_button == py5.LEFT:
        # painting = True  # Start painting immediately
        py5.loop()
        
def mouseReleased():
    global painting  # Declare when modifying
    if py5.mouse_button == py5.LEFT:
        painting = False
        py5.no_loop()

py5.run_sketch()