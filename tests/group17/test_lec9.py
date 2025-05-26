import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test_animal_5A():
    a = inh.Animal(5)
    print(a)
    print(a.get_age())
    a.set_name("bunny")
    print(a)
    assert a.get_name() == "bunny"
    assert a.get_age() == 5
def test_group7_animal():
    a = inh.Animal(78)
    print(a)
    print(a.get_age())
    a.set_name("vickey")
    print(a)
    assert a.get_name() == "vickey"
    assert a.get_age() == 78


def test_10_animal():
    a = inh.Animal(5)
    assert a.get_age() == 5


def test_100_animal():
    a = inh.Animal(10)
    a.set_name("candy")
    assert a.get_name() == "candy"
    assert a.get_age() == 10
