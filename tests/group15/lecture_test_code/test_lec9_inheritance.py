import pytest
import io
import sys
from lec9_inheritance import Animal, Cat, Person, Student, Rabbit

# ===== 測試 Animal (父類別) ===
def test_animal_base():
    """測試 Animal 基礎功能的設定與取得"""
    animal = Animal(10)
    assert animal.get_age() == 10
    assert animal.get_name() is None
    
    animal.set_name("buddy")
    assert animal.get_name() == "buddy"
    
    animal.set_name() # 測試預設參數
    assert animal.get_name() == ""
    
    assert str(animal) == "animal::10"

# ===== 測試 Cat (繼承 Animal) =====
def test_cat_inheritance_and_methods():
    """測試 Cat 是否繼承了 Animal 的屬性，以及自己的方法"""
    cat = Cat(5)
    cat.set_name("whiskers")
    
    # 測試繼承來的方法
    assert cat.get_age() == 5
    assert cat.get_name() == "whiskers"
    
    # 測試 Cat 覆寫 (override) 的 __str__ 方法
    assert str(cat) == "cat:whiskers:5"
    
    # 測試 Cat 自己的 speak 方法
    # 需要捕捉 print 的輸出才能進行斷言
    captured_output = io.StringIO()
    sys.stdout = captured_output
    cat.speak()
    sys.stdout = sys.__stdout__ # 恢復標準輸出
    assert captured_output.getvalue().strip() == "meow"

# =========================================
# ===== 測試 Person (繼承 Animal) ===
# =========================================
def test_person_extended_init_and_methods():
    """測試 Person 擴充的 __init__ 和自己的方法"""
    p1 = Person("Jack", 30)
    p2 = Person("Jill", 25)
    
    assert str(p1) == "person:Jack:30"
    
    # 測試 add_friend 和 get_friends
    assert p1.get_friends() == []
    p1.add_friend("Jill")
    p1.add_friend("John")
    p1.add_friend("Jill") # 測試重複添加
    assert p1.get_friends() == ["Jill", "John"]
    
    # 測試 age_diff
    captured_output = io.StringIO()
    sys.stdout = captured_output
    p1.age_diff(p2)
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "5 year difference"
    
# ===== 測試 Student (繼承 Person) =====
def test_student_further_inheritance():
    """測試 Student 的多層繼承和方法"""
    s = Student("Alice", 20, "CS")
    
    # 測試是否繼承了 Person 和 Animal 的屬性
    assert s.get_name() == "Alice"
    assert s.get_age() == 20
    
    # 測試 Student 的 __str__
    assert str(s) == "student:Alice:20:CS"
    
    # 測試 change_major
    s.change_major("Physics")
    assert s.major == "Physics"
    
    # 測試隨機的 speak 方法
    # 由於結果是隨機的，我們無法斷言某個特定輸出
    # 但我們可以驗證輸出是四個可能性之一
    possible_speaks = {"i have homework", "i need sleep", "i should eat", "i am watching tv"}
    captured_output = io.StringIO()
    sys.stdout = captured_output
    s.speak()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() in possible_speaks

# ====================================================
# ===== 測試 Rabbit (類別變數和特殊方法) =====
# =================================================
@pytest.fixture(autouse=True)
def reset_rabbit_tag():
    """這個 fixture 會在每次測試 Rabbit 前自動重設 tag，確保測試獨立性"""
    Rabbit.tag = 1

def test_rabbit_class_variable_rid():
    """測試 Rabbit 的類別變數 tag 和實例 ID"""
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    assert r1.get_rid() == "001"
    assert r2.get_rid() == "002"
    assert Rabbit.tag == 3 # 驗證類別變數已被修改

# 在 lec9_test.py 中
def test_rabbit_special_methods_add_and_eq():
    """測試 Rabbit 的 __add__ 和 __eq__ 特殊方法"""
    r1 = Rabbit(3) # rid: 1
    r2 = Rabbit(4) # rid: 2
    
    # 測試 __add__
    r3 = r1 + r2   # rid: 3, parents: r1, r2
    assert r3.get_rid() == "003"
    
    # 療法：使用 'is' 來檢查物件的身份是否相同
    assert r3.get_parent1() is r1
    assert r3.get_parent2() is r2
    
    # 測試 __eq__
    r4 = r2 + r1 # rid: 4, parents: r2, r1
    
    assert r3 == r4
    
    # 測試與沒有父母的兔子比較
    assert (r3 == r1) is False
