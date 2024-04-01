import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("apple", 10, 50)

def test_get_value(food):
    assert food.get_value() == 10

def test_get_cost(food):
    assert food.get_cost() == 50

def test_density(food):
    assert food.density() == 0.2

def test_str(food):
    assert str(food) == "apple: <10, 50>"

def test_13_food():
    food = Food("molafish", 100, 60)
    assert food.get_value() == 100
    assert food.get_cost() == 60
    assert food.density() == 1.6666666666666667
    assert str(food) == "molafish: <100, 60>"
