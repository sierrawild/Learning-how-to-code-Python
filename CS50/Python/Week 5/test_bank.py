
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0
    assert value("HELlo") == 0

def test_h():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("H") == 20
    assert value("how's it going") == 20

def test_other():
    assert value("") == 100
    assert value("What?") == 100
    assert value("That") == 100
    assert value("123") == 100