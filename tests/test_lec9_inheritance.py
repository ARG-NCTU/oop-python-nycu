import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test_animal():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4

def test_animal1():
    b = inh.Animal(1)
    print(b)
    print(b.get_name())
    b.set_age(5)
    print(b)
    assert b.get_name() is None
    assert b.get_age() == 5
