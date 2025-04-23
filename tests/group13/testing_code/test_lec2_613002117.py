import add_path
import pytest
import mit_ocw_data_science.lec2.menu as lec2
import random

def test_food():
    # 測試 Food 類別的基本功能
    food = lec2.Food("lemon_water", 25, 3)
    assert food.get_value() == 25
    assert food.get_cost() == 3
    assert food.density() == pytest.approx(25 / 3)
    # Food 的 **str** 方法回傳: "lemon_water: <25, 3>"
    assert str(food) == "lemon_water: <25, 3>"
    
    food_I = lec2.Food("black_tea", 78, 42)
    assert food_I.get_value() == 78
    assert food_I.get_cost() == 42
    assert food_I.density() == pytest.approx(78 / 42)
    assert str(food_I) == "black_tea: <78, 42>"

def test_menu():
    # 測試 Menu 建構子的功能
    jojo = lec2.Menu(["lemon_water", "black_tea"], [25, 78], [3, 42])
    assert len(jojo.get_foods()) == 2
    # 依照 Food 的 **str**，各項目之間以 "; " 隔開，尾端也有 "; "
    assert str(jojo) == "lemon_water: <25, 3>; black_tea: <78, 42>; "
    # 測試 build_large_menu 方法
    pro = lec2.Menu()
    # 初始化時 Menu 應為空
    assert len(pro.get_foods()) == 0
    
def test_greedy():
    # 測試 greedy 函數
    # 建立一組 Food 物件的列表
    foods = [
        lec2.Food("apple", 60, 3),    # density = 20
        lec2.Food("banana", 45, 2),   # density = 22.5
        lec2.Food("pear", 35, 5)       # density = 7
    ]
    # 使用 greedy 函數，依照密度排序，設定最大成本為 5
    # 預期先選擇 density 最高的 banana (cost=2)，再選擇 apple (cost=3)
    selected_items, total_value = lec2.greedy(foods, 5, key_function=lambda f: f.density())
    selected_names = [item.name for item in selected_items]
    assert selected_names == ["banana", "apple"]
    assert total_value == pytest.approx(45 + 60)
    
    # 當最大成本充裕時，全部選上且依據 density 由高至低排序
    selected_items, total_value = lec2.greedy(foods, 100, key_function=lambda f: f.density())
    selected_names = [item.name for item in selected_items]
    assert selected_names == ["banana", "apple", "pear"]

test_food()
test_menu()
test_greedy()