import pytest
import lec9_inheritance as lec9
import math


# ---------- Animal ----------
def test_animal():
    animal_obj = lec9.Animal(6)
    assert animal_obj.get_name() is None

    animal_obj.set_age(7)
    assert animal_obj.get_age() == 7

    animal_obj.set_name("bruno")
    assert animal_obj.get_name() == "bruno"

    animal_obj.set_name("bruno_mars")
    assert animal_obj.get_name() == "bruno_mars"


# ---------- Cat ----------
def test_cat():
    kitty = lec9.Cat(9)
    assert kitty.get_age() == 9


# ---------- Rabbit ----------
def test_rabbit():
    rabbit_alpha = lec9.Rabbit(5)   # rid = 007
    rabbit_beta  = lec9.Rabbit(7)   # rid = 008
    assert rabbit_alpha.rid == 7

    rabbit_gamma = rabbit_alpha + rabbit_beta   # rid = 009
    assert rabbit_gamma.get_rid() == "009"

    rabbit_delta = rabbit_beta + rabbit_alpha   # rid = 010
    assert rabbit_gamma == rabbit_delta

