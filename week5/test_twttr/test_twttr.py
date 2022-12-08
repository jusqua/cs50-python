from twttr import shorten


def test_shorten_lower():
    assert shorten("twitter") == "twttr"


def test_shorten_upper():
    assert shorten("TWITTER") == "TWTTR"


def test_shorten_mixed():
    assert shorten("TwittEr") == "Twttr"


def test_shorten_numbers():
    assert shorten("Tw1tt3r") == "Tw1tt3r"


def test_shorten_punctuation():
    assert shorten("Tw.tt,r") == "Tw.tt,r"

