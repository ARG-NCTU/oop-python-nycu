import add_path
import mit_ocw_exercises.lec9_inheritance as lec9
import pytest

def test_animal():
    a = lec9.Animal(4)
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
    c = lec9.Cat(3)
    c.set_name("kitty")
    assert str(c) == "cat:kitty:3"
    assert c.get_age() == 3
    c.set_age(10)
    assert c.get_age() == 10
    assert str(c) == "cat:kitty:10"

def test_person():
    p = lec9.Person("Alice", 30)
    assert str(p) == "person:Alice:30"
    assert p.get_age() == 30
    p.set_age(35)
    assert p.get_age() == 35
    assert str(p) == "person:Alice:35"

def test_student():
    s = lec9.Student("Bob", 20, "Computer Science")
    assert str(s) == "student:Bob:20:Computer Science"
    assert s.get_age() == 20
    s.set_age(22)
    assert s.get_age() == 22
    s.set_name("Charlie")
    assert str(s) == "student:Charlie:22:Computer Science"
    s.change_major("Mathematics")
    assert str(s) == "student:Charlie:22:Mathematics"

def test_Rabbit():
    r1 = lec9.Rabbit(2, "r0")
    assert lec9.Rabbit.tag == 8
    r2 = lec9.Rabbit(3, "r1", "r3")
    assert lec9.Rabbit.tag == 9
    assert r1.get_rid() == "007"
    assert r2.get_rid() == "008"
    assert r1.age == 2
    assert r2.age == 3
    r1.set_age(4)
    r2.set_age(5)
    assert r1.get_age() == 4
    assert r2.get_age() == 5
