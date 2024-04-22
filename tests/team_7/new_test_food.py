import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("guava", 900, 150)

def test_get_value(food):
    assert food.get_value() == 900

def test_get_cost(food):
    assert food.get_cost() == 150

def test_density(food):
    assert food.density() == 6

def test_str(food):
    assert str(food) == "guava: <900, 150>"
