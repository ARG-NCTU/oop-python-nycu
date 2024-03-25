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


def test_7_animal():
    a = inh.Animal(6)
    a.set_name("juicy")
    print(a)
    assert a.get_name() == "juicy"
    assert a.get_age() == 6
    a.set_age(5)
    print(a)
    assert a.get_age() == 5
    a.set_age(7)
    print(a)
    assert a.get_age() == 7
    a.set_name("bouncy")
    print(a)
    assert a.get_name() == "bouncy"
