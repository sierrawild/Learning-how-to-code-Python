import py5

def settings():
    py5.size(1000,1000)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background("#2990AD")
    py5.fill('#ffffff')
    py5.stroke("#FF4D4D")
    py5.stroke_weight(5)
    
    # py5.no_fill()
    # py5.no_stroke()
    
    ernest = py5.create_font('py5\data\Ernest.ttf', 20)
    py5.text_font(ernest)
    py5.no_loop()
    
def draw():
    global painting, paintmode
    
    print(py5.frame_count)
    
    if py5.mouse_x < palette:
        paintmode = 'select'
    
    if paintmode == "free":
        if painting:
            py5.stroke(brushcolor)
            py5.stroke_cap(brushshape)
            py5.stroke_weight(brushsize)

            py5.line(py5.mouse_x, py5.mouse_y, py5.pmouse_x, py5.pmouse_y)
        
        elif py5.frame_count > 1:
            painting = True
            
   
    black_panel()
    color_swatches()
    brush_preview()
    clear_button()
    

    paintmode = 'free'
    

    
    ### end of draw() ###
    
def brush_preview():
    py5.fill(brushcolor)
    if brushshape == py5.ROUND:
        py5.circle(palette/2, 123, brushsize)
        # py5.circle(py5.mouse_x, py5.mouse_y, brushsize)
    

def color_swatches():
    # color swatches
    for i, swatch in enumerate(swatches):
        sx= int(i%2) * palette/2
        sy= (i//2) * palette/2
        py5.fill(swatch)
        py5.square(sx,sy, palette/2)
        
        
def black_panel():
    # black panel
    py5.no_stroke()
    py5.fill('#000000')
    py5.rect(0,0,palette, py5.height)

def clear_button():
    py5.fill('#ffffff')
    py5.text('CLEAR', 10, py5.height-12)      
            
def mouse_pressed():
    global painting
    # start painting
    if py5.mouse_button == py5.LEFT:
        py5.loop()
        
    # swatch select
    if py5.mouse_button == py5.LEFT and py5.mouse_x < palette and py5.mouse_y < 90:
        global brushcolor
        brushcolor = py5.get_pixels(py5.mouse_x, py5.mouse_y)
        
def mouse_released():
    global painting
    if py5.mouse_button == py5.LEFT:
        painting = False
        py5.no_loop()
        
def mouse_wheel(e):
    # resize the brush
    global brushsize, paintmode
    paintmode = 'select'
    brushsize += e.get_count()
    if brushsize < 3:
        brushsize = 3
    if brushsize > 45:
        brushsize = 45
    py5.redraw()
    
def key_pressed():
    global brushcolor, paintmode
    paintmode = 'select'
    print(py5.key)
    # color swatch shortcuts
    if str(py5.key).isdigit():
        k = int(py5.key) - 1
        if k < len(swatches):
            brushcolor = swatches[k]
            py5.redraw()
    print(str(py5.key) == "c")
    if str(py5.key) == "c":
        py5.background("#2990AD")
    
def mouse_clicked():
    clear_screen()
    
    
def clear_screen():
    if py5.mouse_x < palette and py5.mouse_y > py5.height - 30:
        print("clear")
        py5.background("#2990AD")
        py5.redraw()
        black_panel()
        color_swatches()
        brush_preview()
        clear_button()
    

# Variables
global swatches, brushcolor, brushshape, brushsize, painting, paintmode, palette
swatches = ['#FF0000', '#FF9900', '#FFFF00', 
            '#00FF00', '#0099FF', '#6633FF']
brushcolor = swatches[2]
brushshape = py5.ROUND
brushsize = 3
painting = False
paintmode = 'free'
palette = 60

py5.run_sketch()