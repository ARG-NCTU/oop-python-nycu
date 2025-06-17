import add_path
import pytest
import lec2 as lec2
import random
import copy

def test_food():
    food = lec2.Food("mango", 70, 80)
    assert food.get_value() == 70
    assert food.get_cost() == 80
    assert food.density() == pytest.approx(70 / 80)
    assert str(food) == "mango: <70, 80>"
    
    food2 = lec2.Food("puffin", 3, 50000)
    assert food2.get_value() == 3
    assert food2.get_cost() == 50000
    assert food2.density() == pytest.approx(3 / 50000)
    assert str(food2) == "puffin: <3, 50000>"
    

def test_menu():
    names = ["mango", "peach", "plum"]
    values = [70, 80, 90]
    calories = [80, 90, 110]
    menu = lec2.Menu(names, values, calories)

    foods = menu.get_foods()
    assert len(foods) == 3
    assert str(foods[0]) == "mango: <70, 80>"
    assert str(foods[1]) == "peach: <80, 90>"
    assert str(foods[2]) == "plum: <90, 110>"

    assert str(menu) == "mango: <70, 80>; peach: <80, 90>; plum: <90, 110>; "

def test_greedy():
    names = ["juice", "soda", "water"]
    values = [40, 25, 90]
    calories = [20, 12, 30]
    menu = lec2.Menu(names, values, calories)
    
    result, total_value = lec2.greedy(menu.get_foods(), 12, key_function=lambda x: x.get_value())
    assert total_value == 25
    assert len(result) >= 1

def test_max_val():
    names = ["juice", "soda", "water"]
    values = [15, 25, 18]
    calories = [6, 12, 6]
    menu = lec2.Menu(names, values, calories)
    
    total_value, selected_items = lec2.max_val(menu.get_foods(), 12)
    assert total_value == 33  # 15 + 18 fits in 12 calories (6+6)
    assert len(selected_items) >= 1

def test_fast_max_val():
    names = ["juice", "soda", "water"]
    values = [15, 25, 18]
    calories = [6, 12, 6]
    menu = lec2.Menu(names, values, calories)
    
    total_value, selected_items = lec2.fast_max_val(menu.get_foods(), 12, memo={})
    assert total_value == 33
    assert len(selected_items) >= 1

