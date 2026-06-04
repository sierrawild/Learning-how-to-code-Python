
from bank import value

def test_hello():
    assert value("hello") == "$0"

def test_h():
    assert value("h") == "$20"

def test_other():
    assert value("") == "$100"

def test_other2():
    assert value("What?") == "$100"
