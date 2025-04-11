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
    
    food2 = lec2.Food("neko", 1, 105000)
    assert food2.get_value() == 1
    assert food2.get_cost() == 105000
    assert food2.density() == pytest.approx(1 / 105000)
    assert str(food2) == "neko: <1, 105000>"