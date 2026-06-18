from seasons import process
import pytest

def test_valid_date():
    # assert process("1988-01-31", "2026-06-17") == "Twenty million, one hundred and eighty-four thousand, four hundred and eighty minutes"
    # assert process("2026-06-16", "2026-06-17") == "One thousand, four hundred and forty minutes"
    assert process("2001-01-01", "2003-01-01") == "One million, fifty-one thousand, two hundred minutes"

def test_invalid_date():
    with pytest.raises(ValueError):
        process("2026-06-32", "2026-06-17")
