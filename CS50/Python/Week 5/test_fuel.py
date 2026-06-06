import pytest
from fuel import convert, gauge

def test_covert():
    assert convert('10/100') == 10

def test_ValueError():
    with pytest.raises(ValueError):
        