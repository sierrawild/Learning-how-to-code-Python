import project, palettes, pytest

# paste this to the terminal to test without needing to change directory every time 

# python -m pytest "C:\Users\Pawel\Desktop\Learning how to code Python\CS50\Python\cs50p_final_project"





def test_lerp2d():
    assert project.lerp2d((0,0),(10,10),0.5) == (5.0, 5.0)
    assert project.lerp2d((0,0),(10,10),0) == (0, 0)
    assert project.lerp2d((0,0),(10,10),1) == (10, 10)
    assert project.lerp2d((0,0),(10,10),1.1) == (11.0, 11.0)
    assert project.lerp2d((11,53),(-46,33), 0.3) == (pytest.approx(-6.1), 47.0)
    assert project.lerp2d((0,0),(1,1), 0.5) == (0.5,0.5)
    assert project.lerp2d((0,0),(1,1), 0) == (0,0)
    assert project.lerp2d((0,0),(1,1), 1) == (1,1)
    assert project.lerp2d((0,0),(1,1), 1.1) == (1.1,1.1)
    
def test_number_formatting():
    assert project.number_formatting(-500) == "."
    assert project.number_formatting(-350) == ".."
    assert project.number_formatting(-250) == "..."
    assert project.number_formatting(-150) == "...."

    assert project.number_formatting(0) == "0"
    assert project.number_formatting(42) == "42"
    assert project.number_formatting(1_000) == "1.0 k"
    assert project.number_formatting(1_101) == "1.1 k"
    assert project.number_formatting(1_100_000) == "1.10 m"
    assert project.number_formatting(1_150_000) == "1.15 m"
    
def test_get_polygon_name():
    assert project.get_polygon_name(3) == "Sierpiński triangle"
    assert project.get_polygon_name(4) == "Square"
    assert project.get_polygon_name(10) == "Decagon"
    assert project.get_polygon_name(21) == "n-gon"
    
def test_clamp():
    assert project.clamp(1,0,10) == 1
    assert project.clamp(-1,0,10) == 0
    assert project.clamp(11,0,10) == 10
    
def test_color_value_adjustment():
    assert project.color_value_adjustment(20, 100, 0.8) == 84
    assert project.color_value_adjustment(20, 100, 1) == 100
    assert project.color_value_adjustment(20, 100, 0) == 20
    assert project.color_value_adjustment(20, 100, 0.5) == 60

def test_distance():
    assert project.distance((0,0), (0,0)) == 0
    assert project.distance((0,0), (0,1)) == 1
    assert project.distance((0,0), (-10,0)) == 10
    assert project.distance((0,0), (1,1)) == pytest.approx(1.414213)
    
def test_main_polygon():
    x = project.main_polygon(3, 5, 0, 0)
    assert x[0] == pytest.approx((0, -5.0))
    assert x[1] == pytest.approx((4.33012701, 2.5))
    assert x[2] == pytest.approx((-4.330127, 2.5))

def test_random_palette():
    for _ in range(100):
        palette = project.random_palette()
        assert len(palette["colors"]) >= 1 
        assert type(palette["name"]) == str
        assert palette["name"] != None
        assert type(palette["bg"]) == str
        assert palette["bg"] != None
        assert type(palette["colors"]) == list
        assert palette["colors"] != None
        
        assert palette in palettes.all_palettes