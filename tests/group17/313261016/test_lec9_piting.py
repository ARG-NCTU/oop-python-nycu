import add_path
import lec9_inheritance as lec9
import pytest


def test_animal():
    s=lec9.Animal(4)
    assert s.get_age()==4
    assert s.get_name() is None  # 假設名稱初始為None

    s.set_age(5)
    assert s.get_age()==5

    s.set_name ("news")
    assert s.get_name()=="news"

def test_catanimal():
    c=lec9.Cat(5)
    assert str(c)== "cat:None:5"

def test_personanimal():
    people = lec9.Person("john",25)
    assert people.get_friends()==[]
    
    assert callable(people.speak)
    people.add_friend("tina")
    assert people.get_friends()==["tina"]
    people2=lec9.Person("tod",21)

def test_Student():
        s1 = lec9.Student("alice", 20, "CS")
        s2 = lec9.Student("beth", 18)
        
        # 測試初始狀態
        assert s1.get_name() == "alice", "get_name()方法應該返回正確的名字"
        assert s1.get_age() == 20, "get_age()方法應該返回正確的年齡"
        assert s1.major == "CS", "major屬性應該被正確設置"
        assert s2.major is None, "未指定major時，默認值應為None"
        
        # 測試繼承的方法
        assert s1.get_friends() == [], "Student應該繼承Person的get_friends方法"
        s1.add_friend("john")
        assert s1.get_friends() == ["john"], "Student應該能夠使用繼承的add_friend方法"
        
        # 測試change_major方法
        s1.change_major("Math")
        assert s1.major == "Math", "change_major方法應該更新major屬性"
 # 測試__str__方法
        assert str(s1) == "student:alice:20:Math", "__str__方法應該返回正確格式的字符串"
        assert str(s2) == "student:beth:18:None", "__str__方法應該正確處理None值"
      # 測試speak方法是否可調用
        assert callable(s1.speak), "speak方法應該是可調用的函數"
def test_Rabbit():
    lec9.Rabbit.tag = 1
    s=lec9.Rabbit(3,"dad")
    assert s.get_age() == 3, "get_age()方法應該返回正確的年齡"
    assert s.get_parent1()=='dad'
    assert s.get_parent2() is None
    assert str(s) == "rabbit:001", "__str__方法應該返回正確格式的字符串"

    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    r3 = lec9.Rabbit(5)
    r4 = r1+r2
    # 因為無法直接比較兔子對象，我們改為比較它們的ID
    assert r4.get_parent1().get_rid() == r1.get_rid(), "新兔子的parent1應該是第一個操作數"
    assert r4.get_parent2().get_rid() == r2.get_rid(), "新兔子的parent2應該是第二個操作數"
    assert r4.get_rid() == "005", "新兔子應該獲得下一個ID"
          # 測試__eq__運算符
    r5 = r3 + r4
    r6 = r4 + r3
    assert r5 == r6, "交換父母順序的兔子應該相等"
    assert r4 != r6, "有不同父母的兔子不應該相等"

    assert lec9.Rabbit.tag == 8, "類變量tag應該追蹤創建的兔子數量+1"