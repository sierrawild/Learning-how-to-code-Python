import pygame, random, math, colorsys

pygame.init()

# colors
COLOR_THEME_DEFAULT = {
    "bg": (246, 214, 214),
    "1": (246, 247, 196),
    "2": (161, 238, 189),
    "3": (123, 211, 234),
}

# Surfaces
# screen = pygame.display.set_mode((0, 0)) # production
screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE) # development
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()

fractal_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
fractal_surface.fill(COLOR_THEME_DEFAULT["bg"])



clock = pygame.time.Clock()


# functions

def main_polygon(sides, radius, center_x, center_y):
    corners = []
    for i in range(sides):
        angle = (2* math.pi * i / sides) - math.pi / 2
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        corners.append((x,y))
    return corners

def random_color():
    return (random.randint(10, 240), random.randint(10,245), random.randint(0,230))

def chaos_step(current_pos, corners, ratio):
    target = random.choice(corners)
    new_x = current_pos[0] + (target[0] - current_pos[0]) * ratio
    new_y = current_pos[1] + (target[1] - current_pos[1]) * ratio
    return (new_x, new_y)

# Polygon settings
SIDES = 8
RATIO = 0.7
RADIUS = min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.4
dots_per_frame = 100 # how many dots are being drawn per frame
saved_speed = dots_per_frame
corners = main_polygon(SIDES, RADIUS, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
current_pos = random.choice(corners)
dot_color = random_color()

running = True
while running:
    # event loop handling (closing the window with x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # key input 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: running = False # exit by pressing ESCAPE
            elif event.key == pygame.K_UP: 
                SIDES = min(100, SIDES + 1)
                corners = main_polygon(SIDES, RADIUS, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            elif event.key == pygame.K_DOWN: 
                SIDES = max(3, SIDES - 1)
                corners = main_polygon(SIDES, RADIUS, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            elif event.key == pygame.K_RIGHT:
                dots_per_frame += 10
            elif event.key == pygame.K_LEFT:
                dots_per_frame = max(1, dots_per_frame - 10)
            
            # pausing unpausing the drawing 
            elif event.key == pygame.K_SPACE and dots_per_frame !=0: 
                saved_speed = dots_per_frame
                dots_per_frame = 0
            elif event.key == pygame.K_SPACE and dots_per_frame == 0:
                dots_per_frame = saved_speed
    # TODO Continiue adding shortcuts
    # TODO Simple UI showing variables
    # TODO colorsys for better colors. Maybe implement different colors 
    # for different vertexes and then change them clockwise so it looks like the colors are spining 
    

    # dot loop. How Many dots are drawn each frame
    for i in range(dots_per_frame):
        target = chaos_step(current_pos,corners, RATIO)
        current_pos = target
        pygame.draw.circle(fractal_surface, dot_color, target, 1)
    
    screen.blit(fractal_surface, (0,0))
    pygame.draw.polygon(screen, COLOR_THEME_DEFAULT["3"], corners, 1)
    
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()