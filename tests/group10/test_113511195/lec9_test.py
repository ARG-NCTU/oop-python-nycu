import add_path
import lec9_inheritance.py as lec9

def test_animal_init_defaults():
    a = lec9.Animal(4)
    assert lec9.Animal.get_age(a) == 4
    assert lec9.Animal.get_name(a) is None

def test_animal_set_age():
    a = lec9.Animal(4)
    lec9.Animal.set_age(a, 10)
    assert lec9.Animal.get_age(a) == 10
    
def test_animal_set_name_explicit():
    a = lec9.Animal(4)
    lec9.Animal.set_name(a, "fluffy")
    assert lec9.Animal.get_name(a) == "fluffy"
    assert str(a) == "animal:fluffy:4"