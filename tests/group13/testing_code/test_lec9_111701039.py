import add_path
import pytest
import mit_ocw_exercises.lec9_inheritance as lec9

ele=lec9.Animal(4)
meme=lec9.Cat(1)
def test_animal_init():
    assert ele.age == 4
    assert ele.name == None


def test_animal_set_age():
    ele.set_age(5)
    assert ele.age == 5

