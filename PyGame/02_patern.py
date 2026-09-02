import pygame

# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

size = 500
size_s = size * 0.3
x = (width - size) * 0.5
y = (height - size) * 0.5
border_width = 5

running = True
while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Close the window by pressing ESCAPE
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("#AEF1AA")

    # RENDER YOUR GAME HERE
    
    
    # corners
    pygame.draw.rect(screen,"#FFFFFF", (x,y,size_s,size_s), border_width) # left top
    pygame.draw.rect(screen,"#FFFFFF", (x + size - size_s,y,size_s,size_s), border_width) # right top
    pygame.draw.rect(screen,"#FFFFFF", (x,y + size - size_s,size_s,size_s), border_width) # left bottom
    pygame.draw.rect(screen,"#FFFFFF", (x + size - size_s,y + size - size_s,size_s,size_s), border_width) # right bottom

    # corner leafs 
    radius = 50
    offset = size_s * 0.5
    pygame.draw.rect(screen,"#FFFFFF", (x + offset,y + offset,size_s,size_s), border_width, border_top_right_radius=radius, border_bottom_left_radius=radius) # left top
    pygame.draw.rect(screen,"#FFFFFF", ((x + size - size_s) - offset,y + offset,size_s,size_s), border_width, border_top_left_radius=radius, border_bottom_right_radius=radius) # right top
    pygame.draw.rect(screen,"#FFFFFF", (x + offset,y - offset + size - size_s,size_s,size_s), border_width, border_top_left_radius=radius, border_bottom_right_radius=radius) # left bottom
    pygame.draw.rect(screen,"#FFFFFF", (x - offset + size - size_s,y - offset + size - size_s,size_s,size_s), border_width, border_top_right_radius=radius, border_bottom_left_radius=radius) # right bottom
    
     
    pygame.draw.rect(screen,"#FFFFFF", (x,y,size,size), border_width) # main
    pygame.draw.rect(screen, "#FFFFFF", ((width - size * 0.9)/2,(height - size * 0.9)/2, size * 0.9, size * 0.9), border_width) # main small
    pygame.draw.rect(screen, "#FFFFFF", ((width - size_s)/2,(height - size_s)/2, size_s, size_s), border_width) # middle
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()