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
    # 建立一組 Food 物件的列表
    foods = [
        lec2.Food("apple", 50, 2),    # density = 25
        lec2.Food("banana", 30, 1),   # density = 30
        lec2.Food("pear", 40, 4)       # density = 10
    ]
    # 使用 greedy 函數，依照密度排序，設定最大成本為 3
    # 預期先選擇 density 最高的 banana (cost=1)，再選擇 apple (cost=2)，總成本為 3，總價值為 30+50=80
    selected_items, total_value = lec2.greedy(foods, 3, key_function=lambda f: f.density())
    selected_names = [item.name for item in selected_items]
    assert selected_names == ["banana", "apple"]
    assert total_value == pytest.approx(80)
    