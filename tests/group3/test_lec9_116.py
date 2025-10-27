import add_path
import mit_ocw_exercises.lec9_inheritance as lec9
import pytest

def test_animal():
    a = lec9.Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_name()
    assert a.get_name() == ""

def test_cat():
    c = lec9.Cat(5)
    c.set_name("whiskers")
    assert str(c) == "cat:whiskers:5"
    assert c.get_age() == 5

def test_person():
    p1 = lec9.Person("alice", 30)
    p2 = lec9.Person("bob", 25)
    assert p1.get_name() == "alice"
    assert p1.get_age() == 30
    assert p2.get_name() == "bob"
    assert p2.get_age() == 25
    p1.add_friend("charlie")
    p1.add_friend("david")
    assert p1.get_friends() == ["charlie", "david"]
    p1.age_diff(p2)  # Should print "5 year difference"
    assert str(p1) == "person:alice:30"

def test_student():
    s = lec9.Student("eve", 20, "MIT")
    assert s.get_name() == "eve"
    assert s.get_age() == 20
    s.add_friend("frank")
    assert s.get_friends() == ["frank"]
    assert str(s) == "student:eve:20:MIT"



def test_rabbit():
    r = lec9.Rabbit(3, "white")
    assert r.get_age() == 3
    assert r.get_color() == "white"
    r.set_name("bunny")
    assert str(r) == "rabbit:bunny:3:white"
    r.set_name()
    assert str(r) == "rabbit::3:white"
    r2 = lec9.Rabbit(2)
    assert r2.get_color() is None