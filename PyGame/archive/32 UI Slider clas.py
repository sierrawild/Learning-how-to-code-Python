import pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

color = pygame.Color(0, 255, 245)
cube_size = 100

class Button:
    def __init__(self, x, y, size, color, travel, min_val, max_val, label=None, key=None):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.dragging = False
        self.start_y = y
        self.travel = travel
        self.min_val = min_val
        self.max_val = max_val
        self.value = max_val
        self.label = label
        self.key = key
        self.font = pygame.font.SysFont(None, 24)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.rect.move_ip(0, event.rel[1])
                self.rect.y = max(self.start_y, min(self.start_y + self.travel, self.rect.y))
                t = (self.rect.y - self.start_y) / self.travel
                self.value = self.max_val - t * (self.max_val - self.min_val)
        elif event.type == pygame.KEYDOWN:
            if self.key and event.key == self.key:
                self.dragging = not self.dragging

    def update(self):
        if self.dragging and self.key:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.rect.move_ip(0, -2)
            if keys[pygame.K_DOWN]:
                self.rect.move_ip(0, 2)
            self.rect.y = max(self.start_y, min(self.start_y + self.travel, self.rect.y))
            t = (self.rect.y - self.start_y) / self.travel
            self.value = self.max_val - t * (self.max_val - self.min_val)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0, 5)
        if self.label:
            label_surf = self.font.render(self.label, True, "black")
            label_rect = label_surf.get_rect(centerx=self.rect.centerx, bottom=self.rect.top - 5)
            screen.blit(label_surf, label_rect)
        val_surf = self.font.render(f"{self.value:.2f}", True, "black")
        val_rect = val_surf.get_rect(centerx=self.rect.centerx, top=self.rect.bottom + 5)
        screen.blit(val_surf, val_rect)
        if self.key:
            key_surf = self.font.render(f"[{pygame.key.name(self.key)}]", True, "grey")
            key_rect = key_surf.get_rect(centerx=self.rect.centerx, top=self.rect.bottom + 25)
            screen.blit(key_surf, key_rect)


# --- create buttons ONCE, before the loop ---
button_hue  = Button(50,  100, 50, "tomato",     travel=200, min_val=0,   max_val=360, label="Hue",        key=pygame.K_h)
button_sat  = Button(150, 100, 50, "gold",        travel=200, min_val=0,   max_val=100, label="Saturation", key=pygame.K_s)
button_val  = Button(250, 100, 50, "darkorchid",  travel=200, min_val=0,   max_val=100, label="Value",      key=pygame.K_v)
buttons = [button_hue, button_sat, button_val]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        for button in buttons:
            button.handle_event(event)

    for button in buttons:
        button.update()

    # update color from button values
    color.hsva = (button_hue.value, button_sat.value, button_val.value)

    screen.fill("aliceblue")
    pygame.draw.rect(screen, color,
                    ((screen.get_width()-cube_size)//2, (screen.get_height()-cube_size)//2,
                    cube_size, cube_size), 0, 20)
    for button in buttons:
        button.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()