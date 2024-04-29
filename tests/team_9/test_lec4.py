import random
import pytest
import math
from lec4_module import roll_die, run_sim, same_date, birthday_prob

def test_roll_die():
    """
    Test the roll_die function from lec4_module.
    This function should return an integer between 1 and 6.
    The test is run 100 times to ensure reliability.
    """
    for i in range(100):
        result = roll_die()
        assert isinstance(result, int)
        assert result >= 1 and result <= 6

def test_roll():
    """
    Test the roll_die function by rolling the die 10 times and printing the results.
    """
    n = 10
    result = ''
    for i in range(n):
        result = result + str(roll_die())
    print(f'test_roll: {result}')

def test_run_sim():
    """
    Test the run_sim function from lec4_module.
    The function is tested with a known goal and number of trials.
    """
    random.seed(0)
    goal = '11111'
    num_trials = 1000
    run_sim(goal, num_trials, '11111')
    random.seed(0)
    goal = '1111'
    num_trials = 1000
    run_sim(goal, num_trials, '1111')

def test_same_date():
    """
    Test the same_date function from lec4_module.
    The function is tested with known values for number of people and number of same birthdays.
    """
    random.seed(0)
    num_people = 23
    num_same = 2
    result = same_date(num_people, num_same)
    assert isinstance(result, bool)
    assert result == True

def test_birthday_prob():
    """
    Test the birthday_prob function from lec4_module.
    The function is tested with known values for number of people, number of same birthdays, and number of trials.
    """
    random.seed(0)
    num_people = 23
    num_same = 2
    num_trials = 1000
    result = birthday_prob(num_people, num_same, num_trials)
    assert isinstance(result, float)
    assert result == pytest.approx(0.507, abs=0.05)

def test_birthday_prob_more():
    """
    Test the birthday_prob function with varying number of people.
    The function is tested with 10, 20, 40, and 100 people.
    """
    random.seed(0)
    for num_people in [10, 20, 40, 100]:
        print('For', num_people,
              'est. prob. of a shared birthday is',
              birthday_prob(num_people, 2, 10000))
        numerator = math.factorial(366)
        denom = (366 ** num_people) * math.factorial(366 - num_people)
        print('Actual prob. for N = 100 =',
              1 - numerator / denom)
