import pytest
#!/usr/bin/env python3

import add_path
from mit_ocw_data_science.lec2.menu import Food, Menu, greedy, max_val, fast_max_val

def test_food_get_value():
    food = Food("apple", 10, 50)
    assert food.get_value() == 10

def test_food_get_cost():
    food = Food("apple", 10, 50)
    assert food.get_cost() == 50

def test_food_density():
    food = Food("apple", 10, 50)
    assert food.density() == 0.2

def test_food_str():
    food = Food("apple", 10, 50)
    assert str(food) == "apple: <10, 50>"

def test_menu_get_foods():
    names = ["apple", "banana"]
    values = [10, 20]
    calories = [50, 100]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    assert len(foods) == 2
    assert foods[0].name == "apple"
    assert foods[1].name == "banana"

def test_menu_get_foods_str():
    names = ["apple", "banana"]
    values = [10, 20]
    calories = [50, 100]
    menu = Menu(names, values, calories)
    foods_str = Menu.get_foods_str(menu.get_foods())
    assert foods_str == "apple: <10, 50>; banana: <20, 100>; "

def test_menu_str():
    names = ["apple", "banana"]
    values = [10, 20]
    calories = [50, 100]
    menu = Menu(names, values, calories)
    assert str(menu) == "apple: <10, 50>; banana: <20, 100>; "

def test_greedy():
    foods = [Food("apple", 10, 50), Food("banana", 20, 100), Food("cherry", 15, 75)]
    result, total_value = greedy(foods, 150, Food.density)
    assert total_value == 30
    assert len(result) == 2
    assert result[0].name == "apple"
    assert result[1].name == "banana"

def test_max_val():
    foods = [Food("apple", 10, 50), Food("banana", 20, 100), Food("cherry", 15, 75)]
    total_value, items = max_val(foods, 150)
    assert total_value == 30
    assert items[0].name == "banana"
    assert items[1].name == "apple"

def test_fast_max_val():
    foods = [Food("apple", 10, 50), Food("banana", 20, 100), Food("cherry", 15, 75)]
    total_value, items = fast_max_val(foods, 150)
    assert total_value == 30
    assert items[0].name == "banana"
    assert items[1].name == "apple"
