import pytest
import days

def test_days_not_int():
    with pytest.raises(ValueError) as e:
        days.days("Seven")
    assert str(e.value) == "Day must be an integer"

def test_number_of_days_error_high():
    with pytest.raises(ValueError) as e:
        days.days(10)
    assert str(e.value) == "Out of range"


def test_number_of_days_error_low():
    with pytest.raises(ValueError) as e:
        days.days(-10)
    assert str(e.value) == "Out of range"

def test_days_sunday():
    assert days.days (1) == "Sunday"

def test_days_monday():
    assert days.days (2) == "Monday"

def test_days_tuesday():
    assert days.days (3) == "Tuesday"

def test_days_wednesday():
    assert days.days (4) == "Wednesday"

def test_days_thursday():
    assert days.days (5) == "Thursday"

def test_days_friday():
    assert days.days (6) == "Friday"

def test_days_saturday():
    assert days.days (7) == "Saturday"

def test_print_goodbye():
    assert days.days(-999) == "Goodbye"

