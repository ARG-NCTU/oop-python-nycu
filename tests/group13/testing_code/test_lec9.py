import add_path
import pytest
import mit_ocw_exercises.lec9_inheritance as lec9

ele=lec9.Animal(4)
def test_animal_init():
    assert ele.age == 4
    assert ele.name == None
ele.set_age(5)

def test_animal_set_age():
    assert ele.age == 5
