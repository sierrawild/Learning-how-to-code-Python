import py5

monochrome_palette = [
    '#005461',
    '#0C7779',
    '#249E94',
    '#3BC1A8',    
    ]



def settings():
    py5.size(1000,1000)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    py5.stroke_weight(5)
    # py5.no_stroke()

    global grid_size, spacing, size, random_square
    grid_size = 6   
    spacing = py5.width / grid_size
    size = 80
    random_square = [py5.random_int(0,grid_size-1), py5.random_int(0,grid_size-1)]
    

def draw():
    global random_square
    py5.fill(monochrome_palette[1])
    py5.stroke(monochrome_palette[2])

    
    py5.translate(50,50)
    py5.background(monochrome_palette[0])
    for j in range(grid_size):
        for i in range(grid_size):
            if j == random_square[0] and i == random_square[1]:
                py5.fill(monochrome_palette[3])
                py5.rect(j*spacing,i*spacing, size+10, 10+size)
            else:
                py5.fill(monochrome_palette[1])
                py5.rect(j*spacing,i*spacing, size, size, 20)
                
    if py5.frame_count % (60 * 1) == 0:
        random_square = [py5.random_int(0,grid_size-1), py5.random_int(0,grid_size-1)]
            
    
py5.run_sketch()