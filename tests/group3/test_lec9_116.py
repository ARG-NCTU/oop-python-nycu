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