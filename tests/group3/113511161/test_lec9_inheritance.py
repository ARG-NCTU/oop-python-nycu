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
    assert