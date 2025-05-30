import pytest
from src.mit_ocw_exercises.lec9_inheritance import Animal, Cat, Person, Student, Rabbit

def test_animal_basic():
    a = Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("fluffy")
    assert a.get_name() == "fluffy"
    a.set_age(5)
    assert a.get_age() == 5
    assert "animal:fluffy:5" == str(a)
    a.set_name()
    assert a.get_name() == ""
def test_cat_inheritance_and_methods():
    c = Cat(2)
    c.set_name("kitty")
    assert c.get_name() == "kitty"
    assert c.get_age() == 2
    assert str(c) == "cat:kitty:2"

def test_person_inheritance_and_methods(capsys):
    p1 = Person("jack", 30)
    p2 = Person("jill", 25)
    assert p1.get_name() == "jack"
    assert p1.get_age() == 30
    assert p2.get_name() == "jill"
    assert p2.get_age() == 25
    assert str(p1) == "person:jack:30"
    p1.speak()
    captured = capsys.readouterr()
    assert "hello" in captured.out
    p1.add_friend("jill")
    assert "jill" in p1.get_friends()
    p1.age_diff(p2)
    captured = capsys.readouterr()
    assert "5 year difference" in captured.out
    
def test_student_inheritance_and_methods(monkeypatch, capsys):
    s = Student("alice", 20, "CS")
    assert str(s) == "student:alice:20:CS"
    s.change_major("Math")
    assert s.major == "Math"
    # Test speak randomness by monkeypatching random.random
    monkeypatch.setattr("random.random", lambda: 0.1)
    s.speak()
    captured = capsys.readouterr()
    assert "i have homework" in captured.out
    monkeypatch.setattr("random.random", lambda: 0.3)
    s.speak()
    captured = capsys.readouterr()
    assert "i need sleep" in captured.out
    monkeypatch.setattr("random.random", lambda: 0.6)
    s.speak()
    captured = capsys.readouterr()
    assert "i should eat" in captured.out
    monkeypatch.setattr("random.random", lambda: 0.8)
    s.speak()
    captured = capsys.readouterr()
    assert "i am watching tv" in captured.out

