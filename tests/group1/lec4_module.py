import random
from add_path import add_path
add_path()


# ----------------------------- Dice Simulation -----------------------------
def roll_die():
    """Return a random integer between 1 and 6."""
    return random.choice([1, 2, 3, 4, 5, 6])


def run_sim(goal, num_trials, txt):
    """
    Run Monte Carlo simulation for dice rolls.

    Args:
        goal (str): Target sequence (e.g. '11111' means 5 consecutive 1s)
        num_trials (int): Number of simulation trials
        txt (str): Description text for output
    """
    total = 0
    for _ in range(num_trials):
        result = ''.join(str(roll_die()) for _ in range(len(goal)))
        if result == goal:
            total += 1

    actual_prob = round(1 / (6 ** len(goal)), 8)
    est_prob = round(total / num_trials, 8)

    print(f"🎲 Simulation: {txt}")
    print(f"  Actual probability = {actual_prob}")
    print(f"  Estimated probability = {est_prob}\n")


# ----------------------------- Birthday Problem -----------------------------
def same_date(num_people, num_same):
    """
    Return True if among num_people individuals,
    at least num_same people share the same birthday.
    """
    possible_dates = range(366)  # 366 to include leap year
    birthdays = [0] * 366
    for _ in range(num_people):
        birth_date = random.choice(possible_dates)
        birthdays[birth_date] += 1
    return max(birthdays) >= num_same


def birthday_prob(num_people, num_same, num_trials):
    """
    Estimate the probability that in a group of num_people,
    at least num_same people share a birthday.
    """
    num_hits = 0
    for _ in range(num_trials):
        if same_date(num_people, num_same):
            num_hits += 1
    return num_hits / num_trials


def run_birthday_experiments():
    """
    Run birthday problem simulation for multiple group sizes.
    """
    print("🎂 Birthday Problem Simulation\n")
    random.seed(0)  # fix seed for repeatability

    trials = 10000
    num_same = 2
    people_list = [10, 20, 23, 30, 40, 50]

    for n in people_list:
        prob = birthday_prob(n, num_same, trials)
        print(f"For {n:2d} people → Probability of shared birthday ≈ {prob:.4f}")
    print()


# ----------------------------- Main -----------------------------
def main():
    random.seed(0)  # fix seed to ensure reproducible results

    print("========== Lec4 Simulation ==========\n")

    # Part 1: Dice simulation
    run_sim("11111", 100000, "Five consecutive 1s")
    run_sim("123", 100000, "Sequence 1-2-3")
    run_sim("666", 100000, "Triple 6s")

    # Part 2: Birthday problem
    run_birthday_experiments()

    print("=====================================")


if __name__ == "__main__":
    main()
