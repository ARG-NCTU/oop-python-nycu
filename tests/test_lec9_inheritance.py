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

def test_animal1():
    b = inh.Animal(1)
    print(b)
    print(b.get_name())
    b.set_age(5)
    print(b)
    assert b.get_name() is None
    assert b.get_age() == 5

def test_Student1():
    s1 = inh.Student("Ella",22, "Nano")
    print (s1)
    s1.change_major("ECE")
    print(s1)
    s1.set_name("Johnson")
    print(s1)
    assert s1.get_name() == "Johnson"

    s2 = inh.Student("Sana", 25, "Twice")
    print(s2.get_name,"says, ")
    s2.speak()
    s2.add_friend("Momo")
    print(s2.get_friends())
    s2.add_friend("Mina")
    print(s2.get_friends())
    assert s2.get_friends() == ["Momo", "Mina"]

def test_5_Rabbit():
    p1 = inh.Rabbit(2)
    p2 = inh.Rabbit(3)
    p3 = inh.Rabbit(5)

    print ("p1:",p1)
    print ("p2:",p2)
    print ("p3:" ,p3)

    r1 = p1 + p2
    r2 = p1 + p3
    assert r1 != r2

