import pytest, project, random

# paste this to the terminal to test without needing to change directory every time 

# python -m pytest "C:\Users\Pawel\Desktop\Learning how to code Python\CS50\Python\cs50p_final_project"





def test_lerp2d():
    assert project.lerp2d((0,0),(10,10),0.5) == (5.0, 5.0)
    assert project.lerp2d((0,0),(10,10),0) == (0, 0)
    assert project.lerp2d((0,0),(10,10),1) == (10, 10)
    assert project.lerp2d((0,0),(10,10),1.1) == (11.0, 11.0)
    assert project.lerp2d((11,53),(-46,33), 0.3) == (-6.099999999999998, 47.0)
    
def test_random_palette():
    random.seed(1)
    assert project.random_palette() == {'name': 'Vaporwave', 'bg': (1, 0, 30), 'colors': [(255, 113, 206), (179, 97, 255), (94, 181, 255), (1, 247, 161), (255, 204, 170)]}
    random.seed(99)
    assert project.random_palette() == {'name': 'Terracotta', 'bg': (245, 240, 230), 'colors': [(204, 102, 68), (187, 134, 100), (153, 153, 119), (221, 204, 170), (102, 85, 68)]}
    random.seed(42)
    assert project.random_palette() == {'name': 'Cherry Blossom', 'bg': (245, 240, 235), 'colors': [(255, 183, 197), (255, 138, 172), (218, 112, 148), (140, 93, 113), (93, 79, 84)]}
    
