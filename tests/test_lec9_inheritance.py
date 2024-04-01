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

def test_animal2():
    a = inh.Animal(10)
    print(a)
    print(a.get_age())
    a.set_name("furry")
    print(a)
    assert a.get_name() == "furry"
    assert a.get_age() == 10

