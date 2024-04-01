import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("taco", 180, 100)

def test_get_value(food):
    assert food.get_value() == 180

def test_get_cost(food):
    assert food.get_cost() == 100

def test_density(food):
    assert food.density() == 1.8

def test_str(food):
    assert str(food) == "taco: <180, 100>"
