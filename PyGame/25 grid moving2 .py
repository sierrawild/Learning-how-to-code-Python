import pygame, math, random

pygame.init()

width = 960
height = 960

spacing = 60
rec_size = 40

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

color_time = 0
move_time = 0

square_color = ["#FFFFFF","#97FFD0", "#A397FF", "#FFFC97", "#EE97FF", "#FFA797"]

# random offset for each sqr
num_squares_x = int(width/spacing)
num_squares_y = int(height/spacing)
offset = []

for j in range(num_squares_y):
    row = []
    for i in range(num_squares_x):
        # random phase and speed for each square
        offset_data = {
            "phase_x": random.uniform(0, math.pi * 2),
            "phase_y": random.uniform(0, math.pi * 2),
            "speed_x": random.uniform(0.02, 0.05),
            "speed_y": random.uniform(0.02, 0.05),
            "amplitude": random.uniform(5, 15) # how far they float
        }
        row.append(offset_data)
    offset.append(row)


def draw_sqr(rec_size, screen, color, x, y):
    pygame.draw.rect(screen, color, (x, y, rec_size, rec_size))
    
def draw_dot(size, surface, color, x, y):
    pygame.draw.circle(surface, )

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    color = square_color[int(color_time/60)]
    for j in range(int(height/ spacing)):
        for i in range(int(width/spacing)):
            if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                
                data = offset[j][i]
                
                # calculate floating offset using sine waves
                offset_x =  math.sin(move_time * data["speed_x"] + data["phase_x"]) * data["amplitude"]
                offset_y =  math.cos(move_time * data["speed_y"] + data["phase_y"]) * data["amplitude"]
                
                x = spacing * i + offset_x
                y = spacing * j + offset_y
                draw_sqr(rec_size, screen, color, x, y)
            
    pygame.display.flip()

    color_time += 1
    if color_time == 60 * 6:
        color_time = 0
    move_time += 1

    

        
            
    clock.tick(60)
    

pygame.quit()
