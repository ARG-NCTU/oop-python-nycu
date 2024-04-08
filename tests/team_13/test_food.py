import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

@pytest.fixture
def test_13_food():
    food = Food("molafish", 100, 50)
    assert food.get_value() == 100
    assert food.get_cost() == 50
    assert food.density() == 2
    assert str(food) == "molafish: <100, 50>"

