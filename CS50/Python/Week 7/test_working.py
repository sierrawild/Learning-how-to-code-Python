from working import convert
import pytest

def test_valueError():
    with pytest.raises(ValueError):
        convert("hello")
    
def test_right():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    
def test_wrong():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
