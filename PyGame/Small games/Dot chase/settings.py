import colorsys, os, pygame
WIDTH, HEIGHT = 1280, 720

pygame.font.init()

# palette
palette = {
    'name': 'default',
    'bg': "#B2FFFE",
}

def hex_to_rgb(color):
    hex_color = color.lstrip('#')
    r = int(hex_color[0:2], 16) /255
    g = int(hex_color[2:4], 16) /255
    b = int(hex_color[4:6], 16) /255
    return r, g, b

def add_color(palette, og_color: str, magnitude: float):
    r, g, b = hex_to_rgb(palette[og_color])
    h,s,v = colorsys.rgb_to_hsv(r,g,b)
    h_flipped = (h + magnitude) % 1.0
    r, g, b = colorsys.hsv_to_rgb(h_flipped, s, v)
    return f"#{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}"

# adding complementary color as 'bg_comp' 
palette['bg_comp'] = add_color(palette, 'bg', 0.5)



# fonts
path = os.path.dirname(__file__)
path = os.path.join(path, 'assets')
font_file = os.path.join(path, 'Minecraft.ttf')

font_score = pygame.font.Font(font_file, 36)