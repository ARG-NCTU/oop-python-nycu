import add_path
import mit_ocw_exercises.lec9_inheritance as l9 # type: ignore
import pytest

import random

def test_animal():
    age = random.randint(1, 20)
    a = l9.Animal(age)
    assert str(a) == f"animal:None:{age}"
    assert a.get_age() == age
    a.set_name("fluffy")
    assert str(a) == f"animal:fluffy:{age}"
    a.set_name()
    assert str(a) == f"animal::{age}"

def test_cat():
    age = random.randint(1, 20)
    c = l9.Cat(age)
    c.set_name("weiss")
    assert str(c) == f"cat:weiss:{age}"
    assert c.get_age() == age

    # Capture the output of speak
    from io import StringIO
    import sys
    captured_output = StringIO()
    sys.stdout = captured_output
    c.speak()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "meow"
