import add_path
import lec8_classes as lec8
import pytest


def test_coordinate():
    c = lec8.Coordinate(3, 4)
    origin = lec8.Coordinate(0,0)
    assert c.x == 3
    assert c.y == 4
    assert c.distance(origin) == 5
    assert origin.distance(c) == 5
def test_Fraction():
  # 測試初始化
    f = lec8.Fraction(1, 2)
    assert f.num == 1
    assert f.denom == 2
    
    # 測試字符串表示
    assert str(f) == "1/2"
    
    # 測試加法
    f1 = lec8.Fraction(1, 2)
    f2 = lec8.Fraction(1, 3)
    result = f1 + f2
    assert result.num == 5
    assert result.denom == 6
    
    # 測試減法
    f1 = lec8.Fraction(1, 3)
    f2 = lec8.Fraction(1, 4)
    result = f1 - f2
    assert result.num == 1
    assert result.denom == 12
    
    # 測試轉換為浮點數
    f = lec8.Fraction(1, 2)
    assert float(f) == 0.5
    
    # 測試求倒數
    f = lec8.Fraction(2, 3)
    inv = f.inverse()
    assert inv.num == 3
    assert inv.denom == 2

def test_intSet():
    s = lec8.intSet()
    assert str(s) =="{}","測試 1 失敗: 初始集合不為空"

    s.insert(2)
    s.insert(5)
    s.insert(8)
    assert str(s) == "{2,5,8}", f"測試 2 失敗: 集合內容不正確，得到 {str(s)}"
    
    assert s.member(5) is True,"測試 3-1 失敗: 應包含 5"
    assert s.member(3) is False,"測試 3-1 失敗: 應包含 5"
    
    s.remove(5) 
    assert str(s)=="{2,8}",f"測試 4-1 失敗: 移除後集合內容不正確，得到 {str(s)}" 
    s.remove(2) 
    s.remove(8) 
    
    assert s.member(0) is False,"Test 5-1 failed: Empty set falsely reports membership"
    try:
        s.remove(2)
        assert False, "Test 5-2 failed: Expected exception not raised"
    except ValueError as e:
        assert str(e)=="2 not found"

