import add_path
import pytest
import mit_ocw_exercises.lec9_inheritance as lec9
import random

def test_animal():
    a = lec9.Animal(4)
    assert a.get_age() == 4
    a.set_name("fluffy")
    assert str(a) == "animal:fluffy:4"
    a.set_name()
    assert str(a) == "animal::4"



