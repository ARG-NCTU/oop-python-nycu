import random
def roll_die():
    """Returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])
def run_sim(goal, num_trials, txt):
    total = 0
    for i in range(num_trials):
        result = ''
        for j in range(len(goal)):
            result += str(roll_die())
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=',
          round(1/(6**len(goal)), 8))
    est_probability = round(total/num_trials, 8)
    print('Estimated Probability of', txt, '=',
          round(est_probability, 8))
def same_date(num_people, num_same):
    possible_dates = range(366)
    # possible_dates = 4*list(range(0, 57)) + [58]\
    #                 + 4*list(range(59, 366))\
    #                 + 4*list(range(180, 270))
    birthdays = [0] * 366
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
def test_roll_die():
    """Test roll_die function"""
    # Test if the function returns an integer
    result = roll_die()
    assert isinstance(result, int), "roll_die should return an integer"
    # Test if the result is between 1 and 6
    assert 1 <= result <= 6, "roll_die should return a value between 1 and 6"
    print("roll_die test passed!")
def test_run_sim():
    """Test run_sim function"""
    # Test if the function returns None
    result = run_sim("123", 1000, "test")
    assert result is None, "run_sim should return None"
    # Test if the output is printed correctly
    # This is a bit tricky to test directly, but we can check if the function runs without errors
    try:
        run_sim("123", 1000, "test")
    except Exception as e:
        assert False, f"run_sim raised an exception: {e}"
    print("run_sim test passed!")
def test_same_date():
    """Test same_date function"""
    # Test if the function returns a boolean
    result = same_date(23, 2)
    assert isinstance(result, bool), "same_date should return a boolean"
    # Test if the function works for a known case
    assert same_date(23, 2) == True, "same_date should return True for 23 people and 2 same birthdays"
    print("same_date test passed!")
def test_birthday_prob():
    """Test birthday_prob function"""
    # Test if the function returns a float
    result = birthday_prob(23, 2, 1000)
    assert isinstance(result, float), "birthday_prob should return a float"
    # Test if the result is between 0 and 1
    assert 0 <= result <= 1, "birthday_prob should return a value between 0 and 1"
    print("birthday_prob test passed!")
# Run tests
if __name__ == "__main__":
    test_roll_die()
    test_run_sim()
    test_same_date()
    test_birthday_prob()

# The tests should pass without any
# assertion errors. If they do, the functions are working as expected.
# Note: The actual output of the functions is not tested here, only the types and ranges of the outputs.
# The tests should pass without any
# assertion errors. If they do, the functions are working as expected.
# Note: The actual output of the functions is not tested here, only the types and ranges of the outputs.
# The tests should pass without any