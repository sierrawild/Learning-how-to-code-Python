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
    
    if grid_not_full:
        draw_grid()
        
        # wait for time to infect and refine next square to infect        
        if py5.frame_count % (time_to_infect) == 0:
            random_square = [py5.random_int(0,grid_size-1), py5.random_int(0,grid_size-1)]
            
            # check if infected square have been already infected. 
            while random_square in infected_cells and grid_not_full:
                # If square in infected_cell chose another square
                random_square = [py5.random_int(0,grid_size-1), py5.random_int(0,grid_size-1)]
                # if no of infected squares >= to the whole grid, brake the while loop
                if len(infected_cells) >= (grid_size*grid_size):
                    print("Grid is full")
                    grid_not_full = False
            # after all above checks are satisfied, append the list of squares
            infected_cells.append(random_square)       
        
        # draw infected cells
        for i in infected_cells:
            py5.fill(monochrome_palette[3])
            py5.rect(i[0]*spacing,i[1]*spacing, size+10, 10+size)
     
    # reverse infection (heal the cells)   
    if grid_not_full == False:
        py5.background(monochrome_palette[0])
        py5.fill(monochrome_palette[1])
        draw_grid()
        for i in infected_cells:
            py5.fill(monochrome_palette[3])
            py5.rect(i[0]*spacing,i[1]*spacing, size+10, 10+size)
            
        if py5.frame_count % (time_to_infect) == 0:
            infected_cells.pop(-1)
            # check if grid is empty
            if len(infected_cells) == 0:
                print("Grid is empty")
                grid_not_full = True

def draw_grid():
    for j in range(grid_size):
        for i in range(grid_size):
            py5.fill(monochrome_palette[1])
            py5.rect(j*spacing,i*spacing, size, size, 20)
        
        
grid_size = 6   
size = 80
infected_cells = []
grid_not_full = True 
time_to_infect = 10 # 6 = 1s

       

py5.run_sketch()