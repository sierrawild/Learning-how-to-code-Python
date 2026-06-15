from um import count

def test_ok():
    assert count("um") == 1
    
def test_ok2():
    assert count("Um, thanks for the album. Its Yoummy") == 1
    
def test_ok0():
    assert count("U, thanks for the album.") == 0
    