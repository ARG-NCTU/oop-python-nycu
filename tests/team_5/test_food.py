import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def food():
    return Food("orange", 20, 40)

def test_get_value(food):
    assert food.get_value() == 20

def test_get_cost(food):
    assert food.get_cost() == 40

def test_density(food):
    assert food.density() == 0.5

def test_str(food):
    assert str(food) == "orange: <20, 40>"

@pytest.fixture
def food1():
    return Food("banana", 10, 50)

def test_get_value1(food1):
    assert food1.get_value() == 10

def test_get_cost1(food1):
    assert food1.get_cost() == 50

def test_density1(food1):
    assert food1.density() == 0.2

def test_str1(food1):
    assert str(food1) == "banana: <10, 50>"

