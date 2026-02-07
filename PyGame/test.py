import pygame
import math
import random

pygame.init()

width = 960
height = 960

spacing = 60
rec_size = 40

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

time = 0
square_color = ["#FFFFFF","#97FFD0", "#A397FF", "#FFFC97", "#EE97FF", "#FFA797"]

# Create random offsets for each square
num_squares_x = int(width/spacing)
num_squares_y = int(height/spacing)
offsets = []
for j in range(num_squares_y):
    row = []
    for i in range(num_squares_x):
        # Random phase and speed for each square
        offset_data = {
            'phase_x': random.uniform(0, math.pi * 2),
            'phase_y': random.uniform(0, math.pi * 2),
            'speed_x': random.uniform(0.02, 0.05),
            'speed_y': random.uniform(0.02, 0.05),
            'amplitude': random.uniform(5, 15)  # How far they float
        }
        row.append(offset_data)
    offsets.append(row)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    color = square_color[int(time/60)]
    
    for j in range(num_squares_y):
        for i in range(num_squares_x):
            if i % 2 == 0 and j % 2 == 0 or i % 2 != 0 and j % 2 != 0:
                # Get this square's offset data
                data = offsets[j][i]
                
                # Calculate floating offset using sine waves
                offset_x = math.sin(time * data['speed_x'] + data['phase_x']) * data['amplitude']
                offset_y = math.cos(time * data['speed_y'] + data['phase_y']) * data['amplitude']
                
                # Draw with offset
                x = spacing * i + offset_x
                y = spacing * j + offset_y
                pygame.draw.rect(screen, color, (x, y, rec_size, rec_size))
        
    pygame.display.flip()

    time += 1
    if time == 60 * 6:
        time = 0
        
    clock.tick(60)

pygame.quit()