import pytest
from lec8_source_code import Coordinate, Fraction, intSet  # 假設你的程式碼保存在 examples.py 檔案中

# 測試 Coordinate 類別
def test_coordinate():
    c = Coordinate(3, 4)
    origin = Coordinate(0, 0)
    assert c.x == 3
    assert origin.x == 0
    assert c.distance(origin) == pytest.approx(5.0, rel=1e-9)
    assert str(c) == "<3,4>"

# 測試 Fraction 類別
def test_fraction():
    a = Fraction(1, 4)
    b = Fraction(3, 4)
    
    # 測試加法
    c = a + b
    assert str(c) == "16/16"  # 加法後分子為16，分母為16
    assert float(c) == 1.0

    # 測試減法
    d = b - a
    assert str(d) == "8/16"
    assert float(d) == 0.5

    # 測試浮點值
    assert float(a) == 0.25

    # 測試反轉
    inv_b = b.inverse()
    assert str(inv_b) == "4/3"
    assert float(inv_b) == pytest.approx(1.3333333333333333, rel=1e-9)

    # 測試不合法輸入
    with pytest.raises(AssertionError):
        Fraction(3.14, 2.7)

    # 測試除法
    e = a.divide(b)
    assert str(e) == "4/12"

    # 測試約分
    f = Fraction(2, 4)
    reduced_f = f.reduce()
    assert str(reduced_f) == "1/2"

# 測試 intSet 類別
def test_intSet():
    s = intSet()
    assert str(s) == "{}"

    # 測試插入元素
    s.insert(3)
    s.insert(4)
    s.insert(3)  # 重複插入應無效果
    assert str(s) == "{3,4}"
    
    # 測試成員檢查
    assert s.member(3) == True
    assert s.member(5) == False

    # 測試刪除元素
    s.remove(3)
    assert str(s) == "{4}"
    
    # 測試刪除不存在的元素
    with pytest.raises(ValueError, match="5 not found"):
        s.remove(5)