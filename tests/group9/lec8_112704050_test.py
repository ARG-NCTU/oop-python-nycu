import pytest
from lec8_112704050 import Coordinate

def test_add():
    a = Coordinate(3, 4)
    b = Coordinate(1, 2)
    result = a + b
    assert result.x == 4
    assert result.y == 6

def test_sub():
    a = Coordinate(3, 4)
    b = Coordinate(1, 2)
    result = a - b
    assert result.x == 2
    assert result.y == 2

def test_mul():
    a = Coordinate(3, 4)
    b = Coordinate(2, 5)
    result = a * b
    assert result.x == 6
    assert result.y == 20

def test_truediv():
    a = Coordinate(10, 20)
    b = Coordinate(2, 4)
    result = a / b
    assert result.x == 5
    assert result.y == 5

def test_truediv_zero():
    a = Coordinate(1, 2)
    b = Coordinate(0, 1)
    with pytest.raises(ZeroDivisionError):
        _ = a / b

def test_str():
    a = Coordinate(3, 4)
    assert str(a) == "<3 , 4>"

def test_float():
    a = Coordinate(9, 16)
    assert float(a) == pytest.approx((9 + 16) ** 0.5)

def test_distace():
    a = Coordinate(6,8)
    b = Coordinate(0,0)
    result = 10
    assert result == a.distance(b)
    a = Coordinate(4,10)
    b = Coordinate(-1,-2)
    result = 13
    assert result == a.distance(b)

def test_vector():
    a = Coordinate(6,8)
    b = Coordinate(0,0)
    result = "<6,8>"
    assert result == a.vector(b)
    result = "<-6,-8>"
    assert result == b.vector(a)

import pytest
from lec8_112704050 import Vendingmachine

def test_buy_success():
    vm = Vendingmachine(100)
    result = vm.buy("Coke", 2)
    assert result == "Successfully purchased 2 Coke(s). Remaining cash: 50"
    assert vm.inventory["Coke"] == 8
    assert vm.dollar == 50

def test_buy_invalid_item():
    vm = Vendingmachine(100)
    result = vm.buy("Tea", 1)
    assert result == "Invalid item."

def test_buy_not_enough_stock():
    vm = Vendingmachine(100)
    result = vm.buy("Coke", 20)
    assert result == "Not enough stock."

def test_buy_insufficient_cash():
    vm = Vendingmachine(10)
    result = vm.buy("Coke", 1)
    assert result == "Insufficient Cash."
