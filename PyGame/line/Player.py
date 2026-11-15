import pygame, os

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        path = os.path.dirname(__file__)
        path = os.path.join(path, 'assets', 'character_round_red.png')
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos