import pygame, random, math, palettes

# TODO UI
# TODO Keyboard input
# TODO saturation based on distance


sides = 3
ratio = 0.5
dots_per_frame = 100 # how many dots are being drawn per frame



def main():
    # pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    
    # import random palette and print the name to the console 
    palette = random_palette()
    # palette = palettes.w_b # debugging 
    print(f"Palette used: {palette['name']}")
    
    
    ### screen setup ###
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE) # Main surface where the main polygon is being drawn
    screen_width, screen_height = screen.get_size()
    fractal_surface = pygame.Surface((screen_width, screen_height))# surface where dots are being drawn
    fractal_surface.fill(pygame.Color(palette["bg"])) # its being filled once before the loop as I dont want it to wipe out the dots
    
    center_point = [screen_width /2, screen_height /2]
    current_position = center_point # starting point, can be any
    skip_first_iterations = 500
    iteration = -skip_first_iterations
    
    # game loop
    running = True
    while running:
        for event in pygame.event.get(): # pygame.QUIT event means the user clicked X to close your window
            if event.type == pygame.QUIT:
                running = False
            # Close the window by pressing ESCAPE
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        old_width, old_height = screen_width, screen_height
        screen_width, screen_height = screen.get_size() # keep inside the loop to keep updated
        if old_width != screen_width or old_height != screen_height: # checks if the screen was resized
            fractal_surface = pygame.Surface((screen_width, screen_height))# surface where dots are being drawn
            fractal_surface.fill(pygame.Color(palette["bg"]))
            screen.fill(pygame.Color(palette["bg"]))
            iteration = -skip_first_iterations
            center_point = [screen_width /2, screen_height /2]
            current_position = center_point
            
        radius = min(screen_width, screen_height) * 0.45
        corners = main_polygon(sides, radius, screen_width // 2, screen_height // 2)
        screen.fill(pygame.Color(palette["bg"])) # fill the screen with a color to wipe away anything from last frame
        

        # RENDER HERE
        ###################################################################################
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
        pygame.draw.polygon(screen, pygame.Color(palette["colors"][0]),corners, width=5)
        ###################################################################################
        
        pygame.display.flip() # flip() the display to put your work on screen

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

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