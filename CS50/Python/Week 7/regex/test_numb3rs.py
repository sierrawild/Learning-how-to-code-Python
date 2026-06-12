def valid_ip():
    assert '255.123.01.01' == True
    assert '255.123.21.01' == True
    assert '255.123.01.123' == True

def not_valid_ip():
    assert '257.123.01.01' == False
    assert '512.512.512.512' == False
    assert '1.2.3.1000' == False