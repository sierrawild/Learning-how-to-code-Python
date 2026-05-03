import py5, palette

# Variables

W, H = 1000, 1000
SIDES = 3
RATIO = 0.5
''' Perfect ratios according to wikipedia
Triangle    3   0.5
Carpet      4   2/3 but I find better results going bit above 0.5
Pentagon    5   0.618(golden ratio related)
Hexagon     6   0.667(2/3)
Octagon     8   0.707
'''

RADIUS = W * 0.47
p = palette.random_palette()

def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(5)
    
    
    py5.no_fill()
    # py5.no_stroke()
    
def draw():
    global current_pos
    # py5.background(*p['bg'])
    
    py5.push_matrix()
    py5.translate(W/2, H/2)
    py5.rotate(py5.frame_count * 0.001)
    # draw_main_polygon()
    
    for _ in range(1000):
        draw_dot()
    
    
    
    py5.pop_matrix()

def draw_dot():
    global current_pos
    new_point = chaos_step(current_pos, corners, RATIO)
    current_pos = new_point['new_point']
    
    # manage colors
    target = new_point['target']
    target_index = (corners.index(target) + 1) % len(p['colors']) 
    py5.stroke(*p['colors'][target_index])
    
    py5.point(current_pos[0], current_pos[1])

    
    
def main_polygon(sides, radius):
    corners = []
    for i in range(sides):
        angle = (2* py5.PI * i / sides) - py5.PI / 2
        x = radius * py5.cos(angle)
        y = radius * py5.sin(angle)
        corners.append((x,y))
    return corners


def draw_main_polygon():
    py5.begin_shape()
    for i in corners:
        py5.vertex(i)
    py5.end_shape(py5.CLOSE)
    
    
def chaos_step(current_pos, corners, ratio):
    target = py5.random_choice(corners)
    new_x = current_pos[0] + (target[0] - current_pos[0]) * ratio
    new_y = current_pos[1] + (target[1] - current_pos[1]) * ratio
    return {'new_point': (new_x,new_y), 'target': target}



corners = main_polygon(SIDES, RADIUS) 
current_pos = py5.random_choice(corners)

py5.run_sketch()