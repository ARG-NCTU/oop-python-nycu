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