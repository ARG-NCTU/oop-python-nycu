import os
import sys
import pytest

# --- Path Setup ---
# Cleaned up path logic: removed duplicate imports and ensured robust path addition.
try:
    from add_path import add_path
    add_path()
except ImportError:
    # Fallback: specific to the expected directory structure (repo root 2 levels up)
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from lec2_menu import Food, Menu, greedy, max_val, fast_max_val


# --- Fixtures (Setup Data) ---
@pytest.fixture
def sample_menu():
    """Creates a standard menu for reuse in multiple tests."""
    names = ["wine", "beer", "pizza", "burger", "fries", "cola", "apple", "donut"]
    values = [89, 90, 95, 1000, 900, 709, 50, 10]
    calories = [146, 145, 268, 374, 385, 140, 90, 190]
    return Menu(names, values, calories)


# --- Tests ---

def test_food_basic():
    """Test the basic properties of the Food class."""
    f = Food("apple", 50, 70)
    assert f.get_value() == 50
    assert f.get_cost() == 70
    assert f.get_density() == pytest.approx(50 / 70, rel=1e-6)
    assert f.get_name() == "apple"
    # Use pytest.approx for floating point comparisons
    assert f.density() == pytest.approx(50 / 60, rel=1e-6)
    assert str(f) == "apple: <50, 60>"  # added string representation check


def test_greedy_algorithm():
    """Test the greedy algorithm with specific small data."""
    names = ["a", "b", "c"]
    values = [10, 20, 30]
    calories = [1, 2, 3]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    
    # Test Greedy by Value
    taken, total_val = greedy(foods, 4, Food.get_value)
    
    # Expecting 'c' (30 val, 3 cal) first. Remaining cap = 1. 'a' (10 val, 1 cal) fits.
    # Total value should be 40.
    assert total_val == 40.0
    assert len(taken) == 2
    
    # Verify exact items taken
    taken_names = {item.get_name() for item in taken}
    assert taken_names == {"c", "a"}


def test_memoized_equals_bruteforce(sample_menu):
    """
    Ensure the fast (memoized) solution returns the exact same result 
    as the slow (brute force) solution.
    """
    foods = sample_menu.get_foods()
    max_units = 750

    # 1. Run Brute Force (Slow)
    val_brute, items_brute = max_val(foods, max_units) # pyright: ignore[reportCallIssue]

    # 2. Run Memoized (Fast)
    val_fast, items_fast = fast_max_val(foods, max_units) # type: ignore

    # 3. Compare Results
    assert val_brute == val_fast
    
    # Check data integrity: Sum of items must equal the returned value
    assert sum(item.get_value() for item in items_brute) == val_brute
    assert sum(item.get_value() for item in items_fast) == val_fast


def test_edge_cases():
    """Test empty menus or zero capacity."""
    empty_menu = Menu([], [], [])
    foods = empty_menu.get_foods()
    
    val, items = fast_max_val(foods, 100)
    assert val == 0
    assert items == []

    # Test with 0 capacity
    f = Food("apple", 50, 60)
    val, items = fast_max_val([f], 0)
    assert val == 0
    assert items == []