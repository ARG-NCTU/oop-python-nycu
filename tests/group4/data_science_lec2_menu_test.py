import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec4_functions import is_even_with_return,is_even_without_return,is_even,bisection_cuberoot_approx

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
import numpy as np
from src.mit_ocw_data_science.lec2.menu import Food, Menu, greedy  

def test_food_class():
    apple = Food("apple", 10, 50)
    assert apple.name == "apple"
    assert apple.get_value() == 10
    assert apple.get_cost() == 50
    assert abs(apple.density() - 0.2) < 1e-6
    assert str(apple) == "apple: <10, 50>"

def test_menu_class():
    names = ["apple", "banana", "cherry"]
    values = [10, 20, 15]
    calories = [50, 100, 75]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    assert len(foods) == 3
    assert str(menu) == "apple: <10, 50>; banana: <20, 100>; cherry: <15, 75>; "

# def test_greedy_function():
#     items = [
#         Food("item1", 10, 20),
#         Food("item2", 20, 30),
#         Food("item3", 30, 50)
#     ]
#     max_cost = 50

#     # Test greedy by value
#     selected_by_value = greedy(items, max_cost, lambda x: x.get_value())
#     assert selected_by_value[0].name == "item3"
#     assert selected_by_value[1].name == "item2"

#     # Test greedy by cost
#     selected_by_cost = greedy(items, max_cost, lambda x: -x.get_cost())
#     assert selected_by_cost[0].name == "item1"
#     assert selected_by_cost[1].name == "item2"

#     # Test greedy by density
#     selected_by_density = greedy(items, max_cost, lambda x: x.density())
#     assert selected_by_density[0].name == "item1"
#     assert selected_by_density[1].name == "item2"


