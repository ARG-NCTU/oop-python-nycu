import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("banana", 8, 48)

def test_get_value(food):
    assert food.get_value() == 8

def test_get_cost(food):
    assert food.get_cost() == 48

def test_density(food):
    assert food.density() == 0.16666666666666666

def test_str(food):
    assert str(food) == "banana: <8, 48>"

