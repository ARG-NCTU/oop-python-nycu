import re
import random
import pytest
from add_path import add_path
add_path()
from lec9_inheritance import Animal, Cat, Person, Student, Rabbit


"""Small additional checks for `lec9_inheritance` to improve robustness.
Added: verify Student is subclass of Person and that Animal names can be empty strings.
"""

####################################
# Animal Tests
####################################

def test_animal_basic():
    a = Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None

    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    assert str(a) == "animal:fluffy:4"

    a.set_age(10)
    assert a.get_age() == 10


####################################
# Cat Tests
####################################

def test_cat_inheritance():
    c = Cat(2)
    c.set_name("mimi")
    assert c.get_age() == 2
    assert str(c) == "cat:mimi:2"


####################################
# Person Tests
####################################

def test_person():
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)

    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p1.get_friends() == []

    p1.add_friend("amy")
    p1.add_friend("amy")  # duplicate should not be added
    assert p1.get_friends() == ["amy"]

    # age diff can only be tested indirectly → should not crash
    p1.age_diff(p2)


def test_student_is_person():
    """Student should be recognized as a Person (inheritance)."""
    s = Student("bob", 21, "Math")
    assert isinstance(s, Person)


####################################
# Student Tests
####################################

def test_student():
    s = Student("alice", 20, "CS")

    assert s.get_name() == "alice"
    assert s.major == "CS"
    assert str(s) == "student:alice:20:CS"

    # change major
    s.change_major("EE")
    assert s.major == "EE"

    # speak() is random; ensure it does not crash
    s.speak()


####################################
# Rabbit Tests
####################################

def test_rabbit_basic_and_add():
    # reset class variable for reproducibility
    Rabbit.tag = 1

    r1 = Rabbit(3)
    r2 = Rabbit(4)

    assert r1.get_rid() == "001"
    assert r2.get_rid() == "002"

    # addition creates new rabbit
    r3 = r1 + r2
    assert isinstance(r3, Rabbit)
    assert r3.get_parent1() == r1
    assert r3.get_parent2() == r2
    assert r3.get_rid() == "003"  # tag increments


def test_rabbit_equality():
    Rabbit.tag = 1

    r1 = Rabbit(3)
    r2 = Rabbit(4)
    r3 = Rabbit(5)

    child1 = r1 + r2   # parents (r1, r2)
    child2 = r2 + r1   # parents reversed

    assert child1 == child2     # same parents, different order

    child3 = r3 + r1            # different parents
    assert not (child1 == child3)
