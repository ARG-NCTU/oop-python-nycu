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

def test_13_animal():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("Yuyu")
    print(a)
    assert a.get_name() == "Yuyu"
    assert a.get_age() == 19

def test_14_rabbit():
    r1 = inh.Rabbit(3)
    r1.set_name("fluffy")
    r2 = inh.Rabbit(4)
    r2.set_name("peter")
    r3 = r1 + r2
    r4 = r1 + r2
    assert r1.get_name() == "fluffy"
    assert r1.get_age() == 3
    assert r3 == r4
