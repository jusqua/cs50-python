from bank import value


def test_value_100():
    assert value("What's up?") == 100


def test_value_20():
    assert value("Hi, how can I help you?") == 20


def test_value_0():
    assert value("Hello, welcome!") == 0

