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

def test_cat():
    c = inh.Cat(6)
    print(c)
    print(c.get_age())
    c.set_name("lulu")
    print(c)
    assert c.get_name() == "lulu"
    assert c.get_age() == 6
    c.set_age(3)
    assert c.get_age() == 3