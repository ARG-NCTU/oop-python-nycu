import add_path
import mit_ocw_exercises.lec9_inheritance as inh
#import pytest

def test_group7_animal():
    a = inh.Animal(69)
    print(a)
    print(a.get_age())
    a.set_name("cookie")
    print(a)
    assert a.get_name() == "cookie"
    assert a.get_age() == 69
