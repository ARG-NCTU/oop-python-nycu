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
    # Food 的 __str__ 方法回傳: "lemon_water: <15, 1>"
    assert str(food) == "lemon_water: <15, 1>"
    
    food_I = lec2.Food("black_tea", 114, 514)
    assert food_I.get_value() == 114
    assert food_I.get_cost() == 514
    assert food_I.density() == pytest.approx(114 / 514)
    assert str(food_I) == "black_tea: <114, 514>"

def test_menu():
    # 測試 Menu 建構子的功能
    jojo = lec2.Menu(["lemon_water", "black_tea"], [15, 114], [1, 514])
    assert len(jojo.get_foods()) == 2
    # 依照 Food 的 __str__，各項目之間以 "; " 隔開，尾端也有 "; "
    assert str(jojo) == "lemon_water: <15, 1>; black_tea: <114, 514>; "

    # 測試 build_large_menu 方法
    pro = lec2.Menu()
    # 初始化時 Menu 應為空
    assert len(pro.get_foods()) == 0
    

def test_greedy():
    # 測試 greedy 函數
    # 建立一組 Food 物件的列表
    foods = [
        lec2.Food("apple", 50, 2),    # density = 25
        lec2.Food("banana", 30, 1),   # density = 30
        lec2.Food("pear", 40, 4)       # density = 10
    ]
    # 使用 greedy 函數，依照密度排序，設定最大成本為 3
    # 預期先選擇 density 最高的 banana (cost=1)，再選擇 apple (cost=2)
    selected_items, total_value = lec2.greedy(foods, 3, key_function=lambda f: f.density())
    selected_names = [item.name for item in selected_items]
    assert selected_names == ["banana", "apple"]
    assert total_value == pytest.approx(30 + 50)
    
    # 當最大成本充裕時，全部選上且依據 density 由高至低排序
    selected_items, total_value = lec2.greedy(foods, 100, key_function=lambda f: f.density())
    selected_names = [item.name for item in selected_items]
    assert selected_names == ["banana", "apple", "pear"]