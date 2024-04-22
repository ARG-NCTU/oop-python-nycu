import random
import pytest
import add_path
from menu import *

def test_16_greedy():
    items = [
        Food("guava", 30, 200),
        Food("grape", 20, 100),
        Food("watermelon", 50, 300),
    ]
    constraint = 100
    key_function = lambda x: 1 / Food.get_cost(x)

    taken, val = greedy(items, constraint, key_function)
    
    print('Total value of items taken =', val)
    print(Menu.get_foods_str(taken))

    assert val == 20
    assert Menu.get_foods_str(taken) == "grape: <20, 100>; "

def test_16_greedys():

    names = ['water', 'juice', 'soda', 'cola', 'milkshake']
    values = [10, 30, 30, 40, 50]
    calories = [100, 100, 200, 400, 300]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    max_units = 800

    print('Use greedy by value to allocate', max_units,
          'calories')
    taken, val = greedy(foods, max_units, Food.get_value)
    expected_str = Menu.get_foods_str(taken)
    assert val == 120
    assert expected_str == "milkshake: <50, 300>; cola: <40, 400>; juice: <30, 100>; "

    print('\nUse greedy by cost to allocate', max_units,
          'calories')
    taken, val = greedy(foods, max_units,
               lambda x: 1/Food.get_cost(x))
    expected_str = Menu.get_foods_str(taken)
    assert val == 120
    assert expected_str == \
        "water: <10, 100>; juice: <30, 100>; soda: <30, 200>; milkshake: <50, 300>; "
    
    print('\nUse greedy by density to allocate', max_units,
          'calories')
    taken, val = greedy(foods, max_units, Food.density)
    expected_str = Menu.get_foods_str(taken)
    assert val == 120
    assert expected_str == \
        "juice: <30, 100>; milkshake: <50, 300>; soda: <30, 200>; water: <10, 100>; "