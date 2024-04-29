import add_path
from menu import *
import pytest

def test_menu():
    names = ["tea", "coco", "milk"]
    values = [10, 20, 30]
    calories = [1, 20, 120]
    expected_foods = [
        Food("tea", 10, 1),
        Food("coco", 20, 20),
        Food("milk", 30, 120),
    ]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    print(menu)

    assert foods[0].get_cost() == expected_foods[0].get_cost()
    assert foods[1].get_value() == expected_foods[1].get_value()
    assert foods[2].get_cost() == expected_foods[2].get_cost()
    assert Menu.get_foods_str(foods) == 'tea: <10, 1>; coco: <20, 20>; milk: <30, 120>; '

def test_build_large_menu():
    menu = Menu()
    num_items = 10
    max_val = 50
    max_cost = 400
    menu.build_large_menu(num_items, max_val, max_cost)
    foods = menu.get_foods()

    print(menu)
    assert len(foods) == num_items
    if num_items > 0:
        assert foods[0].get_value() <= max_val
        assert foods[0].get_cost() <= max_cost
