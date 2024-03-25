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
def test_person():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("PPPP")
    print(a)
    assert a.get_name() == "PPPP"
    assert a.get_age() == 19

