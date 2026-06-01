import py5, palette

# Variables
W, H = 1000, 1000
p = palette.INK

x,y = 0,0
def settings():
    py5.size(W,H)
    # py5.full_screen()
    
def setup():
    py5.frame_rate((60))
    
    py5.background(*p['bg'])
    py5.stroke(*p['colors'][0])
    py5.fill(*p['colors'][1])
    py5.stroke_weight(5)
    
    py5.no_fill()
    # py5.no_stroke()
    
def draw():
    global x,y
    
    ghost_trails(p['bg'],25) 
    center_coordinates()
    
    angle = py5.noise(x * 0.01, y * 0.01) * py5.TWO_PI
    x += py5.cos(angle)
    y += py5.sin(angle)
    
    py5.circle(x,y, 10)
    
    # END OF DRAW
    
    
"""
Noise Flow Fields

Many generative artists use noise to create directions.

angle = py5.noise(x * 0.01,
                  y * 0.01) * py5.TWO_PI

Now each point in space has a direction.

You can move particles through that field:

x += py5.cos(angle)
y += py5.sin(angle)

This creates beautiful flowing patterns.

If you've seen:

ink simulations
flowing lines
topographic art
smoke-like particle trails

they often use noise fields.

Noise Seed

Want repeatable results?

py5.noise_seed(42)

Now every run generates the same noise pattern.

Useful when creating artwork you want to recreate later.

A Challenge

Try building this yourself:

Start with one dot.
Use noise() to control X.
Use a second noise() stream to control Y.
Don't clear the background.
Draw a tiny circle each frame.

Something like:

x = noise(...)
y = noise(...)

mapped to screen coordinates.

You'll get an organic scribble that never repeats and feels much more natural than random motion.

A good next step after that is learning flow fields, because that's where Perlin noise becomes incredibly powerful for the kind of generative-art videos and py5 experiments you've been making.

"""

    
def center_coordinates():
    py5.translate(py5.width/2,py5.height/2)
    py5.scale(1,-1)

def ghost_trails(color, alpha):  
    py5.push_style()
    py5.fill(*color,alpha) 
    py5.rect_mode(py5.CORNER)
    py5.no_stroke()
    py5.rect(0,0,py5.width,py5.height)
    py5.pop_style()

    
    

    

py5.run_sketch()