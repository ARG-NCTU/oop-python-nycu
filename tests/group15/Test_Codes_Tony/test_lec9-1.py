import lec9_inheritance as lec
import pytest

def test_animal():
    z = lec.Animal(10)
    print (z)
    print(z.get_age())
    assert z.get_age() == 10
    z.set_name('Zoro')
    assert z.get_name() == "Zoro"
    print(z)
test_animal()

def test_cat():
    c = lec.Cat(9)
    assert c.get_age() == 9
    assert c.get_name() == None
    print(c)
test_cat()

def test_people():
    p1 = lec.Person("jack", 30)
    p2 = lec.Person("jill", 25)
    assert p1.get_age() == 30
    assert p1.get_name() == "jack"
    print(p1.get_name())
    print(p1.get_age())
    print(p2)
    p1.speak()
    p1.age_diff(p2)
test_people()