# import pytest
from lec9_source_code import Animal, Cat, Person, Student, Rabbit

# parent class
def test_animal():
    a = Animal(8)
    assert a.get_age() == 8, "Error in get_age"
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_name()
    assert a.get_name() == ""
    a.set_age(5)
    assert a.get_age() == 5

# child-class
def test_cat():
    c = Cat(5)
    c.set_name("fishy")
    assert str(c) == "cat:fishy:5"

def test_person():
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p2.get_name() == "jill"
    assert p1.get_age() == 30
    assert p2.get_age() == 25
    p1.add_friend("jill")
    assert p1.get_friends() == ["jill"]

def test_student():
    s1 = Student("alice", 20, "CS")
    s2 = Student("beth", 18)
    assert s1.major == "CS"
    assert s2.major is None
    s1.change_major("Math")
    assert s1.major == "Math"

# test for class variable
def test_rabbit_creation():
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    assert r1.get_age() == 3
    assert r2.get_age() == 4
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None

def test_rabbit_addition():
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r4 = r1.__add__(r2)
    r5 = r1+r2
    assert r4 == r5
    assert r1.istargetrabbit(r4.get_parent1())

def test_rabbit_equality():
    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)
    r4 = r1 + r2
    r5 = r3 + r4
    r6 = r4 + r3
    assert r5 == r6
    assert r4 != r6

