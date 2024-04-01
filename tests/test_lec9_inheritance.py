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
  
def test_6_cat():
    c = inh.Cat(5)
    print(c)
    print(c.get_age())
    c.set_name("fluffy")
    print(c)
    assert c.get_name() == "fluffy"
    assert c.get_age() == 5
  

