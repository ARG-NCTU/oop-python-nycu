# -*- coding: utf-8 -*-
import pytest

import lec9_inheritance as lec9

def test_animal_basic():
    a = lec9.Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    assert str(a) == "animal:None:4"

    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    assert str(a) == "animal:fluffy:4"

    a.set_name()
    assert a.get_name() == ""
    assert str(a) == "animal::4"


def test_cat_inherits_animal_and_speaks(capsys):
    c = lec9.Cat(5)
    c.set_name("fluffy")
    assert c.get_age() == 5
    assert c.get_name() == "fluffy"
    assert str(c) == "cat:fluffy:5"

    c.speak()
    out = capsys.readouterr().out.strip()
    assert out == "meow"


def test_person_friends_and_age_diff(capsys):
    p1 = lec9.Person("jack", 30)
    p2 = lec9.Person("jill", 25)

    assert p1.get_name() == "jack"
    assert p2.get_name() == "jill"
    assert str(p1) == "person:jack:30"

    p1.speak()
    out = capsys.readouterr().out.strip()
    assert out == "hello"

    p1.add_friend("bob")
    p1.add_friend("bob")  # duplicate should not add
    assert p1.get_friends() == ["bob"]

    p1.age_diff(p2)
    out = capsys.readouterr().out.strip()
    assert out == "5 year difference"


@pytest.mark.parametrize("r, expected", [
    (0.10, "i have homework"),
    (0.30, "i need sleep"),
    (0.60, "i should eat"),
    (0.90, "i am watching tv"),
])
def test_student_speak_branches(monkeypatch, capsys, r, expected):
    # Force random.random() to return r
    monkeypatch.setattr(lec9.random, "random", lambda: r)

    s = lec9.Student("alice", 20, "CS")
    s.speak()
    out = capsys.readouterr().out.strip()
    assert out == expected


def test_student_change_major():
    s = lec9.Student("beth", 18)
    assert str(s) == "student:beth:18:None"
    s.change_major("EE")
    assert str(s) == "student:beth:18:EE"


def test_rabbit_rid_format_and_parents_and_add_and_eq():
    # Reset class variable tag so test is deterministic
    lec9.Rabbit.tag = 1

    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    r3 = lec9.Rabbit(5)

    assert r1.get_rid() == "001"
    assert r2.get_rid() == "002"
    assert r3.get_rid() == "003"
    assert str(r1) == "rabbit:001"

    # parents of base rabbits should be None
    assert r1.get_parent1() is None
    assert r1.get_parent2() is None

    r4 = r1 + r2
    assert r4.get_parent1() is r1
    assert r4.get_parent2() is r2

    assert r4.get_age() == 0

    # Equality: same parents regardless of order
    r5 = r3 + r4
    r6 = r4 + r3
    assert (r5 == r6) is True

    # A rabbit with missing parents should not be equal to a parented rabbit
    assert (r4 == r6) is False
