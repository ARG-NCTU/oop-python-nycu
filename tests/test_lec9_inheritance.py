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

def test_9_animal():
    a = inh.Animal(18)
    print(a)
    print(a.get_age())
    a.set_name("Cutie")
    print(a)
    assert a.get_name() == "Cutie"
    assert a.get_age() == 18
    a.set_age(19)
    assert a.get_age() == 19
