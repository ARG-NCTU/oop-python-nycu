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

def test_cat():
    c = inh.Cat(5)
    print(c)
    print(c.get_age())
    c.set_name("Dog")
    print(c)
    c.speak()
    assert c.get_name() == "Dog"
    assert c.get_age() == 5

def test_person():
    p = inh.Person("Johnson",18)
    print(p)
    print(p.get_age())
    print(p)
    p.speak()
    p.friends = ["AI", "GPT"]

    #check if certain friend is in the friends list
    assert "AI" in p.get_friends()
    assert not "john" in p.get_friends()

    assert p.get_name() == "Johnson"
    assert not p.get_age() == 30
    #creat another person to test age_diff
    p2 = inh.Person("AI",30)
    p.age_diff(p2)
    
def test_student():
    s = inh.Student("JJ",20)
    print(s)
    print(s.get_age())
    s.set_name("Smith")
    print(s)
    s.speak()
    s.friends = ["AI", "GPT"]
    s.change_major("CS")
    print(s)
    assert s.get_name() == "Smith"
    assert s.get_age() == 20

def test_Rabbit():
    r = inh.Rabbit(3)
    print(r)
    print(r.get_age())
    r.set_name("puppy")
    print(r)
    assert not r.get_name() == "Rabbit"
    assert r.get_age() == 3

    #create two rabbits to test parents
    r1 = inh.Rabbit(1)
    r2 = inh.Rabbit(2)
    r3 = r1+r2
    r4 = r2+r1
    print("r1: "+r1.get_rid())
    print("r3: "+r3.get_rid())
    print(r4.get_parent1())   
    assert r3 == r4









