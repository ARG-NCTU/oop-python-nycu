import add_path
import pytest
import mit_ocw_exercises.lec9_inheritance as lec9

def test_animal():
    # 測試 Animal 類別基本功能
    animal = lec9.Animal(6)
    assert animal.age == 6
    assert animal.name == None
    
    # 測試設置年齡和名稱
    animal.set_age(8)
    assert animal.age == 8
    
    animal.set_name("小動物")
    assert animal.name == "小動物"

def test_cat():
    # 測試 Cat 類別的基本功能和繼承性
    cat = lec9.Cat(3)
    assert cat.age == 3
    assert cat.name == None
    
    cat.set_name("小貓")
    assert cat.name == "小貓"

def test_person():
    # 測試 Person 類別
    person = lec9.Person("小明", 25)
    assert person.name == "小明"
    assert person.age == 25
    assert person.friends == []
    
    # 測試添加朋友
    person.add_friend("小華")
    assert "小華" in person.friends

def test_student():
    # 測試 Student 類別
    student = lec9.Student("小華", 20, "資訊工程")
    assert student.name == "小華"
    assert student.age == 20
    assert student.major == "資訊工程"
    
    # 測試更改主修
    student.change_major("電機工程")
    assert student.major == "電機工程"

def test_rabbit():
    # 測試 Rabbit 類別
    rabbit1 = lec9.Rabbit(2)
    rabbit2 = lec9.Rabbit(3)
    
    # 測試基本屬性
    assert rabbit1.age == 2
    assert rabbit2.age == 3
    
    # 測試加法運算
    child = rabbit1 + rabbit2
    assert child.age == 0

test_animal()
test_cat()
test_person()
test_student()
test_rabbit()