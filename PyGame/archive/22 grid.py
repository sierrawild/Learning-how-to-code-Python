import pygame

pygame.init()

width = 1000
height = 1000

rec_size = 40

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

time = 0
square_color = ["#FFFFFF","#97FFD0", "#A397FF", "#FFFC97", "#EE97FF", "#FFA797"]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    color = square_color[int(time/60)]
    for j in range(int(height/ rec_size)):
        for i in range(int(width/rec_size)):
            if i % 2 == 0 and j % 2 == 0:
                pygame.draw.rect(screen, color, (rec_size * i, rec_size * j, rec_size, rec_size))
            if i % 2 != 0 and j % 2 != 0:
                pygame.draw.rect(screen, color, (rec_size * i, rec_size * j, rec_size, rec_size))
        
    pygame.display.flip()

    time += 1
    if time == 60 * 6:
        time = 0
        
    # print(f"{color=}\n{int(time/60)} \n\n {time=}")
        
    clock.tick(60)
    

pygame.quit()
