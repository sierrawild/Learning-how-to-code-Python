import pygame
import random

class Coin:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 25
        self.collected = False
        self.speed = 300
    
    def update(self, delta_time):
        self.x -= self.speed * delta_time
    
    def draw(self, screen):
        if not self.collected:
            # Draw golden coin
            # Outer circle (gold)
            pygame.draw.circle(screen, (255, 215, 0), (int(self.x), int(self.y)), self.radius)
            # Inner circle (darker gold for depth)
            pygame.draw.circle(screen, (218, 165, 32), (int(self.x), int(self.y)), self.radius - 5)
            # Shine effect
            pygame.draw.circle(screen, (255, 255, 200), (int(self.x - 6), int(self.y - 6)), 6)
    
    def check_collision(self, plane_rect):
        if not self.collected:
            # Check if coin overlaps with plane
            coin_rect = pygame.Rect(self.x - self.radius, self.y - self.radius, 
                                   self.radius * 2, self.radius * 2)
            return plane_rect.colliderect(coin_rect)
        return False
    
    def is_off_screen(self):
        return self.x < -50


class CoinStreak:
    def __init__(self, lane_y, start_x=None):
        self.lane_y = lane_y
        self.coins = []
        self.num_coins = random.randint(5, 25)
        self.spacing = 60
        
        if start_x is None:
            start_x = 1800 + 100  # screen width + offset
        
        # Create a line of coins
        for i in range(self.num_coins):
            coin = Coin(start_x + (i * self.spacing), lane_y)
            self.coins.append(coin)
    
    def update(self, delta_time):
        for coin in self.coins:
            coin.update(delta_time)
    
    def draw(self, screen):
        for coin in self.coins:
            coin.draw(screen)
    
    def check_collisions(self, plane_rect):
        collected_count = 0
        for coin in self.coins:
            if coin.check_collision(plane_rect):
                coin.collected = True
                collected_count += 1
        return collected_count
    
    def is_complete(self):
        # Check if all coins are either collected or off screen
        return all(coin.collected or coin.is_off_screen() for coin in self.coins)