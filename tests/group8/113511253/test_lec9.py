import pytest
from add_path import add_path
add_path()
from lec9_inheritance import Animal, Cat, Person, Student, Rabbit

"""
Lec 9 Tests: Inheritance checks.
Refined for pytest compatibility.
"""

def test_animal_basic():
    a = Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    assert str(a) == "animal:fluffy:4"
    a.set_age(10)
    assert a.get_age() == 10

def test_cat_inheritance():
    c = Cat(2)
    c.set_name("mimi")
    assert c.get_age() == 2
    assert str(c) == "cat:mimi:2"

def test_person():
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p1.get_friends() == []
    p1.add_friend("amy")
    p1.add_friend("amy") 
    assert p1.get_friends() == ["amy"]
    p1.age_diff(p2)

def test_student_is_person():
    s = Student("bob", 21, "Math")
    assert isinstance(s, Person)

def test_student():
    s = Student("alice", 20, "CS")
    assert s.get_name() == "alice"
    assert s.major == "CS"
    s.change_major("EE")
    assert s.major == "EE"
    s.speak()

def test_rabbit_basic_and_add():
    Rabbit.tag = 1
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    assert r1.get_rid() == "001"
    assert r2.get_rid() == "002"
    r3 = r1 + r2
    assert isinstance(r3, Rabbit)
    assert r3.get_rid() == "003"

def test_rabbit_equality():
    Rabbit.tag = 1
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    child1 = r1 + r2
    child2 = r2 + r1
    assert child1 == child2
    child3 = r3 + r1
    assert not (child1 == child3)

# Verified with pytest
