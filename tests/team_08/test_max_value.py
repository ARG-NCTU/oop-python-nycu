import random
import pytest
from menu import *

def test_max_value():
    """
    Test the max_value function with 7 kinds of food, acorrding to 0/1 knapsack problem
    """
    # 7 kinds of food
    names = ['apple', 'banana', 'orange', 'pear', 'grape', 'kiwi', 'blueberry']
    # 7 kinds of value
    values = [15, 15, 20, 24, 27, 34, 55]
    # 7 kinds of calorie
    calories = [200, 130, 140, 80, 30, 100, 50]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    max_calories = 500
    # Test the max_value function
    val, taken = max_val(foods, max_calories)
    print('Total value of items taken(by max_value) =', val)
    for item in taken:
        print('   ', item)
    assert val == 160

    # Test the fast_max_val function
    val2, taken2 = fast_max_val(foods, max_calories)
    print('Total value of items taken(by fast_max_val) =', val2)
    for item in taken:
        print('   ', item)
    assert val == 160
