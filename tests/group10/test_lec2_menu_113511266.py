import pytest
from practice.lec2_menu import Food, Menu, greedy, max_val, fast_max_val

def test_food():
    food = Food("apple", 50, 30)
    assert food.get_value() == 50
    assert food.get_cost() == 30
    assert food.density() == 50 / 30
    assert str(food) == "apple: <50, 30>"

def test_menu():
    names = ["apple", "banana", "cherry"]
    values = [50, 60, 70]
    calories = [30, 40, 50]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    assert len(foods) == 3
    assert str(foods[0]) == "apple: <50, 30>"
    assert str(foods[1]) == "banana: <60, 40>"
    assert str(foods[2]) == "cherry: <70, 50>"

def test_greedy():
    names = ["apple", "banana", "cherry"]
    values = [50, 60, 70]
    calories = [30, 40, 50]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    # Test greedy by value
    result, total_value = greedy(foods, 100, lambda x: x.get_value())
    assert total_value == 130
    assert len(result) == 2
    assert str(result[0]) == "cherry: <70, 50>"
    assert str(result[1]) == "banana: <60, 40>"

    # Test greedy by cost
    result, total_value = greedy(foods, 100, lambda x: 1 / x.get_cost())
    assert total_value == 110
    assert len(result) == 2
    assert str(result[0]) == "apple: <50, 30>"
    assert str(result[1]) == "banana: <60, 40>"

    # Test greedy by density
    result, total_value = greedy(foods, 100, lambda x: x.density())
    assert total_value == 110
    assert len(result) == 2
    assert str(result[0]) == "apple: <50, 30>"
    assert str(result[1]) == "banana: <60, 40>"

def test_max_val():
    names = ["apple", "banana", "cherry"]
    values = [50, 60, 70]
    calories = [30, 40, 50]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    # Test max_val
    total_value, items = max_val(foods, 100)
    assert total_value == 130
    assert len(items) == 2
    assert str(items[0]) == "cherry: <70, 50>"
    assert str(items[1]) == "banana: <60, 40>"

def test_fast_max_val():
    names = ["apple", "banana", "cherry"]
    values = [50, 60, 70]
    calories = [30, 40, 50]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()

    # Test fast_max_val
    total_value, items = fast_max_val(foods, 100)
    assert total_value == 130
    assert len(items) == 2
    assert str(items[0]) == "cherry: <70, 50>"
    assert str(items[1]) == "banana: <60, 40>"