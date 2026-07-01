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
    assert project.random_palette() == {'name': 'White on Black', 'bg': '#000000', 'colors': ['#FFFFFF']}
    random.seed(99)
    assert project.random_palette() == {'name': 'Forest', 'bg': '#101A13', 'colors': ['#D8F3DC', '#95D5B2', '#52B788', '#40916C', '#B7A57A']}
    random.seed(42)
    assert project.random_palette() == {'name': 'Cyberpunk', 'bg': '#090A1A', 'colors': ['#00F0FF', '#FF2A6D', '#D300C5', '#F9F871', '#05FFA1']}
    
def test_number_formatting():
    assert project.number_formatting(-500) == "."
    assert project.number_formatting(-350) == ".."
    assert project.number_formatting(-250) == "..."
    assert project.number_formatting(-150) == "...."

    assert project.number_formatting(42) == "42"
    assert project.number_formatting(1_001) == "1.0 k"
    assert project.number_formatting(1_101) == "1.1 k"
    assert project.number_formatting(1_100_000) == "1.10 m"
    assert project.number_formatting(1_150_000) == "1.15 m"