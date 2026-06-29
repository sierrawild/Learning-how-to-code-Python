import pygame, random, math, palettes

sides = 3
ratio = 0.5
dots_per_frame = 100 # how many dots are being drawn per frame



def main():
    # pygame setup
    pygame.init()
    clock = pygame.time.Clock()
    
    # import random palette and print the name to the console 
    palette = random_palette()
    print(f"Palette used: {palette['name']}")
    
    
    ### screen setup ###
    screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE) # Main surface where the main polygon is being drawn
    screen_width, screen_height = screen.get_size()
    fractal_surface = pygame.Surface((screen_width, screen_height))# surface where dots are being drawn
    fractal_surface.fill(palette["bg"]) # its being filled once before the loop as I dont want it to wipe out the dots
    
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
            fractal_surface.fill(palette["bg"])
            screen.fill(palette["bg"])
            iteration = -skip_first_iterations
            current_position = center_point
            
        radius = min(screen_width, screen_height) * 0.45
        corners = main_polygon(sides, radius, screen_width // 2, screen_height // 2)
        screen.fill(palette["bg"]) # fill the screen with a color to wipe away anything from last frame

        # RENDER HERE
        ###################################################################################
        for _ in range(dots_per_frame):
            target = random.choice(corners)
            new_position = lerp2d(current_position, target, ratio)
            current_position = new_position
            
            iteration += 1
            if iteration > 0:
                dot_color = pygame.Color(palette["colors"][corners.index(target)%len(palette["colors"])])
                # dot_color.hsva = (hue, 80, 80)
                pygame.draw.circle(fractal_surface, dot_color, current_position, radius=1)
        
        screen.blit(fractal_surface, (0,0))
        # main polygon
        pygame.draw.polygon(screen, palette["colors"][0],corners, width=5)
        ###################################################################################
        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()



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
    main()