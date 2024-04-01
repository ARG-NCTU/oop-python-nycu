import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("apple", 20, 80)

def test_get_value(food):
    assert food.get_value() == 20

def test_get_cost(food):
    assert food.get_cost() == 80

def test_density(food):
    assert food.density() == 0.25

def test_str(food):
    assert str(food) == "apple: <20, 80>"

    
