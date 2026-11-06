import pygame

# CONSTANTS
WIDTH, HEIGHT = 1280, 720
# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Drag')
clock = pygame.time.Clock()
dt = 0

cube_rec = pygame.Rect(0,0,100,100)
cube_rec.center = (WIDTH/2, HEIGHT/2)

mouse_pressed = False
mouse_pos = (0,0)
running = True
can_drag = False
mouse_offset = (0,0)

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Close the window by pressing ESCAPE
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                
        # mouse button handling
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True
            mouse_pos = event.pos
            if cube_rec.collidepoint(mouse_pos):
                can_drag = True
                mouse_offset = pygame.Vector2(cube_rec.center) - pygame.Vector2(mouse_pos) 
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_pressed = False
            can_drag = False
            mouse_offset = (0,0)


    ### UPDATE ###
    mouse_pos = pygame.mouse.get_pos()
    mouse_pos = pygame.Vector2(mouse_pos) + mouse_offset
    
    
    if can_drag:
        cube_rec.center = mouse_pos
        
    ### DRAW ###
    screen.fill("#AEF1AA") # fill the screen with a color to wipe away anything from last frame

    pygame.draw.rect(screen, 'red', cube_rec,0, 16)

    pygame.display.flip()     # put your work on screen
    dt = clock.tick(60) / 1000 # limits FPS to 60
    
pygame.quit()