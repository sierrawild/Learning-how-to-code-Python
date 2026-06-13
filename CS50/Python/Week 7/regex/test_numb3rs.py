from numb3rs import validate

def test_validip():
    # assert validate('255.123.01.01') == True
    # assert validate('255.123.21.01') == True
    # assert validate('255.123.01.123') == True
    # assert validate('127.0.0.1') == True
    assert validate('255.255.255.255') == True

def test_not_valid_ip():
    assert validate('257.123.01.01') == False
    assert validate('512.512.512.512') == False
    assert validate('1.2.3.1000') == False
    assert validate('192.168.001.1') == False
    assert validate('cat') == False
