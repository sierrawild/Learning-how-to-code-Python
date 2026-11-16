import pygame, os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'assets', 'character_round_red.png')
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        
    def update(self):
        self.pos = pygame.mouse.get_pos()
        self.pos = pygame.Vector2(self.pos)
        self.rect.center = self.pos