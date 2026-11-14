import colorsys
WIDTH, HEIGHT = 1280, 720

palette = {
    'name': 'default',
    'bg': "#73FBBE",
}

def hex_to_rgb(color):
    hex_color = color.lstrip('#')
    r = int(hex_color[0:2], 16) /255
    g = int(hex_color[2:4], 16) /255
    b = int(hex_color[4:6], 16) /255
    return r, g, b

r, g, b = hex_to_rgb(palette['bg'])

h,s,v = colorsys.rgb_to_hsv(r,g,b)

h_flipped = (h + 0.5) % 1.0

r, g, b = colorsys.hsv_to_rgb(h_flipped, s, v)
palette['1'] = f"#{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}"

print(palette)