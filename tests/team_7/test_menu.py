import random
import pytest
import add_path
from mit_ocw_data_science.lec2.menu import *


def test_7_menu():
    names = ["steak", "spaghetti", "lasagne"]
    values = [600, 300, 400]
    calories = [400, 250, 650]
    expected_foods = [
        Food("steak", 600, 400),
        Food("spaghetti", 300, 250),
        Food("lasagne", 400, 650),
    ]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    print(menu)

    assert foods[0].get_cost() == expected_foods[0].get_cost()
    assert foods[1].get_value() == expected_foods[1].get_value()
    assert Menu.get_foods_str(foods) == \
        'steak: <600, 400>; spaghetti: <300, 250>; lasagne: <400, 650>; '

def test_7_build_large_menu():
    menu = Menu()
    num_items = 20
    max_val = 100
    max_cost = 500
    menu.build_large_menu(num_items, max_val, max_cost)
    foods = menu.get_foods()

    print(menu)
    assert len(foods) == num_items
    if num_items > 0:
        assert foods[0].get_value() <= max_val
        assert foods[0].get_cost() <= max_cost

