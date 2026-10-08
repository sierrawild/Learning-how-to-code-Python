import pygame, random

class Player:
    def __init__(self, size, palette, hand):
        self.hand = hand
        self.size = size
        self.palette = palette
        self.shape_rect = None
        
    def choose_random_hand(self, hands):
        self.hand = random.choice(hands)
        
    def draw_shape(self,x,y, surface, palette):
        self.shape_rect = pygame.Rect(x,y,self.size,self.size)
        self.shape_rect.center = (x,y)
        if self.hand == 'rock':
            pygame.draw.aacircle(surface, palette['rock'], (x,y), self.size/2)
        elif self.hand == 'paper':
            pygame.draw.rect(surface, palette['paper'], self.shape_rect)
        elif self.hand == 'scissors':
            points = [(x - self.size/2, y + self.size/2), (x, y - self.size/2), (x + self.size/2, y+self.size/2)]
            pygame.draw.polygon(surface, palette['scissors'], points)