import sys, os, py5

base_path = None

def initialize_directory(folder_name, bottom_limit):
    global base_path
    sketch_name = os.path.splitext(os.path.basename(sys.argv[0]))[0] # Get the sketch filename
    base_path = f"D:/VIDEO/py5/{sketch_name}/{folder_name}/"
    os.makedirs(base_path, exist_ok = True)
    print(f'Files will save to: {base_path}frame_00XX.png')
    print(f'Saving started at frame: {bottom_limit}')
    

def save_img(folder_name='0', top_limit=1000, bottom_limit=1):
    
    if base_path == None:
        initialize_directory(folder_name, bottom_limit)
    
    
    # Early return - skip everything if outside save range
    if py5.frame_count < bottom_limit or py5.frame_count > top_limit:
        return
    
    frame_no_padded = str(py5.frame_count).zfill(4)
    
    py5.save_frame(f'{base_path}frame_{frame_no_padded}.png')  
        
    if top_limit == py5.frame_count:
        print(f'Saving stopped at frame: {top_limit}')
        return 