import pytest
import add_path
from mit_ocw_data_science.lec2.menu import Food

def test_food():
    food = Food("apple", 100, 200)
    assert food.name == "apple"
    assert food.calories == 200

