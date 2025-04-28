import random
import pytest
import math

#funcs

def roll_die():
    """Returns a random int between 1 and 6*2"""
    return random.choice([i for i in range(1, 13)])

def run_sim(goal, num_trials, txt):
    total = 0
    for i in range(num_trials):
        result = ''
        for j in range(len(goal)):
            result += str(roll_die())
        if result == goal:
            total += 1
    print('Ideal probability of', txt, '=',
          round(1/(12**len(goal)), 8))
    est_probability = round(total/num_trials, 8)
    print('Estimated Probability of', txt, '=',
          round(est_probability, 8))

def same_date(num_people, num_same):
    possible_dates = range(366)
    # possible_dates = 4*list(range(0, 57)) + [58]\
    #                 + 4*list(range(59, 366))\
    #                 + 4*list(range(180, 270))
    birthdays = [0] * 366
    #print(type(birthdays))
    for p in range(num_people):
        birth_date = random.choice(possible_dates)
        birthdays[birth_date] += 1
    return max(birthdays) >= num_same

def birthday_prob(num_people, num_same, num_trials):
    num_hits = 0
    for t in range(num_trials):
        if same_date(num_people, num_same):
            num_hits += 1
    return num_hits / num_trials


#main


def test_roll_die():
    # Test that the function returns an int between 1 and 12
    for i in range(50):
        result = roll_die()
        assert isinstance(result, int)
        assert result >= 1 and result <= 12
        print(result)

def test_roll():
    n = 10
    result = ''
    for i in range(n):
        result = result + str(roll_die())
    print(f'test_roll: {result}')

def test_run_sim():
    # Test with a known goal and numTrials
    random.seed(0)
    goal = '11211'
    num_trials = 10000
    run_sim(goal, num_trials, '12111')

def test_same_date():
    # Test with known values for numPeople and numSame
    random.seed(0)
    num_people = 23
    num_same = 2
    result = same_date(num_people, num_same)
    assert isinstance(result, bool)
    assert result == True

def test_birthday_prob():
    # Test with known values for numPeople, numSame, and numTrials
    random.seed(0)
    num_people = 23
    num_same = 2
    num_trials = 1000
    result = birthday_prob(num_people, num_same, num_trials)
    assert isinstance(result, float)
    assert result == pytest.approx(0.507, abs=0.05)

def test_birthday_prob_more():
    random.seed(0)
    for num_people in [10, 20, 40, 100]:
        print('For', num_people,
              'est. prob. of a shared birthday is',
              birthday_prob(num_people, 2, 10000))
        numerator = math.factorial(366)
        denom = (366 ** num_people) * math.factorial(366 - num_people)
        print('Actual prob. for N = 100 =',
              1 - numerator / denom)

#test_roll_die()
#same_date(num_people=5, num_same=5)
test_roll()