import random
import pytest
from menu import *

def test_max_value():

    names = ['wine', 'beer', 'pizza', 'burger', 'fries',
             'cola', 'apple', 'donut', 'cake']
    values = [89, 90, 95, 100, 90, 79, 50, 10]
    calories = [123, 154, 258, 354, 365, 150, 95, 195]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    max_units = 750
    print_items = True

    print('Use search tree to allocate', max_units,
          'calories')
    val, taken = max_val(foods, max_units)
    print('Total value of items taken =', val)
    if print_items:
        for item in taken:
            print('   ', item)

def test_max_val_large_menu():

    menu = Menu()
    for num_items in (5, 10, 15, 20, 25, 30, 35):
        print('Try a menu with', num_items, 'items')
        menu.build_large_menu(num_items, 90, 250)
        foods = menu.get_foods()
        val, taken = max_val(foods, 750)

def test_fast_max_val_large_menu():

    menu = Menu()
    for num_items in (5, 10, 15, 20, 25, 30, 35, 40, 45):
        print('Try a fast menu with', num_items, 'items')
        menu.build_large_menu(num_items, 90, 250)
        foods = menu.get_foods()
        val, taken = fast_max_val(foods, 750)


