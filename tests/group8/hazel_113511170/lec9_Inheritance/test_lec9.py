import lec9 as lc
import pytest

def test_animal():
    c=lc.Cat(5)
    c.set_name("Kiki")
    r1=lc.Rabbit(4)
    r2=lc.Rabbit(6)
    r3=r1.__add__(r2)
    r5=r2.__add__(r1)
    r4=r3.get_parent1()
    r6=r5.get_parent2()
    hazel=lc.Student("Hazel",19,"EE")
    assert str(c)=="cat:Kiki:5"
    assert r4 is r1
    assert r4 is r6
