import py5
import random

def setup():
    py5.size(800, 600)
    py5.background(255)
    py5.stroke(0)

def draw():
    # Clear with transparency for trail effect
    py5.fill(255, 10)
    py5.rect(0, 0, py5.width, py5.height)
    
    # center the screen
    py5.push_matrix()
    py5.translate(py5.width/2,0)


    # Uniform (for comparison) - evenly spread
    x = random.uniform(0, 200)
    py5.fill("#FF0000")
    py5.circle(x, 100, 5)
    
    # Gaussian - clusters in middle
    x = random.gauss(0, 50)
    py5.fill("#15FF00")
    py5.circle(x, 250, 5)
    
    # Triangular - peaks at 100, range 0-200
    x = random.triangular(0, 200, 50)
    py5.fill("#FFBB00")
    py5.circle(x, 400, 5)
    
    # Exponential - lots near left, few far right
    x = random.expovariate(1.0 / 50.0)
    x = min(x, 200)  # cap it
    py5.fill("#009DFF")
    py5.circle(x, 550, 5)
    
    py5.pop_matrix()

py5.run_sketch()