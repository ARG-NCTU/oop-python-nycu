import os
import sys
import pytest
import random

# --- Path Setup ---
# Robustly add the parent directory to sys.path to find the local modules
try:
    from add_path import add_path
    add_path()
except ImportError:
    # Fallback: specific to the expected directory structure
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from lec2_menu import Food, Menu, greedy, max_val, fast_max_val

# ==============================================================================
# 1. Fixtures & Setup 🛠️
# ==============================================================================

@pytest.fixture
def sample_menu():
    """Creates a standard menu for reuse in multiple tests."""
    names = ["wine", "beer", "pizza", "burger", "fries", "cola", "apple", "donut"]
    values = [89, 90, 95, 1000, 900, 709, 50, 10]
    calories = [146, 145, 268, 374, 385, 140, 90, 190]
    return Menu(names, values, calories)

# ==============================================================================
# 2. Basic Class Tests 🧪
# ==============================================================================

def test_food_basic():
    """Test the basic properties of the Food class."""
    # FIXED: Cost changed from 70 to 60 to match assertions below
    f = Food("apple", 50, 60)
    
    assert f.get_value() == 50
    assert f.get_cost() == 60
    assert f.get_name() == "apple"
    
    # Check density calculation
    expected_density = 50 / 60
    assert f.get_density() == pytest.approx(expected_density, rel=1e-6)
    
    # Check string representation
    assert str(f) == "apple: <50, 60>"

# ==============================================================================
# 3. Algorithm Tests (Greedy) 🏃
# ==============================================================================

@pytest.mark.parametrize("key_func, reverse, expected_total_val", [
    (Food.get_value, True, 40.0),       # Greedy by Value: Takes 'c'(30) + 'a'(10)
    (Food.get_cost, False, 30.0),       # Greedy by Cost (inverse): Takes 'a'(1) + 'b'(2) + 1/3 of 'c' (not fractional here) -> 'a', 'b'. Total val 30.
    (Food.get_density, True, 40.0),     # Greedy by Density: 'c'(10), 'b'(10), 'a'(10). All same density.
])
def test_greedy_strategies(key_func, reverse, expected_total_val):
    """
    Parametrized test to check different greedy strategies.
    Menu: a(10,1), b(20,2), c(30,3). Capacity: 4
    """
    names = ["a", "b", "c"]
    values = [10, 20, 30]
    calories = [1, 2, 3]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    
    taken, total_val = greedy(foods, 4, key_func, reverse)
    
    assert total_val == expected_total_val

# ==============================================================================
# 4. Algorithm Tests (Dynamic Programming) 🧠
# ==============================================================================

def test_memoized_equals_bruteforce(sample_menu):
    """
    Ensure the fast (memoized) solution returns the EXACT same result 
    as the slow (brute force) solution for small inputs.
    """
    
    
    foods = sample_menu.get_foods()
    max_units = 750

    # 1. Run Brute Force (Slow)
    val_brute, items_brute = max_val(foods, max_units)

    # 2. Run Memoized (Fast)
    val_fast, items_fast = fast_max_val(foods, max_units)

    # 3. Compare Results
    assert val_brute == val_fast
    
    # Check data integrity
    assert sum(item.get_value() for item in items_brute) == val_brute
    assert sum(item.get_value() for item in items_fast) == val_fast


def test_large_menu_performance():
    """
    Stress test: Ensure fast_max_val handles inputs that would
    cause the recursive max_val to hang (recursion depth/time limit).
    """
    # Create a large random menu
    n = 50  # 2^50 is impossible for brute force
    names = [f"item_{i}" for i in range(n)]
    values = [random.randint(10, 100) for _ in range(n)]
    costs = [random.randint(5, 50) for _ in range(n)]
    
    menu = Menu(names, values, costs)
    foods = menu.get_foods()
    
    # This should finish instantly with Memoization (DP)
    # If it hangs, the memoization logic is broken.
    val, items = fast_max_val(foods, 100)
    
    assert val >= 0
    assert len(items) <= len(foods)


def test_edge_cases():
    """Test empty menus or zero capacity."""
    empty_menu = Menu([], [], [])
    foods = empty_menu.get_foods()
    
    # Case 1: Empty food list
    val, items = fast_max_val(foods, 100)
    assert val == 0
    assert items == []

    # Case 2: Zero capacity
    f = Food("apple", 50, 60)
    val, items = fast_max_val([f], 0)
    assert val == 0
    assert items == []