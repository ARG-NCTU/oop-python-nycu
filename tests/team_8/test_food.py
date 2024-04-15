import pytest
import add_path
from menu import Food

@pytest.fixture
def food():
    return Food("pineapple", 100, 500)

def test_get_value(food):
    assert food.get_value() == 100

def test_get_cost(food):
    assert food.get_cost() == 500

def test_density(food):
    assert food.density() == 0.2

def test_str(food):
    assert str(food) == "pineapple: <100, 500>"

