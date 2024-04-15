import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

# This fixture is used to setup a Food object that can be used in tests.
# It creates a Food object with a value of 20 and a cost of 15.
@pytest.fixture
def food():
    return Food("group", 20, 15)

# This test checks the get_value method of the Food class.
# It asserts that the value of the food object is 20.
def test_get_value(food):
    assert food.get_value() == 20

# This test checks the get_cost method of the Food class.
# It asserts that the cost of the food object is 15.
def test_get_cost(food):
    assert food.get_cost() == 15

# This test checks the density method of the Food class.
# It asserts that the density of the food object is the value divided by the cost (20/15).
def test_density(food):
    assert food.density() == 20/15

# This test checks the __str__ method of the Food class.
# It asserts that the string representation of the food object is "group: <20, 15>".
def test_str(food):
    assert str(food) == "group: <20, 15>"

31: @pytest.fixture
32: def food():
33:     """
    This is a pytest fixture that sets up a Food object for testing.
    The Food object is initialized with the name "watermelon", a value of 50, and a cost of 100.
    """
34:     return Food("watermelon", 50, 100)
35: 
36: def test_get_value(food):
37:     """
    This test checks the get_value method of the Food class.
    It asserts that the value of the food object created in the fixture is 50.
    """
38:     assert food.get_value() == 50
39: 
40: def test_get_cost(food):
41:     """
    This test checks the get_cost method of the Food class.
    It asserts that the cost of the food object created in the fixture is 100.
    """
42:     assert food.get_cost() == 100
43: 
44: def test_density(food):
45:     """
    This test checks the density method of the Food class.
    It asserts that the density of the food object created in the fixture is 0.5.
    """
46:     assert food.density() == 0.5
47: 
48: def test_str(food):
49:     """
    This test checks the __str__ method of the Food class.
    It asserts that the string representation of the food object created in the fixture is "watermelon: <50, 100>".
    """
50:     assert str(food) == "watermelon: <50, 100>"

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

@pytest.fixture
def food():
    return Food("grape", 15, 90)

def test_get_value(food):
    assert food.get_value() == 15

def test_get_cost(food):
    assert food.get_cost() == 90

def test_density(food):
    assert food.density() == 1/6

def test_str(food):
    assert str(food) == "grape: <15, 90>"


@pytest.fixture
def food():
    return Food("sherry", 15, 90)

def test_get_value(food):
    assert food.get_value() == 15

def test_get_cost(food):
    assert food.get_cost() == 90

def test_density(food):
    assert food.density() == 1/6

def test_str(food):
    assert str(food) == "sherry: <15, 90>"



