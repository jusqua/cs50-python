from um import count 


def test_count_um_between():
    assert count("yummy") == 0
    assert count("yum") == 0
    assert count("umumum") == 0
    assert count("um") == 1


def test_count_um_among():
    assert count("hello um") == 1
    assert count("hello um um um") == 3
    assert count("um hello um") == 2


def test_count_ignore_case():
    assert count("Um uM UM") == 3

