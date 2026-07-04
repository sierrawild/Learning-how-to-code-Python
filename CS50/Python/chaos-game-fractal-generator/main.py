import asyncio
import pygame, random, math, palettes

async def main():
    ### variables
    paused = False
    border = True
    hide = False
    sides = 3
    ratio = 0.5
    dots_per_frame = 50 # how many dots are being drawn per frame
    speed_adjustment = int(dots_per_frame / 2) # how much speed is added/subtracted using arrows
    skip_first_iterations = 500 # helps stabilize the pattern before its drawn 
    iteration = -skip_first_iterations
    frames = 30
    
    ### pygame setup ###
    pygame.init()
    pygame.display.set_caption("Chaos Game Fractal Generator")
    clock = pygame.time.Clock()
    
    ### import random palette
    palette = random_palette()
    
    ### font ###
    font_size = 24
    font = pygame.font.Font(None, font_size)
    font_paused = pygame.font.Font(None, 50)
    backdrop_w, backdrop_h = 0, 0
    
    ### screen setup ###
    screen = pygame.display.set_mode((1600, 900)) # Main surface where the main polygon is being drawn
    screen_width, screen_height = screen.get_size()
    fractal_surface = pygame.Surface((screen_width, screen_height))# surface where dots are being drawn
    fractal_surface.fill(pygame.Color(palette["bg"])) # its being filled once before the loop as I dont want it to wipe out the dots
    
    center_point = [screen_width /2, screen_height /2]
    current_position = center_point # starting point, can be any
    
    ### main loop ###
    running = True
    while running:
            
        # variables inside the loop to update after screen resize
        radius = min(screen_width, screen_height) * 0.45
        corners = main_polygon(sides, radius, screen_width // 2, screen_height // 2)
        ### 
        
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
                
                # border
                elif event.key == pygame.K_b:
                    border = not border
                    
                # hide
                elif event.key == pygame.K_h:
                    hide = not hide
                    
                # number of sides
                elif event.key == pygame.K_UP:
                    sides = clamp(sides + 1, 3, 42)
                    
                elif event.key == pygame.K_DOWN:
                    sides = clamp(sides - 1, 3, 42)
                    
                # speed
                
                elif event.key == pygame.K_LEFT:
                    dots_per_frame = clamp(dots_per_frame - speed_adjustment, 1, 100000)
                    
                elif event.key == pygame.K_RIGHT:
                    dots_per_frame = clamp(dots_per_frame + speed_adjustment, 1, 100000)
                    
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
        ### Drawing dots
        if not paused:
            for _ in range(dots_per_frame):
                # calculating point
                target_index = random.randrange(len(corners))
                target = corners[target_index]
                new_position = lerp2d(current_position, target, ratio)
                current_position = new_position
                
                # distance for color change
                distance_from_0 = distance(center_point, current_position)
                normalized_distance = distance_from_0 / radius
                normalized_distance = clamp(normalized_distance, 0.0, 1.0) # clamping the value between 0 and 1
                
                # drawing
                iteration += 1
                if iteration > 0: # this skips some iterations so the pattern can stabilize before its being drawn
                    dot_color = pygame.Color(palette["colors"][target_index % len(palette["colors"])])
                
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

        if paused:
            pause_surface = font_paused.render("Paused", antialias=True, color=palette["colors"][0])
            paused_rect = pause_surface.get_rect()
            paused_rect.center = (screen_width/2, screen_height * 0.9) 

            screen.blit(pause_surface, paused_rect)
                
        
        # main polygon
        if border:
            pygame.draw.polygon(screen, pygame.Color(palette["colors"][0]),corners, width=5)
        
        if not hide:
            ### Text and UI ###
            
            # panel 1        
            x1, y1 = 20, 20
            padding = 20
            line_spacing = font_size
            
            pygame.draw.rect(screen, palette["colors"][0], (x1,y1, backdrop_w + padding * 2, backdrop_h + padding), width=5, border_radius= 20) # backdrop
            
            shape = get_polygon_name(sides)
            text = ['CHAOS GAME',
                    'Fractal Generator',
                    f'',
                    shape,
                    f'',
                    f'Ratio: {ratio:.2f}',
                    f'No of sides: {sides}',
                    f'Dots drawn: {number_formatting(iteration)}',
                    f'Dots per frame: {number_formatting(dots_per_frame)}',
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
                    'H','hide UI',
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
        
        
        pygame.display.flip()
        await asyncio.sleep(0)
        

        clock.tick(frames)  # limits FPS 

    
def reset_fractal(fractal_surface, palette, skip_first_iterations):
    '''Redraws a surface, returns skipped iterations so iterations can be reset as well'''
    fractal_surface.fill(pygame.Color(palette["bg"]))
    return -skip_first_iterations
    
def number_formatting(number):
    '''Formats larger numbers as the number of dots on the screen will become very large very quickly'''
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
        return str(number)
    
def get_polygon_name(sides):
    '''Gets the name of the polygon based on the number of its sides'''

    shape_names = {
    "3": "Sierpinski triangle",
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
        return shape_names['n-gon']
    else:
        return shape_names[str(sides)]

def clamp(value, min_v, max_v):
    '''Clamping given value between min and max value'''
    return max(min_v, min(max_v, value))
  
def color_value_adjustment(min_v, max_v, normalized_distance):
    '''Sets min and max value for the color channel'''
    value_range = max_v - min_v
    return min_v + normalized_distance * value_range

def distance(center_point, current_position):
    '''Calculates distance between two points'''
    x = center_point[0] - current_position[0]
    y = center_point[1] - current_position[1]
    return math.sqrt(x**2+y**2)

def lerp2d(current_point,chosen_vertex,distance_traveled):
    """Linear interpolation for 2d point. Expects 2 tuples of 2 coordinates, x and y. Returns new point based on distance traveled"""
    a = (current_point[0]+(chosen_vertex[0]-current_point[0]) * distance_traveled)
    b = (current_point[1]+(chosen_vertex[1]-current_point[1]) * distance_traveled)
    return (a, b)
    
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
    asyncio.run(main())