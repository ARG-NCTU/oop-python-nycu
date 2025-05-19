import add_path
import pytest
import random
import mit_ocw_exercises.lec9_inheritance as lec9

def test_cat():
    cat1= lec9.Cat(3)
    cat1.set_name("fluffy")
    cat2= lec9.Cat(5)
    cat2.set_name("whiskers")
    assert cat1.get_age() == 3
    assert cat2.get_age() == 5
    assert cat1.get_name() == "fluffy"
    assert cat2.get_name() == "whiskers"
    cat1.set_name("fluffy2")
    cat2.set_name("whiskers2")
    cat1.set_age(4)
    assert cat1.get_name() == "fluffy2"
    assert cat2.get_name() == "whiskers2"
    assert str(cat1) == "cat:fluffy2:4"
    assert str(cat2) == "cat:whiskers2:5"

def test_student():
    student1= lec9.Student("Alice", 20, "EE")
    student2= lec9.Student("Bob", 22, "CS")
    assert student1.get_name() == "Alice"
    assert student2.get_name() == "Bob"
    assert student1.get_age() == 20
    assert student2.get_age() == 22
    assert str(student1) == "student:Alice:20:EE"
    assert str(student2) == "student:Bob:22:CS"
    student1.change_major("ME")
    student2.change_major("CE")
    assert str(student1) == "student:Alice:20:ME"
    assert str(student2) == "student:Bob:22:CE"
    student1.add_friend(student2)
    assert student1.friends == [student2]
    assert student2.major == "CE"
    assert student1.major == "ME"

def test_rabbit():
    r1 = lec9.Rabbit(3)
    r2 = lec9.Rabbit(4)
    assert str(r1) == "rabbit:007"
    assert str(r2) == "rabbit:008"


    baby1 = r1 + r2
    assert str(baby1) == "rabbit:009"
    #assert baby1.get_parent1() == r2
    #assert baby1.get_parent2() == r1

    baby2 = r1 + r2
    assert str(baby2) == "rabbit:010"
    #assert baby2.get_parent1() == r1
    #assert baby2.get_parent2() == r2

    assert baby1 == baby2

    baby3 = r1 + baby1 #亂倫
    assert str(baby3) == "rabbit:011"

    assert baby1 != baby3
