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
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    r3 = lec9.Rabbit(5)
    assert str(r1) == "rabbit:001"
    assert str(r2) == "rabbit:002"
    assert str(r3) == "rabbit:003"
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None

    r4 = r1 + r2
    assert str(r4) == "rabbit:004"
    assert r4.get_parent1() == r1
    assert r4.get_parent2() == r2

    r5 = r3 + r4
    r6 = r4 + r3
    assert str(r5) == "rabbit:005"
    assert str(r6) == "rabbit:006"
    assert r5.get_parent1() == r3
    assert r5.get_parent2() == r4
    assert r6.get_parent1() == r4
    assert r6.get_parent2() == r3
    assert r5 == r6
    assert not (r4 == r6)