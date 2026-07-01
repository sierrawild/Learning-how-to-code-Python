import pygame, random, math, palettes

# TODO Keyboard input





def main():
    ### variables
    paused = False
    border = True
    sides = 3
    ratio = 0.5
    dots_per_frame = 30 # how many dots are being drawn per frame
    
    ### pygame setup ###
    pygame.init()
    clock = pygame.time.Clock()
    
    # import random palette and print the name to the console 
    palette = random_palette()
    ### palette = palettes.w_b # debugging  ###
    print(f"Palette used: {palette['name']}")
    
    ### font ###
    font_size = 24
    font = pygame.font.Font(None, font_size)
    backdrop_w, backdrop_h = 0, 0
    
    ### screen setup ###
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE) # Main surface where the main polygon is being drawn
    screen_width, screen_height = screen.get_size()
    fractal_surface = pygame.Surface((screen_width, screen_height))# surface where dots are being drawn
    fractal_surface.fill(pygame.Color(palette["bg"])) # its being filled once before the loop as I dont want it to wipe out the dots
    
    
    center_point = [screen_width /2, screen_height /2]
    current_position = center_point # starting point, can be any
    skip_first_iterations = 500
    iteration = -skip_first_iterations
    
    ### main loop ###
    running = True
    while running:
        ### resizing the window ###
        old_width, old_height = screen_width, screen_height
        screen_width, screen_height = screen.get_size() # keep inside the loop to keep updated
        if old_width != screen_width or old_height != screen_height: # checks if the screen was resized
            
            fractal_surface = pygame.Surface((screen_width, screen_height))# surface where dots are being drawn
            iteration = reset_fractal(fractal_surface, palette, skip_first_iterations)
            center_point = [screen_width /2, screen_height /2]
            current_position = center_point
        ### 
        
        radius = min(screen_width, screen_height) * 0.45
        corners = main_polygon(sides, radius, screen_width // 2, screen_height // 2)
        screen.fill(pygame.Color(palette["bg"])) # fill the screen with a color to wipe away anything from last frame
        

        # Rendering
        ###################################################################################
        # Drawing dots
        if not paused:
            for _ in range(dots_per_frame):
                # calculating point
                target = random.choice(corners)
                new_position = lerp2d(current_position, target, ratio)
                current_position = new_position
                
                # distance for color change
                distance_from_0 = distance(center_point, current_position)
                normalized_distance = distance_from_0 / radius
                normalized_distance = clamp(normalized_distance, 0.0, 1.0) # clamping the value between 0 and 1
                # print(normalized_distance)
                
                #drawing
                iteration += 1
                if iteration > 0: # this skips some iterations so the pattern can stabilize before its being drawn
                    dot_color = pygame.Color(palette["colors"][corners.index(target)%len(palette["colors"])])
                
                    h,s,v,a = dot_color.hsva
                    
                    # saturation adjustment based on the distance from center of the polygon
                    new_s = s
                    if s != 0:
                        new_s = color_value_adjustment(60,100,normalized_distance)

                    # value adjustment based on the distance from center of the polygon
                    new_v = color_value_adjustment(40,100, normalized_distance)
                    
                    dot_color.hsva = (h,new_s,new_v,a)
                    pygame.draw.circle(fractal_surface, dot_color, current_position, radius=1)

        screen.blit(fractal_surface, (0,0))
        
        # main polygon
        if border:
            pygame.draw.polygon(screen, pygame.Color(palette["colors"][0]),corners, width=5)
        
        
        ### Text and UI ###
        
        # panel 1        
        x1, y1 = 20, 20
        padding = 20
        line_spacing = font_size
        
        
        pygame.draw.rect(screen, palette["colors"][0], (x1,y1, backdrop_w + padding * 2, backdrop_h + padding), width=5, border_radius= 20) # backdrop
        
        shape = get_polygon_name(sides)
        text = ['CHAOS GAME',
                'Fractal creation',
                f'',
                shape,
                f'',
                f'Ratio: {ratio:.2f}',
                f'No of sides: {sides}',
                f'Dots drawn: {number_formatting(iteration)}',
                f"Palette used: {palette['name']}",]
        
        for line in text:
            text_surface = font.render(line, antialias=True, color=palette["colors"][0])
            text_rect = text_surface.get_rect()
            text_rect.topleft = (x1 + padding, y1 + padding)
            screen.blit(text_surface, text_rect)
            y1 += line_spacing
            # backdrop
            text_width, _ = text_surface.get_size()
            if backdrop_w < text_width:
                backdrop_w = text_width
        
        backdrop_h = y1
        
        # panel 2
        
        x2, y2 = x1, y1 + padding * 3
        pygame.draw.rect(screen, palette["colors"][0], (x2,y2, backdrop_w + padding * 2, backdrop_h + padding * 4), width=5, border_radius= 20) # backdrop
        
        text2 = ['CONTROLS',
                'UP:','+1 side',
                'Down:','-1 side',
                'Left:','speed -',
                'Right:','speed +',
                ']','ratio up',
                '[','ratio down',
                'P:','palette',
                'R:','reset',
                'B','border',
                'Space:','pause',]

        for line in enumerate(text2):
            text_surface2 = font.render(line[1], antialias=True, color=palette["colors"][0])
            text2_rec = text_surface2.get_rect()
            if line[0] == 0:
                text2_rec.topleft = (x2 + padding, y2 + padding)
                y2 += line_spacing
            elif line[0] % 2 != 0:
                text2_rec.topleft = (x2 + padding, y2 + padding)
            else:
                text2_rec.topleft = (x2 + 80, y2 + padding)
                y2 += line_spacing
                
            screen.blit(text_surface2, text2_rec)
            # backdrop
            text_width, _ = text_surface2.get_size()
            if backdrop_w < text_width:
                backdrop_w = text_width
        
        
        pygame.display.flip() # flip() the display to put your work on screen
        ###################################################################################
        
        ### Event handling ###
        for event in pygame.event.get(): # pygame.QUIT event means the user clicked X to close your window
            if event.type == pygame.QUIT:
                running = False
            
            ### Key binding ###
            elif event.type == pygame.KEYDOWN:
                
                # Close the window by pressing ESCAPE
                if event.key == pygame.K_ESCAPE: 
                    running = False

                # reset
                elif event.key == pygame.K_r:
                    iteration = reset_fractal(fractal_surface, palette, skip_first_iterations)
                
                # palette
                elif event.key == pygame.K_p:
                    palette = random_palette()
                    iteration = reset_fractal(fractal_surface, palette, skip_first_iterations)
                    
                # pause
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                    print('Paused = ', paused)
                
                # border
                elif event.key == pygame.K_b:
                    border = not border
                    
                # number of sides
                elif event.key == pygame.K_UP:
                    sides = clamp(sides + 1, 3, 42)
                    
                elif event.key == pygame.K_DOWN:
                    sides = clamp(sides - 1, 3, 42)
                    
                # speed
                elif event.key == pygame.K_LEFT:
                    dots_per_frame = clamp(dots_per_frame - 10, 0, 100000)
                    print(f'There are {dots_per_frame} drawn each frame')
                    
                elif event.key == pygame.K_RIGHT:
                    dots_per_frame = clamp(dots_per_frame + 10, 0, 100000)
                    print(f'There are {dots_per_frame} drawn each frame')
                    
                # ratio
                elif event.key == pygame.K_EQUALS:
                    ratio = clamp(ratio + 0.01, 0, 10)
                    
                elif event.key == pygame.K_MINUS:
                    ratio = clamp(ratio - 0.01, 0, 10)
                    
                elif event.key == pygame.K_RIGHTBRACKET:
                    ratio = clamp(ratio + 0.1, 0, 10)
                    
                elif event.key == pygame.K_LEFTBRACKET:
                    ratio = clamp(ratio - 0.1, 0, 10)
            ###
        ###

        clock.tick(30)  # limits FPS to 60

    pygame.quit()
    
def reset_fractal(fractal_surface, palette, skip_first_iterations):
    
    fractal_surface.fill(pygame.Color(palette["bg"]))
    return -skip_first_iterations
    
def number_formatting(number):
    if number < -400:
        return '.'
    elif number < -300:
        return '..'
    elif number < -200:
        return '...'
    elif number < 0:
        return '....'
    elif number >= 1_000_000:
        return f'{number / 1_000_000:.2f} m'
    elif number >= 1_000:
        return f'{number / 1000:.1f} k'
    elif number >= 0:
        return number
    
def get_polygon_name(sides):
    shapeNames = {
    "3": "Sierpiński triangle",
    "4": "Square",
    "5": "Pentagon",
    "6": "Hexagon",
    "7": "Heptagon",
    "8": "Octagon",
    "9": "Nonagon",
    "10": "Decagon",
    "11": "Hendecagon",
    "12": "Dodecagon",
    "13": "Tridecagon",
    "14": "Tetradecagon",
    "15": "Pentadecagon",
    "16": "Hexadecagon",
    "17": "Heptadecagon",
    "18": "Octadecagon",
    "19": "Enneadecagon",
    "20": "Icosagon",
    "n-gon": "n-gon",
    }
    if sides > 20:
        return shapeNames['n-gon']
    else:
        return shapeNames[str(sides)]

def clamp(value, min_v, max_v):
    return max(min_v, min(max_v, value))
  
def color_value_adjustment(min_v, max_v, normalized_distance):
    value_range = max_v - min_v
    return min_v + normalized_distance * value_range

def distance(center_point, current_position):
    x = center_point[0] - current_position[0]
    y = center_point[1] - current_position[1]
    return math.sqrt(x**2+y**2)

def lerp2d(current_point,chosen_vertex,distance_traveled):
    """Linear interpolation for 2d point. Expects 2 tuples of 2 coordinates, x and y. Returns new point based on distance traveled"""
    a = (current_point[0]+(chosen_vertex[0]-current_point[0]) * distance_traveled)
    b = (current_point[1]+(chosen_vertex[1]-current_point[1]) * distance_traveled)
    return (a, b)
    
def lerp(current_point,chosen_vertex,distance_traveled):
    return (current_point[0]+(chosen_vertex[0]-current_point[0]) * distance_traveled)
    
def random_palette():
    '''Return a random palette from list of palettes in a file of the same name'''
    return random.choice(palettes.all_palettes)
    
def main_polygon(sides, radius, center_x, center_y):
    """
    Define base polygon to draw chaos game on.
    Args:
        sides (int): Number of sides of the polygon.
        radius (float): Radius of the polygon.
        center_x (float): Center on X axis.
        center_y (float): Center on Y axis.
    
    Returns:
        list: List of polygon corners
    """
    corners = []
    for i in range(sides):
        angle = (2* math.pi * i / sides) - math.pi / 2
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        corners.append((x,y))
    return corners


if __name__ == "__main__":
    main()