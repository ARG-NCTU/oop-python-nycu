import pytest
import add_path # 假設這是你用來修正路徑的模組
from lec8_classes import Coordinate, Fraction, intSet

# -----------------
# 測試資料 (全域變數)
# -----------------
c1 = Coordinate(3, 4)
c2 = Coordinate(0, 0)

f1_4 = Fraction(1, 4)
f3_4 = Fraction(3, 4)

# -----------------
# 測試 Coordinate
# -----------------

def test_coordinate_init():
    """測試 Coordinate 初始化"""
    assert c1.x == 3 and c1.y == 4
    assert c2.x == 0 and c2.y == 0
    
def test_coordinate_dist():
    """測試 Coordinate.distance"""
    assert c1.distance(c2) == 5.0  # (3^2 + 4^2) ** 0.5 = 5
    
def test_coordinate_str():
    """測試 Coordinate.__str__"""
    assert str(c1) == "<3,4>"

# -----------------
# 測試 Fraction
# -----------------

def test_fraction_init():
    """測試 Fraction 初始化"""
    assert f1_4.num == 1 and f1_4.denom == 4
    assert f3_4.num == 3 and f3_4.denom == 4

def test_fraction_str():
    """測試 Fraction.__str__"""
    assert str(f1_4) == "1/4"

def test_fraction_add():
    """測試 Fraction.__add__"""
    f_sum = f1_4 + f3_4  # 1/4 + 3/4 = 4/4
    f_sum = f_sum.reduce()
    assert f_sum.num == 1 and f_sum.denom == 1

def test_fraction_sub():
    """測試 Fraction.__sub__"""
    f_sub = f3_4 - f1_4  # 3/4 - 1/4 = 2/4
    f_sub = f_sub.reduce()
    assert f_sub.num == 1 and f_sub.denom == 2
def test_fraction_mul():
    """測試 Fraction.__mul__"""
    f_mul = f1_4 * f3_4  # (1/4) * (3/4) = 3/16
    assert f_mul.num == 3 and f_mul.denom == 16

def test_fraction_truediv():
    """測試 Fraction.__truediv__"""
    f_div = f1_4 / f3_4  # (1/4) / (3/4) = 4/12
    assert f_div.num == 4 and f_div.denom == 12

def test_fraction_float():
    """測試 Fraction.__float__"""
    assert float(f1_4) == 0.25
    assert float(f3_4) == 0.75

def test_fraction_inverse():
    """測試 Fraction.inverse"""
    f_inv = Fraction(3, 5).inverse() # 5/3
    assert f_inv.num == 5 and f_inv.denom == 3

def test_fraction_reduce():
    """測試 Fraction.reduce"""
    f_unreduced = Fraction(10, 20)
    f_reduced = f_unreduced.reduce()
    assert f_reduced.num == 1 and f_reduced.denom == 2

def test_fraction_eq():
    """測試 Fraction.__eq__ (假設已修正)"""
    assert Fraction(1, 2) == Fraction(2, 4)
    assert Fraction(4, 12) == Fraction(2, 6)

def test_fraction_init_raises_error():
    """測試 Fraction 初始化 (非 int)"""
    with pytest.raises(AssertionError, match="ints not used"):
        Fraction(3.14, 2.7)

# -----------------
# 測試 intSet
# -----------------

def test_intset_init():
    """測試 intSet 初始化"""
    s = intSet()
    assert str(s) == "{}"

def test_intset_insert():
    """測試 intSet.insert (含重複插入)"""
    s = intSet()
    s.insert(3)
    s.insert(4)
    s.insert(3)  # 重複
    assert str(s) == "{3,4}"

def test_intset_member():
    """測試 intSet.member"""
    s = intSet()
    s.insert(3)
    assert s.member(3) is True
    assert s.member(5) is False

def test_intset_remove():
    """測試 intSet.remove"""
    s = intSet()
    s.insert(3)
    s.insert(4)
    s.remove(3)
    assert str(s) == "{4}"

def test_intset_remove_raises_error():
    """測試 intSet.remove (移除不存在的元素)"""
    s = intSet()
    s.insert(10)
    with pytest.raises(ValueError, match="3 not found"):
        s.remove(3)

def test_intset_str_sorting():
    """測試 intSet.__str__ (自動排序)"""
    s = intSet()
    s.insert(6)
    s.insert(3)
    s.insert(4)
    assert str(s) == "{3,4,6}"