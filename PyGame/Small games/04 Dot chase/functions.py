import pygame
def dr_K_patter(surface, color,x,y,size):
    size_s = size * 0.3
    border_width = int(size * 0.02)
    # corners
    pygame.draw.rect(surface,color, (x,y,size_s,size_s), border_width) # left top
    pygame.draw.rect(surface,color, (x + size - size_s,y,size_s,size_s), border_width) # right top
    pygame.draw.rect(surface,color, (x,y + size - size_s,size_s,size_s), border_width) # left bottom
    pygame.draw.rect(surface,color, (x + size - size_s,y + size - size_s,size_s,size_s), border_width) # right bottom

    # corner leafs 
    radius = int(size * 0.1)
    offset = size_s * 0.5
    pygame.draw.rect(surface,color, (x + offset,y + offset,size_s,size_s), border_width, border_top_right_radius=radius, border_bottom_left_radius=radius) # left top
    pygame.draw.rect(surface,color, ((x + size - size_s) - offset,y + offset,size_s,size_s), border_width, border_top_left_radius=radius, border_bottom_right_radius=radius) # right top
    pygame.draw.rect(surface,color, (x + offset,y - offset + size - size_s,size_s,size_s), border_width, border_top_left_radius=radius, border_bottom_right_radius=radius) # left bottom
    pygame.draw.rect(surface,color, (x - offset + size - size_s,y - offset + size - size_s,size_s,size_s), border_width, border_top_right_radius=radius, border_bottom_left_radius=radius) # right bottom
    
    
    pygame.draw.rect(surface,color, (x,y,size,size), border_width) # main
    s = size * 0.9
    ss = size * 0.05
    pygame.draw.rect(surface, color, (x+ss,y+ss, s, s), border_width) # main small
    pygame.draw.rect(surface, color, (x + size/2 - size_s/2,y + size/2 - size_s/2, size_s, size_s), border_width) # middle
