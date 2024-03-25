import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test_4_turtle():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("ninja")
    print(a)
    assert a.get_name() == "ninja"
    assert a.get_age() == 4
