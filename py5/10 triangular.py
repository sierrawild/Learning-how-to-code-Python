import py5
import random

# favours left-middle side of the screen

def setup():
    py5.size(800, 600)
    py5.background(255)
    py5.frame_rate(60)
    
def draw():
    # Circles favor left side of screen
    for _ in range(200):
        # Peak at 200px, range 0-800
        x = random.triangular(0, py5.width, 200)
        y = random.triangular(0, py5.height, py5.height/2)
        
        py5.fill(0, 50)
        py5.circle(x, y, 10)
        
py5.run_sketch()