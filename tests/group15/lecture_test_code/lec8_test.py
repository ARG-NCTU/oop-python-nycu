import pytest

from lec8 import Coordinate, Fraction, intSet

# ==================================
# ===== 測試 Coordinate Class =====
# ==================================
def test_coordinate_creation_and_str():
    """測試 Coordinate 物件的初始化和字串表示"""
    c = Coordinate(3, 4)
    assert c.x == 3
    assert c.y == 4
    assert str(c) == "<3,4>"

def test_coordinate_distance():
    """測試兩點之間的距離計算"""
    c1 = Coordinate(3, 4)
    c2 = Coordinate(0, 0)
    # 使用 pytest.approx 處理浮點數比較
    assert c1.distance(c2) == pytest.approx(5.0)
    assert c2.distance(c1) == pytest.approx(5.0)
    assert c1.distance(c1) == pytest.approx(0.0)


# ================================
# ===== 測試 Fraction Class =====
# ================================
def test_fraction_creation_and_float():
    """測試 Fraction 物件的初始化、型別檢查和浮點數轉換"""
    f = Fraction(3, 4)
    assert f.num == 3
    assert f.denom == 4
    assert float(f) == 0.75
    
    # 驗證型別檢查是否如預期運作
    with pytest.raises(AssertionError, match="ints not used"):
        Fraction(3.14, 2)

def test_fraction_operations():
    """測試分數的加、減、反轉運算"""
    f1 = Fraction(1, 4)
    f2 = Fraction(3, 4)
    
    # 測試加法
    f_add = f1 + f2
    assert isinstance(f_add, Fraction) # 驗證回傳的也是 Fraction 物件
    assert f_add.num == 16 # (1*4 + 4*3)
    assert f_add.denom == 16 # (4*4)
    assert float(f_add) == 1.0

    # 測試減法
    f_sub = f2 - f1
    assert isinstance(f_sub, Fraction)
    assert f_sub.num == 8 # (3*4 - 4*1)
    assert f_sub.denom == 16 # (4*4)
    assert float(f_sub) == 0.5
    
    # 測試反轉
    f_inv = f1.inverse()
    assert isinstance(f_inv, Fraction)
    assert f_inv.num == 4
    assert f_inv.denom == 1
    assert float(f_inv) == 4.0


# ==============================
# ===== 測試 intSet Class =====
# ==============================
def test_intSet_initialization_and_insertion():
    """測試 intSet 的初始化、插入和重複插入"""
    s = intSet()
    assert str(s) == "{}" # 初始應為空集合
    
    s.insert(3)
    assert str(s) == "{3}"
    
    s.insert(4)
    s.insert(3) # 重複插入應無效
    assert str(s) == "{3,4}" # 驗證 `__str__` 的排序功能

def test_intSet_member():
    """測試 member 方法"""
    s = intSet()
    s.insert(10)
    s.insert(-5)
    assert s.member(10) is True
    assert s.member(-5) is True
    assert s.member(0) is False

def test_intSet_remove():
    """測試 remove 方法和例外處理"""
    s = intSet()
    s.insert(4)
    s.insert(6)
    
    s.remove(4)
    assert str(s) == "{6}"
    
    # 驗證移除不存在的元素時是否拋出 ValueError
    with pytest.raises(ValueError) as excinfo:
        s.remove(99)
    # 檢查拋出的錯誤訊息內容是否符合預期
    assert "99 not found" in str(excinfo.value)
