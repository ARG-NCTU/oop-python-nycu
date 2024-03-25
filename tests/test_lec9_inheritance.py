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

def test_13_rabbit():
    r1 = inh.Rabbit("Yuyu2", 3)
    r2 = inh.Rabbit("reb", 4)
    r3 = r1 + r2
    r4 = r2 + r1
    assert r3.get_parent1().get_rid() == "007"
    assert r3.get_parent2().get_rid() == "008"
    assert r4.get_parent1().get_rid() == "008"
    assert r4.get_parent2().get_rid() == "007"
    assert r3 == r4 #r3 and r4 have same parents?
