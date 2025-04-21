import add_path
import pytest
import mit_ocw_data_science.lec2.menu as lec2
import random

def test_food():
    # 測試 Food 類別的基本功能
    food = lec2.Food("lemon_water", 15, 1)
    assert food.get_value() == 15
    
    assert food.get_cost() == 1
    assert food.density() == pytest.approx(15 / 1)
    
    assert str(food) == "food: <15, 1>"
    
    food_I = lec2.Food("black_tea", 114, 514)
    assert food_I.get_value() == 114
    assert food_I.get_cost() == 514
    assert food_I.density() == pytest.approx(114 / 514)
    assert str(food_I) == "black_tea: <114, 514>"

def test_menu():
    jojo=lec2.Menu(["lemon_water", "black_tea"], [15, 114], [1, 514])
    assert len(jojo.get_foods()) == 2
    assert str(jojo) == "lemon_water: <15, 1>; black_tea: <114, 514>; "

    pro= lec2.Menu()
    assert len(pro.get_foods()) == 0
    pro.build_large_menu(["beef","noodles","water","coffee"], 4,100)
    assert len(pro.get_foods()) == 4

def test_greedy():
    # 測試 greedy 函數
    menu = lec2.Menu(["lemon_water", "black_tea"], [15, 114], [1, 514])
    assert menu.greedy(100) == ["black_tea", "lemon_water"]
    
    menu2 = lec2.Menu(["beef", "noodles", "water", "coffee"], [4, 100, 1, 10], [100, 4, 1, 10])
    assert menu2.greedy(100) == ["beef", "water"]
    
    