import lec9_inheritance as inh
import pytest

def test_animal():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4
