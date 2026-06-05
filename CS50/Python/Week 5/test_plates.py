from plates import is_valid

def test_1():
    assert is_valid("123") == False
    assert is_valid("123567") == False
    assert is_valid("1") == False

def test_2():
    assert is_valid("AA22A") == False
    assert is_valid("22A") == False

def test_3():
    assert is_valid("Hello World") == False

def test_4():
    assert is_valid("AAA222") == True

def test_5():
    assert is_valid("AAB1234") == False

def test_6():
    assert is_valid("") == False
    assert is_valid("??AA") == False
    assert is_valid("AA??") == False

def test_7():
    assert is_valid("HELLO") == True

def test_8():
    assert is_valid("AA") == True
    assert is_valid("A2") == False

    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid("2") == False


def test_0():
    assert is_valid("AA012") == False

