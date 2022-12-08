import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/1") == 100
    assert convert("1/10") == 10
    with pytest.raises(Exception):
        convert("cat/dog")
    with pytest.raises(Exception):
        convert("10/5")
    with pytest.raises(Exception):
        convert("1/0")


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(75) == "75%"
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"

