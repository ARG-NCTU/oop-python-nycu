import add_path
import mit_ocw_exercises.lec9_inheritance as l9 # type: ignore
import pytest

import random
from io import StringIO
import sys

def test_animal():
    age = random.randint(1, 20)
    a = l9.Animal(age)
    assert str(a) == f"animal:None:{age}"
    assert a.get_age() == age
    a.set_name("fluffy")
    assert str(a) == f"animal:fluffy:{age}"
    a.set_name()
    assert str(a) == f"animal::{age}"

#########################

def test_cat():
    age = random.randint(1, 20)
    c = l9.Cat(age)
    name = "weiss"
    c.set_name(name)
    assert str(c) == f"cat:{name}:{age}"
    assert c.get_age() == age

    # Capture the output of speak
    captured_output = StringIO()
    sys.stdout = captured_output
    c.speak()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "meow"

#########################

def test_person():
    age = random.randint(1, 20)
    name = "yang"
    p = l9.Person(name, age)
    assert str(p) == f"person:{name}:{age}"
    assert p.get_age() == age
    assert p.get_name() == name
    assert p.get_friends() == []

    # Capture the output of speak
    captured_output = StringIO()
    sys.stdout = captured_output
    p.speak()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "hello"

def test_person_with_friends():
    p = l9.Person("alice", 25)

    p.add_friend("charlie")
    p.add_friend("david")
    assert p.get_friends() == ["charlie", "david"]

    # Test adding the same friend again
    p.add_friend("charlie")
    assert p.get_friends() == ["charlie", "david"]


def test_person_age_diff():
    p1 = l9.Person("alice", 25)
    p2 = l9.Person("bob", 30)

    # Capture the output of age_diff
    captured_output = StringIO()
    sys.stdout = captured_output
    p1.age_diff(p2)
    sys.stdout = sys.__stdout__
    expected_diff = abs(25 - 30)
    assert captured_output.getvalue().strip() == f"{expected_diff} year difference"

#########################

def test_student():
    age = random.randint(1, 20)
    name = "bob"
    major = "Mathematics"
    s = l9.Student(name, age, major)
    assert str(s) == f"student:{name}:{age}:{major}"
    assert s.get_age() == age
    assert s.get_name() == name

    major = "Computer Science"
    s.change_major(major)
    assert str(s) == f"student:{name}:{age}:{major}"

    # Capture the output of speak
    captured_output = StringIO()
    sys.stdout = captured_output
    s.speak()
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip()
    assert output in ["i have homework", "i need sleep", "i should eat", "i am watching tv"]

def test_student_no_major():
    age = random.randint(1, 20)
    name = "carol"
    s = l9.Student(name, age)
    assert str(s) == f"student:{name}:{age}:None"

##########################

def test_rabbit():
    l9.Rabbit.tag = 1

    # Test rebbit creation
    age1 = random.randint(1, 10)
    age2 = random.randint(1, 10)
    age3 = random.randint(1, 10)
    r1 = l9.Rabbit(age1)
    r2 = l9.Rabbit(age2)
    r3 = l9.Rabbit(age3)

    assert str(r1) == f"rabbit:001"
    assert str(r2) == f"rabbit:002"
    assert str(r3) == f"rabbit:003"

    assert r1.get_age() == age1
    assert r2.get_age() == age2
    assert r3.get_age() == age3

    assert r1.parent1 == None and r1.parent2 == None
    assert r2.parent1 == None and r2.parent2 == None
    assert r3.parent1 == None and r3.parent2 == None

def test_rabbit_produce():
    l9.Rabbit.tag = 1

    r1 = l9.Rabbit(random.randint(1, 10))
    r2 = l9.Rabbit(random.randint(1, 10))

    # Test rebbit addition
    r3 = r1 + r2
    assert str(r3) == "rabbit:003"
    assert r3.get_parent1() in [r1, r2]
    assert r3.get_parent2() in [r1, r2]

    # Test rabbit equality
    r4 = r2 + r1
    assert r3 == r4
    r5 = r1 + r3
    assert r3 != r5