import random
import pytest
import add_path
from menu import *


def test_menu():
    names = ["apple", "banana", "orange"]
    values = [105, 204, 301]
    calories = [509, 10, 15]
    expected_foods = [
        Food("apple", 105, 509),
        Food("banana", 204, 10),
        Food("orange", 301, 15),
    ]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    print(menu)

    assert foods[0].get_cost() == expected_foods[0].get_cost()
    assert foods[1].get_value() == expected_foods[1].get_value()
    assert not Menu.get_foods_str(foods) == \
        'apple: <10, 50>; banana: <20, 100>; orange: <30, 150>; '

def test_build_large_menu():
    menu = Menu()
    num_items = 10
    max_val = 86
    max_cost = 655
    menu.build_large_menu(num_items, max_val, max_cost)
    foods = menu.get_foods()

    print(menu)
    assert len(foods) == num_items
    if num_items > 0:
        assert foods[0].get_value() <= max_val
        assert foods[0].get_cost() <= max_cost
