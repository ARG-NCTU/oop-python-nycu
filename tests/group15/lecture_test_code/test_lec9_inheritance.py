import importlib
import lec_test_codes.add_path
import mit_ocw_exercises.lec9_inheritance as lec9
import pytest

def test_animal_basic():
    a = lec9.Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert str(a) == "animal:fluffy:4"
    a.set_name()
    assert a.get_name() == ""
    assert str(a) == "animal::4"
    a.set_age(7)
    assert a.get_age() == 7

def test_cat_inherit_and_speak(capsys):
    c = lec9.Cat(5)
    c.set_name("fluffy")
    assert str(c) == "cat:fluffy:5"
    c.speak()
    out = capsys.readouterr().out.strip()
    assert out.splitlines()[-1] == "meow"

def test_person_init_friends_and_age_diff(capsys):
    p1 = lec9.Person("jack", 30)
    p2 = lec9.Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p1.get_friends() == []
    p1.add_friend("mike")
    p1.add_friend("mike")
    p1.add_friend("rose")
    assert p1.get_friends() == ["mike", "rose"]
    p1.age_diff(p2)
    out = capsys.readouterr().out.strip().splitlines()[-1]
    assert out.endswith("year difference")
    assert out.startswith("5")

def test_student_str_major_and_all_speak_branches(monkeypatch, capsys):
    s = lec9.Student("alice", 20, "CS")
    assert str(s) == "student:alice:20:CS"
    s.change_major("EE")
    assert str(s) == "student:alice:20:EE"

    monkeypatch.setattr(lec9.random, "random", lambda: 0.0)
    s.speak()
    assert capsys.readouterr().out.strip().splitlines()[-1] == "i have homework"

    monkeypatch.setattr(lec9.random, "random", lambda: 0.3)
    s.speak()
    assert capsys.readouterr().out.strip().splitlines()[-1] == "i need sleep"

    monkeypatch.setattr(lec9.random, "random", lambda: 0.6)
    s.speak()
    assert capsys.readouterr().out.strip().splitlines()[-1] == "i should eat"

    monkeypatch.setattr(lec9.random, "random", lambda: 0.9)
    s.speak()
    assert capsys.readouterr().out.strip().splitlines()[-1] == "i am watching tv"

def test_rabbit_tag_ids_and_add_and_eq_is_order_insensitive():
    start = lec9.Rabbit.tag
    r1 = lec9.Rabbit(1)
    r2 = lec9.Rabbit(2)
    assert r1.get_rid() == str(start).zfill(3)
    assert r2.get_rid() == str(start + 1).zfill(3)
    child = r1 + r2
    assert isinstance(child, lec9.Rabbit)
    assert child.get_age() == 0
    assert child.get_parent1() is r1
    assert child.get_parent2() is r2

    a = r1 + r2
    b = r2 + r1
    assert a == b
    assert r1 != b

def test_rabbit_eq_requires_parents():
    x = lec9.Rabbit(3)
    y = lec9.Rabbit(4)
    assert (x == y) is False

def test_module_reload_does_not_break_classes():
    m = importlib.reload(lec9)
    assert hasattr(m, "Animal")
    assert hasattr(m, "Rabbit")
    assert m.Rabbit.tag >= 1
