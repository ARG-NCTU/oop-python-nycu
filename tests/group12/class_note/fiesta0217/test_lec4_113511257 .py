#import add_path
import pytest
#import mit_ocw_data_science.lec4.lec4 module as lec4

def test_roll_die():
    # Test the roll_die function
    results = [lec4.roll_die() for _ in range(1000)]
    assert all(1 <= result <= 6 for result in results), "roll_die should return a number between 1 and 6"
def test_same_date():
    # Test the same_date function
    num_people = 23
    num_same = 2
    result = lec4.same_date(num_people, num_same)
    assert isinstance(result, bool), "same_date should return a boolean"
def test_birthday_prob():
    # Test the birthday_prob function
    num_people = 23
    num_same = 2
    num_trials = 1000
    result = lec4.birthday_prob(num_people, num_same, num_trials)
    assert isinstance(result, float), "birthday_prob should return a float"
    assert 0 <= result <= 1, "birthday_prob should return a value between 0 and 1"

