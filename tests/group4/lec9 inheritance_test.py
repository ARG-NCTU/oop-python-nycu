import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import add_path
from src.mit_ocw_exercises.lec9_inheritance import Animal, Cat, Person, Student, Rabbit

def test_animal():
    a = Animal(4)
    assert str(a) == "animal:None:4"
    assert a.get_age() == 4
    a.set_name("fluffy")
    assert str(a) == "animal:fluffy:4"
    a.set_name()
    assert str(a) == "animal::4"
    a.set_age(20)
    assert a.get_age() == 20
    assert str(a) == "animal::20"

def test_cat():
    c = Cat(3)
    c.set_name("kitty")
    assert str(c) == "cat:kitty:3"
    assert c.get_age() == 3
    c.set_age(10)
    assert c.get_age() == 10
    assert str(c) == "cat:kitty:10"

def test_person():
    p1 = Person("Alice", 30)
    p2 = Person("Bob", 25)
    assert str(p1) == "person:Alice:30"
    assert str(p2) == "person:Bob:25"
    assert p1.get_friends() == []
    p1.add_friend("Charlie")
    assert p1.get_friends() == ["Charlie"]
    p1.add_friend("David")
    assert p1.get_friends() == ["Charlie", "David"]
    p1.set_age(35)
    assert p1.get_age() == 35
    assert str(p1) == "person:Alice:35"

def test_student():
    s = Student("Eve", 18, "Computer Science")
    assert str(s) == "student:Eve:18:Computer Science"
    assert s.speak() != "hello"
    assert s.get_friends() == []
    s.add_friend("Frank")
    assert s.get_friends() == ["Frank"]
    s.set_age(21)
    s.set_name("Tom")
    s.change_major("Physics")
    assert s.get_age() == 21
    assert str(s) == "student:Tom:21:Physics"
    s_no_major = Student("Grace", 22)
    assert str(s_no_major) == "student:Grace:22:None"

def test_Rabbit():
    r1 = Rabbit(2, "r0")
    assert Rabbit.tag == 8
    r2 = Rabbit(3, "r1", "r3")
    assert Rabbit.tag == 9
    assert r1.get_rid() == "007"
    assert r1.get_parent1() == "r0"
    assert r2.get_parent2() == "r3"
    r1.set_age(5)
    assert r1.get_age() == 5
    r4 = r1 + r2
    assert isinstance(r4, Rabbit)
    assert r4.get_parent1() is r1
    assert str(r4) == "rabbit:009"
    r5 = r2 + r1
    assert (r4 == r5) is True
