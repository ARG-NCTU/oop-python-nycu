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

def test_2_animal():
    a = inh.Animal(5)
    print(a)
    print(a.get_age())
    a.set_name("fluff")
    print(a)
    assert a.get_name() == "fluff"
    assert a.get_age() == 5
