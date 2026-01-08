import pygame, math

pygame.init()
WIDTH = 1280
HEIGHT = 920
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

time = 0


# WAVE settings 
POS_X = 90
AMPLITUDE = 300
CIRCLE_SIZE = 30

# FONT
font = pygame.font.Font(None, 40)


screen.fill("#FFF9C9")

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill("#FFF9C9")
                time = 0

    time += 1
    speed = time * 0.04
    
 
    # ========== BASELINE ==========
    label = font.render("Baseline", True, "#62F6B4")
    screen.blit(label, (POS_X - 40, 20))
    # Formula: y = A * sin(ωt) + offset
    # Standard sine wave with no modifications
    y = AMPLITUDE * math.sin(speed) + HEIGHT / 2
    pygame.draw.circle(screen, "#62F6B4", (POS_X*1, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#4AB987", (POS_X*1, y), CIRCLE_SIZE * 0.5)
    
    
    # ========== AMPLITUDE MODIFICATIONS ==========
    
    label = font.render("Taller", True, "#62C0F6")
    screen.blit(label, (POS_X*2 - 40, HEIGHT - 40))
    # Formula: y = 1.2A * sin(ωt) + offset
    # Taller wave: amplitude increased by 20%
    y = AMPLITUDE * 1.2 * math.sin(speed) + HEIGHT / 2
    pygame.draw.circle(screen, "#62C0F6", (POS_X*2, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#4A85B9", (POS_X*2, y), CIRCLE_SIZE * 0.5)
    
    label = font.render("Damped", True, "#F612C5")
    screen.blit(label, (POS_X*3 - 40, 20))
    # Formula: y = A * e^(-kt) * sin(ωt) + offset
    # Damped wave: amplitude decreases exponentially over time
    y = AMPLITUDE * math.exp(-speed * 0.1) * math.sin(speed) + HEIGHT / 2
    pygame.draw.circle(screen, "#F612C5", (POS_X*3, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#Fbb2C5", (POS_X*3, y), CIRCLE_SIZE * 0.5)
    
    label = font.render("Growing", True, "#d679f5")
    screen.blit(label, (POS_X*4 - 40, HEIGHT - 40))
    # Formula: y = A * (1 - e^(-kt)) * sin(ωt) + offset
    # Growing wave: amplitude increases exponentially over time
    y = AMPLITUDE * (1 - math.exp(-speed * 0.1)) * math.sin(speed) + HEIGHT / 2
    pygame.draw.circle(screen, "#d679f5", (POS_X*4, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#ac2ce8", (POS_X*4, y), CIRCLE_SIZE * 0.5)
    
    
    # ========== PHASE SHIFTS ==========
    
    label = font.render("Starts at top", True, "#EAEAEA")
    screen.blit(label, (POS_X*5 - 40, 20))
    # Formula: y = A * sin(ωt - π/2) + offset
    # Phase shift: starts at top of wave (90° ahead)
    y = AMPLITUDE * math.sin(speed - math.pi/2) + HEIGHT / 2
    pygame.draw.circle(screen, "#FFFFFF", (POS_X*5, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#000000", (POS_X*5, y), CIRCLE_SIZE * 0.5)
    
    label = font.render("Starts at bottom", True, "#000000")
    screen.blit(label, (POS_X*6 - 40, HEIGHT - 40))
    # Formula: y = A * sin(ωt + π/2) + offset
    # Phase shift: starts at bottom of wave (90° behind)
    y = AMPLITUDE * math.sin(speed + math.pi/2) + HEIGHT / 2
    pygame.draw.circle(screen, "#000000", (POS_X*6, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#FFFFFF", (POS_X*6, y), CIRCLE_SIZE * 0.5)
    
    label = font.render("Arbitrary shift", True, "#626EF6")
    screen.blit(label, (POS_X*7 - 40, 20))
    # Formula: y = A * sin(ωt + 2) + offset
    # Arbitrary phase shift by 2 radians (~115°)
    y = AMPLITUDE * math.sin(speed + 2) + HEIGHT / 2
    pygame.draw.circle(screen, "#626EF6", (POS_X*7, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#4A69B9", (POS_X*7, y), CIRCLE_SIZE * 0.5)
    
    
    # ========== FREQUENCY MODIFICATIONS ==========
    
    label = font.render("Faster", True, "#1BC7F7")
    screen.blit(label, (POS_X*8 - 40, HEIGHT - 80))
    # Formula: y = A * sin(1.6ωt) + offset
    # Faster wave: frequency increased by 60% (compressed wave)
    y = AMPLITUDE * math.sin(speed * 1.6) + HEIGHT / 2
    pygame.draw.circle(screen, "#1BC7F7", (POS_X*8, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#81AFE0", (POS_X*8, y), CIRCLE_SIZE * 0.4)
    
    label = font.render("Slower", True, "#62C7F6")
    screen.blit(label, (POS_X*9 - 40, 80))
    # Formula: y = A * sin(ωt/2) + offset
    # Slower wave: frequency halved (stretched wave)
    y = AMPLITUDE * math.sin(speed / 2) + HEIGHT / 2
    pygame.draw.circle(screen, "#62C7F6", (POS_X*9, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#2DA5DD", (POS_X*9, y), CIRCLE_SIZE * 0.5)
    
    
    # ========== COMPLEX WAVEFORMS ==========
    
    label = font.render("Harmonic", True, "#E748F2")
    screen.blit(label, (POS_X*10 - 40, HEIGHT - 80))
    # Formula: y = A * [sin(ωt) + 0.3sin(3ωt)] / 1.4 + offset
    # Harmonic wave: combines fundamental frequency with 3rd harmonic
    y = AMPLITUDE * (math.sin(speed) + 0.3 * math.sin(speed * 3)) / 1.4 + HEIGHT / 2
    pygame.draw.circle(screen, "#E748F2", (POS_X*10, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#EE98FF", (POS_X*10, y), CIRCLE_SIZE * 0.5)
    
    label = font.render("Beat", True, "#D1F618")
    screen.blit(label, (POS_X*11 - 40, 20))
    # Formula: y = A * sin(ωt) * sin(0.1ωt) + offset
    # Beat pattern: amplitude modulation creates "wobble" effect
    y = AMPLITUDE * math.sin(speed) * math.sin(speed * 0.1) + HEIGHT / 2
    pygame.draw.circle(screen, "#D1F618", (POS_X*11, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#6F9913", (POS_X*11, y), CIRCLE_SIZE * 0.5)
    
    label = font.render("Top and bottom", True, "#62F67B")
    screen.blit(label, (POS_X*12 - 40, HEIGHT - 40))
    # Formula: y = A * sgn(sin(ωt)) + offset where sgn = sign function
    # Square wave: only top and bottom positions (sharp transitions)
    y = AMPLITUDE * (1 if math.sin(speed) > 0 else -1) + HEIGHT / 2
    pygame.draw.circle(screen, "#62F67B", (POS_X*12, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#4FB94A", (POS_X*12, y), CIRCLE_SIZE * 0.5)

    label = font.render("From top", True, "#62F6C7")
    screen.blit(label, (POS_X*13 - 40, 20))
    # Formula: y = A * (2(t mod 2π)/(2π) - 1) + offset
    # Sawtooth wave: linear rise with sharp drop
    y = AMPLITUDE * (2 * (speed % (2 * math.pi)) / (2 * math.pi) - 1) + HEIGHT / 2
    pygame.draw.circle(screen, "#62F6C7", (POS_X*13, y), CIRCLE_SIZE)
    pygame.draw.circle(screen, "#81B94A", (POS_X*13, y), CIRCLE_SIZE * 0.5)
    
    
    
    pygame.display.flip()
    clock.tick(60)            
      
pygame.quit()