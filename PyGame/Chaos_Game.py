import pygame, random, math, colorsys

pygame.init()



# screen = pygame.display.set_mode((0, 0)) # production
screen = pygame.display.set_mode((1200, 800)) # development

SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
clock = pygame.time.Clock()


# colors
COLOR_THEME_DEFAULT = {
    "bg": (246, 214, 214),
    "yellow": (246, 247, 196),
    "green": (161, 238, 189),
    "blue": (123, 211, 234),
}

# functions

def main_polygon(sides, radius, center_x, center_y):
    corners = []
    for i in range(sides):
        angle = (2* math.pi * i / sides) - math.pi / 2
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        corners.append((x,y))
    return corners

# Polygon settings
SIDES = 1
RATIO = 0.703
RADIUS = min(SCREEN_WIDTH, SCREEN_HEIGHT) * 0.4
corners = main_polygon(SIDES, RADIUS, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

running = True
while running:
    # event loop handling (closing the window with x)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # key input 
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]: running = False # exit by pressing ESCAPE

    # events
    screen.fill(COLOR_THEME_DEFAULT["bg"])
    
    pygame.draw.polygon(screen, COLOR_THEME_DEFAULT["blue"], corners, 10)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()