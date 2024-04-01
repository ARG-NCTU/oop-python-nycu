import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("banana", 30, 100)

def test_get_value(food):
    assert food.get_value() == 30

def test_get_cost(food):
    assert food.get_cost() == 100

def test_density(food):
    assert food.density() == 0.3

def test_str(food):
    assert str(food) == "banana: <30, 100>"
