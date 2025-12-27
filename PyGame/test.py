import pygame

pygame.init()

screen = pygame.display.set_mode((1000,1000))

cloud_posX = 500
cloud_posY = 500
cloud_size = 50
cloud_width = 0
cloud_color = "white"

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#94EAFF")
    
    pygame.draw.circle(screen, cloud_color, (cloud_posX, cloud_posY), cloud_size, cloud_width)
    pygame.draw.circle(screen, cloud_color, (cloud_posX + 40, cloud_posY + 30), cloud_size - 10, cloud_width)
    pygame.draw.circle(screen, cloud_color, (cloud_posX + 80, cloud_posY + 15), cloud_size - 5, cloud_width)
    pygame.draw.circle(screen, cloud_color, (cloud_posX + 120, cloud_posY + 25), cloud_size - 10, cloud_width)
    pygame.draw.circle(screen, cloud_color, (cloud_posX + 160, cloud_posY), cloud_size, cloud_width)
 
    pygame.draw.circle(screen, cloud_color, (cloud_posX + 35, cloud_posY - 30), cloud_size + 10, cloud_width)
    pygame.draw.circle(screen, cloud_color, (cloud_posX + 80, cloud_posY - 45), cloud_size + 5, cloud_width)
    pygame.draw.circle(screen, cloud_color, (cloud_posX + 130, cloud_posY - 35), cloud_size - 5, cloud_width)
    
    
    pygame.display.flip()



pygame.quit()