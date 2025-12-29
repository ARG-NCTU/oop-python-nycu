import os
import sys 
import pytest
from add_path import add_path
add_path()

# Ensure repo root is on sys.path so lec2_menu can be imported consistently
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import add_path  # project helper (keeps existing repo pattern)

from lec2_menu import Food, Menu, greedy, max_val, fast_max_val


# ===== Food Class Tests =====

def test_food_basic():
    """Test basic Food class functionality."""
    f = Food("apple", 50, 60)
    assert f.get_value() == 50
    assert f.get_cost() == 60
    # Use pytest.approx to avoid floating point precision problems
    assert f.density() == pytest.approx(50 / 60, rel=1e-6)


def test_food_zero_cost():
    """Test Food with zero cost (edge case)."""
    f = Food("weightless", 100, 0)
    assert f.get_value() == 100
    assert f.get_cost() == 0
    # Density calculation should handle zero division gracefully or raise error
    with pytest.raises(ZeroDivisionError):
        _ = f.density()


def test_food_string_representation():
    """Test Food __str__ method."""
    f = Food("banana", 40, 30)
    assert "banana" in str(f)
    assert "40" in str(f)
    assert "30" in str(f)


# ===== Menu and Greedy Algorithm Tests =====

def test_menu_and_greedy():
    """Test Menu creation and greedy algorithm."""
    names = ["a", "b", "c"]
    values = [10, 20, 30]
    calories = [1, 2, 3]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    taken, total = greedy(foods, 4, Food.get_value)
    assert total == 40.0
    assert len(taken) == 2
    # ensure items in taken are from the provided foods
    taken_names = {item.name for item in taken}
    assert taken_names.issubset({*names})


def test_greedy_empty_list():
    """Test greedy with empty food list."""
    menu = Menu()
    taken, total = greedy(menu.get_foods(), 10, Food.get_value)
    assert total == 0.0
    assert len(taken) == 0


def test_greedy_by_density():
    """Test greedy algorithm sorted by density."""
    names = ["high_density", "low_density"]
    values = [100, 50]
    calories = [10, 100]  # First has density 10, second has 0.5
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    taken, total = greedy(foods, 15, Food.density)
    # Should pick high_density first
    assert len(taken) >= 1
    assert taken[0].name == "high_density"


# ===== Dynamic Programming Tests (max_val vs fast_max_val) =====

def test_memoized_equals_bruteforce():
    """Test that memoized approach matches brute force."""
    names = ["apple", "banana", "cake"]
    values = [50, 40, 100]
    calories = [60, 30, 150]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    v1, items1 = max_val(foods, 200)
    v2, items2 = fast_max_val(foods, 200)
    assert v1 == v2
    # Optional sanity: chosen items sums should match returned value
    assert sum(item.get_value() for item in items1) == v1
    assert sum(item.get_value() for item in items2) == v2


def test_knapsack_zero_capacity():
    """Test knapsack with zero capacity (edge case)."""
    names = ["apple"]
    values = [50]
    calories = [60]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    v1, items1 = max_val(foods, 0)
    v2, items2 = fast_max_val(foods, 0)
    assert v1 == 0
    assert v2 == 0
    assert len(items1) == 0
    assert len(items2) == 0


def test_knapsack_single_item():
    """Test knapsack with single item."""
    names = ["expensive"]
    values = [100]
    calories = [50]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    
    # Capacity enough for item
    v1, items1 = max_val(foods, 50)
    v2, items2 = fast_max_val(foods, 50)
    assert v1 == v2 == 100
    assert len(items1) == len(items2) == 1
    
    # Capacity insufficient
    v1, items1 = max_val(foods, 30)
    v2, items2 = fast_max_val(foods, 30)
    assert v1 == v2 == 0
    assert len(items1) == len(items2) == 0


def test_knapsack_performance_difference():
    """Verify that memoized approach is available (doesn't timeout on reasonable input)."""
    # Create a moderate-sized problem
    names = [f"item_{i}" for i in range(15)]
    values = list(range(1, 16))
    calories = list(range(15, 0, -1))
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    
    # Both should complete quickly; memoized much faster
    v1, items1 = max_val(foods, 30)
    v2, items2 = fast_max_val(foods, 30)
    assert v1 == v2