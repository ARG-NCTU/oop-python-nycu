import add_path
import mit_ocw_exercises.lec9_inheritance as inh
import pytest

def test_animal_5A():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4

def test_7_animal():
    a = inh.Animal(6)
    a.set_name("juicy")
    print(a)
    assert a.get_name() == "juicy"
    assert a.get_age() == 6
    a.set_age(5)
    print(a)
    assert a.get_age() == 5
    a.set_age(7)
    print(a)
    assert a.get_age() == 7
    a.set_name("bouncy")
    print(a)
    assert a.get_name() == "bouncy"
    a.set_name('outgoing')
    assert a.get_name() == 'outgoing'
    a.set_age(5)
    assert a.get_age() ==  5
    assert a.__str__() == "animal:outgoing:5"

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

def test_11_animal():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())

def test_9_animal():
    a = inh.Animal(18)
    print(a)
    print(a.get_age())
    a.set_name("Cutie")
    print(a)
    assert a.get_name() == "Cutie"
    assert a.get_age() == 18
    a.set_age(19)
    assert a.get_age() == 19

def test_1_animal():
    a = inh.Animal(4)
    print(a)
    print(a.get_age())  
    a.set_name("fluffy")
    print(a)
    assert a.get_name() == "fluffy"
    assert a.get_age() == 4
    b = inh.Animal(5)
    assert b.get_age() == 5
    b.set_name("tiger")
    assert b.get_name() == "tiger"
    c = inh.Animal(6)
    assert c.get_age() == 6
    c.set_name("lion")
    assert c.get_name() == "lion"
    d = inh.Animal(7)
    assert d.get_age() == 7
    d.set_name("elephant")
    assert d.get_name() == "elephant"
    e = inh.Animal(8)
    assert e.get_age() == 8
    e.set_name("giraffe")
    assert e.get_name() == "giraffe"

def test_person():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("PPPP")
    print(a)
    assert a.get_name() == "PPPP"

def test_1_animal():
    b= inh.Animal(7)
    print(b)
    b.set_name("What is this?")
    assert b.get_name() == "What is this?"
    assert b.get_age() == 7

def test_1_animal():
    b = inh.Animal(7)
    b.set_name("luffy")
    assert b.get_age() == 7
    assert b.get_name() == "luffy"

def test_13_animal():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("Yuyu")
    print(a)
    assert a.get_name() == "Yuyu"
    assert a.get_age() == 19
    
def test_person():
    a = inh.Animal(19)
    print(a)
    print(a.get_age())
    a.set_name("PPPP")
    print(a)
    assert a.get_name() == "PPPP"
    assert a.get_age() == 19

def test_14_rabbit():
    r1 = inh.Rabbit(3)
    r1.set_name("fluffy")
    r2 = inh.Rabbit(4)
    r2.set_name("peter")
    r3 = r1 + r2
    r4 = r1 + r2
    assert r1.get_name() == "fluffy"
    assert r1.get_age() == 3
    assert r3 == r4

def test_dog():
    a = inh.Animal(3)
    print(a)
    print(a.get_age())
    a.set_name("gg")
    print(a)
    assert a.get_name() == "gg"
    assert a.get_age() == 3

