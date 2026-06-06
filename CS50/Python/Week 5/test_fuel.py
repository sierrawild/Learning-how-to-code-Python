import pytest
from fuel import convert, gauge

def test_covert():
    assert convert('1/100') == 1
    assert convert('10/100') == 10
    assert convert('10/10') == 100

def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    
def test_errors():
    with pytest.raises(ValueError):
        convert("100/10")
    with pytest.raises(ValueError):
        convert("cat/10")
    with pytest.raises(ValueError):
        convert("-1/10")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    
        