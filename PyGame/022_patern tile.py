import pygame

# pygame setup
pygame.init()
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()




def dr_K_patter(color,x,y,size):
    size_s = size * 0.3
    border_width = int(size * 0.02)
    # corners
    pygame.draw.rect(screen,color, (x,y,size_s,size_s), border_width) # left top
    pygame.draw.rect(screen,color, (x + size - size_s,y,size_s,size_s), border_width) # right top
    pygame.draw.rect(screen,color, (x,y + size - size_s,size_s,size_s), border_width) # left bottom
    pygame.draw.rect(screen,color, (x + size - size_s,y + size - size_s,size_s,size_s), border_width) # right bottom

    # corner leafs 
    radius = int(size * 0.1)
    offset = size_s * 0.5
    pygame.draw.rect(screen,color, (x + offset,y + offset,size_s,size_s), border_width, border_top_right_radius=radius, border_bottom_left_radius=radius) # left top
    pygame.draw.rect(screen,color, ((x + size - size_s) - offset,y + offset,size_s,size_s), border_width, border_top_left_radius=radius, border_bottom_right_radius=radius) # right top
    pygame.draw.rect(screen,color, (x + offset,y - offset + size - size_s,size_s,size_s), border_width, border_top_left_radius=radius, border_bottom_right_radius=radius) # left bottom
    pygame.draw.rect(screen,color, (x - offset + size - size_s,y - offset + size - size_s,size_s,size_s), border_width, border_top_right_radius=radius, border_bottom_left_radius=radius) # right bottom
    
    
    pygame.draw.rect(screen,color, (x,y,size,size), border_width) # main
    s = size * 0.9
    ss = size * 0.05
    pygame.draw.rect(screen, color, (x+ss,y+ss, s, s), border_width) # main small
    pygame.draw.rect(screen, color, (x + size/2 - size_s/2,y + size/2 - size_s/2, size_s, size_s), border_width) # middle


def lerp(a,b,t):
    return a + (b-a) * t 


counter = 0
up = True

min_size = 100
max_size = 200

current_size = min_size
target = max_size

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
    
    if up:
        target = max_size
    else:
        target = min_size
        
    current_size = lerp(current_size, target, 0.1)
    
    off = 50
    for i in range(6):
        for j in range(3):
            dr_K_patter('#ffffff',off + (200 * i),off + (200 * j),current_size)
    
    if up:
        counter += 1
    else:
        counter -=1
        
    if counter > 100:
        up = False
    elif counter < 0:
        up = True
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()