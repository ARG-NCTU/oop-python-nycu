import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from lec2_menu import Food, Menu, greedy, max_val, fast_max_val


def test_food_basic():
    f = Food("apple", 50, 60)
    assert f.get_value() == 50
    assert f.get_cost() == 60
    assert round(f.density(), 3) == round(50/60, 3)


def test_menu_and_greedy():
    names = ["a", "b", "c"]
    values = [10, 20, 30]
    calories = [1, 2, 3]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    taken, total = greedy(foods, 4, Food.get_value)
    assert total == 40.0
    assert len(taken) == 2


def test_memoized_equals_bruteforce():
    names = ["apple", "banana", "cake"]
    values = [50, 40, 100]
    calories = [60, 30, 150]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    v1, items1 = max_val(foods, 200)
    v2, items2 = fast_max_val(foods, 200)
    assert v1 == v2
