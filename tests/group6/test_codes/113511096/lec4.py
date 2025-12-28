import random
import pytest

# NOTE: Commented out local dependency to ensure script runs standalone.
# from add_path import add_path
# add_path()

# ----------------------------- Dice Simulation -----------------------------
def run_sim(goal: str, num_trials: int, txt: str) -> None:
    """
    Run Monte Carlo simulation for dice rolls.

    Args:
        goal (str): Target sequence (e.g. '11111' means 5 consecutive 1s)
        num_trials (int): Number of simulation trials
        txt (str): Description text for output
    """
    # 1. Calculate Theoretical Probability
    # The probability of a specific sequence of length L is (1/6)^L
    seq_len = len(goal)
    actual_prob = 1 / (6 ** seq_len)

    # 2. Run Simulation
    # Optimization: random.choices is faster than calling random.choice in a loop
    population = ['1', '2', '3', '4', '5', '6']
    matches = 0

    for _ in range(num_trials):
        # Generate a random sequence of the same length as the goal
        result = "".join(random.choices(population, k=seq_len))
        if result == goal:
            matches += 1

    est_prob = matches / num_trials

    # 3. Output Results
    print(f"🎲 Simulation: {txt}")
    print(f"   Target Sequence      : {goal}")
    print(f"   Actual probability   : {actual_prob:.8f}")
    print(f"   Estimated probability: {est_prob:.8f}")
    print("-" * 40)


# ----------------------------- Birthday Problem -----------------------------
def has_shared_birthday(num_people: int, num_same: int) -> bool:
    """
    Return True if among num_people, at least num_same share a birthday.
    Includes optimization to return early if condition is met.
    """
    # Generate all birthdays at once using integers 0-365 (366 days)
    birthdays = random.choices(range(366), k=num_people)
    
    # Bucket sort approach to count frequencies
    counts = [0] * 366
    
    for day in birthdays:
        counts[day] += 1
        # Optimization: Return immediately if we hit the threshold
        if counts[day] >= num_same:
            return True
            
    return False


def run_birthday_experiments() -> None:
    """
    Run birthday problem simulation for multiple group sizes.
    """
    print("\n🎂 Birthday Problem Simulation")
    print(f"{'People':<10} | {'Probability':<15}")
    print("-" * 25)

    random.seed(0)  # fix seed for repeatability
    trials = 10_000 # Use underscore for readability
    num_same = 2
    people_list = [10, 20, 23, 30, 40, 50]

    for n in people_list:
        matches = 0
        for _ in range(trials):
            if has_shared_birthday(n, num_same):
                matches += 1
        
        prob = matches / trials
        print(f"{n:<10} | {prob:.4f}")
    print("-" * 25)


# ----------------------------- Main -----------------------------
def main():
    random.seed(0)  # fix seed to ensure reproducible results

    print("========== Lec4 Simulation ==========\n")

    # Part 1: Dice simulation
    run_sim("11111", 100_000, "Five consecutive 1s")
    run_sim("123", 100_000, "Sequence 1-2-3")
    run_sim("666", 100_000, "Triple 6s")

    # Part 2: Birthday problem
    run_birthday_experiments()

    print("\n=====================================")


if __name__ == "__main__":
    main()