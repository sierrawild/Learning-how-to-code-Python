import pygame
import pygame_gui

pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

manager = pygame_gui.UIManager((800, 600))

play_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((350, 250), (100, 50)),
    text="Play",
    manager=manager
)

running = True
while running:
    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == play_button:
                print("Play clicked")

        manager.process_events(event)

    manager.update(time_delta)

    screen.fill((20, 20, 30))
    manager.draw_ui(screen)

    pygame.display.update()