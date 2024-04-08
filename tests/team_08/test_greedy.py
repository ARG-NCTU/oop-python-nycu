import random
import pytest
from menu import *

#test greedy algorithm
def test_greedy():
    items = [
        Food("apple", 20, 100),
        Food("banana", 30, 200),
        Food("cherry", 30, 300),
    ]
    max_cal = 400
    key_function = lambda x: 1 / Food.get_cost(x)

    result, total_val = greedy(items, max_cal, key_function)
    
    print('Total value: ', total_val)
    print(Menu.get_foods_str(result))

    assert total_val == 50
    assert Menu.get_foods_str(result) == "apple: <20, 100>; banana: <30, 200>; " 

def test_greedy2():
    """
    Test greedy algorithm with 5 items.
    And test it by 3 ways
    1. greedy by value to allocate the items.
    2. greedy by calories to allocate the items.
    3. greedy by density(value/calories) to allocate the items.
    """
    #set up
    names = ["apple", "banana", "cherry", "date", "elderberry"]
    values = [20, 30, 30, 40, 50]
    calories = [100, 200, 300, 600, 500]
    menu = Menu(names, values, calories)
    items = menu.get_foods()
    max_cal = 1000 # maximum calories
    # 1. greedy by value to allocate the items."       
    taken, val = greedy(items, max_cal, Food.get_value)
    assert val == 110
    assert Menu.get_foods_str(taken) == "elderberry: <50, 500>; banana: <30, 200>; cherry: <30, 300>; "
    # 2. greedy by calories to allocate the items.
    taken, val = greedy(items, max_cal, Food.get_cost)
    assert val == 90
    assert Menu.get_foods_str(taken) == "date: <40, 600>; cherry: <30, 300>; apple: <20, 100>; "
    # 3. greedy by density(value/calories) to allocate the items.
    taken, val = greedy(items, max_cal, Food.density)
    assert val == 80
    assert Menu.get_foods_str(taken) == "apple: <20, 100>; banana: <30, 200>; cherry: <30, 300>; "



