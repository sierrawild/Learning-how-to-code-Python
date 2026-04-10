from py5 import *

def settings():
    size(1000, 1000, P2D)
    
    
def setup():
    background("#98F7CC")  # Light gray background so we can see both shapes

def draw():
    no_loop()  # Only draw once
    
    # Mint green rectangle
    fill("#4BF2A7")
    rect(100, 100, 200, 300)
    
    # Red rectangle next to it
    fill("#4BaaAa")
    rect(350, 100, 200, 300)
    
run_sketch()