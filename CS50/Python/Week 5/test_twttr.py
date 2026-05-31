from twttr import shorten


def test_uppercase_vowels():
    assert shorten("AEIOU") == ""

def test_lowercase_vowels():
    assert shorten("aei") == ""

def test_mixed_sentence():
    assert shorten("Hello World!") == "Hll Wrld!"

def test_symbols():
    assert shorten("!£$") == "!£$"

def test_numbers():
    assert shorten("123") == "123"
