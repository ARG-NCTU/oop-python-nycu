import add_path
import pytest
import mit_ocw_data_science.lec2.menu as lec2

def test_food():
    food = lec2.Food("apple", 20, 50)
    assert food.get_value() == 20
    assert food.get_cost() == 50
    assert food.density() == 20/50
    assert str(food) == "apple: <20, 50>"

def test_menu():
    names = ["apple", "banana", "cherry"]
    values = [20, 10, 40]
    calories = [50, 60, 70]
    menu = lec2.Menu(names, values, calories)

    foods = menu.get_foods()
    assert len(foods) == 3
    assert str(foods[0]) == "apple: <20, 50>"
    assert str(foods[1]) == "banana: <10, 60>"
    assert str(foods[2]) == "cherry: <40, 70>"

def test_greedy():
    names = ["apple", "banana", "cherry"]
    values = [20, 10, 40]
    calories = [50, 60, 70]
    menu = lec2.Menu(names, values, calories)

    result, total_value = lec2.greedy(menu.get_foods(), 100, key_function=lambda x: x.get_value())
    assert total_value == 60  # Should take apple (20) and cherry (40)
    assert len(result) == 2
    assert str(result[0]) == "cherry: <40, 70>"
    assert str(result[1]) == "apple: <20, 50>"

def test_max_val():
    names = ["apple", "banana", "cherry"]
    values = [20, 10, 40]
    calories = [50, 60, 70]
    menu = lec2.Menu(names, values, calories)

    total_value, selected_items = lec2.max_val(menu.get_foods(), 100)
    assert total_value == 60
    assert len(selected_items) == 2
    assert str(selected_items[0]) == "cherry: <40, 70>"
    assert str(selected_items[1]) == "apple: <20, 50>"
    
def test_fast_max_val():
    names = ["apple", "banana", "cherry"]
    values = [20, 10, 40]
    calories = [50, 60, 70]
    menu = lec2.Menu(names, values, calories)

    total_value, selected_items = lec2.fast_max_val(menu.get_foods(), 100)
    assert total_value == 60
    assert len(selected_items) == 2
    assert str(selected_items[0]) == "cherry: <40, 70>"
    assert str(selected_items[1]) == "apple: <20, 50>"
