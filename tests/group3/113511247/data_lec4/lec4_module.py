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
          round(1/(6**len(goal)), 8)) #eight decimal places
    est_probability = round(total/num_trials, 8)
    print('Estimated Probability of', txt, '=',
          round(est_probability, 8))

def same_date(num_people, num_same):
    # guess there will be at least num_same people with the same birthday
    possible_dates = range(366) #including 2/29
    # weighted birthdays:
    # possible_dates = 4*list(range(0, 57)) + [58]\
    #                 + 4*list(range(59, 366))\
    #                 + 4*list(range(180, 270))
    birthdays = [0] * 366 # a list of 366 elements, all 0
    for p in range(num_people):
        birth_date = random.choice(possible_dates)
        birthdays[birth_date] += 1
        # index means the birthday date
        # value means the number of people born on that date
    return max(birthdays) >= num_same

def birthday_prob(num_people, num_same, num_trials):
    num_hits = 0
    for t in range(num_trials):
        if same_date(num_people, num_same):
            num_hits += 1
    return num_hits / num_trials