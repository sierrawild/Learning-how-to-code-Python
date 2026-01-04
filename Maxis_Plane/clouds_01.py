import random
import pygame

class Cloud:
    def __init__(self, x, y, size, color="white", width=0):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.width = width
        
        offset1 = -5
        offset2 = 5
        
        self.parts = [
            (0, 0, size),
            (40 + random.randrange(offset1, offset2), 30 + random.randrange(offset1, offset2), size - 10 + random.randrange(offset1, offset2)),
            (80 + random.randrange(offset1, offset2), 15 + random.randrange(offset1, offset2), size - 5 + random.randrange(offset1, offset2)),
            (120 + random.randrange(offset1, offset2), 25 + random.randrange(offset1, offset2), size - 10 + random.randrange(offset1, offset2)),
            (160 + random.randrange(offset1, offset2), random.randrange(offset1, offset2), size + random.randrange(offset1, offset2)),
            (35 + random.randrange(offset1, offset2), -30 + random.randrange(offset1, offset2), size + 10 + random.randrange(offset1, offset2)),
            (80 + random.randrange(offset1, offset2), -45 + random.randrange(offset1, offset2), size + 5 + random.randrange(offset1, offset2)),
            (130 + random.randrange(offset1, offset2), -35 + random.randrange(offset1, offset2), size - 5 + random.randrange(offset1, offset2)),
        ]
    def draw(self, screen):
        for dx, dy, radius in self.parts:
            pygame.draw.circle(screen, self.color, (self.x + dx, self.y + dy), radius, self.width)