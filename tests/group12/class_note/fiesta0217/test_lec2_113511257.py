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