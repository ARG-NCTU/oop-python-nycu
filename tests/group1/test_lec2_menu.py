# test_knapsack.py
import random
import math
from knapsack import Food, Menu, greedy, max_val, fast_max_val

def _names(items):
    return sorted([it.name for it in items])

def _total_value(items):
    return sum(it.get_value() for it in items)

def _total_cost(items):
    return sum(it.get_cost() for it in items)


def test_food_basic_methods():
    f = Food("apple", 50, 60)
    assert f.get_value() == 50
    assert f.get_cost() == 60
    assert math.isclose(f.density(), 50/60)


def test_menu_init_and_get_foods():
    names = ["a", "b", "c"]
    values = [10, 20, 30]
    calories = [1, 2, 3]
    menu = Menu(names, values, calories)
    foods = menu.get_foods()
    assert len(foods) == 3
    assert _names(foods) == ["a", "b", "c"]


def test_greedy_variants_and_optimal_compare():
    # 設計一組資料：讓 greedy by value 非最優，方便比對
    names   = ["A","B","C","D"]
    values  = [60, 100, 120, 80]
    costs   = [10, 20, 30, 24]
    menu = Menu(names, values, costs)
    foods = menu.get_foods()
    cap = 50

    # 三種貪婪
    take_v, val_v = greedy(foods, cap, Food.get_value)
    take_c, val_c = greedy(foods, cap, lambda x: 1/x.get_cost())
    take_d, val_d = greedy(foods, cap, Food.density)

    # 最優解
    opt_val, opt_items = max_val(foods, cap)

    # 都不應超過最優解
    assert val_v <= opt_val
    assert val_c <= opt_val
    assert val_d <= opt_val

    # memo 版與最優解一致
    memo_val, memo_items = fast_max_val(foods, cap)
    assert memo_val == opt_val
    assert _total_cost(opt_items) <= cap
    assert _total_cost(memo_items) <= cap


def test_zero_capacity_returns_zero():
    names = ["x","y"]
    values = [10, 20]
    costs  = [5,  7]
    menu = Menu(names, values, costs)
    foods = menu.get_foods()

    v1, items1 = max_val(foods, 0)
    v2, items2 = fast_max_val(foods, 0)

    assert v1 == 0 and items1 == ()
    assert v2 == 0 and items2 == ()


def test_all_items_too_heavy():
    names = ["p","q"]
    values = [100, 200]
    costs  = [100, 300]
    menu = Menu(names, values, costs)
    foods = menu.get_foods()

    cap = 50
    v1, items1 = max_val(foods, cap)
    v2, items2 = fast_max_val(foods, cap)

    assert v1 == 0 and items1 == ()
    assert v2 == 0 and items2 == ()


def test_build_large_menu_is_within_bounds_and_deterministic_with_seed():
    random.seed(42)  # 讓測試可重現
    menu = Menu()
    menu.build_large_menu(num_items=10, max_val=20, max_cost=15)
    foods = menu.get_foods()

    assert len(foods) == 10
    # 檢查每個項目都在指定範圍內
    for f in foods:
        assert 1 <= f.get_value() <= 20
        assert 1 <= f.get_cost() <= 15

    # 若再次用相同 seed 建同樣菜單，內容（值/成本分布）一致
    random.seed(42)
    menu2 = Menu()
    menu2.build_large_menu(num_items=10, max_val=20, max_cost=15)
    foods2 = menu2.get_foods()

    assert [ (f.get_value(), f.get_cost()) for f in foods ] == \
           [ (f.get_value(), f.get_cost()) for f in foods2 ]


def test_fast_equals_bruteforce_on_random_small_instances():
    # 小型隨機案例，多次比對兩者結果一致
    random.seed(7)
    for _ in range(5):
        n = 6
        names = [f"i{k}" for k in range(n)]
        values = [random.randint(1, 40) for _ in range(n)]
        costs  = [random.randint(1, 20) for _ in range(n)]
        cap    = random.randint(10, 40)

        menu = Menu(names, values, costs)
        foods = menu.get_foods()

        v1, it1 = max_val(foods, cap)
        v2, it2 = fast_max_val(foods, cap)

        assert v1 == v2
        assert _total_cost(it1) <= cap
        assert _total_cost(it2) <= cap
