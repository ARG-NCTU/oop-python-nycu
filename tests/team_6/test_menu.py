import random
import pytest
import add_path
from mit_ocw_data_science.lec2.menu import *


def test_menu():
    names = ["huihsin", "chinju", "rk"]
    values = [10, 20, 30]
    calories = [50, 100, 150]
    expected_foods = [
        Food("huihsin", 10, 50),
        Food("chinju", 20, 100),
        Food("rk", 30, 150),
    ]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    print(menu)

    assert foods[0].get_cost() == expected_foods[0].get_cost()
    assert foods[1].get_value() == expected_foods[1].get_value()
    assert Menu.get_foods_str(foods) == \
        'huihsin: <10, 50>; chinju: <20, 100>; rk: <30, 150>; '

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
