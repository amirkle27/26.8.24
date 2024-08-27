import pytest
import guess_number

def test_guess_correct():
    assert guess_number.check_guess(50, 50) == "BINGO!!"

def test_guess_low():
    assert guess_number.check_guess(90, 10) == "Guess higher"

def test_guess_high():
    assert guess_number.check_guess(10, 90) == "Guess lower"

def test_input_str():
    with pytest.raises(ValueError) as e:
        guess_number.check_guess(50, "hi")
        assert (e.value) == "Input must be an integer"


def test_out_of_range_high():
    with pytest.raises(ValueError) as e:
        guess_number.check_guess(50, 404)
        assert (e.value) =="Number out of range"


def test_out_of_range_low():
    with pytest.raises(ValueError) as e:
        guess_number.check_guess(50, -500)
        assert (e.value) =="Number out of range"

