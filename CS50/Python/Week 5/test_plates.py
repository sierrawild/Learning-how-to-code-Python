from plates import is_valid

def test_1():
    assert is_valid("123") == False
    assert is_valid("123567") == False
    assert is_valid("1") == False
    
def test_2():
    assert is_valid("AA22A") == False

def test_3():
    assert is_valid("Hello World") == False

def test_4():
    assert is_valid("AAA222") == True

