import pygame, random

class Enemy(pygame.Rect):
    def __init__(self, x, y, width, height, speed, color):
        super().__init__(x, y, width, height)
        self.speed = speed
        self.directions = ['N', 'E', 'W', 'S']
        self.direction = random.choice(self.directions)
        self.color = color
        self.velocity = pygame.Vector2(0,0)
        self.move_by = pygame.Vector2(0,0)
    
    def move(self, dt):
        self.velocity.update(0,0)
        if self.direction == 'N':
            self.velocity.y = -1
        elif self.direction == 'S':
            self.velocity.y = 1
        elif self.direction == 'W':
            self.velocity.x = -1
        elif self.direction == 'E':
            self.velocity.x = 1
        
        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalize()
        self.move_by = self.velocity * self.speed * dt
        self.x += self.move_by.x
        self.y += self.move_by.y
        
    def change_direction(self):
        right_to = {'N':'E', 'E':'S', 'S':'W','W':'N'}
        left_to = {'N':'W','W':'S','S':'E','E':'N'}
        new_direction = random.choice([right_to,left_to])
        self.direction = new_direction[self.direction] 
    
    def bounce_back(self, n):
        if self.direction == 'N':
            self.y += self.height / n
        elif self.direction == 'S':
            self.y -= self.height / n
        elif self.direction == 'W':
            self.x += self.height / n
        elif self.direction == 'E':
            self.x -= self.height / n
        
    def draw(self, surf):
        pygame.draw.rect(surf,self.color, self)