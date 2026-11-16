import pygame, os

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'assets', 'character_round_purple.png')
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(0,0)
        self.acc = pygame.Vector2(0,0)
        self.rect.center = self.pos
        
    def update(self, player_pos, dt):
        direction = player_pos - self.pos
        if direction.length() > 0:
            direction = direction.normalize()
        
        speed = 300
        self.pos += speed * direction * dt
        self.rect.center = self.pos