import os
import sys
import pytest
import math

sys.path.append(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../src'))

import mit_ocw_exercises.lec9_inheritance as lec9

### --- Animal --- ###
def test_animal_attributes():
    a = lec9.Animal(5)
    assert a.get_age() == 5
    assert a.get_name() is None
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_name()
    assert a.get_name() == ""

def test_animal_str():
    a = lec9.Animal(3)
    a.set_name("leo")
    assert str(a) == "animal:leo:3"

### --- Cat --- ###
def test_cat_str_and_speak(capsys):
    c = lec9.Cat(2)
    c.set_name("whiskers")
    assert str(c) == "cat:whiskers:2"
    c.speak()
    captured = capsys.readouterr()
    assert "meow" in captured.out

### --- Person --- ###
def test_person_creation_and_friends():
    p = lec9.Person("jack", 30)
    assert p.get_name() == "jack"
    assert p.get_age() == 30
    assert p.get_friends() == []
    p.add_friend("jill")
    p.add_friend("jill")  # duplicate
    assert p.get_friends() == ["jill"]

def test_person_age_diff(capsys):
    p1 = lec9.Person("a", 20)
    p2 = lec9.Person("b", 25)
    p1.age_diff(p2)
    captured = capsys.readouterr()
    assert "5 year difference" in captured.out

### --- Student --- ###
def test_student_creation_and_major():
    s = lec9.Student("alice", 20, "CS")
    assert str(s) == "student:alice:20:CS"
    s.change_major("Math")
    assert str(s) == "student:alice:20:Math"

def test_student_speak_random(monkeypatch, capsys):
    s = lec9.Student("bob", 18)
    monkeypatch.setattr("random.random", lambda: 0.3)
    s.speak()
    captured = capsys.readouterr()
    assert "i need sleep" in captured.out

### --- Rabbit --- ###
def test_rabbit_id_and_str():
    r = lec9.Rabbit(2)
    assert r.get_rid().isdigit()
    assert str(r).startswith("rabbit:")

def test_rabbit_add():
    r1 = lec9.Rabbit(2)
    r2 = lec9.Rabbit(3)
    baby = r1 + r2
    assert isinstance(baby, lec9.Rabbit)
    assert baby.get_parent1() is r1
    assert baby.get_parent2() is r2
    assert baby.get_age() == 0

def test_rabbit_equality():
    r1 = lec9.Rabbit(2)
    r2 = lec9.Rabbit(3)
    r3 = lec9.Rabbit(4)
    baby1 = r1 + r2
    baby2 = r2 + r1
    baby3 = r3 + r1
    assert baby1 == baby2
    assert baby1 != baby3
