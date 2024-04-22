import random

def roll_die():
    """Returns a random int between 1 and 6"""
    return random.choice([1, 2, 3, 4, 5, 6])

def run_sim(goal, num_trials, txt):
    """
    Simulates rolling a die multiple times and calculates the probability of a specific outcome.

    Parameters:
    - goal (str): The desired outcome of the dice rolls.
    - num_trials (int): The number of times to simulate the dice rolls.
    - txt (str): A description of the desired outcome.

    Returns:
    None
    """
    total = 0
    for i in range(num_trials):
        result = ''
        for j in range(len(goal)):
            result += str(roll_die())
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=', round(1/(6**len(goal)), 8))
    est_probability = round(total/num_trials, 8)
    print('Estimated Probability of', txt, '=', round(est_probability, 8))

def same_date(num_people, num_same):
    """
    Determines if there are at least `num_same` people with the same birth date
    among `num_people` randomly generated birth dates.

    Args:
        num_people (int): The number of people to generate birth dates for.
        num_same (int): The minimum number of people with the same birth date.

    Returns:
        bool: True if there are at least `num_same` people with the same birth date,
              False otherwise.
    """
    possible_dates = range(366)
    birthdays = [0] * 366
    for p in range(num_people):
        birth_date = random.choice(possible_dates)
        birthdays[birth_date] += 1
    return max(birthdays) >= num_same

def birthday_prob(num_people, num_same, num_trials):
    """
    Calculate the probability of having at least 'num_same' people with the same birthday
    in a group of 'num_people' for 'num_trials' trials.

    Args:
        num_people (int): The number of people in the group.
        num_same (int): The number of people with the same birthday.
        num_trials (int): The number of trials to run.

    Returns:
        float: The probability of having at least 'num_same' people with the same birthday.

    """
    num_hits = 0
    for t in range(num_trials):
        if same_date(num_people, num_same):
            num_hits += 1
    return num_hits / num_trials

