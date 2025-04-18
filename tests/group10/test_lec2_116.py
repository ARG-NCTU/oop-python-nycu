import add_path
import pytest
import mit_ocw_data_science.lec2.menu as lec2
import random

def test_food():
    # 測試 Food 類別的基本功能
    food = lec2.Food("apple", 50, 95)
    assert food.get_value() == 50
    assert food.get_cost() == 95
    assert food.density() == pytest.approx(50 / 95)
    assert str(food) == "apple: <50, 95>"
    
    food2 = lec2.Food("neko", 1, 105000)
    assert food2.get_value() == 1
    assert food2.get_cost() == 105000
    assert food2.density() == pytest.approx(1 / 105000)
    assert str(food2) == "neko: <1, 105000>"
    

def test_menu():
    # 測試 Menu 類別的基本功能
    names = ["apple", "banana", "cherry"]
    values = [50, 60, 70]
    calories = [95, 105, 120]
    menu = lec2.Menu(names, values, calories)

    # 測試 get_foods 方法
    foods = menu.get_foods()
    assert len(foods) == 3
    assert str(foods[0]) == "apple: <50, 95>"
    assert str(foods[1]) == "banana: <60, 105>"
    assert str(foods[2]) == "cherry: <70, 120>"

    # 測試 __str__ 方法
    assert str(menu) == "apple: <50, 95>; banana: <60, 105>; cherry: <70, 120>; "

def test_greedy():
    names = ["Chips", "Candy", "Instant Noodles"]
    values = [10, 20, 15]
    calories = [5, 10, 5]
    menu = lec2.Menu(names, values, calories)
    
    result, total_value = lec2.greedy(menu.get_foods(), 10, key_function=lambda x: x.get_value())
    assert total_value == 20  # Should take Chips (10) and Instant Noodles (15)
    assert len(result) == 1
    
def test_max_val():
    names = ["Chips", "Candy", "Instant Noodles"]
    values = [10, 20, 15]
    calories = [5, 10, 5]
    menu = lec2.Menu(names, values, calories)
    
    total_value, selected_items = lec2.max_val(menu.get_foods(), 10)
    assert total_value == 25
    assert len(selected_items) == 2
    
def test_fast_max_val():
    names = ["Chips", "Candy", "Instant Noodles"]
    values = [10, 20, 15]
    calories = [5, 10, 5]
    menu = lec2.Menu(names, values, calories)
    
    total_value, selected_items = lec2.fast_max_val(menu.get_foods(), 10, memo={})
    assert total_value == 25
    assert len(selected_items) == 2
