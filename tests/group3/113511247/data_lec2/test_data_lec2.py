import random
import pytest
from knapsack import Food, Menu, greedy, max_val, fast_max_val

def test_food():
    f = Food("apple", 10, 5)
    assert f.get_value() == 10
    assert f.get_cost() == 5
    # density = value / calories
    assert f.density() == 10 / 5
    expected_str = "apple: <10, 5>"
    assert str(f) == expected_str

def test_menu_static():
    names = ["apple", "banana"]
    values = [10, 7]
    calories = [5, 3]
    m = Menu(names, values, calories)
    foods = m.get_foods()
    assert len(foods) == 2
    assert foods[0].name == "apple"
    assert foods[1].name == "banana"
    # __str__ 由 get_foods_str 組成，每個項目後都有 "; "
    expected = "apple: <10, 5>; banana: <7, 3>; "
    assert str(m) == expected

def test_menu_large():
    m = Menu()
    num_items = 5
    max_val_param = 20
    max_cost_param = 10
    m.build_large_menu(num_items, max_val_param, max_cost_param)
    foods = m.get_foods()
    assert len(foods) == num_items
    # 每個 food 的 value 與 calories 應在對應範圍內
    for food in foods:
        assert 1 <= food.get_value() <= max_val_param
        assert 1 <= food.get_cost() <= max_cost_param

def test_greedy():
    # 建立一組固定的 Food 物件
    apple  = Food("apple", 10, 5)    # density = 2.0
    banana = Food("banana", 7, 3)     # density ≈ 2.33
    cookie = Food("cookie", 5, 10)    # density = 0.5
    steak  = Food("steak", 25, 15)    # density ≈ 1.67
    items = [apple, banana, cookie, steak]
    max_cost = 20
    # 使用 density 作為排序依據
    key_function = lambda x: x.density()
    chosen, total_value = greedy(items, max_cost, key_function)
    # greedy 依照密度排序（由大到小）嘗試選取：
    # banana (cost 3) → apple (cost 5) → steak (cost 15) 超過預算 → cookie (cost 10)
    # 總成本 = 3 + 5 + 10 = 18，總價值 = 7 + 10 + 5 = 22
    assert total_value == 22
    chosen_names = [item.name for item in chosen]
    assert chosen_names == ["banana", "apple", "cookie"]

def test_max_val():
    # 建立 Food 物件列表
    apple  = Food("apple", 10, 5)
    banana = Food("banana", 7, 3)
    cookie = Food("cookie", 5, 10)
    steak  = Food("steak", 25, 15)
    items = [apple, banana, cookie, steak]
    avail = 20
    total, taken = max_val(items, avail)
    # 0/1 背包問題最佳解為選取 apple 與 steak，總價值 = 10 + 25 = 35
    assert total == 35
    taken_names = set(item.name for item in taken)
    assert taken_names == {"apple", "steak"}

def test_fast_max_val():
    # 與 max_val 相同的測試，但使用 memo 加速版
    apple  = Food("apple", 10, 5)
    banana = Food("banana", 7, 3)
    cookie = Food("cookie", 5, 10)
    steak  = Food("steak", 25, 15)
    items = [apple, banana, cookie, steak]
    avail = 20
    total, taken = fast_max_val(items, avail, memo={})
    # 最佳解同樣為 apple 與 steak，總價值 35
    assert total == 35
    taken_names = set(item.name for item in taken)
    assert taken_names == {"apple", "steak"}
