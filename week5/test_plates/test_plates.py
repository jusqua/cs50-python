from plates import is_valid


def test_is_valid_length():
    assert is_valid("AAA1000") == False
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAAA") == True
    assert is_valid("AAAA1") == True
    assert is_valid("AAAA12") == True


def test_is_valid_number_placement():
    assert is_valid("AAA0A0") == False
    assert is_valid("AAA1A0") == False
    assert is_valid("AAA012") == False
    assert is_valid("AAA120") == True


def test_is_valid_nonalphanum_placement():
    assert is_valid("C$50") == False
    assert is_valid("AA,.10") == False


def test_is_valid_letter_placement():
    assert is_valid("00AAAA") == False
    assert is_valid("A123") == False
    assert is_valid("CS50") == True

