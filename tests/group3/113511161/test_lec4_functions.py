import add_path
import mit_ocw_exercises.lec4_functions as lec4
import pytest

def test_is_even_with_return():
    assert lec4.is_even_with_return(2) == True
    assert lec4.is_even_with_return(3) == False

