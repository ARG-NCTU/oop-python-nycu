import add_path
import pytest
import mit_ocw_data_science.lec2.menu.py as lec2
import random

def test_food():
    # 測試 Food 類別的基本功能
    food = lec2.Food("apple", 50, 95)
    assert food.get_value() == 50
    assert food.get_cost() == 95
    assert food.density() == pytest.approx(50 / 95)
    assert str(food) == "apple: <50, 95>"


