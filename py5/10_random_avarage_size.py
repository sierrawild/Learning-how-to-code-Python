import py5
import random

def settings():
    py5.size(800, 600)
def setup():
    py5.background(255)

def draw():
    # Set seed for reproducible randomness
    random.seed(12345)
    
    # Draw 50 circles with random positions and sizes
    for _ in range(50):
        x = random.uniform(0, py5.width)
        y = random.uniform(0, py5.height)
        diameter = random.gauss(30, 10)  # average 30, some variation
        
        # Pick a random color from your palette
        color = random.choice(['#FF6B6B', '#4ECDC4', '#45B7D1'])
        py5.fill(color)
        py5.circle(x, y, diameter)
        
py5.run_sketch()