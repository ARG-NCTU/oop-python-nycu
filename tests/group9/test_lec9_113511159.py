import random
import math
import pytest
import add_path
from mit_ocw_exercises.lec9_inheritance import Animal, Cat, Person, Student, Rabbit

def test_Animal():
    a = Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert str(a) == "animal:fluffy:4"
    a.set_name()
    assert str(a) == "animal::4"

def test_Cat():
    c = Cat(5)
    c.set_name("fluffy")
    assert str(c) == "cat:fluffy:5"
    import io, sys
    captured = io.StringIO()
    sys.stdout = captured
    c.speak()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "meow"
    assert c.get_age() == 5

def test_Person():
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p2.get_name() == "jill"
    assert p2.get_age() == 25
    assert str(p1) == "person:jack:30"
    import io, sys
    captured = io.StringIO()
    sys.stdout = captured
    p1.speak()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() == "hello"
    captured = io.StringIO()
    sys.stdout = captured
    p1.age_diff(p2)
    sys.stdout = sys.__stdout__
    assert "5 year difference" in captured.getvalue()

def test_Student():
    s1 = Student("alice", 20, "CS")
    s2 = Student("beth", 18)
    assert str(s1) == "student:alice:20:CS"
    assert str(s2) == "student:beth:18:None"
    s1.change_major("Math")
    assert s1.major == "Math"
    phrases = {"i have homework", "i need sleep", "i should eat", "i am watching tv"}
    import io, sys
    captured = io.StringIO()
    sys.stdout = captured
    s1.speak()
    sys.stdout = sys.__stdout__
    assert captured.getvalue().strip() in phrases

def test_Rabbit():
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None
    assert r1.get_rid().isdigit() and len(r1.get_rid()) == 3
    r4 = r1 + r2
    assert isinstance(r4, Rabbit)
    assert r4.get_parent1() is r1
    assert r4.get_parent2() is r2
    assert str(r4).startswith("rabbit:")
    r5 = r3 + r4
    r6 = r4 + r3
    assert r5 == r6
    assert (r4 == r6) is False

if __name__ == "__main__":
    test_Animal()
    test_Cat()
    test_Person()
    test_Student()
    test_Rabbit()
    print("All tests passed!")