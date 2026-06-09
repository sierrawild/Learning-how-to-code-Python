import os
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)


import  sys
from PIL import Image, ImageOps


# if len(sys.argv) < 3:
#     sys.exit("To few command line arguments")
# if len(sys.argv) > 3:
#     sys.exit("To many command line arguments")


# input_file = sys.argv[1]
# output_file = sys.argv[2]

shirt_img = "shirt.png"
input_file = "before1.jpg"
output_file = 'output_img.jpg'
file_name, file_format = output_file.split(".")

if not input_file.endswith('jpg') and output_file.endswith('jpg') or\
    not input_file.endswith('jpeg') and output_file.endswith('jpeg') or\
    not input_file.endswith('png') and output_file.endswith('png'):
        sys.exit('Not an image file')
        
try:
    with Image.open(shirt_img) as shirt:
        width, height = shirt.size
        # print(f'{width=}{height=}')
        with Image.open(input_file) as img:
            img = ImageOps.fit(img, size=(width,height))
            
            
            # combining images
            img.paste(shirt,box=(0,0,width,height), mask=shirt)
            img.save(output_file)
        
    
except FileExistsError:
    sys.exit('file not found')