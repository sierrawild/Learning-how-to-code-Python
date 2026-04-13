import py5

# https://py5coding.org/reference/sketch_rect.html

'''
This is a example file explaining py5 basic shapes
'''
x = 100

def settings():
    py5.size(1000,1000)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    py5.background("#2B2B2B")
    py5.fill("#ffffff")
    py5.stroke("#FF7171")
    
    
    ### RECT MODE'S ###   
    # The default mode is rect_mode(CORNER), which interprets the first two parameters of rect() as the upper-left corner of the shape, while the third and fourth parameters are its width and height.
    py5.rect_mode(py5.CORNER)
    
    # rect_mode(CORNERS) interprets the first two parameters of rect() as the location of one corner, and the third and fourth parameters as the location of the opposite corner.
    py5.rect_mode(py5.CORNERS)
    
    # rect_mode(CENTER) interprets the first two parameters of rect() as the shape’s center point, while the third and fourth parameters are its width and height.
    py5.rect_mode(py5.CENTER)
    
    # rect_mode(RADIUS) also uses the first two parameters of rect() as the shape’s center point, but uses the third and fourth parameters to specify half of the shapes’s width and height.
    py5.rect_mode(py5.RADIUS)
    
    # We will use default mode for this example
    py5.rect_mode(py5.CENTER) 
    
    # text settings
    py5.text_align(py5.CENTER)
    py5.text_size(20)
    
    
def draw():
    # standard rect
    py5.stroke_weight(5)
    py5.rect(py5.width * 0.2,py5.height * 0.25, 100, 150)
    
    py5.text('Standard rect', py5.width * 0.2, py5.height * 0.1)
    
    # standard rect with thick border
    py5.stroke_weight(50)
    py5.rect(py5.width * 0.4,py5.height * 0.25, 100, 150)
    
    py5.text('Standard rect\nwith thick border', py5.width * 0.4, py5.height * 0.1)
    
    # standard rect with rounded corners
    py5.stroke_weight(5)
    py5.rect(py5.width * 0.6,py5.height * 0.25, 100, 150, 25)
    
    py5.text('Rounded corners', py5.width * 0.6, py5.height * 0.1)
    
    # standard rect with rounded corners
    py5.stroke_weight(5)
    py5.no_fill()
    py5.rect(py5.width * 0.8,py5.height * 0.25, 100, 150, 25)
    
    py5.text('no_fill', py5.width * 0.8, py5.height * 0.1)
    
    
    # Rounded corners
    py5.stroke_weight(10)
    py5.no_fill()
    
    # Top left
    py5.rect(py5.width * 0.2,py5.height * 0.75, 100, 150, 50,0,0,0)
    
    py5.text('Top Left', py5.width * 0.2, py5.height * 0.65)
    
    # Top right
    py5.rect(py5.width * 0.4,py5.height * 0.75, 100, 150, 0,50,0,0)
    
    py5.text('Top Right', py5.width * 0.4, py5.height * 0.65)
    
    # Bottom right
    py5.rect(py5.width * 0.6,py5.height * 0.75, 100, 150, 0,0,50,0)
    
    py5.text('Bottom Right', py5.width * 0.6, py5.height * 0.65)
    
    # Bottom left
    py5.rect(py5.width * 0.8,py5.height * 0.75, 100, 150, 0,0,0,50)
    
    py5.text('Bottom Left', py5.width * 0.8, py5.height * 0.65)
    
    
py5.run_sketch()


'''
# SIGNATURE
note: rect() do not support keyword arguments

Claude:
rect(x, y, width, height, [radius])
# or
rect(x, y, width, height, [tl, tr, br, bl])  # top-left, top-right, bottom-right, bottom-left


Documentation:
rect(
    a: float,  # x-coordinate of the rectangle by default
    b: float,  # y-coordinate of the rectangle by default
    c: float,  # width of the rectangle by default
    d: float,  # height of the rectangle by default
    /,
) -> None

rect(
    a: float,  # x-coordinate of the rectangle by default
    b: float,  # y-coordinate of the rectangle by default
    c: float,  # width of the rectangle by default
    d: float,  # height of the rectangle by default
    r: float,  # radii for all four corners
    /,
) -> None

rect(
    a: float,  # x-coordinate of the rectangle by default
    b: float,  # y-coordinate of the rectangle by default
    c: float,  # width of the rectangle by default
    d: float,  # height of the rectangle by default
    tl: float,  # radius for top-left corner
    tr: float,  # radius for top-right corner
    br: float,  # radius for bottom-right corner
    bl: float,  # radius for bottom-left corner
    /,
) -> None
'''
