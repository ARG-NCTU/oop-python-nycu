import menu as inh
import pytest

def test_food():
    food = inh.Food('apple', 50, 200)
    assert food.get_value() == 50
    assert food.get_cost() == 200
    assert food.density() == 50 / 200


