import os
import sys 
import pytest
from add_path import add_path
add_path()

# Ensure repo root is on sys.path so lec2_menu can be imported consistently
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
import add_path  # project helper (keeps existing repo pattern)

from lec2_menu import Food, Menu, greedy, max_val, fast_max_val


def test_food_basic():
    f = Food("apple", 50, 60)
    assert f.get_value() == 50
    assert f.get_cost() == 60
    # Use pytest.approx to avoid floating point precision problems
    assert f.density() == pytest.approx(50 / 60, rel=1e-6)


def test_menu_and_greedy():
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


def test_memoized_equals_bruteforce():
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