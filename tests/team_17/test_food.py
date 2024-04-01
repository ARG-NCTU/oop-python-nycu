import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food
111111111111
@pytest.fixture
def food():
    return Food("banana", 20, 100)

def test_get_value(food):
    assert food.get_value() == 20

def test_get_cost(food):
    assert food.get_cost() == 100

def test_density(food):
    assert food.density() == 0.2

def test_str(food):
    assert str(food) == "banana: <20, 100>"
