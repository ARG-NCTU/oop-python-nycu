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


