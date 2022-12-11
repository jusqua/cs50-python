from datetime import date
from seasons import convert


def test_convert_phrase():
    assert convert(date.fromisoformat("1999-12-31"), date.fromisoformat("2000-01-01")) == "One thousand, four hundred forty minutes"
    assert convert(date.fromisoformat("1970-01-01"), date.fromisoformat("2000-01-01")) == "Fifteen million, seven hundred seventy-eight thousand eighty minutes"
