import pytest
from working import convert


def test_convert_without_minutes():
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    with pytest.raises(Exception):
        convert("13 AM to 11 PM")
    with pytest.raises(Exception):
        convert("11 AM to 13 PM")


def test_convert_with_minutes():
    assert convert("12:00 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"
    with pytest.raises(Exception):
        convert("11:60 AM to 13:79 PM")


def test_convert_wrong_format():
    with pytest.raises(Exception):
        convert("hello, world")
    with pytest.raises(Exception):
        convert("Prologue: A Silent of Three Parts")
    with pytest.raises(Exception):
        convert("09h to 23h")
    with pytest.raises(Exception):
        convert("10 AM - 11 PM")
    
