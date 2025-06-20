import pytest
import add_path  
from lec9 import Animal, Cat, Person, Student, Rabbit

def test_animal():
    a = Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_age(5)
    assert a.get_age() == 5
    a.set_name()
    assert a.get_name() == ""
    assert str(a) == "animal::5"

def test_cat(capsys):
    c = Cat(5)
    c.set_name("fluffy")
    assert str(c) == "cat:fluffy:5"
    c.speak()
    captured = capsys.readouterr()
    assert captured.out == "meow\n"
    assert c.get_age() == 5
    assert c.get_name() == "fluffy"

def test_person(capsys):
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p2.get_name() == "jill"
    assert p2.get_age() == 25
    assert str(p1) == "person:jack:30"
    p1.speak()
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    p1.age_diff(p2)
    captured = capsys.readouterr()
    assert captured.out == "5 year difference\n"
    p1.add_friend("jill")
    assert p1.get_friends() == ["jill"]
    p1.add_friend("jill")  # Duplicate, no effect
    assert p1.get_friends() == ["jill"]

def test_student():
    s1 = Student("alice", 20, "CS")
    s2 = Student("beth", 18)
    assert str(s1) == "student:alice:20:CS"
    assert str(s2) == "student:beth:18:None"
    s1.change_major("Math")
    assert str(s1) == "student:alice:20:Math"

def test_rabbit():
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    assert str(r1) == "rabbit:001"
    assert str(r2) == "rabbit:002"
    assert str(r3) == "rabbit:003"
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None
    r4 = r1 + r2
    assert str(r4) == "rabbit:004"
    assert r4.get_parent1() == r1
    assert r4.get_parent2() == r2
    assert r4.get_age() == 0
    r5 = r3 + r4
    r6 = r4 + r3
    assert r5 == r6  # Same parents (order swapped)
    assert r4 != r6  # Different parents
