import random
import pytest
import add_path
from mit_ocw_data_science.lec2.menu import *


def test_menu():
    names = ["rice", "noodles", "dumplings"]
    values = [100, 200, 300]
    calories = [500, 1000, 1500]
    expected_foods = [
        Food("rice", 100, 500),
        Food("noodles", 200, 1000),
        Food("dumplings", 300, 1500),
    ]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    print(menu)

    assert foods[0].get_cost() == expected_foods[0].get_cost()
    assert foods[1].get_value() == expected_foods[1].get_value()
    assert Menu.get_foods_str(foods) == \
        'rice: <100, 500>; noodles: <200, 1000>; dumplings: <300, 1500>; '

def test_build_large_menu():
    menu = Menu()
    num_items = 10
    max_val = 500
    max_cost = 4000
    menu.build_large_menu(num_items, max_val, max_cost)
    foods = menu.get_foods()

    print(menu)
    assert len(foods) == num_items
    if num_items > 0:
        assert foods[0].get_value() <= max_val
        assert foods[0].get_cost() <= max_cost
