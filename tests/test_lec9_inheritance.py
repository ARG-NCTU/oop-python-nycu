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

def test_17_animal():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("PulsarGlory")
    print(a)
    assert a.get_name() == "PulsarGlory"
    assert a.get_age() == 19

