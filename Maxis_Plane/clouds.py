import pygame
import random

class Cloud:
    def __init__(self, x, y, size, color="white", width=0):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.width = width
        self.speed = random.uniform(30, 80)  # pixels per second
        
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
    
    def update(self, delta_time):
        """Move the cloud to the left"""
        self.x -= self.speed * delta_time
    
    def draw(self, screen):
        for dx, dy, radius in self.parts:
            pygame.draw.circle(screen, self.color, (self.x + dx, self.y + dy), radius, self.width)
    
    def is_off_screen(self):
        """Check if cloud has moved off the left side of screen"""
        return self.x < -200  # Assuming clouds are about 200 pixels wide


class CloudManager:
    def __init__(self, screen_width, screen_height, num_clouds=8):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.clouds = []
        
        # Create initial clouds spread across the screen
        for _ in range(num_clouds):
            x = random.randint(0, screen_width)
            y = random.randint(50, screen_height - 300)
            size = random.randint(40, 45)
            self.clouds.append(Cloud(x, y, size))
    
    def update(self, delta_time):
        """Update all clouds and remove off-screen ones"""
        for cloud in self.clouds:
            cloud.update(delta_time)
        
        # Remove clouds that have gone off screen
        self.clouds = [cloud for cloud in self.clouds if not cloud.is_off_screen()]
        
        # Add new clouds on the right side when needed
        if len(self.clouds) < 8:
            if random.random() < 0.015:  # 1.5% chance each frame
                x = self.screen_width + 100
                y = random.randint(50, self.screen_height - 300)
                size = random.randint(25, 55)
                self.clouds.append(Cloud(x, y, size))
    
    def draw(self, screen):
        """Draw all clouds"""
        for cloud in self.clouds:
            cloud.draw(screen)