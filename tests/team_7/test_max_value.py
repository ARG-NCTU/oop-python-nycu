import random
import pytest
import add_path
from mit_ocw_data_science.lec2.menu import *

def test_7_max_value():

    names = ['wine', 'beer', 'whisky', 'vodka', 'water',
             'cola', 'milk', 'sprite', 'tea']
    values = [200, 30, 250, 150, 10, 20, 30, 20]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    max_units = 1000
    print_items = True

    print('Use search tree to allocate', max_units,
          'calories')
    val, taken = max_val(foods, max_units)
    print('Total value of items taken =', val)
    if print_items:
        for item in taken:
            print('   ', item)

@pytest.mark.slow
def test_7_max_val_large_menu():

    menu = Menu()
    for num_items in (10, 20, 30, 40, 50):
        print('Try a menu with', num_items, 'items')
        menu.build_large_menu(num_items, 100, 300)
        foods = menu.get_foods()
        val, taken = max_val(foods, 1000)

def test_7_fast_max_val_large_menu():

    menu = Menu()
    for num_items in (10, 20, 30, 40, 50):
        print('Try a fast menu with', num_items, 'items')
        menu.build_large_menu(num_items, 100, 300)
        foods = menu.get_foods()
        val, taken = fast_max_val(foods, 1000)


