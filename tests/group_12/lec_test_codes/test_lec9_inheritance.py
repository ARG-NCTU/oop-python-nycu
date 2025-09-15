import lec_test_codes.add_path
import mit_ocw_exercises.lec9_inheritance as l9
import pytest

def test_animal_basic():
    a = l9.Animal(4)
    assert a.get_age() == 4
    assert a.get_name() is None
    a.set_name("test_animal_a")
    assert a.get_name() == "test_animal_a"
    a.set_age(10)
    assert a.get_age() == 10
    assert "animal:test_animal_a:10" == str(a)

def test_cat_inheritance(capsys):
    b = l9.Cat(5)
    b.set_name("test_animal_b")
    assert str(b) == "cat:test_animal_b:5"
    b.speak()
    captured = capsys.readouterr()
    assert "meow" in captured.out

def test_person_methods(capsys):
    p1 = l9.Person("P1", 101)
    p2 = l9.Person("P2", 102)
    assert p1.get_name() == "P1"
    assert p2.get_age() == 102
    p1.add_friend("Nobody")
    assert p1.get_friends() == ["Nobody"]
    p1.speak()
    captured = capsys.readouterr()
    assert "hello" in captured.out
    p1.age_diff(p2)
    captured = capsys.readouterr()
    assert "1 year difference" in captured.out
    assert "person:P1:101" == str(p1)
