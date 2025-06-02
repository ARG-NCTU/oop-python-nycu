from lec9_final import *
import re

def test_animal():
    a = Animal(4)
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4
    assert str(a) == "animal:fluffy:4"

def test_cat():
    c = Cat(2)
    c.set_name("whiskers")
    assert c.speak() == "meow"
    assert str(c) == "cat:whiskers:2"

def test_person():
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    p1.add_friend("jill")
    p1.add_friend("amy")
    assert "jill" in p1.get_friends()
    assert "amy" in p1.get_friends()
    assert p1.age_diff(p2) == 5
    assert p1.speak() == "hello"
    assert str(p2) == "person:jill:25"

def test_student():
    s = Student("alice", 20, "CS")
    s.change_major("EE")
    result = s.speak()
    assert result in {"i have homework", "i need sleep", "i should eat", "i am watching tv"}
    assert str(s) == "student:alice:20:EE"

def test_rabbit_creation_and_id():
    Rabbit.tag = 1  # reset for test consistency
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = r1 + r2
    assert r3.get_parent1() == r1
    assert r3.get_parent2() == r2
    assert r3.get_rid() == "003"

def test_rabbit_equality():
    Rabbit.tag = 1
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    r4 = r1 + r2
    r5 = r3 + r4
    r6 = r4 + r3
    assert r5 == r6
    assert not (r4 == r6)
