import add_path
import lec9_inheritance as lec9
import pytest

def test_animal():
    a = lec9.Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4

def test_cat():
    c = lec9.Cat(5)
    c.set_name("cookie")
    print(c)
    c.speak()
    assert c.get_age() == 5
    assert c.get_name() == "cookie"

def test_person():
    p1 = lec9.Person("daniel", 8)
    p2 = lec9.Person("shelly", 5)
    p1.add_friend("cookie")
    print(p1)
    p1.speak()
    assert p1.get_name() == "daniel"
    assert p1.get_age() == 8
    assert p1.get_friends() == ["cookie"]
    assert p2.get_name() == "shelly"
    assert p2.get_age() == 5

def test_student():
    s1 = lec9.Student("Holly", 20, "CS")
    s2 = lec9.Student("Shelly", 23, "Finance")
    print(s1)
    s1.speak()
    assert s1.get_name() == "Holly"
    assert s1.get_age() == 20

def test_rabbit():
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    r3 = r1 + r2
    r4 = r2 + r1
    print(r1)
    print("r3.parent1:", r3.parent1)
    print("r1:", r1)
    print("r3.parent2:", r3.parent2)
    print("r2:", r2)

    assert r1.get_rid() == '001'
    assert r2.get_rid() == '002'
    assert r3.get_rid() == '003'
    assert r1.get_parent1() == None
    assert r1.get_parent2() == None
    assert r1.get_age() == 3
    assert r2.get_age() == 4
    assert r3.get_age() == 0
    assert r3.__eq__(r4) == True
    
    
