import sys, os, py5


def save_img(folder_name='0', top_limit=1000, bottom_limit=0):
    # Get the sketch filename without extension
    sketch_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    base_path = f"D:/VIDEO/py5/{sketch_name}/{folder_name}/"
    no_frame = str(py5.frame_count).zfill(6)
    
    # create directory if doesn't exist
    os.makedirs(base_path, exist_ok = True)
    
    # print instruction 
    if py5.frame_count == 1:
        print(f'Files will save to: {base_path}frame_{no_frame}.png')
    
    # save the image
    if py5.frame_count <= top_limit and py5.frame_count >= bottom_limit:
        py5.save_frame(f'{base_path}frame_{no_frame}.png')   