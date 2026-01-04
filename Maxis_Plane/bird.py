import pygame
import random

class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 45
        self.speed = 350
        self.wing_angle = 0
        self.wing_speed = 10
    
    def update(self, delta_time):
        self.x -= self.speed * delta_time
        self.wing_angle += self.wing_speed * delta_time
    
    def draw(self, screen):
        # Bird body (brown)
        body_color = (139, 69, 19)
        pygame.draw.ellipse(screen, body_color, 
                          (self.x, self.y, self.width, self.height))
        
        # Bird head
        head_size = 22
        pygame.draw.circle(screen, body_color, 
                         (int(self.x + self.width - 8), int(self.y + self.height // 2)), 
                         head_size)
        
        # Eye
        pygame.draw.circle(screen, (255, 255, 255), 
                         (int(self.x + self.width - 2), int(self.y + self.height // 2 - 3)), 6)
        pygame.draw.circle(screen, (0, 0, 0), 
                         (int(self.x + self.width - 2), int(self.y + self.height // 2 - 3)), 3)
        
        # Beak
        beak_points = [
            (self.x + self.width + 15, self.y + self.height // 2),
            (self.x + self.width + 22, self.y + self.height // 2 - 5),
            (self.x + self.width + 22, self.y + self.height // 2 + 5)
        ]
        pygame.draw.polygon(screen, (255, 140, 0), beak_points)
        
        # Animated wings
        wing_offset = abs(int(8 * pygame.math.Vector2(1, 0).rotate(self.wing_angle * 20).y))
        
        # Left wing
        wing_color = (101, 67, 33)
        pygame.draw.ellipse(screen, wing_color,
                          (self.x - 15, self.y + 8 - wing_offset, 38, 22))
        # Right wing
        pygame.draw.ellipse(screen, wing_color,
                          (self.x - 15, self.y + 15 + wing_offset, 38, 22))
    
    def get_rect(self):
        # Return a tighter collision box for the bird's body only
        # Exclude wings and beak from collision
        padding = 15
        return pygame.Rect(self.x + padding, self.y + padding, 
                          self.width - (padding * 2), self.height - (padding * 2))
    
    def is_off_screen(self):
        return self.x < -100


class ObstacleManager:
    def __init__(self, lanes):
        self.obstacles = []
        self.spawn_timer = 0
        self.spawn_interval = random.uniform(4, 7)
        self.lanes = lanes
        self.screen_width = 1800
    
    def update(self, delta_time, occupied_lanes):
        self.spawn_timer += delta_time
        
        # Spawn new obstacle
        if self.spawn_timer >= self.spawn_interval:
            self.spawn_timer = 0
            self.spawn_interval = random.uniform(4, 7)
            
            # Get available lanes (not occupied by coins)
            available_lanes = [i for i in range(3) if i not in occupied_lanes]
            
            # Random lane
            if available_lanes:
                lane_index = random.choice(available_lanes)
                lane_y = self.lanes[lane_index] - 22
                
                bird = Bird(self.screen_width + 50, lane_y)
                self.obstacles.append(bird)
        
        # Update all obstacles
        for obstacle in self.obstacles:
            obstacle.update(delta_time)
        
        # Remove off-screen obstacles
        self.obstacles = [obs for obs in self.obstacles if not obs.is_off_screen()]
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def check_collision(self, plane_rect):
        # Create a more accurate hitbox for the plane based on its center position
        # Use a fixed size hitbox that doesn't change with rotation
        plane_hitbox = pygame.Rect(0, 0, 80, 40)
        plane_hitbox.center = plane_rect.center
        
        for obstacle in self.obstacles:
            bird_rect = obstacle.get_rect()
            
            if plane_hitbox.colliderect(bird_rect):
                return True
        return False