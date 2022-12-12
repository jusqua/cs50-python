from jar import Jar
import pytest


def test_init():
    jar = Jar(50)
    assert jar.capacity == 50
    assert jar.size == 0
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(12)
    with pytest.raises(Exception):
        jar.deposit(1)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(12)
    with pytest.raises(Exception):
        jar.withdraw(1)

