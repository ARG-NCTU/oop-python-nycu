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
def test_birthday_prob_edge_cases():
    # Test edge cases for birthday_prob
    assert lec4.birthday_prob(0, 2, 1000) == 0, "With 0 people, probability should be 0"
    assert lec4.birthday_prob(1, 2, 1000) == 0, "With 1 person, probability should be 0"
    assert lec4.birthday_prob(23, 1, 1000) > 0, "With 23 people and at least one match, probability should be greater than 0"
    assert lec4.birthday_prob(23, 23, 1000) > 0, "With 23 people and all matching birthdays, probability should be greater than 0"
def test_birthday_prob_large_trials():
    # Test birthday_prob with a large number of trials
    num_people = 23
    num_same = 2
    num_trials = 1000000
    result = lec4.birthday_prob(num_people, num_same, num_trials)
    assert isinstance(result, float), "birthday_prob should return a float"
    assert 0 <= result <= 1, "birthday_prob should return a value between 0 and 1"
def test_birthday_prob_invalid_input():
    # Test birthday_prob with invalid inputs
    with pytest.raises(ValueError):
        lec4.birthday_prob(-1, 2, 1000)  # Negative number of people
    with pytest.raises(ValueError):
        lec4.birthday_prob(23, -1, 1000)  # Negative number of matches
    with pytest.raises(ValueError):
        lec4.birthday_prob(23, 2, -1000)  # Negative number of trials
def test_roll_die_invalid_input():
    # Test roll_die with invalid inputs
    with pytest.raises(ValueError):
        lec4.roll_die(0)  # Invalid die size
    with pytest.raises(ValueError):
        lec4.roll_die(-6)  # Invalid die size
    with pytest.raises(TypeError):
        lec4.roll_die("six")  # Non-integer input
def test_same_date_invalid_input():
    # Test same_date with invalid inputs
    with pytest.raises(ValueError):
        lec4.same_date(-1, 2)  # Negative number of people
    with pytest.raises(ValueError):
        lec4.same_date(23, -1)  # Negative number of matches
    with pytest.raises(TypeError):
        lec4.same_date("twenty-three", 2)  # Non-integer input for number of people
def test_same_date_edge_cases():
    # Test same_date with edge cases
    assert lec4.same_date(0, 2) is False, "With 0 people, there can't be a match"
    assert lec4.same_date(1, 2) is False, "With 1 person, there can't be a match"
    assert lec4.same_date(23, 1) is True, "With 23 people and at least one match, there should be a match"
    assert lec4.same_date(23, 23) is True, "With 23 people and all matching birthdays, there should be a match"
def test_roll_die_edge_cases():
    # Test roll_die with edge cases
    assert lec4.roll_die(1) == 1, "With a 1-sided die, the result should always be 1"
    assert lec4.roll_die(6) in [1, 2, 3, 4, 5, 6], "With a standard 6-sided die, the result should be between 1 and 6"
    assert lec4.roll_die(100) in range(1, 101), "With a 100-sided die, the result should be between 1 and 100"
