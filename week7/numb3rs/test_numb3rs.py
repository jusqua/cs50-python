from numb3rs import validate


def test_validate_regex_match():
    assert validate("cat.dog.pip.fog") == False
    assert validate("1.dog.2.fog") == False
    assert validate("1111.2222.3232.4343") == False
    assert validate("256.2.115.3") == False
    assert validate("2.256.115.3") == False
    assert validate("2.115.256.3") == False
    assert validate("2.115.3.256") == False
    assert validate("255.255.255.255") == True

def test_validate_values():
    assert validate("255.255.255.255") == True
    assert validate("1.1.1.1") == True
    assert validate("127.0.0.1") == True

