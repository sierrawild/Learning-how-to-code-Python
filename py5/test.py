"""
Harmonograph / Rotating Things in py5
Based on Piter Pasma's article "How to make interesting rotating things"
https://piterpasma.nl/articles/rotating
 
Press keys 1-9, 0, q-u to switch between presets
Mouse X controls modulation amount
"""
 
import py5
import math
 
TAU = math.pi * 2
 
# Vector functions
def vec2(x, y):
    return {'x': x, 'y': y}
 
def vec2_add(a, b):
    return vec2(a['x'] + b['x'], a['y'] + b['y'])
 
# Circle/rotation function
def circle(phi, r):
    return vec2(r * math.cos(phi), r * math.sin(phi))
 
# R = Rotating function
# f = frequency, p = phase, a = amplitude, s = parameter (0 to 1)
def R(f, p, a, s):
    return circle((s * f + p) * TAU, a)
 
# O = Oscillator function
# f = frequency, p = phase, v = value, d = deviation, s = parameter (0 to 1)
def O(f, p, v, d, s):
    return v + d * math.sin((s * f + p) * TAU)
 
 
# Preset formulas (15 combinations of frequencies 1-6)
PRESETS = [
    {'name': '1:2', 'f1': 1, 'f2': -2, 'sym': 3},
    {'name': '1:3', 'f1': 1, 'f2': -3, 'sym': 4},
    {'name': '1:4', 'f1': 1, 'f2': -4, 'sym': 5},
    {'name': '1:5', 'f1': 1, 'f2': -5, 'sym': 6},
    {'name': '1:6', 'f1': 1, 'f2': -6, 'sym': 7},
    {'name': '2:3', 'f1': 2, 'f2': -3, 'sym': 5},
    {'name': '2:4', 'f1': 2, 'f2': -4, 'sym': 3},
    {'name': '2:5', 'f1': 2, 'f2': -5, 'sym': 7},
    {'name': '2:6', 'f1': 2, 'f2': -6, 'sym': 4},
    {'name': '3:4', 'f1': 3, 'f2': -4, 'sym': 7},
    {'name': '3:5', 'f1': 3, 'f2': -5, 'sym': 8},
    {'name': '3:6', 'f1': 3, 'f2': -6, 'sym': 3},
    {'name': '4:5', 'f1': 4, 'f2': -5, 'sym': 9},
    {'name': '4:6', 'f1': 4, 'f2': -6, 'sym': 5},
    {'name': '5:6', 'f1': 5, 'f2': -6, 'sym': 11},
]
 
current_preset = 0
num_points = 1000
 
 
def settings():
    py5.size(800, 800)
 
 
def setup():
    py5.frame_rate(60)
 
 
def draw():
    py5.background(15, 15, 20)
    py5.translate(py5.width / 2, py5.height / 2)
    
    # Get current preset
    preset = PRESETS[current_preset]
    f1 = preset['f1']
    f2 = preset['f2']
    
    # Mouse X controls modulation amount (0 to 0.3)
    mouse_factor = py5.remap(py5.mouse_x, 0, py5.width, 0, 0.3)
    
    # Scale for drawing
    scale = min(py5.width, py5.height) * 0.35
    
    # Draw the harmonograph
    py5.no_fill()
    py5.stroke(100, 200, 255, 200)
    py5.stroke_weight(2)
    
    py5.begin_shape()
    for i in range(num_points + 1):
        s = i / num_points
        
        # Basic formula: vec2_add(R(f1, 0, 1, s), R(f2, 0, 1, s))
        # With modulation: vec2_add(R(f1, 0, 1, s), R(f2, O(...), 1, s))
        
        # Modulate the phase of the second rotation with an oscillator
        # The oscillator frequency matches the symmetry for best results
        mod_freq = preset['sym']
        phase_mod = O(mod_freq, 0, 0, mouse_factor, s)
        
        # Calculate the point
        point = vec2_add(
            R(f1, 0, 1, s),
            R(f2, phase_mod, 1, s)
        )
        
        # Scale and draw
        x = point['x'] * scale
        y = point['y'] * scale
        py5.vertex(x, y)
    
    py5.end_shape()
    
    # Draw info text
    py5.fill(200)
    py5.no_stroke()
    py5.text_align(py5.LEFT, py5.TOP)
    info = f"Preset: {preset['name']} (symmetry: {preset['sym']})"
    info += f"\nModulation: {mouse_factor:.2f}"
    info += f"\nPress 1-9, 0, q-u to change preset"
    py5.text(info, -py5.width/2 + 20, -py5.height/2 + 20)
    
    # Draw small markers at start/end point
    s = 0
    point = vec2_add(R(f1, 0, 1, s), R(f2, 0, 1, s))
    py5.fill(255, 100, 100)
    py5.circle(point['x'] * scale, point['y'] * scale, 8)
 
 
def key_pressed():
    global current_preset
    
    # Map keys 1-9, 0, q-u to presets 0-14
    key_map = {
        '1': 0, '2': 1, '3': 2, '4': 3, '5': 4,
        '6': 5, '7': 6, '8': 7, '9': 8, '0': 9,
        'q': 10, 'w': 11, 'e': 12, 'r': 13, 't': 14
    }
    
    if py5.key in key_map:
        current_preset = key_map[py5.key]
 
 
py5.run_sketch()
 