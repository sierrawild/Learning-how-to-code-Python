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

    global spacing
    spacing = py5.width / grid_size
    


def draw():
    global infected_cells, grid_not_full
    
    py5.fill(monochrome_palette[1])
    py5.stroke(monochrome_palette[2])

    
    py5.translate(50,50)
    py5.background(monochrome_palette[0])
    
    for j in range(grid_size):
        for i in range(grid_size):
            py5.fill(monochrome_palette[1])
            py5.rect(j*spacing,i*spacing, size, size, 20)
            
    recursive_infection(0)      
    
    # if py5.frame_count % (60 * 0.1) == 0:
    #     random_square = [py5.random_int(0,grid_size-1), py5.random_int(0,grid_size-1)]
        
    #     while random_square in infected_cells and grid_not_full:
    #         random_square = [py5.random_int(0,grid_size-1), py5.random_int(0,grid_size-1)]
    #         if len(infected_cells) >= (grid_size*grid_size):
    #             print("Grid is full")
    #             grid_not_full = False
    #     infected_cells.append(random_square)       
    
    # for i in infected_cells:
    #     py5.fill(monochrome_palette[3])
    #     py5.rect(i[0]*spacing,i[1]*spacing, size+10, 10+size)
            
grid_size = 6   
size = 80
infected_cells = []
grid_not_full = True   

def recursive_infection(n):
    global infected_cells
    if n > 36:
        print("Grid is full")
        return
    else:
        # if py5.frame_count % (60 * 0.1) == 0:
            
        random_square = [py5.random_int(0,grid_size-1), py5.random_int(0,grid_size-1)]
        while random_square in infected_cells:
            random_square = [py5.random_int(0,grid_size-1), py5.random_int(0,grid_size-1)]
        infected_cells.append(random_square)
        for i in infected_cells:
            py5.fill(monochrome_palette[3])
            py5.rect(i[0]*spacing,i[1]*spacing, size+10, 10+size)
        
        recursive_infection(n+1)
        

py5.run_sketch()