import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

# This fixture is used to setup a Food object that can be used in tests.
# It creates a Food object with a value of 20 and a cost of 15.
@pytest.fixture
def food_group():
    return Food("group", 20, 15)

# This test checks the get_value method of the Food class.
# It asserts that the value of the food object is 20.
def test_group_get_value(food_group):
    assert food_group.get_value() == 20

# This test checks the get_cost method of the Food class.
# It asserts that the cost of the food object is 15.
def test_group_get_cost(food_group):
    assert food_group.get_cost() == 15

# This test checks the density method of the Food class.
# It asserts that the density of the food object is the value divided by the cost (20/15).
def test_group_density(food_group):
    assert food_group.density() == 20/15

# This test checks the __str__ method of the Food class.
# It asserts that the string representation of the food object is "group: <20, 15>".
def test_group_str(food_group):
    assert str(food_group) == "group: <20, 15>"

# This is a test suite for the Food class in Python. It uses pytest for testing.

@pytest.fixture
def food_watermelon():
    """
    This is a pytest fixture that sets up a Food object for testing.
    It creates a Food object with name "watermelon", value 50, and cost 100.
    """
    return Food("watermelon", 50, 100)

def test_watermelon_get_value(food_watermelon):
    """
    This test checks the get_value method of the Food class.
    It asserts that the value of the food object is 50.
    """
    assert food_watermelon.get_value() == 50

def test_watermelon_get_cost(food_watermelon):
    """
    This test checks the get_cost method of the Food class.
    It asserts that the cost of the food object is 100.
    """
    assert food_watermelon.get_cost() == 100

def test_watermelon_density(food_watermelon):
    """
    This test checks the density method of the Food class.
    It asserts that the density of the food object is 0.5.
    """
    assert food_watermelon.density() == 0.5

def test_watermelon_str(food_watermelon):
    """
    This test checks the __str__ method of the Food class.
    It asserts that the string representation of the food object is "watermelon: <50, 100>".
    """
    assert str(food_watermelon) == "watermelon: <50, 100>"
#=======
@pytest.fixture
def food_poyuan():
    
    return Food("poyuan", 200, 400)

def test_get_value(food_poyuan):
    assert food_poyuan.get_value() == 200

def test_get_cost(food_poyuan):
    assert food_poyuan.get_cost() == 400

def test_density(food_poyuan):
     assert food_poyuan.density() == 0.5
 
def test_str(food_poyuan):

     assert str(food_poyuan) == "poyuan: <200, 400>"
#>>>>>>> c7f6697a930141922778e6915d3541fb1b5a1b9c

# This is a test suite for the Food class in Python.

# The pytest.fixture decorator is used to create a fixture. A fixture is a function that returns a specific object that you want to test.
# In this case, the fixture is a Food object with name "banana", value 30, and cost 100.
@pytest.fixture
def food_banana():
    return Food("banana", 30, 100)

# This test checks if the get_value method of the Food class returns the correct value.
def test_banana_get_value(food_banana):
    assert food_banana.get_value() == 30

# This test checks if the get_cost method of the Food class returns the correct cost.
def test_banana_get_cost(food_banana):
    assert food_banana.get_cost() == 100

# This test checks if the density method of the Food class returns the correct density.
# The density is calculated as value/cost.
def test_banana_density(food_banana):
    assert food_banana.density() == 0.3

# This test checks if the __str__ method of the Food class returns the correct string representation.
# The string representation should be in the format "name: <value, cost>".
def test_str(food_banana):
    assert str(food_banana) == "banana: <30, 100>"
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

@pytest.fixture
def food_ytlin():
    
    return Food("ytlin", 200, 400)

def test_get_value(food_ytlin):
    assert food_ytlin.get_value() == 200

def test_get_cost(food_ytlin):
    assert food_ytlin.get_cost() == 400

def test_density(food_ytlin):
     assert food_ytlin.density() == 0.5
 
def test_str(food_ytlin):

     assert str(food_ytlin) == "ytlin: <200, 400>"



