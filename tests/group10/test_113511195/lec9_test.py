import add_path
import lec9_inheritance.py as lec9

def test_animal_init_defaults():
    a = lec9.Animal(4)
    assert lec9.Animal.get_age(a) == 4
    assert lec9.Animal.get_name(a) is None