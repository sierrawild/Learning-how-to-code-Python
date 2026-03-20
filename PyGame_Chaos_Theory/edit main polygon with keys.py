import pygame, random, math

pygame.init()

# screen = pygame.display.set_mode((0, 0), pygame.RESIZABLE) # production/resizable
screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE) # development
clock = pygame.time.Clock()

def theme_default():
    return {
        "bg": (246, 214, 214),
        "yellow": (246, 247, 196),
        "green": (161, 238, 189),
        "blue": (123, 211, 234),
    }

colors = theme_default()

def regular_polygon(sides, radius, cx, cy):
    if sides < 1:
        return []
    return [
        (
            cx + radius * math.cos((2 * math.pi * i / sides) - math.pi / 2),
            cy + radius * math.sin((2 * math.pi * i / sides) - math.pi / 2),
        )
        for i in range(sides)
    ]

def random_color():
    return (random.randint(30, 240), random.randint(30, 240), random.randint(30, 240))

SIDES = 5
fill = False  # False = outline, True = filled

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key in (pygame.K_UP, pygame.K_w):
                SIDES = min(200, SIDES + 1)
            elif event.key in (pygame.K_DOWN, pygame.K_s):
                SIDES = max(1, SIDES - 1)
            elif event.key == pygame.K_f:
                fill = not fill
            elif event.key == pygame.K_c:
                colors["blue"] = random_color()
            elif event.key == pygame.K_r:
                colors = theme_default()
                SIDES = 5
                fill = False

    width, height = screen.get_size()
    screen.fill(colors["bg"])
    radius = min(width, height) * 0.4
    cx, cy = width // 2, height // 2
    corners = regular_polygon(SIDES, radius, cx, cy)

    if SIDES >= 3:
        if fill:
            pygame.draw.polygon(screen, colors["blue"], corners, 0)  # filled
        else:
            pygame.draw.polygon(screen, colors["blue"], corners, 8)  # outline
    elif SIDES == 2:
        pygame.draw.line(screen, colors["blue"], corners[0], corners[1], 8)
    elif SIDES == 1:
        x, y = corners[0]
        pygame.draw.circle(screen, colors["blue"], (int(x), int(y)), 6)

    # Simple HUD
    font = pygame.font.SysFont(None, 28)
    info = f"Sides: {SIDES} | {'Filled' if fill else 'Outline'} | F: toggle fill, C: random color, UP/DOWN: change sides, R: reset, ESC: quit"
    text_surf = font.render(info, True, (30, 30, 30))
    screen.blit(text_surf, (16, 16))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
